-- Q5) Write down DML trigger to raise the error when user deletes more than one record from table
-- RUN: psql "postgresql://postgres:postgres@127.0.0.1:5432/adbms" -f lca/lca1.sql

drop table if exists resturant;

create table resturant(
    id   INT Primary Key,
    name VARCHAR(50),
    city VARCHAR(50)
);

insert into resturant values
(1, 'Max','Brooklyn'),
(2, 'Caroline', 'Brooklyn'),
(3, 'Han Lee','Brooklyn'),
(4, 'Oleg',  'Manhattan');


create or replace function check_delete_limit()
returns trigger
language plpgsql
as $$
declare
    deleted_count INT;
begin
    select count(*) into deleted_count from deleted_rows;

    if deleted_count > 1 then
        raise exception 'Cannot delete more than 1 row';
    end if;


    return null;
end;
$$;

drop trigger if exists trg_delete_limit on resturant;

create trigger trg_delete_limit
after delete on resturant                     
referencing old table as deleted_rows        
for each statement                           
execute function check_delete_limit();


-- delete from resturant where id = 4;

delete from resturant where city = 'Brooklyn';

-- select * from resturant order by id;

