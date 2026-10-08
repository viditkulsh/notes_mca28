-- Q7) Create a table of 10 names, sorted into ascending order by a trigger.
--     Insert one more name, then rename the name in the 3rd row -- both times
--     the trigger re-sorts the table.

drop table if exists students cascade;       -- cascade also drops the trigger

create table students(
    id   INT Primary Key,
    name VARCHAR(50)
);


-- ---------- The trigger ----------

create or replace function sort_students()
returns trigger
language plpgsql
as $$
begin
    -- 1. Lift every row out, already in ascending order of name.
    create temp table tmp_sorted as
        select * from students order by name;

    -- 2. Empty the table.
    delete from students;

    -- 3. Write the rows back. They are stored in the order they are inserted,
    --    so the table is now physically in ascending order.
    insert into students select * from tmp_sorted;

    drop table tmp_sorted;                   -- so the next fire can re-create it

    -- AFTER ... FOR EACH STATEMENT triggers ignore the return value.
    return null;
end;
$$;

drop trigger if exists trg_sort_students on students;

create trigger trg_sort_students
after insert or update on students           -- INSERT: a new name arrives.
for each statement                           -- UPDATE: a name CHANGES, so the
when (pg_trigger_depth() = 0)                --   row belongs somewhere else now
execute function sort_students();

-- ---------- Load the 10 names ----------

insert into students (id, name) values
    (1,  'Michael Scott'),                   -- The Office
    (2,  'Rachel Green'),                    -- Friends
    (3,  'Sheldon Cooper'),                  -- The Big Bang Theory
    (4,  'Barney Stinson'),                  -- How I Met Your Mother
    (5,  'Joey Tribbiani'),                  -- Friends
    (6,  'Dwight Schrute'),                  -- The Office
    (7,  'Ted Mosby'),                       -- How I Met Your Mother
    (8,  'Chandler Bing'),                   -- Friends
    (9,  'Leonard Hofstadter'),              -- The Big Bang Theory
    (10, 'Howard Wolowitz');                 -- The Big Bang Theory
select * from students;


-- ---------- Insert one more name ----------

insert into students values (11, 'Monica Geller');

select * from students;                      -- still no ORDER BY: mid-table


-- ---------- Rename the name in the 3rd row ----------

-- Look before you leap -- this is the row about to be renamed.
select * from students order by name offset 2 limit 1;      -- Dwight Schrute

update students
   set name = 'Amy Farrah Fowler'                           -- The Big Bang Theory
 where id = (select id from students order by name offset 2 limit 1);

select * from students;


select count(*) as out_of_order_pairs
  from (select name, lag(name) over (order by ctid) as prev_name from students) t
 where prev_name > name;

select count(*) as rows_total from students;   -- 11

-- The ids, side by side with storage order: id 6 (Dwight, now Amy) sits first.
select ctid, * from students;

\d students
