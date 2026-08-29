# ADBMS Practicals — Local Setup Notes

Working notes for running the SQL labs in this folder against a local Supabase (PostgreSQL) instance.

> Local-only scratch notes; this file is listed in `.gitignore`.

## Start the local database

Run from `ADBMS/prac_adbms/` (the folder containing `supabase/`):

```bash
supabase start
```

Ports come from [supabase/config.toml](supabase/config.toml) — the database listens on **54422**, the API on 54421, and Studio on 54423.

## Run a SQL file

```bash
psql "postgresql://postgres:postgres@127.0.0.1:54422/postgres" -f <filename>.sql
```

Replace `<filename>.sql` with the lab you want to execute, for example:

```bash
psql "postgresql://postgres:postgres@127.0.0.1:54422/postgres" -f lab1.sql
```

## Open an interactive session

Useful for checking tables after a script has run:

```bash
psql "postgresql://postgres:postgres@127.0.0.1:54422/postgres"
```

Handy meta-commands once inside: `\dt` (list tables), `\df` (list functions and procedures), `\d student` (describe a table), `\q` (quit).

## Lab files

| File | Topic |
| --- | --- |
| [lab1.sql](lab1.sql) | `student` table and the `insert_stud` stored procedure |
| [lab3.sql](lab3.sql) | `stud` table with a `BEFORE INSERT` trigger rejecting duplicate emails |
| [trigger.sql](trigger.sql) | Trigger programming — duplicate `stud_id` check (MySQL-style syntax) |

## Gotchas

- `trigger.sql` uses MySQL syntax (`SIGNAL SQLSTATE`, `DELIMITER`) and will not run on PostgreSQL as-is. The PostgreSQL equivalent is a `plpgsql` trigger function raising an exception — see `check_dup_stud()` in [lab3.sql](lab3.sql).
- Re-running a lab file fails if the objects already exist. Drop them first, or use `CREATE OR REPLACE` for functions and procedures.
