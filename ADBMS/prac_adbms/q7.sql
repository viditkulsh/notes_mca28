-- Compare results before and after indexing by considering any sample table

-- Compare results before and after indexing

-- Create sample table
DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    emp_id      SERIAL PRIMARY KEY,
    emp_name    VARCHAR(50),
    department  VARCHAR(50),
    salary      NUMERIC(10,2)
);

-- Insert sample data
INSERT INTO employees (emp_name, department, salary)
SELECT
    'Employee_' || generate_series,
    CASE
        WHEN generate_series % 4 = 0 THEN 'IT'
        WHEN generate_series % 4 = 1 THEN 'HR'
        WHEN generate_series % 4 = 2 THEN 'Finance'
        ELSE 'Sales'
    END,
    30000 + (generate_series * 100)
FROM generate_series(1, 1000);

COMMIT;


-- BEFORE INDEXING

EXPLAIN ANALYZE
SELECT *
FROM employees
WHERE department = 'IT';


-- CREATE INDEX

CREATE INDEX idx_employees_department
ON employees(department);


-- AFTER INDEXING

EXPLAIN ANALYZE
SELECT *
FROM employees
WHERE department = 'IT';


-- Display index information

SELECT
    indexname,
    indexdef
FROM pg_indexes
WHERE tablename = 'employees';