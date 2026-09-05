# MITWPU MCA '28 — Student Notes

![Repository views](https://hits.sh/github.com/viditkulsh/mitwpu-mca28.svg?label=Repository%20views&color=blue)

Unofficial, student-maintained notes for the MCA (2026–28 batch) at MIT World Peace University.

These are **not** official course materials — they're personal notes, practice programs, and important questions collected by students while going through the course. Use them as a supplement to your own study, and expect the occasional mistake.

## What's inside

| Folder | Subject | Contents |
| --- | --- | --- |
| [ADBMS/](ADBMS/) | Advanced DBMS | [Question bank](ADBMS/Ques_bank.md) grouped by lecture date, [important links](ADBMS/Important_Links.md), syllabus PDFs, SQL lab practicals (stored procedures, triggers) in [prac_adbms/](ADBMS/prac_adbms/), and theory SQL in [theo_adbms/](ADBMS/theo_adbms/) |
| [DCN/](DCN/) | Data Communication & Networking | Unit-wise [question bank](DCN/question_bank.md) plus the Module 1 lecture PDFs |
| [JAVA/](JAVA/) | Java | Theory [notes](JAVA/src/theory/notes.md) plus source under `src/` — `theory/` for concept demos (arrays, loops, utilities) and `practical/` for lab programs, one folder per lab |
| [Python/](Python/) | Python | Programs covering data types, strings, arrays, dictionaries, and important questions |
| [Research_Methodology/](Research_Methodology/) | Research Methodology | Reference links and reading material on paper structure and the research gap framework |
| [peace/](peace/) | Peace Studies | Submission links and deadlines for CCA assignments |
| [Class_Notes/](Class_Notes/) | — | Cross-subject housekeeping notes (notebook and lab-file requirements per subject) |

The overall course structure is in [Stampped copy MCA 2026-28 Syllabus and structure.pdf](Stampped%20copy%20MCA%202026-28%20Syllabus%20and%20structure.pdf) at the repository root.

## Repository layout

```
mitwpu-mca28/
├── ADBMS/
│   ├── Ques_bank.md         # important questions, grouped by date
│   ├── Important_Links.md   # shared sheets and drive folders
│   ├── prac_adbms/          # SQL labs (lab*.sql, q*.sql) + local Supabase setup
│   │   └── prac_notes.md    # how to start the local DB and run the .sql files
│   └── theo_adbms/          # SQL written during theory lectures
├── DCN/
│   └── question_bank.md     # official question bank, unit-wise
├── JAVA/
│   └── src/
│       ├── theory/          # concept demos and notes.md
│       └── practical/       # lab1/, lab2/, lab3/ — one q<n>.java per question
├── Python/                  # standalone .py programs per topic
├── Research_Methodology/    # links and PDFs
├── Class_Notes/             # what to maintain for each subject
└── peace/                   # submission dates and links
```

Compiled Java output (`JAVA/bin/`) and the local Supabase state (`ADBMS/prac_adbms/supabase/`) are gitignored — you generate those locally.

## Running the code

- **Java** — compile and run from the `JAVA/` folder. Classes are packaged by their folder path, so use the fully qualified name:
  ```bash
  javac -d bin src/theory/arrays/Array.java
  java -cp bin theory.arrays.Array

  javac -d bin src/practical/lab3/q1.java
  java -cp bin practical.lab3.q1
  ```
- **Python** — each file is standalone: `python3 Python/Strings.py`
- **SQL** — start the local Supabase/PostgreSQL stack and run a file against it, as described in [ADBMS/prac_adbms/prac_notes.md](ADBMS/prac_adbms/prac_notes.md):
  ```bash
  cd ADBMS/prac_adbms && supabase start
  psql "postgresql://postgres:postgres@127.0.0.1:54422/postgres" -f lab1.sql
  ```

## Contributing

Everyone is welcome to contribute — if you have notes, solved practicals, question banks, or anything else you think would help the batch, please add it.

1. Fork this repository.
2. Add your notes in the relevant subject folder (create a new folder if the subject doesn't exist yet).
3. Open a Pull Request with a short description of what you added.

Markdown (`.md`) is preferred for written notes, but source files, PDFs, and images are fine too. Please don't upload copyrighted material such as textbook scans.

## Stay connected

If you found this useful, feel free to follow:

- GitHub: [@viditkulsh](https://github.com/viditkulsh)
- LinkedIn: [Vidit Kulshrestha](https://www.linkedin.com/in/vidit-kulshrestha)

---

Maintained by students, for students. Not affiliated with or endorsed by MIT-WPU.
