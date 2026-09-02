# ADBMS Practicals — Local Setup Notes

Working notes for running the SQL labs in this folder against a local Supabase (PostgreSQL) instance.

> Note: this file **is** tracked by git (only `supabase/` is ignored here), so keep real credentials out of it. The `postgres:postgres` login below is the Supabase CLI's fixed local default, not a secret.

## Start the local database

Run from `ADBMS/prac_adbms/` (the folder containing `supabase/`):

```bash
supabase start
```

## Ports

Ports come from [supabase/config.toml](supabase/config.toml). Note which speak **HTTP** (open in a browser) and which speak the **PostgreSQL wire protocol** (`psql` only):

| Port | Service | Protocol | Open in a browser? |
| --- | --- | --- | --- |
| 54421 | API gateway (Kong) | HTTP | Yes, but the root path returns 404 — it routes `/rest/v1`, `/auth/v1`, etc. |
| **54422** | **PostgreSQL** | **Postgres wire** | **No** — see the gotcha below |
| 54423 | Studio (web UI) | HTTP | **Yes — this is the one you want** |
| 54424 | Inbucket (test inbox) | HTTP | Yes |

## View the database in a browser

Open **<http://127.0.0.1:54423>** — it redirects to `/project/default`.

Use the **Table Editor** to browse and edit rows in `student`, `stud`, and `stud_tab`, or the **SQL Editor** to run queries without leaving the browser.

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

- **Port 54422 in a browser gives `ERR_EMPTY_RESPONSE`.** That is expected, not a fault. 54422 is PostgreSQL, which speaks its own binary protocol — the browser sends an HTTP request and gets back nothing it can parse. Use `psql` for 54422, and 54423 for a browser.
- **`supabase start` says "already running" but Studio is down.** The stack can end up *partially* running: if Docker runs out of memory (or restarts), the service containers are killed with exit code 137 while `supabase_db_*` restarts on its own. `supabase start` then sees the healthy `db` container, concludes the project is already running, prints its `Stopped services: [...]` list, and exits without starting anything.

  Check with `docker ps -a --filter name=prac_adbms`, then restart just the dead containers — no data is touched:

  ```bash
  docker start $(docker ps -aq --filter name=prac_adbms --filter status=exited)
  ```

  Prefer that over `supabase stop && supabase start`, which tears the stack down and round-trips the database through a dump/restore.
- `supabase_imgproxy_prac_adbms` was never created in this project. It only serves storage image transformations, so it is irrelevant to the SQL labs; `supabase stop && supabase start` would create it if ever needed.
- `trigger.sql` uses MySQL syntax (`SIGNAL SQLSTATE`, `DELIMITER`) and will not run on PostgreSQL as-is. The PostgreSQL equivalent is a `plpgsql` trigger function raising an exception — see `check_dup_stud()` in [lab3.sql](lab3.sql).
- Re-running a lab file fails if the objects already exist. Drop them first, or use `CREATE OR REPLACE` for functions and procedures.
