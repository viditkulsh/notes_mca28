-- Create and manipulate a employee object using type constructor perform the following operations. 
-- 1. Create employee object type with the attributes object name of employee_students.
-- 2. Create object name employe using emp object type.
-- 3. Insert details into the employee_details table using employee type constructor.

-- Create and manipulate an Employee object using Type Constructor
--
-- Operations:
-- 1. Create employee object type with attributes
-- 2. Create employee object using employee type
-- 3. Insert details into employee_details using type constructor

-- 1. Create Employee Object Type
-- PostgreSQL composite type is used to represent the
-- employee object.

DROP TYPE IF EXISTS employee CASCADE;

CREATE TYPE employee AS (
    employee_name VARCHAR(50),
    department    VARCHAR(50),
    salary        NUMERIC(10,2)
);


-- 2. Create Employee Details Table

DROP TABLE IF EXISTS employee_details;

CREATE TABLE employee_details (
    employee employee
);


-- 3. Insert Employee Details Using Employee Type Constructor

INSERT INTO employee_details
VALUES (
    ROW('Rahul Sharma', 'IT', 50000.00)::employee
);

INSERT INTO employee_details
VALUES (
    ROW('Priya Mehta', 'HR', 45000.00)::employee
);

INSERT INTO employee_details
VALUES (
    ROW('Aman Verma', 'Finance', 55000.00)::employee
);

-- 4. Display Employee Details

SELECT
    (employee).employee_name AS employee_name,
    (employee).department AS department,
    (employee).salary AS salary
FROM employee_details;