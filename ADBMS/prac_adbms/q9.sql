-- =============================================================================
-- Q9) Write down a function which prints higher salaried person from table
--     by inputting his empid and name
-- =============================================================================
--
-- ONE-BREATH ANSWER
--   higher_salaried(p_emp_id, p_emp_name) first checks that the id and the
--   name belong to the same employee in `emp`, and raises an error if they do
--   not. It then loops over every employee who earns MORE than that person,
--   prints each one with RAISE NOTICE, and also returns them as rows. If no
--   one earns more, it prints that the given person is the highest paid.
--
--   Why a FUNCTION and not a procedure: a function can RETURN rows, so you
--   call it with SELECT * FROM higher_salaried(...). A procedure is run with
--   CALL and cannot return a result set.
--
-- Run:  psql "postgresql://postgres:postgres@127.0.0.1:54422/postgres" -f q9.sql
--       (the last call is MEANT to fail -- that is the demonstration)
-- =============================================================================


drop table if exists emp cascade;

create table emp(
    emp_id   INT Primary Key,
    emp_name VARCHAR(50),
    salary   INT
);

insert into emp values
(1, 'Harvey Specter', 150000),
(2, 'Mike Ross',       70000),
(3, 'Louis Litt',     120000),
(4, 'Donna Paulsen',   90000),
(5, 'Rachel Zane',     65000),
(6, 'Jessica Pearson',200000);


-- -----------------------------------------------------------------------------
-- The function
-- -----------------------------------------------------------------------------
create or replace function higher_salaried(
    p_emp_id   INT,
    p_emp_name VARCHAR(50)
)
-- RETURNS TABLE: the function gives back a set of rows with these columns.
-- These column names also act as variables inside the body, so the queries
-- below prefix table columns with "e." to avoid "column reference is
-- ambiguous" errors.
returns table(emp_id INT, emp_name VARCHAR(50), salary INT)
language plpgsql
as $$
declare
    v_salary INT;                            -- the input person's salary
    rec      RECORD;                         -- one row in the loop
    found_any BOOLEAN := false;
begin
    -- Step 1: find the person. BOTH the id and the name must match.
    select e.salary into v_salary
    from emp e
    where e.emp_id = p_emp_id
      and e.emp_name = p_emp_name;

    -- FOUND is a built-in flag. SELECT INTO sets it to false when no row
    -- matched.
    if not found then
        raise exception 'No employee with id % and name %', p_emp_id, p_emp_name;
    end if;

    raise notice '% (id %) earns %', p_emp_name, p_emp_id, v_salary;

    -- Step 2: everyone who earns MORE than that person, highest first.
    for rec in
        select e.emp_id, e.emp_name, e.salary
        from emp e
        where e.salary > v_salary
        order by e.salary desc
    loop
        raise notice 'Higher salaried: % (id %) earns %',
                     rec.emp_name, rec.emp_id, rec.salary;   -- PRINT

        emp_id   := rec.emp_id;              -- fill the output columns
        emp_name := rec.emp_name;
        salary   := rec.salary;
        return next;                         -- add this row to the result
        found_any := true;
    end loop;

    if not found_any then
        raise notice '% is the highest salaried person', p_emp_name;
    end if;

    -- RETURN with no value ends a set-returning function.
    return;
end;
$$;


-- A function is called with SELECT, not CALL.

-- Mike earns 70000, so four people earn more.
select * from higher_salaried(2, 'Mike Ross');
-- NOTICE:  Mike Ross (id 2) earns 70000
-- NOTICE:  Higher salaried: Jessica Pearson (id 6) earns 200000
-- NOTICE:  Higher salaried: Harvey Specter (id 1) earns 150000
-- NOTICE:  Higher salaried: Louis Litt (id 3) earns 120000
-- NOTICE:  Higher salaried: Donna Paulsen (id 4) earns 90000

-- Jessica is the top earner, so nobody is returned.
select * from higher_salaried(6, 'Jessica Pearson');
-- NOTICE:  Jessica Pearson (id 6) earns 200000
-- NOTICE:  Jessica Pearson is the highest salaried person
-- (0 rows)

-- The id and name belong to different people, so the function raises an error.
select * from higher_salaried(1, 'Mike Ross');
-- ERROR:  No employee with id 1 and name Mike Ross
