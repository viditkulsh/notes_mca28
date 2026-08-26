-- Progam 3. Lab 3. Trigger Programming
create trigger trg_check_duplicate
before insert on student
for each row
BEGIN
    if exists (
        select 1 from student
        where stud_id = new.stud_id
    ) then
        signal sqlstate '45000'
        set message_text = 'Duplicate student ID: ' || new.stud_id;
    end if;
end;
delimiter;