-- ============================================
-- SET COLLECTION
-- ============================================

DROP TABLE IF EXISTS student_subjects CASCADE;
DROP TABLE IF EXISTS student_table CASCADE;
DROP TYPE IF EXISTS student_type CASCADE;


-- Student object/composite type
CREATE TYPE student_type AS (
    roll_no INTEGER,
    name    VARCHAR(30)
);


-- Student table
CREATE TABLE student_table (
    student_data student_type
);


-- Separate table representing SET collection
CREATE TABLE student_subjects (
    roll_no INTEGER,
    subject VARCHAR(30),
    UNIQUE (roll_no, subject)
);


-- Insert student
INSERT INTO student_table
VALUES (
    ROW(101, 'Manan')::student_type
);


-- Insert subjects
INSERT INTO student_subjects VALUES
    (101, 'Java'),
    (101, 'SQL'),
    (101, 'Python');


-- Display student
SELECT
    (student_data).roll_no AS roll_no,
    (student_data).name AS name
FROM student_table;


-- Display student's subjects
SELECT
    s.student_data,
    ss.subject
FROM student_table s
JOIN student_subjects ss
    ON ss.roll_no = (s.student_data).roll_no;