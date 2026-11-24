-- Q9) Write down a function which prints higher salaried person from table
--     by inputting his empid and name

drop table if exists emp;

create table emp(
    emp_id   INT Primary Key,
    emp_name VARCHAR(50),
    salary   INT
);

insert into emp values
(1, 'Harvey Specter',  150000),
(2, 'Mike Ross',        70000),
(3, 'Louis Litt',      120000),
(4, 'Donna Paulsen',    90000),
(5, 'Rachel Zane',      65000),
(6, 'Jessica Pearson', 200000);


create or replace function higher_salaried(p_id INT, p_name VARCHAR)
returns void
language plpgsql
as $$
declare
    v_salary INT;
    r        RECORD;
begin
    -- salary of the given employee
    select salary into v_salary
    from emp
    where emp_id = p_id and emp_name = p_name;

    if v_salary is null then
        raise notice 'Employee not found';
        return;
    end if;

    -- print everyone who earns more
    for r in select * from emp where salary > v_salary order by salary desc loop
        raise notice '% earns %', r.emp_name, r.salary;
    end loop;
end;
$$;


select higher_salaried(2, 'Mike Ross');      -- prints 4 people
select higher_salaried(1, 'Mike Ross');      -- Employee not found
