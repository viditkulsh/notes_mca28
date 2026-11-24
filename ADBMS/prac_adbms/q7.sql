-- Q7) Compare results before and after indexing by considering any sample table

drop table if exists employees;

create table employees(
    emp_id   INT Primary Key,
    emp_name VARCHAR(50),
    salary   INT
);

-- 1,00,000 rows so the difference is easy to see
insert into employees
select i, 'Employee_' || i, 30000 + i
from generate_series(1, 100000) as i;


-- BEFORE indexing: Seq Scan (checks every row)
explain analyze
select * from employees where emp_name = 'Employee_50000';

create index idx_emp_name on employees(emp_name);

-- AFTER indexing: Index Scan (goes straight to the row)
explain analyze
select * from employees where emp_name = 'Employee_50000';

-- Compare the "Execution Time" of both outputs.
