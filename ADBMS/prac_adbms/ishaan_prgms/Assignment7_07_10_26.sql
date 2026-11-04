--Q7. Compare results before and after indexing by considering any sample table
CREATE TABLE Students(
student_id INT,
name VARCHAR(50),
department VARCHAR(30),
marks INT
);

INSERT INTO Students VALUES
(1, 'Amit', 'Computer', 85),
(2, 'Rahul', 'IT', 78),
(3, 'Sneha', 'Computer', 92),
(4, 'Priya', 'ENTC', 88),
(5, 'Sachin', 'IT', 75);

EXPLAIN ANALYZE
SELECT * FROM Students
WHERE department = 'Computer';

CREATE INDEX idx_students_department
ON Students(department);

EXPLAIN ANALYZE
SELECT * FROM Students
WHERE department = 'Computer';

