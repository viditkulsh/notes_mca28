-- Q8) Write down the stored procedure for selecting the first five records
--     and copy those five records in another table

drop table if exists staff_copy;
drop table if exists staff;

create table staff(
    emp_id   INT Primary Key,
    emp_name VARCHAR(50),
    salary   INT
);

insert into staff values
(1, 'Michael Scott',  80000),
(2, 'Dwight Schrute', 60000),
(3, 'Jim Halpert',    55000),
(4, 'Pam Beesly',     40000),
(5, 'Angela Martin',  45000),
(6, 'Kevin Malone',   42000),
(7, 'Oscar Martinez', 50000),
(8, 'Creed Bratton',  38000);

-- Second table with the same columns (empty)
create table staff_copy(
    emp_id   INT Primary Key,
    emp_name VARCHAR(50),
    salary   INT
);


create or replace procedure copy_first_five()
language plpgsql
as $$
begin
    delete from staff_copy;              -- clear old copies first

    insert into staff_copy
    select * from staff
    order by emp_id
    limit 5;

    raise notice 'First five records copied';
end;
$$;


call copy_first_five();

select * from staff_copy;               -- emp_id 1 to 5
