-- Q5) Write down DML trigger to raise the error when user deletes more than 1 record from table

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    age INT
);

INSERT INTO students VALUES
(1, 'Barney', 28),
(2, 'Ted', 27),
(3, 'Robin', 27),
(4, 'Marshal', 28),
(5, 'Lily', 26);

CREATE OR REPLACE FUNCTION check_delete_limit()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
    deleted_count INT;
BEGIN
    SELECT COUNT(*)
    INTO deleted_count
    FROM deleted_rows;

    IF deleted_count > 1 THEN
        RAISE EXCEPTION 'Cannot delete more than 1 record at a time';
    END IF;

    RETURN NULL;
END;
$$;

CREATE TRIGGER student_delete_limit
AFTER DELETE ON students
REFERENCING OLD TABLE AS deleted_rows
FOR EACH STATEMENT
EXECUTE FUNCTION check_delete_limit();

-- allowed: deletes one row
DELETE FROM students
WHERE student_id = 1;

-- rejected: deletes three rows, raises the error
DELETE FROM students
WHERE age = 22;
