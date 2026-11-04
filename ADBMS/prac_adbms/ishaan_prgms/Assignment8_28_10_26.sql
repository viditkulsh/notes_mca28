create table source_table(
   id numeric,
   name varchar(50)
);

insert into source_table values (1, 'Amit');
insert into source_table values (2, 'Priya');
insert into source_table values (3, 'Rahul');
insert into source_table values (4, 'Sneha');
insert into source_table values (5, 'Rohit');
insert into source_table values (6, 'Neha');

create table target_table(
    id numeric,
	name varchar(50)
);

create or replace procedure copy_five_records()
language plpgsql
as $$
begin
    insert into target_table
	select *
	from source_table
	order by id
	limit 5;

end;
$$;

call copy_five_records();

select * from target_table;

select * from target_table;
delete from target_table
where id = 2;