create table Student (
     id int primary key,
	 fullname varchar(100)
);

insert into Student values
(1, 'Amit Kumar Sharma'),
(2, 'Rahul Raj Patil'),
(3, 'Priya Sunil Deshmukh');

select * from Student;

create table StudentNameParts(
   id int
   fullname varchar(50),
   middlename varchar(50),
   surname varchar(50)
);
delimiter//

CREATE TABLE studentnameparts (
    id INT,
    firstname VARCHAR(50),
    middlename VARCHAR(50),
    surname VARCHAR(50)
);

CREATE OR REPLACE FUNCTION getfirstname(fullname VARCHAR(100))
RETURNS VARCHAR(50)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN SPLIT_PART(fullname, ' ', 1);
END;
$$;


CREATE OR REPLACE FUNCTION getmiddlename(fullname VARCHAR(100))
RETURNS VARCHAR(50)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN SPLIT_PART(fullname, ' ', 2);
END;
$$;


CREATE OR REPLACE FUNCTION getsurname(fullname VARCHAR(100))
RETURNS VARCHAR(50)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN SPLIT_PART(fullname, ' ', 3);
END;
$$;


INSERT INTO studentnameparts (id, firstname, middlename, surname)
SELECT
    id,
    getfirstname(fullname),
    getmiddlename(fullname),
    getsurname(fullname)
FROM student;


SELECT * FROM studentnameparts;