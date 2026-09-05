-- Q3) Write down DML trigger to raise the error while inserting duplicate value in the table

create table if not exists friends(
    id INT Primary Key,
    name VARCHAR(50),
    email VARCHAR(50)
);

insert into friends values
(1, 'Ross Geller', 'ross@friends.com'),
(2, 'Rachel Green', 'rachel@friends.com');

create or replace function check_duplicate_email()
returns trigger
language plpgsql
as $$
begin
    if exists (select 1 from friends where email = new.email) then
        raise exception 'Duplicate email not allowed: %', new.email;
    end if;
    return new;
end;
$$;

create trigger trg_duplicate_email
before insert on friends
for each row
execute function check_duplicate_email();

-- allowed
insert into friends values (3, 'Chandler Bing', 'chandler@friends.com');

-- rejected: email already present
insert into friends values (4, 'Joey Tribbiani', 'ross@friends.com');

select * from friends;
