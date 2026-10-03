# MITWPU MCA '28 — Student Notes

![Repository views](https://hits.sh/github.com/viditkulsh/mitwpu-mca28.svg?label=Repository%20views&color=blue)

Unofficial, student-maintained notes for the MCA (2026–28 batch) at MIT World Peace University.

These are **not** official course materials — they're personal notes, practice programs, and important questions collected by students while going through the course. Use them as a supplement to your own study, and expect the occasional mistake.

## What's inside

| Folder | Subject | Contents |
| --- | --- | --- |
| [ADBMS/](ADBMS/) | Advanced DBMS | [Question bank](ADBMS/Question_Bank.md) (unit-wise and by lecture date) with [answers](ADBMS/Question_Bank_Ans.md), [important links](ADBMS/Important_Links.md) and exam dates, syllabus PDFs, lecture [slides](ADBMS/Slides/), SQL lab practicals (stored procedures, triggers, indexing) in [prac_adbms/](ADBMS/prac_adbms/), the LCA lab-test solution in [lca/](ADBMS/lca/), and theory SQL in [theo_adbms/](ADBMS/theo_adbms/) |
| [DCN/](DCN/) | Data Communication & Networking | Unit-wise [question bank](DCN/Question_Bank.md) with [answers](DCN/Question_Bank_Ans.md), the exam [syllabus](DCN/Syllabus.md), and the Module 1–2 lecture [slides](DCN/Slides/) |
| [JAVA/](JAVA/) | Java | [Question bank](JAVA/Question_Bank.md) with [answers](JAVA/Question_Bank_Ans.md), theory [notes](JAVA/src/theory/notes.md), and source under `src/` — `theory/` for concept demos (arrays, loops, utilities) and `practical/` for lab programs, one folder per lab |
| [Python/](Python/) | Python | [Question bank](Python/Question_Bank.md) with [answers](Python/Question_Bank_Ans.md), the mid-term [paper pattern](Python/Paper_pattern.pdf), unit-wise lecture [slides](Python/Slides/), and programs covering data types, strings, lists, dictionaries, conditionals, and functions |
| [Research_Methodology/](Research_Methodology/) | Research Methodology | [Reference links](Research_Methodology/Important_Links.md), lecture [slides](Research_Methodology/Slides/), and [reading material](Research_Methodology/Reference/) on paper structure and the research gap framework |
| [peace/](peace/) | Peace Studies | [Submission links and deadlines](peace/dates.md) for CCA assignments, plus the CCA brief and study material PDFs |
| [Exams/](Exams/) | — | Mid-term [syllabus, dates and timetable](Exams/MidTerm/Syllabus_MidTerm.md) |

The overall course structure is in [Stampped copy MCA 2026-28 Syllabus and structure.pdf](Stampped%20copy%20MCA%202026-28%20Syllabus%20and%20structure.pdf) at the repository root.

## Repository layout

```
mitwpu-mca28/
├── ADBMS/
│   ├── Question_Bank.md       # important questions — unit-wise, then by lecture date
│   ├── Question_Bank_Ans.md   # structured answers to the question bank
│   ├── Important_Links.md     # shared sheets, drive folders and exam dates
│   ├── Slides/                # lecture slides
│   ├── lca/                   # LCA lab-test solutions
│   ├── prac_adbms/            # SQL labs (q1–q7.sql, trigger.sql) + local Supabase setup
│   │   └── prac_notes.md      # how to start the local DB and run the .sql files
│   └── theo_adbms/            # SQL written during theory lectures
├── DCN/
│   ├── Question_Bank.md       # official question bank, unit-wise
│   ├── Question_Bank_Ans.md   # structured answers to the question bank
│   ├── Syllabus.md            # exam syllabus
│   └── Slides/                # Module 1–2 lecture slides
├── Exams/
│   └── MidTerm/               # mid-term syllabus, dates and timetable
├── JAVA/
│   ├── Question_Bank.md       # Unit 1 question bank (theory, MCQs, practicals)
│   ├── Question_Bank_Ans.md   # structured answers to the question bank
│   └── src/
│       ├── theory/            # concept demos and notes.md
│       └── practical/         # lab1/–lab3/ (one q<n>.java per question) + dated lab files
├── Python/
│   ├── Question_Bank.md       # important questions with CO and Bloom's level
│   ├── Question_Bank_Ans.md   # structured answers to the question bank
│   ├── Slides/                # lecture slides, one folder per unit
│   ├── basics/                # data types, strings, tuples, dictionaries
│   ├── func_prgm/             # function exercises (questions.txt + q1–q19.py)
│   └── lec/                   # questions solved in class, by date
├── Research_Methodology/
│   ├── Important_Links.md     # reference links
│   ├── Slides/                # Unit 1–2 lecture slides
│   └── Reference/             # books, a sample review paper, research gap workbook
└── peace/                     # CCA submission dates, brief and study material
```

Compiled Java output (`JAVA/bin/`) and the local Supabase state (`ADBMS/prac_adbms/supabase/`) are gitignored — you generate those locally.

## Running the code

- **Java** — compile and run from the `JAVA/` folder. Classes are packaged by their folder path, so use the fully qualified name. `-sourcepath src` lets `javac` find classes from other packages (for example `ArrayDemo` uses `theory.util.Stats`):
  ```bash
  javac -d bin -sourcepath src src/theory/arrays/Array.java
  java -cp bin theory.arrays.Array

  javac -d bin -sourcepath src src/practical/lab3/q1.java
  java -cp bin practical.lab3.q1
  ```
- **Python** — each file is standalone: `python3 Python/basics/Strings.py`
- **SQL** — start the local Supabase/PostgreSQL stack and run a file against it, as described in [ADBMS/prac_adbms/prac_notes.md](ADBMS/prac_adbms/prac_notes.md):
  ```bash
  cd ADBMS/prac_adbms && supabase start
  psql "postgresql://postgres:postgres@127.0.0.1:54422/postgres" -f q1.sql
  ```

## Contributing

Everyone is welcome to contribute — if you have notes, solved practicals, question banks, or anything else you think would help the batch, please add it.

1. Fork this repository.
2. Add your notes in the relevant subject folder (create a new folder if the subject doesn't exist yet).
3. Open a Pull Request with a short description of what you added.

Markdown (`.md`) is preferred for written notes, but source files, PDFs, and images are fine too. Please don't upload copyrighted material such as textbook scans.

To keep folders tidy, each subject keeps its questions in `Question_Bank.md`, their answers in `Question_Bank_Ans.md`, and lecture slides in a `Slides/` folder.

## Stay connected

If you found this useful, feel free to follow:

- GitHub: [@viditkulsh](https://github.com/viditkulsh)
- LinkedIn: [Vidit Kulshrestha](https://www.linkedin.com/in/vidit-kulshrestha)

---

Maintained by students, for students. Not affiliated with or endorsed by MIT-WPU.
