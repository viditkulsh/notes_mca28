# MITWPU MCA '28 — Student Notes

![Repository views](https://hits.sh/github.com/viditkulsh/mitwpu-mca28.svg?label=Repository%20views&color=blue)

Unofficial, student-maintained notes for the MCA (2026–28 batch) at MIT World Peace University.

These are **not** official course materials — they're personal notes, practice programs, and important questions collected by students while going through the course. Use them as a supplement to your own study, and expect the occasional mistake.

## What's inside

| Folder | Subject | Contents |
| --- | --- | --- |
| [ADBMS/](ADBMS/) | Advanced DBMS | [Important questions](ADBMS/imp_ques.md) by lecture date, and SQL lab practicals — stored procedures, triggers, and a local Supabase/PostgreSQL setup |
| [JAVA/](JAVA/) | Java | Theory [notes](JAVA/src/theory/notes.md) plus source under `src/` — `theory/` for concept demos (arrays, loops, utilities) and `practical/` for lab programs |
| [Python/](Python/) | Python | Programs covering data types, strings, arrays, dictionaries, and important questions |
| [Research_Methodology/](Research_Methodology/) | Research Methodology | Reference links and reading material on paper structure and the research gap framework |
| [peace/](peace/) | Peace Studies | Submission links and deadlines for CCA assignments |

## Repository layout

```
mitwpu-mca28/
├── ADBMS/
│   ├── imp_ques.md          # important questions, grouped by date
│   └── prac_adbms/          # SQL labs (*.sql) + local Supabase config
├── JAVA/
│   └── src/
│       ├── theory/          # concept demos and notes.md
│       └── practical/       # lab programs, named lab<n>_<date>.java
├── Python/                  # standalone .py programs per topic
├── Research_Methodology/    # links and PDFs
└── peace/                   # submission dates and links
```

## Running the code

- **Java** — compile and run from the `JAVA/` folder:
  ```bash
  javac -d bin src/theory/arrays/Array.java
  java -cp bin theory.arrays.Array
  ```
- **Python** — each file is standalone: `python3 Python/Strings.py`
- **SQL** — see [ADBMS/prac_adbms/](ADBMS/prac_adbms/) for the local PostgreSQL connection command.

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
