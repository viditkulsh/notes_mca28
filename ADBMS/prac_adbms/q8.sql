-- =============================================================================
-- Q8) Write down the stored procedure for selecting the first five records
--     and copy those five records in another table
-- =============================================================================
--
-- ONE-BREATH ANSWER
--   `staff` holds 8 rows. `staff_top5` is an empty table with the same
--   structure. copy_first_five() runs a single INSERT ... SELECT that picks
--   the first five rows of `staff` (ORDER BY emp_id LIMIT 5) and writes them
--   into `staff_top5`, then prints how many rows it copied.
--
--   The key point: a table has NO built-in order. "First five" only means
--   something once you add ORDER BY. Without it, LIMIT 5 returns any five
--   rows the database likes.
--
-- Run:  psql "postgresql://postgres:postgres@127.0.0.1:54422/postgres" -f q8.sql
-- =============================================================================


drop table if exists staff_top5 cascade;
drop table if exists staff      cascade;

-- Source table
create table staff(
    emp_id   INT Primary Key,
    emp_name VARCHAR(50),
    dept     VARCHAR(50),
    salary   INT
);

-- Rows are inserted OUT of id order on purpose. If the procedure left out
-- ORDER BY, the five rows it copied could follow insertion order and not
-- emp_id order.
insert into staff values
(6, 'Kevin Malone',   'Accounts',   42000),
(1, 'Michael Scott',  'Management', 80000),
(3, 'Jim Halpert',    'Sales',      55000),
(8, 'Creed Bratton',  'Quality',    38000),
(2, 'Dwight Schrute', 'Sales',      60000),
(5, 'Angela Martin',  'Accounts',   45000),
(4, 'Pam Beesly',     'Reception',  40000),
(7, 'Oscar Martinez', 'Accounts',   50000);

-- Target table: an empty copy of the structure.
-- LIKE ... INCLUDING ALL copies the columns, the PRIMARY KEY, defaults and
-- constraints, but NO rows.
create table staff_top5 (like staff including all);


-- -----------------------------------------------------------------------------
-- The procedure
-- -----------------------------------------------------------------------------
create or replace procedure copy_first_five()
language plpgsql
as $$
declare
    copied_count INT;
begin
    -- Empty the target first, so calling the procedure twice does not hit a
    -- duplicate primary key error. Every call gives the same result.
    delete from staff_top5;

    -- SELECT and COPY in one statement. INSERT ... SELECT sends the rows the
    -- query returns straight into the target table. There is no loop and no
    -- VALUES list.
    insert into staff_top5 (emp_id, emp_name, dept, salary)
    select emp_id, emp_name, dept, salary
    from staff
    order by emp_id                          -- defines what "first" means
    limit 5;                                 -- keep only five rows

    -- ROW_COUNT = number of rows the last SQL statement touched.
    get diagnostics copied_count = row_count;
    raise notice '% records copied from staff to staff_top5', copied_count;
end;
$$;


-- CALL runs the procedure.
call copy_first_five();
-- NOTICE:  5 records copied from staff to staff_top5

-- Source table: still all 8 rows. Copying does not remove anything.
select * from staff order by emp_id;

-- Target table: exactly the first five by emp_id (1 to 5).
select * from staff_top5 order by emp_id;
--  emp_id |    emp_name    |    dept    | salary
-- --------+----------------+------------+--------
--       1 | Michael Scott  | Management |  80000
--       2 | Dwight Schrute | Sales      |  60000
--       3 | Jim Halpert    | Sales      |  55000
--       4 | Pam Beesly     | Reception  |  40000
--       5 | Angela Martin  | Accounts   |  45000
