create table employee(
    empid int primary key,
    name varchar(50),
    salary decimal(10,2)
);

insert into employee values
(101, 'Amit', 25000),
(102, 'Rahul', 45000),
(103, 'Priya', 35000),
(104, 'Sneha', 55000);

select * from employee;

create or replace function highersalary(
    id1 int,
    id2 int
)
returns varchar(100)
language plpgsql
as $$
declare
    result varchar(50);
begin
    select concat(name, ' - Salary: ', salary)
    into result
    from employee
    where empid in (id1, id2)
    order by salary desc
    limit 1;

    return result;
end;
$$;

select highersalary(101, 102);
select highersalary(103, 104);