-- Q4) Write down DML trigger to raise the error violating Check Constraints

create table if not exists marks(
    stud_id INT Primary Key,
    stud_name VARCHAR(50),
    score INT
);

create or replace function check_score()
returns trigger
language plpgsql
as $$
begin
    if new.score < 0 or new.score > 100 then
        raise exception 'Score must be between 0 and 100, given %', new.score;
    end if;
    return new;
end;
$$;

create trigger trg_check_score
before insert or update on marks
for each row
execute function check_score();

-- allowed
insert into marks values (1, 'Sheldon Cooper', 100);
insert into marks values (2, 'Leonard Hofstadter', 85);

-- rejected: score above 100
insert into marks values (3, 'Howard Wolowitz', 120);

select * from marks;
