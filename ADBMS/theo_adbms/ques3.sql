-- Q3: Employee Object Type with Skill Set
-- PostgreSQL Version

-- Remove old table if it exists
DROP TABLE IF EXISTS employee CASCADE;

-- Remove old automatically-created employee type
DROP TYPE IF EXISTS employee CASCADE;

-- Remove employee_type if it exists
DROP TYPE IF EXISTS employee_type CASCADE;


-- 1. Create Employee object/composite type
CREATE TYPE employee_type AS (
    emp_id   INTEGER,
    emp_name VARCHAR(50),
    sal      NUMERIC,
    skills   VARCHAR(30)[]
);


-- 2. Create Employee table using employee_type
CREATE TABLE employee (
    employee_data employee_type
);


-- 3. Insert employee details
INSERT INTO employee
VALUES (
    ROW(
        101,
        'Rahul',
        50000,
        ARRAY['Python', 'SQL', 'Java']::VARCHAR(30)[]
    )::employee_type
);


COMMIT;


-- 4. Display employee details
SELECT
    (employee_data).emp_id AS emp_id,
    (employee_data).emp_name AS emp_name,
    (employee_data).sal AS salary
FROM employee;


-- 5. Display employee details with individual skills
SELECT
    (e.employee_data).emp_id AS emp_id,
    (e.employee_data).emp_name AS emp_name,
    (e.employee_data).sal AS salary,
    s.skill
FROM employee e
CROSS JOIN LATERAL
    unnest((e.employee_data).skills) AS s(skill);