-- Q1) Write down Stored Procedure for inserting, updating values in the table

create table if not exists student(
    stud_id INT Primary Key,
    stud_name VARCHAR(50),
    course VARCHAR(50),
    marks INT
);

-- procedure to insert a student
create or replace procedure insert_stud(
    p_stud_id INT,
    p_stud_name VARCHAR(50),
    p_course VARCHAR(50),
    p_marks INT
)
language plpgsql
as $$
begin
    insert into student(stud_id, stud_name, course, marks)
    values (p_stud_id, p_stud_name, p_course, p_marks);
end;
$$;

-- procedure to update a student
create or replace procedure update_stud(
    p_stud_id INT,
    p_course VARCHAR(50),
    p_marks INT
)
language plpgsql
as $$
begin
    update student
    set course = p_course,
        marks = p_marks
    where stud_id = p_stud_id;
end;
$$;

call insert_stud(1, 'Jake Peralta', 'MCA', 78);
call insert_stud(2, 'Amy Santiago', 'MCA', 98);
call insert_stud(3, 'Rosa Diaz', 'MBA', 85);

call update_stud(1, 'MCA', 88);

select * from student;
