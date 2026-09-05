-- Q2) Write down stored procedures to accept input values as a parameter
--     and update values of the tables

create table if not exists employee(
    emp_id INT Primary Key,
    emp_name VARCHAR(50),
    dept VARCHAR(50),
    salary INT
);

insert into employee values
(1, 'Ted Mosby', 'Architect', 50000),
(2, 'Marshall Eriksen', 'Legal', 60000),
(3, 'Barney Stinson', 'Please', 90000),
(4, 'Robin Scherbatsky', 'News', 55000);

-- procedure to update salary of one employee
create or replace procedure update_salary(
    p_emp_id INT,
    p_salary INT
)
language plpgsql
as $$
begin
    update employee
    set salary = p_salary
    where emp_id = p_emp_id;
end;
$$;

-- procedure to update department of all employees of a department
create or replace procedure update_dept(
    p_old_dept VARCHAR(50),
    p_new_dept VARCHAR(50)
)
language plpgsql
as $$
begin
    update employee
    set dept = p_new_dept
    where dept = p_old_dept;
end;
$$;

call update_salary(1, 65000);
call update_dept('Please', 'Marketing');

select * from employee;
