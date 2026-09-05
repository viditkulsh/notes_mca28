-- Q5) Write down DML trigger to raise the error when user deletes
--     more than one record from table

create table if not exists waitress(
    id INT Primary Key,
    name VARCHAR(50),
    city VARCHAR(50)
);

insert into waitress values
(1, 'Max Black', 'Brooklyn'),
(2, 'Caroline Channing', 'Brooklyn'),
(3, 'Han Lee', 'Brooklyn'),
(4, 'Oleg Golishevsky', 'Manhattan');

create or replace function check_delete_limit()
returns trigger
language plpgsql
as $$
declare
    deleted_count INT;
begin
    select count(*) into deleted_count from deleted_rows;

    if deleted_count > 1 then
        raise exception 'Cannot delete more than 1 record at a time';
    end if;

    return null;
end;
$$;

create trigger trg_delete_limit
after delete on waitress
referencing old table as deleted_rows
for each statement
execute function check_delete_limit();

-- allowed: deletes one row
delete from waitress where id = 4;

-- rejected: deletes three rows
delete from waitress where city = 'Brooklyn';

select * from waitress;
