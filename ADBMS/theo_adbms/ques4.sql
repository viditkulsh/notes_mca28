-- print result of the student whoes name start from 'A' alphabet. Insert 5values. Use set (for subjects) and tuple (for personal info) constructors.

-- Remove previous objects if they exist
DROP TABLE IF EXISTS students CASCADE;
DROP TYPE IF EXISTS student_info CASCADE;

-- Create composite type for personal information
CREATE TYPE student_info AS (
    roll_no INTEGER,
    name VARCHAR(50),
    age INTEGER
);

-- Create student table
CREATE TABLE students (
    personal_info student_info,
    subjects VARCHAR(50)[]
);

-- Insert 5 student records
INSERT INTO students
VALUES (
    ROW(101, 'Aarav', 21),
    ARRAY['DBMS', 'Java', 'Python']::VARCHAR(50)[]
);

INSERT INTO students
VALUES (
    ROW(102, 'Rahul', 22),
    ARRAY['DBMS', 'Java', 'Networks']::VARCHAR(50)[]
);

INSERT INTO students
VALUES (
    ROW(103, 'Ananya', 21),
    ARRAY['Python', 'AI', 'DBMS']::VARCHAR(50)[]
);

INSERT INTO students
VALUES (
    ROW(104, 'Priya', 22),
    ARRAY['Java', 'Networks', 'Cloud']::VARCHAR(50)[]
);

INSERT INTO students
VALUES (
    ROW(105, 'Aditya', 23),
    ARRAY['DBMS', 'Python', 'AI']::VARCHAR(50)[]
);

COMMIT;


-- Display all students
SELECT
    (personal_info).roll_no AS roll_no,
    (personal_info).name AS name,
    (personal_info).age AS age,
    subjects
FROM students;


-- Print students whose name starts with 'A'
SELECT
    (personal_info).roll_no AS roll_no,
    (personal_info).name AS name,
    (personal_info).age AS age,
    subjects
FROM students
WHERE (personal_info).name LIKE 'A%';