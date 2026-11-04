-- =============================================================================
-- Q10) Write down the function which selects part name (substring, like
--      surname, firstname or middle name) and copy that part in another
--      table's column
-- =============================================================================
--
-- ONE-BREATH ANSWER
--   `person` stores each full name in one column. copy_name_part(p_part)
--   takes 'first', 'middle' or 'last'. It cuts that word out of every
--   full_name with split_part() and copies it into the part_value column of
--   `name_parts`, then returns how many rows it copied. Names with no middle
--   name are skipped when you ask for 'middle'.
--
-- Run:  psql "postgresql://postgres:postgres@127.0.0.1:54422/postgres" -f q10.sql
--       (the last call is MEANT to fail -- that is the demonstration)
-- =============================================================================


drop table if exists name_parts cascade;
drop table if exists person     cascade;

-- Source table: the whole name in ONE column.
-- Assumes words are separated by a single space.
create table person(
    person_id INT Primary Key,
    full_name VARCHAR(100)
);

insert into person values
(1, 'Walter Hartwell White'),
(2, 'Jesse Bruce Pinkman'),
(3, 'Saul Goodman'),                         -- no middle name
(4, 'Leslie Barbara Knope'),
(5, 'Ron Swanson');                          -- no middle name

-- Target table: the extracted part goes into part_value.
-- part_type records which part it is, so first, middle and last names can sit
-- in the same table without mixing them up.
create table name_parts(
    person_id  INT REFERENCES person(person_id),
    part_type  VARCHAR(10),                  -- 'first' / 'middle' / 'last'
    part_value VARCHAR(50),                  -- the copied substring
    PRIMARY KEY (person_id, part_type)
);


-- -----------------------------------------------------------------------------
-- How the parts are cut out
-- -----------------------------------------------------------------------------
-- split_part(text, delimiter, n) returns the n-th piece of the text:
--   split_part('Walter Hartwell White', ' ',  1)  ->  'Walter'    first
--   split_part('Walter Hartwell White', ' ',  2)  ->  'Hartwell'  middle
--   split_part('Walter Hartwell White', ' ', -1)  ->  'White'     last
--     (a negative n counts from the END, PostgreSQL 14+)
--
-- The same first name using SUBSTRING and POSITION, if the examiner asks
-- for SUBSTRING by name:
--   substring(full_name from 1 for position(' ' in full_name) - 1)
--
-- Word count = array_length(string_to_array(full_name, ' '), 1).
-- Only a 3-word name has a middle name. For 'Saul Goodman', part 2 would
-- be the surname, not a middle name.


-- -----------------------------------------------------------------------------
-- The function
-- -----------------------------------------------------------------------------
create or replace function copy_name_part(p_part VARCHAR(10))
returns INT                                  -- how many rows were copied
language plpgsql
as $$
declare
    copied_count INT;
begin
    p_part := lower(p_part);                 -- accept 'First', 'LAST', ...

    if p_part not in ('first', 'middle', 'last') then
        raise exception 'Part must be first, middle or last, given %', p_part;
    end if;

    -- Remove this part's earlier copies so the function can be re-run without
    -- a duplicate primary key error.
    delete from name_parts where part_type = p_part;

    -- SELECT the part and COPY it in one statement.
    insert into name_parts (person_id, part_type, part_value)
    select person_id, p_part, part
    from (
        select person_id,
               case p_part
                   when 'first'  then split_part(full_name, ' ', 1)
                   when 'last'   then split_part(full_name, ' ', -1)
                   when 'middle' then
                       case when array_length(string_to_array(full_name, ' '), 1) = 3
                            then split_part(full_name, ' ', 2)
                       end                   -- no ELSE, so NULL
               end as part
        from person
    ) t
    where part is not null;                  -- skips missing middle names

    get diagnostics copied_count = row_count;
    raise notice '% % name(s) copied into name_parts', copied_count, p_part;
    return copied_count;
end;
$$;


-- A function is called with SELECT. Each call copies one part.
select copy_name_part('last');               -- 5 surnames
select copy_name_part('first');              -- 5 first names
select copy_name_part('middle');             -- 3 (Saul and Ron have none)

select p.full_name, n.part_type, n.part_value
from name_parts n
join person p on p.person_id = n.person_id
order by n.person_id, n.part_type;

-- Rejected: not a valid part
select copy_name_part('nickname');
-- ERROR:  Part must be first, middle or last, given nickname
