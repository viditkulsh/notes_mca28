-- 1st September 2026
create type stud_type as (
    stud_id int,
    stud_name varchar(20),
    stud_course varchar(50)
);

create table stud_tab of stud_type;

insert INTO stud_tab values (1, 'Vidit Kulshrestha', 'BCA');
insert INTO stud_tab values (2, 'Tony Stark', 'MCA');
insert INTO stud_tab VALUES (3, 'Black Widow', 'MCA (Hons)');
commit;

SELECT * FROM stud_tab;
