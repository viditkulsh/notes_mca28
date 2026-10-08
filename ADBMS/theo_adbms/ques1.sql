-- create an employee object table using OID (Object Identity) Perform the following operations:
-- 1. Create Employee Object type with the attributes employee name, department, salalry
-- 2. Create an object table name, employee_details using the employee object type. 
-- 3. Display the employee_details along with their OID. 
-- 4. Use the OID to update the salary or department details of the selected employee. Display the updated employee details and verify the changes. 

-- ============================================================
-- ADBMS Practical
-- Create and manipulate an Employee object table using
-- Object Identity (OID)
--
-- ============================================================


-- ============================================================
-- 1. Create Employee Object Type
-- ============================================================
-- PostgreSQL does not support Oracle-style:
-- CREATE TYPE employee AS OBJECT
--
-- Therefore, the employee object is represented as a table
-- with an identity column acting as the object identifier.

DROP TABLE IF EXISTS employee_details;


-- ============================================================
-- 2. Create Employee Object Table
-- ============================================================

CREATE TABLE employee_details (
    employee_oid BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    employee_name VARCHAR(50) NOT NULL,
    department VARCHAR(50) NOT NULL,
    salary NUMERIC(10,2) NOT NULL
);


-- ============================================================
-- 3. Insert Employee Records
-- ============================================================

INSERT INTO employee_details
    (employee_name, department, salary)
VALUES
    ('Rahul Sharma', 'IT', 50000),
    ('Priya Mehta', 'HR', 45000),
    ('Aman Verma', 'Finance', 55000);


-- ============================================================
-- 4. Display Employee Details Along With OID
-- ============================================================

SELECT
    employee_oid AS OID,
    employee_name,
    department,
    salary
FROM employee_details
ORDER BY employee_oid;


-- ============================================================
-- 5. Select the OID of the Employee to be Updated
-- ============================================================

SELECT
    employee_oid AS OID,
    employee_name,
    department,
    salary
FROM employee_details
WHERE employee_name = 'Rahul Sharma';


-- ============================================================
-- 6. Update Salary Using Employee OID
-- ============================================================

UPDATE employee_details
SET salary = 60000
WHERE employee_oid = 1;


-- ============================================================
-- 7. Update Department Using Employee OID
-- ============================================================

UPDATE employee_details
SET department = 'Research & Development'
WHERE employee_oid = 1;


-- ============================================================
-- 8. Display Updated Employee Details
-- ============================================================

SELECT
    employee_oid AS OID,
    employee_name,
    department,
    salary
FROM employee_details
WHERE employee_oid = 1;


-- ============================================================
-- 9. Display All Employees to Verify Changes
-- ============================================================

SELECT
    employee_oid AS OID,
    employee_name,
    department,
    salary
FROM employee_details
ORDER BY employee_oid;