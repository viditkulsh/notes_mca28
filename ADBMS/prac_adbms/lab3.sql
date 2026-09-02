-- 4. Write down DML trigger to raise the error violating Check Constraints
create TABLE if not exists stud(
    stud_id Serial Primary Key,
    stud_name Varchar(100) Not Null,
    email VARCHAR(100) Not Null
);

create or replace function check_dup_stud()
returns trigger as $$
begin
    if exists (
        select 1
        from stud
        where email = new.email
    ) then
        raise exception 'Duplicate email: %', new.email;
    end if;
    return new;
end;
$$ language plpgsql;

drop trigger if exists trg_check_dup_stud on stud;

create trigger trg_check_dup_stud
before insert on stud
for each row
execute function check_dup_stud();

-- CALL insert_stud ('Mcqueen', 'mcqueen@example.com', 'Racing', 1, 99);
-- CALL insert_stud ('Tyrion Lannister', 'tyrion@example.com', 'MCA', 1, 100);
-- CALL insert_stud ('Arya Stark', 'arya@example.com', 'MCA', 1, 75);
-- CALL insert_stud ('Hodor', 'hodor@example.com', 'MCA', 1, 40);
-- CALL insert_stud ('Sansa Stark', 'sansa@example.com', 'MCA', 1, 95);

select * FROM stud;

insert into stud (stud_name, email) VALUES ('Jon Snow', 'arya@example.com'); -- This will raise an exception due to duplicate email   