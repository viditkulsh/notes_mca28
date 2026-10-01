create type AddressType AS(
street varchar(50),
city varchar(50),
pincode int
);

create type StudentType AS(
stud_id int,
name varchar(50),
address AddressType
);

create table student2 of StudentType;

insert into student2 values(21,'Vidit',row('Ghaziabad','U.P',201019));

select * from student2;