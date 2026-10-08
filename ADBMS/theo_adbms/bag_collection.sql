-- ============================================
-- BAG COLLECTION
-- ============================================

DROP TABLE IF EXISTS student_courses CASCADE;
DROP TABLE IF EXISTS students CASCADE;
DROP TYPE IF EXISTS course_type CASCADE;
DROP TYPE IF EXISTS student_type CASCADE;


-- Course object/composite type
CREATE TYPE course_type AS (
    course_name VARCHAR(50)
);


-- Student object/composite type
CREATE TYPE student_type AS (
    id      INTEGER,
    name    VARCHAR(50)
);


-- Student table
CREATE TABLE students (
    student_data student_type
);


-- BAG collection table
-- No UNIQUE constraint because duplicates are allowed
CREATE TABLE student_courses (
    student_id INTEGER,
    course_name VARCHAR(50)
);


-- Insert student
INSERT INTO students
VALUES (
    ROW(1, 'Vidit')::student_type
);


-- Insert courses
INSERT INTO student_courses VALUES
    (1, 'DBMS'),
    (1, 'Java'),
    (1, 'DBMS'),
    (1, 'Python');


-- Display courses
SELECT
    (s.student_data).name AS name,
    c.course_name
FROM students s
JOIN student_courses c
    ON c.student_id = (s.student_data).id;