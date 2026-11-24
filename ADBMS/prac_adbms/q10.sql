-- Q10) Write down the function which selects part name (substring, like
--      surname, firstname or middle name) and copy that part in another
--      table's column

drop table if exists name_part;
drop table if exists person;

create table person(
    id        INT Primary Key,
    full_name VARCHAR(100)
);

insert into person values
(1, 'Rahul Kumar Sharma'),
(2, 'Priya Anil Patil'),
(3, 'Amit Suresh Joshi'),
(4, 'Sneha Ravi Kulkarni');

-- Second table: the selected part goes into the "part" column
create table name_part(
    id   INT,
    part VARCHAR(50)
);


-- p_pos: 1 = first name, 2 = middle name, 3 = surname
-- split_part('Rahul Kumar Sharma', ' ', 3)  ->  'Sharma'
create or replace function copy_name_part(p_pos INT)
returns void
language plpgsql
as $$
begin
    delete from name_part;               -- clear old copies first

    insert into name_part
    select id, split_part(full_name, ' ', p_pos)
    from person;
end;
$$;


select copy_name_part(3);                -- copy surnames
select * from name_part;

select copy_name_part(1);                -- copy first names
select * from name_part;
