create TABLE student(
    stud_id Serial Primary Key,
    stud_name Varchar(100) Not Null,
    course VARCHAR(50),
    sem INT,
    marks INT
);

--procdure to insert student details
create or replace procedure insert_stud(
    p_stud_name Varchar(100),
    p_course VARCHAR(50),
    p_sem INT,
    p_marks INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO student(stud_name, course, sem, marks)
    VALUES (p_stud_name, p_course, p_sem, p_marks);
END;
$$;


CALL insert_stud ('Mcqueen', 'Racing', 1, 99);
-- CALL insert_stud ('Tyrion Lannister', 'MCA', 1, 100);
-- CALL insert_stud ('Arya Stark', 'MCA', 1, 75);
-- CALL insert_stud ('Hodor', 'MCA', 1, 40);
-- CALL insert_stud ('Sansa Stark', 'MCA', 1, 95);

-- select * FROM student;

-- procedure to update student details
create or replace procedure update_stud(
    p_stud_id INT,
    p_stud_name Varchar(100),
    p_course VARCHAR(50),
    p_sem INT,
    p_marks INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE student
    SET stud_name = p_stud_name,
        course = p_course,
        sem = p_sem,
        marks = p_marks
    WHERE stud_id = p_stud_id;
END;
$$;
-- CALL update_stud(1, 'Jon Snow', 'MCA', 1, 40);
-- select * FROM student;

-- --procedure to update student marks
-- create or replace procedure update_stud_id(
--     p_course VARCHAR(50),
--     u_id INT
-- )
-- language plpgsql
-- as $$
-- BEGIN
--     UPDATE student
--     SET stud_id = u_id
--     WHERE course = p_course;
-- END;
-- $$;
-- call update_stud_id('Potions', 1);

-- select * FROM student;


