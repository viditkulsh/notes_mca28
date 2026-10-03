# ADBMS — Answers to Important Questions

Structured, exam-oriented answers to every question in [Question_Bank.md](Question_Bank.md). Numbering matches the question bank exactly: unit-wise answers are labelled by unit (U2-Q3 answers Unit 2, question 3), and the date-wise answers keep the continuous numbering, so question 9 here answers question 9 there. Where a date-wise answer already covers a unit-wise question in full, the unit-wise entry points to it instead of repeating it.

Each answer follows the same shape: **Definition → Explanation / Diagram → Key points or comparison table → Advantages & limitations → One-line summary**, so it can be reproduced under exam time pressure.

> Student-written notes. Cross-check terminology against your class notes and the prescribed textbook (Silberschatz, Korth & Sudarshan, *Database System Concepts*) before an exam.

## Contents

- [Unit 1 — Database System Architectures](#unit-1--database-system-architectures)
  - [U1-Q1. Database System Architecture — diagram and short note](#u1-q1-database-system-architecture--diagram-and-short-note)
  - [U1-Q2. Client-server architecture](#u1-q2-client-server-architecture)
  - [U1-Q3. Server system vs client-server](#u1-q3-server-system-vs-client-server)
  - [U1-Q4. Server system architecture and its layers](#u1-q4-server-system-architecture-and-its-layers)
  - [U1-Q5. Distributed vs parallel vs server system architecture](#u1-q5-distributed-vs-parallel-vs-server-system-architecture)
  - [U1-Q6. Distributed system architecture](#u1-q6-distributed-system-architecture)
- [Unit 2 — Parallel and Distributed Databases](#unit-2--parallel-and-distributed-databases)
  - [U2-Q1. Types of I/O parallelism](#u2-q1-types-of-io-parallelism)
  - [U2-Q2. Without vs with I/O parallelism](#u2-q2-without-vs-with-io-parallelism)
  - [U2-Q3. Inter-query vs intra-query parallelism](#u2-q3-inter-query-vs-intra-query-parallelism)
  - [U2-Q4. Inter-query parallelism](#u2-q4-inter-query-parallelism)
  - [U2-Q5. Intra-query parallelism](#u2-q5-intra-query-parallelism)
  - [U2-Q6. Storage and consistency in a distributed database](#u2-q6-storage-and-consistency-in-a-distributed-database)
  - [U2-Q7. How 2PC ensures atomicity and consistency](#u2-q7-how-2pc-ensures-atomicity-and-consistency)
  - [U2-Q8. Distributed transactions and 2PC](#u2-q8-distributed-transactions-and-2pc)
  - [U2-Q9. Concurrency control and consistency](#u2-q9-concurrency-control-and-consistency)
  - [U2-Q10. Types of schedules, the scheduler and serializability](#u2-q10-types-of-schedules-the-scheduler-and-serializability)
- [Unit 3 — Object-Oriented Databases](#unit-3--object-oriented-databases)
  - [U3-Q1. DBMS vs object-oriented system](#u3-q1-dbms-vs-object-oriented-system)
  - [U3-Q2. Object structure and OID](#u3-q2-object-structure-and-oid)
  - [U3-Q3. Type constructors in OODBMS](#u3-q3-type-constructors-in-oodbms)
  - [U3 — 8 Marks Question. Student, Teacher and University with tuple constructors](#u3--8-marks-question-student-teacher-and-university-with-tuple-constructors)
- [10 Aug 2026 — Database & Client-Server Architecture](#10-aug-2026--database--client-server-architecture)
  - [Q1. Difference between Database System Architecture and Client-Server Architecture](#q1-difference-between-database-system-architecture-and-client-server-architecture)
  - [Q2. Short note on Client-Server Architecture](#q2-short-note-on-client-server-architecture)
- [11 Aug 2026 — Three-Tier & Distributed Systems](#11-aug-2026--three-tier--distributed-systems)
  - [Q3. Three-tier architecture with a neat diagram](#q3-three-tier-architecture-with-a-neat-diagram)
  - [Q4. Short note on Distributed Database System](#q4-short-note-on-distributed-database-system)
- [18 Aug 2026 — Replication, Proxies & Parallel Databases](#18-aug-2026--replication-proxies--parallel-databases)
  - [Q5. Short note on Replica](#q5-short-note-on-replica)
  - [Q6. Use of a Proxy Server](#q6-use-of-a-proxy-server)
  - [Q7. Client-Server vs Server System vs Client System Architecture](#q7-client-server-vs-server-system-vs-client-system-architecture)
  - [Q8. Parallel Database Architecture in e-commerce](#q8-parallel-database-architecture-in-e-commerce)
- [21 Aug 2026 — Distributed Storage & Transactions](#21-aug-2026--distributed-storage--transactions)
  - [Q9. Distributed Data Storage, Distributed Transactions and 2PC](#q9-distributed-data-storage-distributed-transactions-and-2pc)
- [24 Aug 2026 — Concurrency Control](#24-aug-2026--concurrency-control)
  - [Q10. Short note on Concurrency and types of Locking](#q10-short-note-on-concurrency-and-types-of-locking)
  - [Q11. Concurrency Control in detail](#q11-concurrency-control-in-detail)
  - [Q12. How Concurrency Control supports the transaction process](#q12-how-concurrency-control-supports-the-database-transaction-process)
- [31 Aug 2026 — OOPS](#31-aug-2026--oops)
  - [Q13. OODBMS vs RDBMS with a real-world example](#q13-oodbms-vs-rdbms-with-a-real-world-example)
  - [Q14. Object-oriented structure — Attributes, Methods, Relationships](#q14-object-oriented-structure--attributes-methods-relationships)

---

## Unit 1 — Database System Architectures

### U1-Q1. Database System Architecture — diagram and short note

*Alternatives:* draw the architecture, write a short note on it, or compare it with client-server architecture. The comparison with client-server architecture (and the ANSI/SPARC three-level view) is answered in full in [Q1](#q1-difference-between-database-system-architecture-and-client-server-architecture); the diagram and short note are below.

**Definition**

Database system architecture is the overall structure of a DBMS — the functional components it is built from, how they interact, and how they connect the different kinds of users to the data stored on disk. Its two main functional parts are the **query processor** and the **storage manager**.

**Diagram — overall structure of a database system**

```
   Naive users      Application       Sophisticated      Database
   (clerks, web     programmers       users (analysts)   administrator
    users)
        |                |                  |                  |
        v                v                  v                  v
   Application      Application       Query tools        Administration
   interfaces       programs                             tools
        |                |                  |                  |
        +----------------+--------+---------+------------------+
                                  |
   +------------------------------v-------------------------------+
   |                       QUERY PROCESSOR                        |
   |  DDL interpreter   DML compiler & organiser   Query          |
   |                    (parsing, optimisation)    evaluation     |
   |                                               engine         |
   +------------------------------+-------------------------------+
                                  |
   +------------------------------v-------------------------------+
   |                       STORAGE MANAGER                        |
   |  Authorisation &     Transaction manager      File manager   |
   |  integrity manager   (concurrency, recovery)  Buffer manager |
   +------------------------------+-------------------------------+
                                  |
   +------------------------------v-------------------------------+
   |                         DISK STORAGE                         |
   |  Data files   Data dictionary   Indices   Statistical data   |
   +--------------------------------------------------------------+
```

**Components**

| Component | Part | Role |
|---|---|---|
| DDL interpreter | Query processor | Interprets DDL statements and records the definitions (schema) in the data dictionary |
| DML compiler & organiser | Query processor | Translates DML/SQL into an evaluation plan of low-level instructions and picks the cheapest plan (query optimisation) |
| Query evaluation engine | Query processor | Executes the low-level instructions produced by the DML compiler |
| Authorisation & integrity manager | Storage manager | Checks integrity constraints and users' authority to access data |
| Transaction manager | Storage manager | Keeps the database consistent despite failures (recovery) and concurrent executions (concurrency control) |
| File manager | Storage manager | Allocates disk space and manages the data structures used to store data |
| Buffer manager | Storage manager | Fetches data from disk into main memory and decides what to keep cached |
| Data files | Disk storage | Store the database itself |
| Data dictionary | Disk storage | Stores metadata — the schema, constraints and authorisations |
| Indices | Disk storage | Give fast access to records with particular values |
| Statistical data | Disk storage | Table sizes and value distributions used by the optimiser |

**Users of the system**

- **Naive users** — interact through application interfaces (forms, ATMs, web pages).
- **Application programmers** — write application programs that embed DML calls.
- **Sophisticated users** — query the database directly with query tools and SQL.
- **Database administrator (DBA)** — defines the schema, storage structures and authorisation, and maintains the system with administration tools.

**How the architecture is deployed**

The same components can run in different physical configurations — the subject of this unit:

- **Centralised** — everything runs on one computer (a single-user desktop DBMS, or a multi-user server).
- **Client-server** — the DBMS runs on a server and clients send requests ([Q2](#q2-short-note-on-client-server-architecture)), in two-tier or three-tier form ([Q3](#q3-three-tier-architecture-with-a-neat-diagram)).
- **Parallel** and **distributed** — the database is spread over many processors or sites ([U1-Q5](#u1-q5-distributed-vs-parallel-vs-server-system-architecture)).

**Summary:** A database system is built from a query processor (DDL interpreter, DML compiler, evaluation engine) and a storage manager (authorisation, transaction, file and buffer managers) over disk storage (data files, data dictionary, indices, statistics), serving naive users, programmers, analysts and the DBA.

---

### U1-Q2. Client-server architecture

Answered in full in [Q2](#q2-short-note-on-client-server-architecture). Points to hit: definition (clients request, a server running the DBMS responds), the diagram, the request–response flow (only result sets travel back), two-tier vs three-tier ([Q3](#q3-three-tier-architecture-with-a-neat-diagram)), advantages (centralised data, security, administration) and limitations (single point of failure, server bottleneck, network dependency).

---

### U1-Q3. Server system vs client-server

"System server" here means the **server system architecture** — the internal organisation of the server machine. [Q7](#q7-client-server-vs-server-system-vs-client-system-architecture) covers both in detail; the focused comparison is:

| Basis | Server System Architecture | Client-Server Architecture |
|---|---|---|
| Scope | Only the inside of the server | The whole system — clients, network and server |
| Question it answers | How is the server organised to serve many requests at once? | How is the work divided between machines that request and a machine that serves? |
| Main types | Transaction-server (query-server) and data-server | Two-tier, three-tier, n-tier |
| Main components | Server processes, lock manager, database writer, log writer, checkpoint and process-monitor processes, shared memory | Client machines, network, database server (plus an application server in three-tier) |
| Focus | Concurrency, throughput and recovery on the server | Communication, resource sharing, centralised control |
| Example | An Oracle or PostgreSQL instance with its background processes and shared buffers | A browser or app talking to a web server backed by a database server |

**Relationship:** server system architecture is the detailed design of the "server" box inside a client-server architecture — its diagram is in [U1-Q4](#u1-q4-server-system-architecture-and-its-layers).

**Summary:** Client-server architecture is the overall request-response model; server system architecture is how the server half of that model is built internally.

---

### U1-Q4. Server system architecture and its layers

**Definition**

Server system architecture describes how a database **server** is organised internally so that it can accept requests from many clients concurrently and process them efficiently and reliably. Server systems are of two kinds: **transaction servers** (query servers) and **data servers**.

**1. Transaction-server (query-server) architecture**

Clients send SQL queries or remote procedure calls; the server executes them and ships back only the results. Almost all relational DBMSs (Oracle, PostgreSQL, SQL Server, MySQL) are built this way.

**Diagram — processes and shared memory of a transaction server**

```
             clients (user processes) over ODBC / JDBC
                  |               |               |
             +----v----+     +----v----+     +----v----+
             | server  |     | server  |     | server  |  one per connection,
             | process |     | process |     | process |  or a thread pool
             +----+----+     +----+----+     +----+----+
                  |               |               |
   +--------------v---------------v---------------v-------------+
   |                       SHARED MEMORY                        |
   |  buffer pool | lock table | log buffer | query plan cache  |
   +------^--------------^--------------^--------------^--------+
          |              |              |              |
    +-----+------+ +-----+------+ +-----+------+ +-----+------+
    |  database  | |    lock    | |    log     | | checkpoint |
    |   writer   | |  manager   | |   writer   | |  process   |
    +-----+------+ +------------+ +-----+------+ +------------+
          |                             |
          v                             v
    [ data files ]                 [ log disk ]

   process monitor: watches all the processes above and recovers any that fail
```

**Role of each process**

| Process / structure | Role |
|---|---|
| Server processes | Receive user queries (transactions), execute them and send the results back; may be multithreaded |
| Lock manager process | Grants and releases locks and detects deadlocks, using the lock table in shared memory |
| Database writer process | Continuously writes modified (dirty) buffer blocks back to disk |
| Log writer process | Writes log records from the log buffer to stable storage; server processes only add records to the log buffer |
| Checkpoint process | Performs periodic checkpoints so that recovery after a crash is faster |
| Process monitor process | Watches the other processes; if one fails, it performs recovery actions for it (e.g. aborts its transaction) and restarts it |
| Shared memory | Holds the buffer pool, lock table, log buffer and cached query plans so that all server processes share them; access is protected by mutual exclusion (semaphores or latches) |

**Layers of a server system**

The same server can also be described as a stack of layers, each using the one below it:

```
   +-------------------------------------------------------+
   | 1. Communication layer    accept connections,         |  listener, ODBC/JDBC
   |                           authenticate clients        |
   +-------------------------------------------------------+
   | 2. Query-processing layer parse, optimise and         |  server processes
   |                           execute SQL                 |
   +-------------------------------------------------------+
   | 3. Transaction layer      locking, logging,           |  lock manager, log writer,
   |                           commit and rollback         |  checkpoint, process monitor
   +-------------------------------------------------------+
   | 4. Buffer/storage layer   buffer pool, file and       |  database writer,
   |                           index management            |  buffer manager
   +-------------------------------------------------------+
   | 5. Physical storage       data files and log files    |  disks
   +-------------------------------------------------------+
```

**2. Data-server architecture**

Used where clients are powerful workstations on a fast LAN and the work is computation-heavy (CAD, object-oriented databases). The server **ships data** — whole pages or individual objects — to the clients, which process it themselves and send updates back. Design issues:

- **Page shipping vs item shipping** — sending a whole page acts as prefetching (cheap per object) but may lock more than needed.
- **Adaptive lock granularity** — lock whole pages or individual items, escalating or de-escalating as needed.
- **Data caching** — clients keep data between transactions but must check that it is still current (cache coherency).
- **Lock caching** — clients keep locks between transactions; the server calls back a lock when another client needs it.

| Basis | Transaction server | Data server |
|---|---|---|
| What travels over the network | Queries go in, result sets come out | Pages or objects go out, updates come back |
| Where processing happens | On the server | On the clients |
| Typical clients | Thin clients, web applications | Powerful workstations |
| Typical systems | Relational DBMSs | Object-oriented DBMSs, CAD systems |
| Main challenge | Server load | Keeping caches and locks coherent across clients |

**Advantages of a server system:** centralised control of data, security and backup; many clients share one consistent copy; background processes keep writing, logging and recovery off the user's critical path.

**Limitations:** the server is a single point of failure and a potential bottleneck; scaling means a bigger machine, or moving to a parallel or distributed system ([U1-Q5](#u1-q5-distributed-vs-parallel-vs-server-system-architecture)).

**Summary:** A server system is either a transaction server — server processes plus lock manager, database writer, log writer, checkpoint and process-monitor processes sharing a buffer pool, lock table and log buffer — or a data server that ships pages or objects to clients; it can also be described as communication, query-processing, transaction, buffer/storage and physical-storage layers.

---

### U1-Q5. Distributed vs parallel vs server system architecture

**Definitions**

- **Server system architecture** — a single (possibly multi-core) server machine holds the database and serves many clients over a network. Data and control are centralised ([U1-Q4](#u1-q4-server-system-architecture-and-its-layers)).
- **Parallel system** — many processors and disks *within one system at one site*, connected by a very fast interconnect, work together as one database machine to improve throughput and response time. Architectures: shared memory, shared disk, shared nothing, hierarchical ([Q8](#q8-parallel-database-architecture-in-e-commerce)).
- **Distributed system** — the database is spread over several **geographically separate sites**, each with its own computer, DBMS and local data, connected by a LAN or WAN; the sites cooperate so that they appear as one logical database ([Q4](#q4-short-note-on-distributed-database-system)).

**Diagram**

```
 SERVER SYSTEM         PARALLEL SYSTEM              DISTRIBUTED SYSTEM
                       (one site)                   (many sites)

 client client client  +-----------------------+          Site A
    \     |     /      | P1   P2   P3   P4     |          (Pune)
     \    |    /       | M1   M2   M3   M4     |         /      \
   +-----------+       | D1   D2   D3   D4     |    WAN /        \ WAN
   |  server   |       |                       |       /          \
   |  (DBMS)   |       | high-speed            |   Site B ------ Site C
   +-----+-----+       | interconnect          |  (Mumbai)  WAN  (Delhi)
         |             +-----------------------+
     [database]        P = processor                each site: own DBMS
                       M = memory, D = disk         and its own data
```

**Comparison table**

| Basis | Server System Architecture | Parallel System | Distributed System |
|---|---|---|---|
| Basic idea | One server serves many clients | Many processors and disks act as one database machine | Many independent sites act as one logical database |
| Location | One machine | One site (same room or rack) | Geographically separate sites |
| Interconnect | Client network only | Very fast, reliable bus or switch | LAN/WAN — slower and less reliable |
| Coupling | Centralised | Tightly coupled | Loosely coupled |
| Autonomy | — | Nodes have no autonomy; one DBMS controls all | Each site has local autonomy |
| Data placement | All data on the server's disks | Partitioned across disks (I/O parallelism) | Fragmented and/or replicated across sites |
| Main goal | Shared, controlled access to centralised data | Performance — speed-up and scale-up | Availability, local autonomy, data close to its users |
| Transactions | Local only | Local (inside one system) | Local and global; global ones need a commit protocol (2PC) |
| Effect of a failure | Server failure stops everything | A failed node is handled inside the system | The other sites keep working |
| Typical use | Departmental or small-business database | Data warehouses, large OLTP, analytics | Multi-branch banks, global applications |
| Examples | A single PostgreSQL or MySQL server | Teradata, Oracle RAC, Greenplum | A bank's branch databases; Google Spanner, Apache Cassandra |

**Key point:** parallel and distributed systems both use many machines; they differ in *geography* (one site vs many), *interconnect speed* and *autonomy* (one DBMS vs cooperating local DBMSs). The server system is the single-machine baseline that both grow out of.

**Summary:** A server system centralises the database on one machine; a parallel system spreads one database over tightly coupled processors and disks at one site for speed; a distributed system spreads it over autonomous sites connected by a network for availability and locality.

---

### U1-Q6. Distributed system architecture

Answered in full in [Q4](#q4-short-note-on-distributed-database-system) — definition, diagram, homogeneous vs heterogeneous systems, transparencies, fragmentation and replication, advantages and disadvantages. Two terms to add for a complete short note:

- **Local transaction** — accesses data only at the site where it started; **global transaction** — accesses data at several sites and is coordinated with a commit protocol such as 2PC ([Q9](#q9-distributed-data-storage-distributed-transactions-and-2pc)).
- Sites are linked by a **LAN** (same building, fast) or a **WAN** (across cities, slower and less reliable), which is why distributed query processing tries to minimise the data shipped between sites.

---

## Unit 2 — Parallel and Distributed Databases

### U2-Q1. Types of I/O parallelism

**Definition**

**I/O parallelism** reduces the time needed to read relations from disk by **partitioning** each relation across several disks, so that the disks can be read at the same time. The usual form is **horizontal partitioning**: the tuples of a relation are divided among *n* disks D0, D1, …, Dn−1, and each tuple lives on exactly one disk.

**Why it is needed**

- Disk I/O is the slowest step of query processing; one disk can transfer only so many MB per second.
- Large relations (gigabytes to terabytes) take hours to scan from a single disk.
- With n disks, about n times as much data can be read per second, so a full scan takes about 1/n of the time.
- It is the foundation of parallel query processing — each processor works on the partition stored on its own disk(s).

**Partitioning techniques**

1. **Round-robin** — the relation is scanned in any order and the tuples are dealt out to the disks in turn, like cards: with tuples counted from 0, the i-th tuple goes to disk D(i mod n).
2. **Hash partitioning** — one or more attributes are chosen as the **partitioning attributes**; a hash function h with range 0 … n−1 is applied to them, and the tuple goes to disk D(h(value)).
3. **Range partitioning** — a **partitioning vector** [v0, v1, …, vn−2] on a partitioning attribute A assigns contiguous ranges of A to the disks: a tuple with A < v0 goes to D0, a tuple with vi ≤ A < vi+1 goes to Di+1, and a tuple with A ≥ vn−2 goes to Dn−1.

**Example — STUDENT(roll_no, name, …) on 3 disks**

| Technique | Rule | Where the tuples go |
|---|---|---|
| Round-robin | Deal tuples out in turn | 1st, 4th, 7th … tuple → D0; 2nd, 5th, 8th … → D1; 3rd, 6th, 9th … → D2 |
| Hash on roll_no | h(roll_no) = roll_no mod 3 | roll_no 102 → D0, 103 → D1, 101 → D2 |
| Range on roll_no | Vector [100, 200] | roll_no < 100 → D0, 100–199 → D1, ≥ 200 → D2 |

**Which access patterns each technique suits**

| Technique | Full scan of the relation | Point query (A = v) | Range query (v1 ≤ A ≤ v2) | Load balance |
|---|---|---|---|---|
| Round-robin | Best — all disks share the work equally | Poor — every disk must be searched | Poor — every disk must be searched | Perfectly even |
| Hash | Good, if the hash function spreads values well | Best — only one disk (when A is the partitioning attribute) | Poor — values are scattered, so every disk is searched | Even, unless many tuples share a value |
| Range | Good | Good — one disk | Best — only the disks holding the range are touched | Can be uneven (skew) |

**Skew — the main problem**

- **Attribute-value skew** — many tuples share the same value of the partitioning attribute, so they all land on one disk (affects hash and range partitioning).
- **Partition skew** — a badly chosen range vector puts too many tuples in one partition, or one "hot" range receives most of the queries (execution skew).
- Remedies: build a **balanced partitioning vector** from a sorted sample or a histogram, or use **virtual processors** — many small partitions assigned round-robin to the real disks.

**Advantages**

- Faster scans — read bandwidth grows with the number of disks.
- Point and range queries can be confined to one or a few disks (hash/range), leaving the other disks free for other queries.
- Scales to very large relations by adding disks.
- Provides the partitioned data that parallel sort, join and aggregation algorithms need.

**Disadvantages**

- Partitioning, and re-partitioning when disks are added, takes time and effort.
- More disks mean more chances of a disk failure, so partitions need RAID or replication.
- Choosing the partitioning attribute and vector requires knowledge of the query workload.

**Limitations**

- Speed-up is limited by skew — the slowest (largest) partition decides the response time.
- Small relations gain nothing: spreading a few blocks over many disks only adds overhead, so small relations are kept on one or a few disks.
- Hash and range partitioning help only queries on the partitioning attribute; queries on other attributes still touch every disk.
- Round-robin, though perfectly balanced, can never direct a point or range query to a single disk.

**Summary:** I/O parallelism partitions a relation across disks — round-robin for even scans, hash for point queries, range for range queries — to multiply read bandwidth, with skew as its main limitation.

---

### U2-Q2. Without vs with I/O parallelism

**Without I/O parallelism**, the whole relation is stored on one disk, so every query that scans it is limited to that disk's transfer rate and requests queue behind each other. **With I/O parallelism**, the relation is partitioned across several disks (round-robin, hash or range — [U2-Q1](#u2-q1-types-of-io-parallelism)) and all the disks are read at the same time.

**Diagram**

```
   WITHOUT I/O PARALLELISM           WITH I/O PARALLELISM (4 disks)

            query                                   query
              |                                       |
         +----v----+             +--------------------v--------------------+
         |  DBMS   |             |          DBMS - parallel scan           |
         +----+----+             +----+----------+----------+----------+---+
              |                       |          |          |          |
         +----v----+             +----v---+ +----v---+ +----v---+ +----v---+
         | Disk 0  |             |   D0   | |   D1   | |   D2   | |   D3   |
         |  10 GB  |             | 2.5 GB | | 2.5 GB | | 2.5 GB | | 2.5 GB |
         +---------+             +--------+ +--------+ +--------+ +--------+

   one disk, blocks read in turn    all four disks read at the same time
```

**Worked example**

A 10 GB relation is scanned; one disk transfers 100 MB/s.

| Setup | Data per disk | Scan time |
|---|---|---|
| Without I/O parallelism (1 disk) | 10 GB | 10,000 MB ÷ 100 MB/s = **100 s** |
| With I/O parallelism, 4 disks | 2.5 GB | 2,500 MB ÷ 100 MB/s = **25 s** |
| With I/O parallelism, 10 disks | 1 GB | 1,000 MB ÷ 100 MB/s = **10 s** |

This is ideal (linear) speed-up. In practice it is a little lower because of start-up costs, interference between disks that share a bus or controller, and skew (one partition larger than the rest).

**Comparison table**

| Basis | Without I/O parallelism | With I/O parallelism |
|---|---|---|
| Data placement | Whole relation on one disk | Relation partitioned over n disks |
| Read bandwidth | One disk's rate | About n × one disk's rate |
| Full-scan time | T | About T ÷ n (ideal) |
| Point and range queries | Served by the single disk (with an index) | Can be directed to one or a few disks (hash/range partitioning) |
| Concurrent queries | Queue on the same disk | Different queries can use different disks |
| Bottleneck | Disk I/O | Skew, interconnect, CPU |
| Effect of a disk failure | Whole relation unavailable | One partition unavailable (unless RAID or replication is used) |
| Cost and complexity | Low | Higher — more disks, partitioning design |
| Suitable for | Small databases, light load | Large databases, data warehouses, decision support, heavy OLTP |

**Summary:** Without I/O parallelism one disk's bandwidth caps every scan; partitioning the relation over n disks lets them be read together, cutting scan time to about 1/n (100 s → 25 s on 4 disks), at the cost of more hardware and partitioning design.

---

### U2-Q3. Inter-query vs intra-query parallelism

**Definitions**

- **Inter-query parallelism** — *different* queries or transactions execute in parallel with one another, each on a different processor. It increases **throughput**, but each individual query runs no faster.
- **Intra-query parallelism** — a *single* query is split into parts that execute in parallel on several processors and disks. It reduces the **response time** of long-running queries.

**Diagram**

```
   INTER-QUERY PARALLELISM              INTRA-QUERY PARALLELISM

   Q1 ---> P1                           Q1 is split into parts:
   Q2 ---> P2                              part 1 ---> P1 --+
   Q3 ---> P3                              part 2 ---> P2 --+--> combine --> result
   Q4 ---> P4                              part 3 ---> P3 --+
   (many queries at the same time)         part 4 ---> P4 --+
```

**Comparison table**

| Basis | Inter-query parallelism | Intra-query parallelism |
|---|---|---|
| What runs in parallel | Different queries/transactions | Parts of one query |
| Main goal | Higher throughput (more transactions per second) | Lower response time of one query |
| Speed of a single query | Not improved | Improved |
| Best suited to | OLTP — many small, concurrent transactions | Decision support / OLAP — large, complex queries |
| Difficulty | Easiest form; an extension of concurrent transaction processing | Needs parallel algorithms for sort, join and aggregation, and partitioned data |
| Main overheads | Locking, logging and cache coherency across processors | Partitioning data, combining partial results, skew |
| Sub-types | — | Intra-operation and inter-operation parallelism |
| Example | Thousands of shoppers placing orders at once on an e-commerce site | One monthly sales report joining a billion order rows |

**Summary:** Inter-query parallelism runs many queries side by side to raise throughput; intra-query parallelism splits one query across processors to cut its response time.

---

### U2-Q4. Inter-query parallelism

**Definition**

In **inter-query parallelism**, different queries or transactions execute in parallel with one another. Each query is still executed by one processor, but many queries run at the same time on different processors.

**How it works**

- Incoming transactions are assigned to whichever processor is free.
- On a **shared-memory** machine this is the natural extension of ordinary concurrent processing — the same DBMS code, lock table and buffer pool serve all processors.
- On **shared-disk** or **shared-nothing** machines the processors must coordinate **locking and logging** by passing messages, and must keep their buffer caches consistent. This is the **cache-coherency** problem: a processor must never read a stale copy of a page that another processor has updated.
- A simple cache-coherency protocol for shared disk: lock a page before reading or writing it; read the page from disk when the lock is obtained (so the latest version is seen); write the page back to disk before releasing an exclusive lock.

**Diagram**

```
   T1 (order)   T2 (payment)   T3 (search)   T4 (login)
       |             |              |             |
       v             v              v             v
     +----+        +----+         +----+        +----+
     | P1 |        | P2 |         | P3 |        | P4 |
     +----+        +----+         +----+        +----+
       |             |              |             |
       +-------------+------+-------+-------------+
                            |
             shared lock table and log (coordinated)
                            |
                        [database]
```

**Advantages**

- Increases throughput — more transactions per second as processors are added (scale-up for transaction processing).
- The easiest form of parallelism to support; existing DBMSs need few changes, especially on shared memory.
- Ideal for OLTP workloads with many short, independent transactions.

**Limitations**

- Does not make any single query faster — a long query takes as long as before.
- Contention for locks and other shared resources grows with the number of processors.
- Cache coherency and distributed locking add overhead on shared-disk and shared-nothing systems.

**Example:** during a sale, an e-commerce database runs thousands of independent order, payment and search transactions at once, each on whichever processor is free.

**Summary:** Inter-query parallelism executes different transactions simultaneously on different processors, raising throughput for OLTP while each query's own response time stays the same.

---

### U2-Q5. Intra-query parallelism

**Definition**

In **intra-query parallelism**, a single query is executed in parallel on multiple processors and disks, which speeds up long-running queries. A query plan is a tree of operations, so it can be parallelised in two complementary ways.

**1. Intra-operation parallelism** — the execution of *each individual operation* (sort, select, project, join, aggregate) is parallelised by partitioning its input data across processors.

- **Parallel sort** — range-partition the relation and sort each partition locally, then concatenate; or sort each partition locally and merge the sorted runs.
- **Parallel join** — *partitioned join* for equi-joins (both relations are partitioned on the join attribute with the same function, then each processor joins its own pair of partitions); *fragment-and-replicate join* for other join conditions (one relation is partitioned and the other is copied to every processor).
- **Parallel selection, projection and aggregation** — each processor works on its own partition, and partial aggregates are combined at the end.
- The degree of parallelism can be very high — it grows with the size of the data.

**2. Inter-operation parallelism** — *different operations* of the same query run in parallel.

- **Pipelined parallelism** — the output tuples of one operation are passed to the next operation as soon as they are produced, so the two operations run at the same time on different processors.
- **Independent parallelism** — operations that do not depend on each other run in parallel.
- The degree of parallelism is limited by the number of operations in the plan.

**Diagram — query r1 ⋈ r2 ⋈ r3 ⋈ r4**

```
   INDEPENDENT PARALLELISM                PIPELINED PARALLELISM

   P1: temp1 = r1 ⋈ r2  --+               P1: r1 ⋈ r2
                          +--> P3:              |  tuples passed on as produced
   P2: temp2 = r3 ⋈ r4  --+    temp1 ⋈ temp2    v
                                          P2: ... ⋈ r3
   P1 and P2 run at the same time;              |  tuples passed on as produced
   P3 combines their results                    v
                                          P3: ... ⋈ r4  --> result
```

**Intra-operation vs inter-operation parallelism**

| Basis | Intra-operation parallelism | Inter-operation parallelism |
|---|---|---|
| What is parallelised | One operation, over partitions of its data | Different operations of the plan |
| Forms | Parallel sort, join, selection, aggregation | Pipelined and independent |
| Degree of parallelism | High — grows with data size | Low — limited by the number of operations |
| Scales to many processors | Yes | No |
| Main limitation | Partitioning cost, skew | Blocking operations (sort, aggregation) cannot pipeline; plans have few operations |

**Advantages:** cuts the response time of large decision-support queries; uses all processors for one heavy query; intra-operation parallelism scales with data size.

**Limitations:** start-up and coordination costs; skew between partitions; blocking operations break pipelines; little benefit for small, short queries.

**Example:** for "total sales per region for the year" over a billion order rows, each processor scans and aggregates its own partition (intra-operation), and the scan feeds the aggregation as tuples are produced (pipelined) — minutes instead of hours.

**Summary:** Intra-query parallelism speeds up one query either by parallelising each operation over data partitions (intra-operation) or by running different operations together through pipelining or independent execution (inter-operation).

---

### U2-Q6. Storage and consistency in a distributed database

**Part 1 — How data is stored**

Answered in full in [Q9, Part A](#part-a--distributed-data-storage). In short:

- **Fragmentation** — split a relation horizontally (rows), vertically (columns, repeating the key) or both, and store each fragment at the sites that use it.
- **Replication** — keep copies of a fragment at several sites (full, partial or none) — see [Q5](#q5-short-note-on-replica).
- **Allocation** — decide which fragment or replica lives at which site.
- All of this is hidden from users by **location, fragmentation and replication transparency** ([Q4](#q4-short-note-on-distributed-database-system)).

**Part 2 — How data consistency is maintained**

When the same data is split or copied across sites, the distributed DBMS must make sure every site sees a correct, up-to-date state. It does so at several levels:

1. **Atomic commitment across sites** — a transaction that updates data at several sites commits everywhere or nowhere, using **Two-Phase Commit (2PC)** ([Q9, Part C](#part-c--two-phase-commit-2pc-protocol)). No site is left with half a transaction.

2. **Replica-control protocols** keep all copies of a data item consistent:

   | Protocol | How it works | Effect |
   |---|---|---|
   | **Synchronous (eager) replication** | Every replica is updated inside the same transaction | Strong consistency, slower writes |
   | **Read-one-write-all (ROWA)** | A read uses any one copy; a write must lock and update all copies | Cheap reads; a write fails if any site is down |
   | **Primary copy** | Each item has one primary site; all updates go there and are propagated to the other copies | Simple, no write conflicts; the primary is a bottleneck |
   | **Majority / quorum consensus** | A read must reach a read quorum Qr and a write a write quorum Qw of the n copies, with Qr + Qw > n and 2 × Qw > n; version numbers identify the newest copy | Every read overlaps the latest write; tolerates some site failures |
   | **Asynchronous (lazy) replication** | Copies are updated after the transaction commits | Fast writes, temporary inconsistency — **eventual consistency** |

   Quorum example: with 5 copies, Qw = 3 and Qr = 3 satisfy 3 + 3 > 5 and 2 × 3 > 5, so every read set shares at least one copy with the last write set.

3. **Distributed concurrency control** — locks or timestamps are coordinated across sites so that concurrent global transactions stay serializable: a single lock manager, distributed lock managers, primary-copy or majority locking, or timestamp ordering with globally unique timestamps (local clock + site id).

4. **Distributed deadlock handling** — a global wait-for graph, or timeouts, detects deadlocks that span sites.

5. **Recovery** — each site keeps its own log; after a failure, the commit protocol's log records (`ready`, `commit`, `abort`) tell each site whether to redo or undo, so all sites converge to the same state.

6. **Integrity constraints and the catalog** — constraints that span sites (such as a foreign key to a table stored elsewhere) are checked globally, and the distributed data dictionary is itself kept consistent.

**Strong vs eventual consistency**

| Basis | Strong consistency | Eventual consistency |
|---|---|---|
| Guarantee | Every read sees the latest committed write | Replicas may differ for a while but converge once updates stop |
| Achieved by | 2PC, synchronous replication, quorums | Asynchronous (lazy) replication |
| Write speed | Slower | Faster |
| Availability during a network partition | Lower | Higher |
| Used by | Banking, reservations | Social-media feeds, DNS, shopping-cart caches |

The **CAP theorem** states the trade-off: during a network partition, a distributed system must choose between consistency and availability.

**Summary:** A distributed database stores data by fragmenting, replicating and allocating it across sites, and keeps it consistent through 2PC for atomic commitment, replica-control protocols (eager, ROWA, primary copy, quorum, or lazy replication for eventual consistency), distributed concurrency control and deadlock handling, and log-based recovery.

---

### U2-Q7. How 2PC ensures atomicity and consistency

Answered in full in [Q9, Part C](#part-c--two-phase-commit-2pc-protocol) — the prepare (voting) phase, the commit/abort decision phase, the message diagram and failure handling. For the "how does it ensure" part, add:

- **Atomicity** — the coordinator commits only if *every* participant has voted `ready` (after force-writing `<ready T>` to its log); a single `abort` vote, or a timeout, aborts the transaction at every site. All sites therefore reach the same outcome — all commit or all roll back.
- **Consistency** — a participant votes `ready` only after checking that its part of the transaction violates no local integrity constraint, and no site can commit unless all sites succeeded. A global state in which one site has applied the transaction and another has not (money debited in Pune but never credited in Mumbai) can therefore never arise.

---

### U2-Q8. Distributed transactions and 2PC

Answered in full in [Q9](#q9-distributed-data-storage-distributed-transactions-and-2pc): [Part B](#part-b--distributed-transactions) covers distributed transactions (definition, transaction manager vs coordinator, failure types, the fund-transfer example) and [Part C](#part-c--two-phase-commit-2pc-protocol) covers 2PC (phases, message diagram, failure handling, advantages, disadvantages and 3PC).

---

### U2-Q9. Concurrency control and consistency

Answered in full in [Q11](#q11-concurrency-control-in-detail), with [Q10](#q10-short-note-on-concurrency-and-types-of-locking) for locking and [Q12](#q12-how-concurrency-control-supports-the-database-transaction-process) for how it supports the transaction process. For this wording, make two points explicit:

- **Maintains consistency** — concurrency control allows only schedules that are equivalent to some serial schedule (serializability), so interleaved transactions leave the database as consistent as if they had run one at a time.
- **Keeps the database up to date** — it prevents lost updates and dirty reads, so every committed update is preserved and every later transaction reads the latest committed value (see the stock example in Q12).

---

### U2-Q10. Types of schedules, the scheduler and serializability

**Definition**

A **schedule** is the chronological order in which the operations (read, write, commit, abort) of a set of concurrent transactions are executed. It contains all the operations of those transactions and preserves the order of operations within each transaction.

**Types of schedules**

1. **Serial schedule** — the transactions run one after another with no interleaving (T1 completes, then T2 starts). Always correct, but there is no concurrency.
2. **Non-serial (concurrent) schedule** — operations of different transactions are interleaved. It gives concurrency but may or may not be correct.
3. **Serializable schedule** — a non-serial schedule whose effect is equivalent to some serial schedule. This is the correctness criterion.
   - **Conflict-serializable** — can be turned into a serial schedule by swapping adjacent non-conflicting operations. It is tested with a **precedence graph**: one node per transaction, and an edge Ti → Tj when an operation of Ti conflicts with a later operation of Tj. The schedule is conflict-serializable if and only if the graph has **no cycle**.
   - **View-serializable** — view-equivalent to a serial schedule (same initial reads, same reads-from relationships, same final writes). Every conflict-serializable schedule is also view-serializable; the extra view-serializable schedules all contain *blind writes*.
4. **Classified by recoverability**
   - **Recoverable** — if Tj reads a value written by Ti, then Ti commits before Tj commits.
   - **Non-recoverable** — Tj commits after reading Ti's uncommitted data and Ti then aborts; Tj's committed result can no longer be undone.
   - **Cascadeless** — transactions read only committed data, so one abort never forces others to abort (no cascading rollback).
   - **Strict** — no transaction reads or writes an item until the transaction that last wrote it has committed or aborted. Strict ⊂ cascadeless ⊂ recoverable.

**Diagram — classification of schedules**

```
                              SCHEDULES
                  +---------------+----------------+
                  |                                |
               Serial                    Non-serial (concurrent)
         (always correct)           +--------------+--------------+
                                    |                             |
                              Serializable                 Non-serializable
                        +-----------+-----------+          (may be incorrect)
                        |                       |
              Conflict-serializable     View-serializable
              (every conflict-serializable schedule is also view-serializable)

   By recoverability:   Strict  ⊂  Cascadeless  ⊂  Recoverable    vs   Non-recoverable
```

**Conflicting operations**

Two operations **conflict** if they belong to different transactions, access the same data item, and at least one of them is a write:

| T1 \ T2 | read(Q) | write(Q) |
|---|---|---|
| **read(Q)** | No conflict | Conflict (read–write) |
| **write(Q)** | Conflict (write–read) | Conflict (write–write) |

**How the scheduler resolves conflicts and ensures serializability**

The **scheduler** is the concurrency-control component that receives every operation from the transaction manager and decides, for each one, to **execute** it, **delay** it, or **reject** it (abort and restart the transaction), so that only serializable, recoverable schedules reach the database.

```
   T1 ops --+                                 +--> execute --> buffer/data manager --> DB
   T2 ops --+--> transaction --> SCHEDULER ---+--> delay (wait in a queue)
   T3 ops --+     manager            |        +--> reject (abort and restart)
                                     |
                       lock table / timestamps / validation data
```

- **Lock-based scheduler (2PL)** — an operation that conflicts with a lock held by another transaction is *delayed* until the lock is released; two-phase locking guarantees a conflict-serializable result ([Q10](#q10-short-note-on-concurrency-and-types-of-locking)).
- **Timestamp-based scheduler** — conflicting operations are allowed only in timestamp order; an operation that arrives "too late" is *rejected* and its transaction restarted ([Q11](#q11-concurrency-control-in-detail)).
- **Optimistic (validation) scheduler** — operations run freely; at commit time the transaction is validated and rejected if it conflicts.
- With strict 2PL (exclusive locks held until commit), the schedule is also **strict**, and therefore recoverable and cascadeless.

**Real-time example — bank account A with a balance of ₹5,000**

- T1: transfer ₹1,000 from A to B → read(A); A = A − 1000; write(A); then B is credited.
- T2: credit 10 % interest to A → read(A); A = A × 1.1; write(A).

The correct serial results are: T1 then T2 gives A = (5000 − 1000) × 1.1 = ₹4,400; T2 then T1 gives A = 5000 × 1.1 − 1000 = ₹4,500.

*Without a scheduler (non-serializable):*

| Time | T1 | T2 | Value of A in the database |
|---|---|---|---|
| t1 | read(A) → 5000 | | 5000 |
| t2 | | read(A) → 5000 | 5000 |
| t3 | A = 5000 − 1000 | | 5000 |
| t4 | | A = 5000 × 1.1 | 5000 |
| t5 | write(A) | | 4000 |
| t6 | | write(A) | **5500** — T1's debit is lost |

Precedence graph: read1(A) before write2(A) gives T1 → T2, and read2(A) before write1(A) gives T2 → T1. The graph has a **cycle**, so the schedule is not conflict-serializable — and A ends at ₹5,500, a value no serial order produces.

*The same transactions under a 2PL scheduler:*

| Time | T1 | T2 | Value of A in the database |
|---|---|---|---|
| t1 | X-lock(A); read(A) → 5000 | | 5000 |
| t2 | | X-lock(A) requested → **delayed** | 5000 |
| t3 | A = 4000; write(A) | | 4000 |
| t4 | credit B; commit; unlock(A) | | 4000 |
| t5 | | lock granted; read(A) → 4000 | 4000 |
| t6 | | A = 4400; write(A); commit | **4400** |

Precedence graph: only T1 → T2 — **acyclic**, so the schedule is serializable and equivalent to the serial order T1 → T2 (A = ₹4,400).

```
   Without a scheduler - cycle          With a 2PL scheduler - no cycle

        T1 ----------> T2                    T1 ----------> T2
         ^             |
         +-------------+
```

**Summary:** Schedules are serial, non-serial or serializable (conflict or view), and by recoverability recoverable, cascadeless or strict; the scheduler executes, delays or rejects each conflicting operation — using locks, timestamps or validation — so that the precedence graph stays acyclic and the result equals some serial execution.

---

## Unit 3 — Object-Oriented Databases

### U3-Q1. DBMS vs object-oriented system

Here "OOS" means an object-oriented (database) system — an OODBMS. Answered in full in [Q13](#q13-oodbms-vs-rdbms-with-a-real-world-example), which compares a relational DBMS with an OODBMS and gives the CAD car-design example. Points to hit: data model (tables vs objects), identity (primary key vs OID), behaviour (methods stored with the data), relationships (foreign keys and joins vs object references), inheritance, complex user-defined types, query language (SQL vs OQL), the impedance mismatch, and the typical applications of each.

---

### U3-Q2. Object structure and OID

**Object identity (OID)**

Every object in an object database has an **object identifier (OID)** — a unique, system-generated identity that stays with the object for its whole life. Objects use OIDs to refer to each other.

**Properties of an OID**

- **Unique** — no two objects in the database have the same OID.
- **System-generated** — created by the DBMS when the object is created, not chosen by the user, and usually not visible to the user.
- **Immutable** — never changes, even if every attribute value of the object changes.
- **Independent of attribute values** — unlike a primary key, it is not built from the object's data.
- **Independent of physical location** — it should not be a disk address, so the object can be moved without changing its identity.
- **Never reused** — the OID of a deleted object is not given to a new object.

**OID vs primary key**

| Basis | OID | Primary key |
|---|---|---|
| Created by | The system | The designer/user |
| Based on attribute values | No | Yes |
| Can change | Never | Yes (updates must cascade to foreign keys) |
| Visible to users | Usually hidden | Visible |
| Two objects with identical values | Still two distinct objects | Not allowed — duplicate key |
| Used for | Identity, references between objects, sharing | Uniqueness, and joins through foreign keys |

**Identity vs equality:** two objects are **identical** if they have the same OID, and **equal** if they have the same state (values). Two students named "Rahul Sharma" with the same address are equal in state but are still two separate objects, because their OIDs differ.

**Object structure — the triple (i, c, v)**

Formally, an object is represented as a triple **(i, c, v)**:

- **i** — the object's OID;
- **c** — the **type constructor** that says how its state is built: atom, tuple, set, list, bag or array ([U3-Q3](#u3-q3-type-constructors-in-oodbms));
- **v** — the object's current **state (value)**: an atomic value for an atom, `<a1:i1, a2:i2, …>` (attribute names paired with the OIDs of their values) for a tuple, and `{i1, i2, …}` for a set.

**Example — a Student object with an address and a set of courses**

```
   o1 = (i1, atom,  'Vidit')
   o2 = (i2, atom,  'Pune')
   o3 = (i3, atom,  '411038')
   o4 = (i4, tuple, <city:i2, pin:i3>)                    Address object
   o5 = (i5, atom,  'ADBMS')
   o6 = (i6, atom,  'DCN')
   o7 = (i7, set,   {i5, i6})                             set of courses
   o8 = (i8, tuple, <name:i1, address:i4, courses:i7>)    Student object
```

The same object drawn as a graph — every arrow is a reference by OID:

```
                       o8 : Student (tuple)
               name /          | address          \ courses
                   v           v                   v
            o1 'Vidit'   o4 : Address (tuple)    o7 : set
                              /        \           /      \
                             v          v         v        v
                       o2 'Pune'  o3 '411038'  o5 'ADBMS'  o6 'DCN'
```

**Object sharing:** if a second Student object also has `address:i4`, both students *share* the same Address object, so changing the city in o4 changes it for both — something value-based tuples cannot express directly.

**Summary:** An object is identified by an OID that is unique, system-generated, immutable and independent of its values and location; its structure is the triple (OID, type constructor, state), and objects refer to each other by OID, forming a graph of possibly shared complex objects.

---

### U3-Q3. Type constructors in OODBMS

**Definition**

In an object database, complex objects are built from simpler ones by applying **type constructors**. The type constructor of an object — the *c* in the triple (i, c, v) of [U3-Q2](#u3-q2-object-structure-and-oid) — says how the object's state is put together. Constructors can be nested to any depth, which is what makes **complex objects** possible.

**Types of type constructors**

1. **Atom constructor** — a single value of a built-in basic type: integer, real, character string, boolean, date. Example: `roll_no = 101`, `name = 'Vidit'`.
2. **Tuple (struct / record) constructor** — groups several named components, possibly of different types, into one structure. Example: `address = <city: 'Pune', pin: '411038'>`. In SQL this is a structured (row) type.
3. **Collection (multivalued) constructors** — a group of values of the same type:
   - **Set** — unordered, no duplicates: `courses = {'ADBMS', 'DCN', 'Java'}`.
   - **Bag (multiset)** — unordered, duplicates allowed: `scores = {85, 78, 85}`.
   - **List** — ordered, duplicates allowed: `chapters = ['Intro', 'Parallel DB', 'Distributed DB']`.
   - **Array** — ordered and accessed by index (with a fixed maximum size in some systems): `marks[1..5]`.
   - **Dictionary** — a set of (key, value) pairs: `{'MCA40150': 'ADBMS', 'MCA40140': 'DCN'}`.

A **reference** type — an attribute that holds the OID of another object — is used alongside these constructors to build relationships between objects.

| Constructor | Ordered? | Duplicates? | Example |
|---|---|---|---|
| Atom | — | — | `101`, `'Vidit'` |
| Tuple | Fixed named fields | — | `<city: 'Pune', pin: '411038'>` |
| Set | No | No | `{'ADBMS', 'DCN'}` |
| Bag | No | Yes | `{85, 78, 85}` |
| List | Yes | Yes | `['Intro', 'Parallel DB']` |
| Array | Yes (indexed) | Yes | `marks[1] = 78` |
| Dictionary | By key | Keys unique | `{'MCA40150': 'ADBMS'}` |

**Example — a Student class in ODMG ODL style**

```
struct Address {
    string city;
    string pin;
};

class Student {
    attribute long            roll_no;      // atom
    attribute string          name;         // atom
    attribute Address         address;      // tuple (struct)
    attribute set<string>     phones;       // set
    attribute list<short>     marks;        // list
    relationship set<Course>  takes
        inverse Course::taken_by;           // set of references to Course objects
    float cgpa();                           // operation (method)
};
```

**"Constructor" in the OOP sense**

In object-oriented programming, a **constructor** is also the special method that creates a new object of a class and initialises its attributes. Its usual kinds are the **default** (no-argument) constructor, the **parameterised** constructor (initial values passed as arguments) and the **copy** constructor (initialises a new object from an existing one). When an OODBMS creates an object, the system also assigns its OID.

**Example in object-relational SQL (PostgreSQL, as done in class)**

PostgreSQL provides the tuple constructor `ROW(...)` for structured types and the collection constructor `ARRAY[...]`:

```sql
-- Class: a structured type (tuple constructor)
CREATE TYPE addr_type AS (
    city varchar(30),
    pin  char(6)
);

CREATE TABLE student_obj (
    roll_no int,            -- atom
    name    varchar(30),    -- atom
    address addr_type,      -- tuple (structured type)
    marks   int[]           -- collection (array)
);

-- ROW(...) builds an addr_type value; ARRAY[...] builds an int[] value
INSERT INTO student_obj VALUES
    (101, 'Vidit', ROW('Pune', '411038'), ARRAY[78, 85, 91]),
    (102, 'Tony',  ROW('Mumbai', '400001'), ARRAY[88, 92]);

SELECT roll_no, name, (address).city, marks, marks[1] AS first_test
FROM   student_obj;
```

Output:

```
 roll_no | name  |  city  |   marks    | first_test
---------+-------+--------+------------+------------
     101 | Vidit | Pune   | {78,85,91} |         78
     102 | Tony  | Mumbai | {88,92}    |         88
(2 rows)
```

`(address).city` reads one attribute of the tuple, and PostgreSQL arrays are indexed from 1. The class files [theo_adbms/constructor_example.sql](theo_adbms/constructor_example.sql) and [theo_adbms/construct.sql](theo_adbms/construct.sql) use the same `ROW(...)` constructor, and an object table (`CREATE TABLE … OF type`, where every row is one object of the type) appears in the 8 Marks Question below.

**Summary:** Type constructors build complex object states — atom for basic values, tuple for records, and the collection constructors set, bag, list, array and dictionary for groups of values — and can be nested; in object-relational SQL they appear as `ROW(...)` for structured types and `ARRAY[...]` for collections.

---

### U3 — 8 Marks Question. Student, Teacher and University with tuple constructors

**Question:** Create a constructor for a class "Student" (name, roll number) with a method to display its details, and a constructor for a class "Teacher" (name, subject) with a method to display its details; create a university table that stores both using tuple constructors, and display all the details.

**Approach — object-relational SQL in PostgreSQL**

| OO concept | PostgreSQL feature |
|---|---|
| Class | Structured type — `CREATE TYPE … AS (…)` |
| Constructor | Tuple constructor `ROW(value1, value2, …)` — builds one object of the type |
| Object | The value that `ROW(...)` produces |
| Object table | `CREATE TABLE … OF type` — every row is one object |
| Method | A function that takes the type as its parameter (PostgreSQL types carry attributes only) |

**Solution** — the class solution is [theo_adbms/uni.sql](theo_adbms/uni.sql):

```sql
-- 1. Class Student
CREATE TYPE student_type AS (
    student_name varchar(50),
    roll_number  int
);

-- 2. Class Teacher
CREATE TYPE teacher_type AS (
    teacher_name varchar(50),
    subject      varchar(50)
);

-- 3. Class University: holds one Student object and one Teacher object
CREATE TYPE university_type AS (
    uni_id  int,
    student student_type,
    teacher teacher_type
);

-- 4. Object table: every row is one university_type object
CREATE TABLE university OF university_type;

-- 5. Create the objects with the tuple constructor ROW(...)
INSERT INTO university VALUES (1, ROW('Vidit Kulshrestha', 101), ROW('Dr. Kulkarni', 'ADBMS'));
INSERT INTO university VALUES (2, ROW('Tony Stark', 102),        ROW('Dr. Banner', 'DCN'));
INSERT INTO university VALUES (3, ROW('Doctor Strange', 103),    ROW('Dr. Wong', 'Java'));

-- 6. Display the objects
SELECT * FROM university;

-- 7. Display the attributes of each object
SELECT uni_id,
       (student).student_name,
       (student).roll_number,
       (teacher).teacher_name,
       (teacher).subject
FROM   university
ORDER  BY uni_id;
```

Output of step 6 — each nested object is shown in brackets:

```
 uni_id |          student          |        teacher
--------+---------------------------+------------------------
      1 | ("Vidit Kulshrestha",101) | ("Dr. Kulkarni",ADBMS)
      2 | ("Tony Stark",102)        | ("Dr. Banner",DCN)
      3 | ("Doctor Strange",103)    | ("Dr. Wong",Java)
(3 rows)
```

Output of step 7 — `(student).student_name` reads one attribute of the nested object:

```
 uni_id |   student_name    | roll_number | teacher_name | subject
--------+-------------------+-------------+--------------+---------
      1 | Vidit Kulshrestha |         101 | Dr. Kulkarni | ADBMS
      2 | Tony Stark        |         102 | Dr. Banner   | DCN
      3 | Doctor Strange    |         103 | Dr. Wong     | Java
(3 rows)
```

**The display methods**

PostgreSQL structured types cannot contain methods, so each "method" is written as a function that takes an object of the type:

```sql
CREATE FUNCTION display_student(s student_type) RETURNS text AS $$
    SELECT 'Student: ' || s.student_name || ', Roll No: ' || s.roll_number;
$$ LANGUAGE sql;

CREATE FUNCTION display_teacher(t teacher_type) RETURNS text AS $$
    SELECT 'Teacher: ' || t.teacher_name || ', Subject: ' || t.subject;
$$ LANGUAGE sql;

SELECT uni_id,
       display_student(student) AS student_details,
       display_teacher(teacher) AS teacher_details
FROM   university
ORDER  BY uni_id;
```

```
 uni_id |             student_details              |            teacher_details
--------+------------------------------------------+---------------------------------------
      1 | Student: Vidit Kulshrestha, Roll No: 101 | Teacher: Dr. Kulkarni, Subject: ADBMS
      2 | Student: Tony Stark, Roll No: 102        | Teacher: Dr. Banner, Subject: DCN
      3 | Student: Doctor Strange, Roll No: 103    | Teacher: Dr. Wong, Subject: Java
(3 rows)
```

Because each function takes a single composite argument, PostgreSQL also accepts a method-style call: `SELECT (student).display_student FROM university;`.

**For comparison — Oracle object types**

In Oracle the constructor is called by the type's own name, and the method is declared inside the type:

```sql
CREATE TYPE student_type AS OBJECT (
    student_name VARCHAR2(50),
    roll_number  NUMBER,
    MEMBER FUNCTION display RETURN VARCHAR2
);
/
CREATE TYPE BODY student_type AS
    MEMBER FUNCTION display RETURN VARCHAR2 IS
    BEGIN
        RETURN 'Student: ' || student_name || ', Roll No: ' || roll_number;
    END;
END;
/
-- constructor call: student_type('Vidit Kulshrestha', 101)
-- method call:      SELECT u.student.display() FROM university u;
```

**Summary:** Structured types act as the Student and Teacher classes, `ROW(...)` is their tuple constructor, `university` is an object table of a type that nests both, and display functions (or Oracle `MEMBER FUNCTION`s) act as the methods; `SELECT` with `(column).attribute` displays every detail.

---

## 10 Aug 2026 — Database & Client-Server Architecture

### Q1. Difference between Database System Architecture and Client-Server Architecture

**Definition**

- **Database System Architecture** describes how a DBMS is organised *internally* and how users are insulated from physical storage. Its classical form is the **ANSI/SPARC three-level schema architecture**: external (view) level, conceptual (logical) level and internal (physical) level. It is a *logical/design* view of the database.
- **Client-Server Architecture** describes how the DBMS is *deployed over a network* — the database engine runs on a server machine, and application programs (clients) request services over a network. It is a *physical/deployment* view of the system.

**The ANSI/SPARC three levels (for context)**

```
        +---------------+  +---------------+  +---------------+
        |  View 1       |  |  View 2       |  |  View 3       |   External level
        +---------------+  +---------------+  +---------------+
                 \               |                /
                  \              |               /        Logical data independence
                   +-------------------------------+
                   |     Conceptual Schema         |      Conceptual level
                   +-------------------------------+
                                 |                         Physical data independence
                   +-------------------------------+
                   |     Internal Schema           |      Internal level
                   +-------------------------------+
                                 |
                          Stored database (files, indexes, blocks)
```

**Comparison table**

| Basis | Database System Architecture | Client-Server Architecture |
|---|---|---|
| Nature | Logical design of the DBMS | Physical deployment over a network |
| Concern | How data is abstracted and described | How processing is divided between machines |
| Main components | External, conceptual, internal schemas | Client machines, network, database server |
| Key goal | Data abstraction and **data independence** | Resource sharing, centralised data, scalability |
| Users | Hidden from users by views | Users sit on clients, data sits on the server |
| Number of machines | Independent of machine count (can be single machine) | Requires at least two roles: client and server |
| Variants | 1-level, 2-level, 3-level (ANSI/SPARC) | 2-tier, 3-tier, n-tier |
| Failure impact | A poor design gives redundancy and anomalies | A server or network failure blocks all clients |
| Example | View / table / index layering in Oracle | An Oracle server accessed by 100 SQL*Plus clients |

**Relationship between the two**

They are complementary, not competing: a client-server *deployment* still uses the three-level *schema* architecture internally. Client-server answers "where does the code run?"; database system architecture answers "how is the data described?".

**Summary:** Database system architecture is about *levels of data abstraction*; client-server architecture is about *distribution of work between machines*.

---

### Q2. Short note on Client-Server Architecture

**Definition**

Client-server architecture is a distributed computing model in which the workload is divided between **clients** (which request services) and a **server** (which provides them). In a database context, the DBMS runs on the server and manages storage, query processing, concurrency and recovery, while clients send SQL requests and present results to the user.

**Diagram**

```
  +----------+   +----------+   +----------+
  | Client 1 |   | Client 2 |   | Client n |     Presentation + application logic
  +----+-----+   +----+-----+   +----+-----+
       |              |              |
       +------------- Network -------+           SQL requests / result sets
                      |
             +--------+---------+
             |  Database Server |                DBMS: query processing,
             |     (DBMS)       |                concurrency, recovery, security
             +--------+---------+
                      |
                 +----+----+
                 | Database|
                 +---------+
```

**How it works**

1. The client establishes a connection (via ODBC/JDBC or a native driver).
2. The client sends an SQL statement over the network.
3. The server parses, optimises and executes the query, applying access control and locking.
4. Only the **result set** — not the whole file — travels back to the client.
5. The client formats and displays the result; the connection is reused or closed.

**Characteristics**

- Clear separation of responsibility between requester and provider.
- Communication follows a **request-response** protocol.
- The server is always listening; clients initiate.
- Many clients can share one server (many-to-one).
- Commonly deployed as **two-tier** (client ↔ server) or **three-tier** (client ↔ application server ↔ database server).

**Advantages**

- Centralised data means one authoritative copy — less redundancy and inconsistency.
- Centralised security, backup and administration.
- Reduced network traffic compared with a file-server model, since only results are sent.
- Clients and server can be upgraded independently; new clients can be added easily.

**Limitations / Disadvantages**

- The server is a **single point of failure** and a potential bottleneck under heavy load.
- Server hardware and licensing are expensive.
- Network dependency — no connectivity means no data access.
- Scaling requires a bigger server (vertical scaling) or clustering.

**Summary:** Client-server architecture centralises data and DBMS processing on a server while clients handle presentation, giving controlled, shared, secure access at the cost of server dependency.

---

## 11 Aug 2026 — Three-Tier & Distributed Systems

### Q3. Three-tier architecture with a neat diagram

**Definition**

Three-tier architecture is a client-server architecture in which the application is split into three physically and logically separate layers: the **Presentation tier** (user interface), the **Application / Business-logic tier** (rules and processing) and the **Data tier** (DBMS and database). The client never talks to the database directly.

**Diagram**

```
   TIER 1 — PRESENTATION (Client)
   +-------------------------------------------------+
   |  Browser / Mobile app / Thin GUI client          |
   |  Input validation, rendering, user interaction   |
   +-----------------------+-------------------------+
                           |  HTTP / HTTPS, REST, forms
                           v
   TIER 2 — APPLICATION (Business logic)
   +-------------------------------------------------+
   |  Web / Application server                        |
   |  Business rules, session mgmt, authentication,   |
   |  connection pooling, transaction coordination    |
   +-----------------------+-------------------------+
                           |  SQL over JDBC / ODBC
                           v
   TIER 3 — DATA (Database)
   +-------------------------------------------------+
   |  DBMS: query processing, concurrency, recovery   |
   |  +-------------------------------------------+  |
   |  |            Physical Database              |  |
   |  +-------------------------------------------+  |
   +-------------------------------------------------+
```

**Role of each tier**

| Tier | Also called | Responsibility | Typical technology |
|---|---|---|---|
| 1 | Presentation / Client tier | Display data, capture input, basic validation | Browser, HTML/CSS/JS, Android app |
| 2 | Application / Logic / Middle tier | Enforce business rules, security, sessions, pool connections | Tomcat, Node.js, .NET, Java EE |
| 3 | Data tier | Store, retrieve and protect data; enforce integrity | Oracle, MySQL, PostgreSQL, SQL Server |

**Working — example flow (placing an order)**

1. User submits an order form in the browser (Tier 1).
2. The application server validates stock, computes price and applies discount rules (Tier 2).
3. It opens a transaction and issues `INSERT`/`UPDATE` statements to the DBMS (Tier 3).
4. The DBMS commits and returns the status; Tier 2 builds the response; Tier 1 renders the confirmation page.

**Advantages**

- **Scalability** — the middle tier can be replicated behind a load balancer.
- **Security** — the database is never exposed directly to clients; only the app server holds credentials.
- **Maintainability** — business logic changes in one place, without touching clients.
- **Reusability** — the same middle tier serves web, mobile and desktop clients.
- **Data integrity** — all access passes through one enforcement point.
- Thin clients need little hardware.

**Disadvantages**

- More complex to build, deploy and debug than two-tier.
- An extra network hop adds latency.
- Higher infrastructure cost (extra server layer).

**Two-tier vs three-tier**

| Basis | Two-tier | Three-tier |
|---|---|---|
| Layers | Client + Database server | Client + Application server + Database server |
| Business logic | In the client (fat client) | In the middle tier |
| Scalability | Limited (each client holds a DB connection) | High (connection pooling, replication) |
| Security | DB credentials on every client | Credentials only on the app server |
| Maintenance | Update every client | Update one server |
| Suitability | Small LAN applications | Web-scale / enterprise applications |

**Summary:** Three-tier architecture separates UI, business logic and data storage into independent layers, giving scalability, security and maintainability that a two-tier design cannot match.

---

### Q4. Short note on Distributed Database System

**Definition**

A **Distributed Database (DDB)** is a single logical database whose data is physically stored across multiple sites connected by a communication network. A **Distributed Database Management System (DDBMS)** is the software that manages this collection and makes the distribution **transparent** to the user — the user writes queries as if against one central database.

**Diagram**

```
                 +-------------------------------+
                 |   Global / Distributed Schema |
                 +---------------+---------------+
                                 |
        +------------------------+------------------------+
        |                        |                        |
  +-----+-----+            +-----+-----+            +-----+-----+
  |  Site A   |            |  Site B   |            |  Site C   |
  |  (Pune)   |<---------->| (Mumbai)  |<---------->| (Delhi)   |
  |  DBMS+DB  |  Network   |  DBMS+DB  |  Network   |  DBMS+DB  |
  +-----------+            +-----------+            +-----------+
```

**Types**

1. **Homogeneous DDB** — all sites run the same DBMS software and schema; sites cooperate willingly. Easier to design and manage.
2. **Heterogeneous DDB (multidatabase)** — sites run different DBMS products or data models; a translation/mediation layer is needed. Harder, but common after mergers.

**Key transparencies (what a DDBMS must hide)**

- **Location transparency** — the user need not know which site stores the data.
- **Fragmentation transparency** — the user need not know a table is split (horizontal, vertical or mixed fragmentation).
- **Replication transparency** — the user need not know how many copies exist.
- **Transaction transparency** — a transaction spanning sites still behaves atomically (via 2PC, see Q9).

**Design techniques**

- **Fragmentation** — splitting a relation into pieces stored at different sites (horizontal = rows, vertical = columns).
- **Replication** — keeping copies of the same fragment at multiple sites (see Q5).
- **Allocation** — deciding which fragment/replica lives at which site, based on the access pattern.

**Advantages**

- **Local autonomy** — each site controls its own data.
- **Improved performance** — data is placed near the users who use it, so queries are local.
- **Reliability and availability** — one site's failure does not stop the whole system.
- **Modular growth** — new sites can be added without redesigning the system.
- Reflects the real structure of a distributed organisation (branches, regions).

**Disadvantages**

- Complex design (fragmentation and allocation are hard problems).
- Costly and complex distributed query optimisation and concurrency control.
- Higher software cost and administration effort.
- Security must be enforced across the network, not at one point.
- Maintaining consistency across replicas is expensive.

**Summary:** A distributed database stores one logical database over many networked sites, offering autonomy, availability and locality of access, at the cost of significantly harder query processing, concurrency control and recovery.

---

## 18 Aug 2026 — Replication, Proxies & Parallel Databases

### Q5. Short note on Replica

**Definition**

A **replica** is a copy of a data item (a table, fragment or entire database) maintained at more than one site. **Replication** is the process of creating and keeping such copies consistent so that a read can be served by any copy and a failure of one site does not lose the data.

**Diagram**

```
              WRITE
                |
        +-------v--------+                +----------------+
        |  Primary /     |  replication   |   Replica 1    |  <-- READ
        |  Master copy   |--------------->|   (Standby)    |
        +-------+--------+     log        +----------------+
                |            shipping     +----------------+
                +----------------------->|   Replica 2    |  <-- READ
                                          +----------------+
```

**Types of replication**

| Type | Description | Trade-off |
|---|---|---|
| **Full replication** | Every site holds a complete copy of the database | Best read performance and availability; worst update cost |
| **Partial replication** | Only selected fragments are copied to selected sites | Balanced; needs careful allocation design |
| **No replication (fragmentation only)** | Exactly one copy of each fragment | Cheapest updates; poor availability |
| **Synchronous (eager)** | All copies updated inside the same transaction | Strong consistency, slower writes |
| **Asynchronous (lazy)** | Copies updated after commit | Fast writes, temporary inconsistency |
| **Master-slave** | One writable primary, many read-only replicas | Simple, no write conflicts |
| **Multi-master (peer-to-peer)** | Any replica accepts writes | High availability, needs conflict resolution |

**Advantages**

- **High availability** — if one site fails, another replica serves the request.
- **Improved read performance** — read load is spread over many copies and served locally.
- **Fault tolerance / disaster recovery** — data survives site loss.
- **Parallelism** — several queries can read different replicas simultaneously.

**Disadvantages**

- **Update overhead** — every write must reach every copy.
- **Consistency problem** — copies can diverge (stale reads) under lazy replication.
- **Storage cost** — n copies need n times the space.
- Complex concurrency control (e.g. read-one-write-all, quorum protocols).

**Summary:** A replica is a maintained copy of data at another site; replication buys availability and read speed at the price of update cost and consistency management.

---

### Q6. Use of a Proxy Server

**Definition**

A **proxy server** is an intermediary server that sits between clients and the destination server. Client requests go to the proxy, which evaluates them and forwards them on its own behalf, then returns the response to the client. It therefore acts as a gateway, a filter and a cache.

**Diagram**

```
   +--------+        +---------------+        +----------------+
   | Client |<------>| Proxy Server  |<------>| Origin /       |
   +--------+        | cache,filter, |        | Database Server|
   +--------+        | log, auth,    |        +----------------+
   | Client |<------>| load balance  |
   +--------+        +---------------+
```

**Uses / Functions**

1. **Caching** — frequently requested pages or query results are stored at the proxy, so repeat requests are served without touching the origin server. Reduces latency and server load.
2. **Security and anonymity** — the origin server sees only the proxy's IP address, hiding internal client addresses.
3. **Access control / content filtering** — blocks disallowed sites or requests (common in colleges and corporate networks).
4. **Load balancing** — a reverse proxy distributes incoming requests across several application or database servers.
5. **Bandwidth saving** — cached content is not re-fetched over the WAN.
6. **Logging and monitoring** — a central point to audit who accessed what.
7. **SSL termination and compression** — offloads encryption/compression work from application servers.
8. **Firewall/gateway function** — the single controlled door between an internal network and the Internet.
9. **Geographic access** — reach services routed through a permitted location.

**Types**

- **Forward proxy** — sits in front of clients, used to reach the Internet.
- **Reverse proxy** — sits in front of servers, used to protect and balance them (e.g. Nginx, HAProxy).
- **Transparent proxy** — intercepts traffic without client configuration.
- **Caching proxy / Web proxy** — optimised for content reuse.

**Advantages:** faster response for cached content, lower bandwidth use, centralised security and policy enforcement, hides internal topology, enables load balancing.

**Disadvantages:** an extra hop (latency for uncached requests), a single point of failure if not replicated, stale cached data, and the proxy itself can read traffic — a privacy concern if untrusted.

**Summary:** A proxy server is a controlled intermediary that caches, filters, secures and balances traffic between clients and servers.

---

### Q7. Client-Server vs Server System vs Client System Architecture

**1. Client-Server Architecture**

The overall model in which functionality is split between service-requesting **clients** and a service-providing **server** connected by a network. It defines the *relationship* between the two parties: clients initiate requests, the server responds. It is described fully in Q2. Variants: two-tier, three-tier, n-tier.

**2. Server System Architecture**

Describes the internal organisation of the **server side** — how the server is structured to process many concurrent requests efficiently. Its main categories are:

- **Transaction-server (query-server) architecture** — clients send SQL/transaction requests; the server executes them and returns only results. This is what most relational DBMSs use. Internally it consists of:
  - *Server processes* — receive queries, execute them, return results.
  - *Lock manager process* — grants/releases locks, handles deadlock detection.
  - *Database writer process* — flushes dirty buffer blocks to disk.
  - *Log writer process* — writes log records to stable storage.
  - *Checkpoint process* — performs periodic checkpoints.
  - *Process monitor* — detects and recovers failed processes.
  - Shared memory holding the **buffer pool**, **lock table**, **log buffer** and **query plan cache**.
- **Data-server (file-server) architecture** — the server ships whole data pages/objects to clients, which do the processing themselves. Used in object-oriented DBMSs; needs page/item shipping, client caching and cache coherence protocols (locking granularity, prefetching, data caching, lock caching).

**3. Client System Architecture**

Describes the organisation of the **client side** — what functionality lives on the client machine. Its two forms:

- **Thin client** — only the user interface; all logic and data processing happen on the server (e.g. a browser). Easy to deploy, low hardware need, server-dependent.
- **Fat (thick) client** — the client holds application logic, local caching and sometimes a local DBMS; the server mainly stores data. Better offline behaviour and lower server load, but harder to update across many machines.

Client-side components typically include the UI layer, application logic (if fat), a local cache, and a database interface/driver (ODBC/JDBC) that converts calls into network requests.

**Comparison table**

| Basis | Client-Server Architecture | Server System Architecture | Client System Architecture |
|---|---|---|---|
| Scope | The whole client + server model | Only the server side | Only the client side |
| Question answered | How do the two sides interact? | How is the server internally structured? | How much work does the client do? |
| Main components | Clients, network, server | Server processes, lock manager, log writer, buffer pool | UI, local logic, cache, DB driver |
| Main types | Two-tier, three-tier, n-tier | Transaction-server, data-server | Thin client, fat client |
| Focus | Communication and division of labour | Concurrency, throughput, recovery on the server | Presentation, responsiveness, local processing |
| Failure impact | Whole system stops if server dies | Affects all connected clients | Affects only that one user |
| Example | Browser + web/database server | Oracle instance with SGA and background processes | Browser (thin) vs MS Access front end (fat) |

**Relationship:** Client-server architecture is the umbrella model; server system architecture and client system architecture describe the internal design of its two halves.

**Summary:** Client-server = the overall interaction model; server system architecture = the server's internal process/memory design; client system architecture = how much intelligence sits on the client (thin vs fat).

---

### Q8. Parallel Database Architecture in e-commerce

**Definition**

A **parallel database** uses multiple CPUs, multiple disks and multiple memory units *within one tightly coupled system* to execute database operations in parallel, thereby improving **throughput** (transactions per second) and reducing **response time**. Unlike a distributed database, the sites are close, fast-connected and managed as one system.

**Forms of parallelism**

- **I/O parallelism** — data is partitioned across disks (round-robin, hash or range partitioning) so scans read many disks at once.
- **Inter-query parallelism** — different queries run simultaneously on different processors (raises throughput; ideal for many concurrent shoppers).
- **Intra-query parallelism** — one query is split across processors (lowers response time; ideal for large reports).
  - *Inter-operation parallelism* — different operators of a plan (e.g. scan and join) run concurrently, pipelined or independently.
  - *Intra-operation parallelism* — one operator (e.g. a join or sort) is executed by many processors on different partitions.

**Parallel architectures**

| Architecture | Description | Note |
|---|---|---|
| **Shared memory** | All processors share one memory and disks | Fast communication; limited scalability (bus contention) |
| **Shared disk (clustered)** | Each processor has private memory, all share disks | Good fault tolerance; disk interconnect can bottleneck |
| **Shared nothing** | Each node has its own CPU, memory and disk | Best scalability — used by large e-commerce/warehouse systems |
| **Hierarchical (hybrid)** | Shared-nothing cluster of shared-memory nodes | Practical compromise, used in modern clusters |

**Diagram (shared-nothing)**

```
        Interconnection network
   ---------------------------------------
     |            |            |
  +--+--+      +--+--+      +--+--+
  | CPU |      | CPU |      | CPU |
  | MEM |      | MEM |      | MEM |
  +--+--+      +--+--+      +--+--+
     |            |            |
   [Disk1]      [Disk2]      [Disk3]     <- Orders partitioned by hash(customer_id)
```

**Usefulness in e-commerce — analysis**

An e-commerce site (Amazon, Flipkart, Myntra) has exactly the workload parallel databases are built for:

1. **Massive concurrency** — lakhs of users browse simultaneously. *Inter-query parallelism* lets each user's catalogue query run on a different processor, so throughput scales with hardware instead of queueing behind one CPU.
2. **Fast product search and filtering** — a search over crores of product rows is split across partitions using *intra-operation parallelism*, so response stays within the sub-second budget shoppers expect.
3. **Peak-load handling (Big Billion Day, Black Friday)** — traffic can rise 10–50×. A shared-nothing cluster absorbs this by adding nodes, giving near-linear **speed-up** (same work, more nodes, less time) and **scale-up** (more work and more nodes, same time).
4. **Order processing and payment transactions** — thousands of `INSERT`s per second into `orders` and `payments` are spread over partitioned disks, removing the single-disk write bottleneck.
5. **Real-time inventory updates** — stock counts across warehouses are partitioned by warehouse or product, so updates to different products never contend.
6. **Recommendation engines and analytics** — "customers who bought this also bought…" needs large joins and aggregations over clickstream and purchase history; intra-query parallelism turns an hours-long scan into minutes.
7. **Business intelligence / sales dashboards** — nightly aggregation over billions of order rows is parallelised across nodes.
8. **High availability** — with replicated partitions, a failed node does not take the storefront offline; lost sales during downtime are directly lost revenue.
9. **Elastic cost control** — commodity shared-nothing nodes are far cheaper than one giant mainframe of equal capacity.

**Measures of benefit**

- **Speed-up** = time on 1 processor ÷ time on N processors (ideally N — *linear speed-up*).
- **Scale-up** = ability to handle N times the work with N times the resources in the same time.
- Real systems fall short of linear because of **start-up cost**, **interference** (shared resource contention) and **skew** (unequal partition sizes) — e.g. one hot-selling product creating a hotspot partition.

**Limitations to mention**

- Data **skew** — a viral product can overload one partition.
- Complex partitioning and query-plan design.
- Higher hardware and licensing costs.
- Distributed deadlocks and cross-partition joins add overhead.

**Summary:** Parallel database architecture — especially shared-nothing — gives e-commerce platforms the throughput, sub-second search response, peak-load elasticity and availability they need, by partitioning data across nodes and executing queries in parallel.

---

## 21 Aug 2026 — Distributed Storage & Transactions

### Q9. Distributed Data Storage, Distributed Transactions and 2PC

#### Part A — Distributed Data Storage

**Definition:** Distributed data storage is the technique of storing a database across multiple sites of a network so that data resides near where it is used, while the system still presents one logical database. Two basic techniques are used, often together.

**1. Fragmentation (Partitioning)** — splitting a relation *r* into fragments r₁, r₂, …, rₙ that together contain all the information of *r*.

| Type | Method | Reconstruction | Example |
|---|---|---|---|
| **Horizontal** | Divide by rows using a selection predicate | `r = r₁ ∪ r₂ ∪ … ∪ rₙ` | `ACCOUNT` split by branch: Pune rows at Pune site, Mumbai rows at Mumbai site |
| **Vertical** | Divide by columns, repeating the primary key in each fragment | `r = r₁ ⋈ r₂ ⋈ …` (natural join on the key) | `EMPLOYEE(emp_id, name, dept)` at HR site; `EMPLOYEE(emp_id, salary)` at Payroll site |
| **Mixed / Hybrid** | Horizontal then vertical (or vice versa) | Combination of union and join | Regional employee data further split by department |

*Correctness rules for fragmentation:* **completeness** (every tuple appears in some fragment), **reconstruction** (the original relation can be rebuilt), and **disjointness** (fragments do not overlap, except the key in vertical fragmentation).

**2. Replication** — storing copies of a fragment at several sites (full, partial or none). Advantages: availability, parallel reads, local access. Disadvantage: costly updates and consistency maintenance. (See Q5.)

**3. Allocation** — deciding which fragment or replica goes to which site, driven by access frequency, network cost, storage cost and availability requirements.

**Advantages of distributed storage:** locality of reference, reliability, availability, load distribution, scalability, and reduced network traffic.
**Challenges:** complex design, distributed query optimisation, cost of keeping replicas consistent, distributed security, and network dependency.

#### Part B — Distributed Transactions

**Definition:** A **distributed transaction** is a transaction that accesses and updates data at **two or more sites**. It must still satisfy **ACID** properties — Atomicity, Consistency, Isolation, Durability — *globally*, not merely at each site.

**Structure**

```
                +--------------------------+
                |  Transaction Coordinator |   (site where T started)
                +------------+-------------+
                             |
        +--------------------+--------------------+
        v                    v                    v
 +-------------+      +-------------+      +-------------+
 | Transaction |      | Transaction |      | Transaction |
 | Manager S1  |      | Manager S2  |      | Manager S3  |
 |  sub-txn T1 |      |  sub-txn T2 |      |  sub-txn T3 |
 +-------------+      +-------------+      +-------------+
```

- **Transaction Manager (TM)** at each site: manages the local log, local concurrency control and the local part of the transaction.
- **Transaction Coordinator (TC)** at the originating site: starts the transaction, splits it into sub-transactions, distributes them, and decides globally whether to **commit** or **abort**.

**Types of failure to handle:** site failure, loss of messages, communication-link failure, and **network partition**.

**The core problem:** every sub-transaction must reach the *same* outcome. If site S1 commits and S2 aborts, atomicity is violated — e.g. money debited in Pune but never credited in Mumbai. A **commit protocol** is therefore required; the standard one is **Two-Phase Commit (2PC)**.

**Classic example (fund transfer of ₹10,000):**
`T1` at Site A: `UPDATE account SET bal = bal − 10000 WHERE acc = 'A101';`
`T2` at Site B: `UPDATE account SET bal = bal + 10000 WHERE acc = 'B202';`
Both must commit, or neither.

#### Part C — Two-Phase Commit (2PC) Protocol

**Definition:** 2PC is a distributed commit protocol that guarantees the atomicity of a distributed transaction by having the coordinator take a global decision in two phases: a **voting (prepare) phase** and a **decision (commit/abort) phase**.

**Phase 1 — Prepare / Voting phase**

1. When transaction *T* finishes execution at all sites, the coordinator Ci writes `<prepare T>` to its log and **force-writes it to stable storage**.
2. Ci sends a **`prepare T`** message to every participating site.
3. Each participating site's TM decides:
   - If it *can* commit: force-write `<ready T>` (with all of T's log records) to stable storage, then reply **`ready T`**. The site is now in a *prepared/uncertain* state and must obey the coordinator's decision.
   - If it *cannot* commit (constraint violation, local failure, deadlock victim): write `<no T>` and reply **`abort T`**.
4. No reply within the timeout is treated as **abort**.

**Phase 2 — Decision / Commit phase**

- If **all** sites voted `ready T`: the coordinator force-writes `<commit T>` and sends **`commit T`** to all sites. Each site writes `<commit T>` to its log, commits locally and releases locks.
- If **any** site voted `abort T` (or timed out): the coordinator force-writes `<abort T>` and sends **`abort T`** to all sites, which roll back and release locks.
- Each site acknowledges; the coordinator writes `<complete T>` when all acknowledgements arrive.

**Message diagram**

```
  COORDINATOR                          PARTICIPANTS (S1, S2, S3)

  write <prepare T>
      |----------- prepare T --------------->|
      |                                      | force-write <ready T> (or <no T>)
      |<-------- ready T / abort T ----------|
      |
  all ready?  ---- yes ---> write <commit T>
              ---- no  ---> write <abort T>
      |
      |------- commit T / abort T ---------->|
      |                                      | write decision, commit/rollback,
      |                                      | release locks
      |<------------- ack -------------------|
  write <complete T>
```

**Failure handling**

| Failure | Recovery action |
|---|---|
| Participant fails **before** writing `<ready T>` | On restart it has no `ready` record → **abort** T (coordinator also aborts on timeout) |
| Participant fails **after** `<ready T>` but before the decision | On restart it is *in doubt*: it must ask the coordinator (or another site) for the decision and wait — it may **not** decide alone |
| Log has `<commit T>` | Redo T |
| Log has `<abort T>` | Undo T |
| **Coordinator fails** | Participants consult each other; if any knows the decision, it is propagated. If all are in `ready` state and none knows, they must **block** until the coordinator recovers |
| Network partition | Sites on the coordinator's side follow the normal protocol; sites cut off behave as though the coordinator failed |

**Advantages of 2PC**

- Guarantees **atomicity** across all sites — all commit or all abort.
- Simple, well understood and widely implemented (XA, JTA, Oracle distributed transactions).
- Handles site and message failures via logging and timeouts.

**Disadvantages of 2PC**

- **Blocking protocol** — a participant in the `ready` state whose coordinator has crashed must hold its locks and wait, freezing data for other transactions.
- The coordinator is a single point of failure.
- High message overhead (multiple rounds) and multiple forced log writes, which are slow.
- Locks are held for the full duration of the protocol, hurting concurrency.

**Improvement — Three-Phase Commit (3PC):** inserts a *pre-commit* phase between voting and commit so that a surviving participant can take the decision itself, making the protocol **non-blocking** when there is no network partition. The cost is an extra round of messages, so 3PC is rarely used in practice.

**Summary:** Distributed data storage uses fragmentation, replication and allocation to place data across sites; a distributed transaction spans several of those sites and must remain ACID globally; 2PC achieves the atomicity part through a prepare/vote phase followed by a global commit/abort decision, at the cost of blocking when the coordinator fails.

---

## 24 Aug 2026 — Concurrency Control

### Q10. Short note on Concurrency and types of Locking

**Concurrency**

**Concurrency** is the simultaneous (interleaved) execution of several transactions on the same database. It is desirable because it increases **throughput**, improves **resource utilisation** (CPU works while another transaction does I/O) and reduces **average waiting time**. But uncontrolled concurrency causes anomalies:

| Problem | Description |
|---|---|
| **Lost update** (write–write) | Two transactions read the same item and both write; one update is overwritten |
| **Dirty read** (uncommitted dependency) | T2 reads a value written by T1, and T1 then aborts |
| **Unrepeatable read** | T1 reads the same item twice and gets different values because T2 updated it in between |
| **Phantom read** | T1 re-runs a range query and finds new rows inserted by T2 |
| **Incorrect summary** | An aggregate is computed while another transaction is updating the rows |

**Locking**

A **lock** is a variable associated with a data item that controls which operations may be performed on it. A transaction must **acquire** a lock before accessing an item and **release** it afterwards. Locking is managed by the **lock manager** using a **lock table**.

**Types of locks**

1. **Binary lock** — two states only: locked (1) or unlocked (0). Simple but too restrictive: it prevents even two readers from proceeding together.

2. **Shared lock (S) / Read lock** — several transactions may hold an S lock on the same item at the same time; they may read but not write it. Requested with `LOCK-S(Q)`.

3. **Exclusive lock (X) / Write lock** — only one transaction may hold an X lock on an item; it may read and write. No other lock (S or X) may coexist with it. Requested with `LOCK-X(Q)`.

**Lock compatibility matrix**

| Requested ↓ / Held → | S | X |
|---|---|---|
| **S** | ✔ compatible | ✘ conflict |
| **X** | ✘ conflict | ✘ conflict |

4. **Update lock (U)** — an intermediate lock taken when a transaction intends to update after reading; it is compatible with S but not with another U or X. It prevents a common deadlock pattern where two transactions holding S locks both try to upgrade to X.

5. **Intention locks (multiple-granularity locking)** — used when locks can be taken at different granularities (database → file → page → record). A transaction sets an intention lock on the ancestors of the node it really wants:
   - **IS** — intention shared: an S lock will be requested lower down.
   - **IX** — intention exclusive: an X lock will be requested lower down.
   - **SIX** — shared + intention exclusive: read the whole node, update part of it.

6. **Certify lock** — used in multiversion two-phase locking, taken at commit time to certify a written version.

**Two-Phase Locking (2PL) protocol** — the rule that makes locking produce serializable schedules. Every transaction has:
- a **growing phase**, during which it may acquire locks but not release any, and
- a **shrinking phase**, during which it may release locks but not acquire any.
The moment of the last acquisition is the **lock point**; ordering transactions by lock point gives a conflict-serializable schedule.

Variants: **Strict 2PL** (all *exclusive* locks held until commit/abort — prevents cascading rollback), **Rigorous 2PL** (all locks held until commit — simplest and most common in practice), **Conservative 2PL** (acquire all locks before starting — deadlock-free but impractical).

**Problems caused by locking**

- **Deadlock** — T1 holds A and wants B while T2 holds B and wants A. Handled by *prevention* (wait-die, wound-wait, timeouts), *avoidance*, or *detection* using a **wait-for graph** plus victim selection and rollback.
- **Starvation** — a transaction repeatedly loses out; solved with fair (FIFO) lock queues.
- Reduced concurrency and lock-management overhead.

**Summary:** Concurrency lets transactions interleave for better throughput but risks lost updates and dirty reads; locking — shared, exclusive, update and intention locks used under a two-phase locking protocol — is the standard mechanism that keeps interleaved schedules serializable.

---

### Q11. Concurrency Control in detail

**Definition**

**Concurrency Control (CC)** is the DBMS component and set of protocols that manage simultaneous access to the database by multiple transactions so that the resulting schedule is **serializable** and **recoverable**, thereby preserving the **isolation** and **consistency** properties of ACID.

**Objectives**

1. Ensure **serializability** — the interleaved schedule must be equivalent to some serial schedule.
2. Preserve **database consistency**.
3. Maximise **concurrency and throughput** (do not serialise more than necessary).
4. Avoid the concurrency anomalies of Q10 (lost update, dirty read, unrepeatable read, phantom).
5. Prevent or resolve **deadlock** and **starvation**.
6. Ensure **recoverability** — no transaction commits after reading data written by a transaction that later aborts.

**Schedules and serializability (foundation)**

- A **schedule** is an ordering of the operations of a set of transactions.
- A **serial schedule** executes transactions one after another — always correct, but no concurrency.
- A **conflict-serializable** schedule can be transformed into a serial schedule by swapping non-conflicting adjacent operations. Two operations conflict if they belong to different transactions, act on the same item, and at least one is a write.
- Tested with a **precedence (serializability) graph**: a node per transaction, an edge Ti → Tj for each conflict where Ti's operation comes first. The schedule is conflict-serializable **iff the graph is acyclic**.
- **View serializability** is a weaker, more permissive but NP-hard-to-test notion.

**Techniques of Concurrency Control**

**1. Lock-Based Protocols (pessimistic)**
Transactions acquire shared/exclusive locks and follow **two-phase locking** (growing then shrinking phase) to guarantee conflict serializability. Strict and rigorous 2PL additionally avoid cascading aborts. Details in Q10. This is the technique used by most commercial DBMSs.

**2. Timestamp-Based Protocol**
Each transaction Ti gets a unique timestamp TS(Ti) at start (older transaction = smaller timestamp). Each item Q keeps `R-timestamp(Q)` (largest timestamp of a successful read) and `W-timestamp(Q)` (largest timestamp of a successful write).

- `read(Q)` by Ti: if `TS(Ti) < W-timestamp(Q)`, Ti is trying to read a value already overwritten by a younger transaction → **roll back Ti**; else read and set `R-timestamp(Q) = max(R-timestamp(Q), TS(Ti))`.
- `write(Q)` by Ti: if `TS(Ti) < R-timestamp(Q)` or `TS(Ti) < W-timestamp(Q)` → **roll back Ti**; else write and set `W-timestamp(Q) = TS(Ti)`.

Deadlock-free (no waiting) and serializable in timestamp order, but can cause many rollbacks and starvation of long transactions. **Thomas's write rule** improves it by ignoring an obsolete write instead of aborting.

**3. Validation / Optimistic Concurrency Control (OCC)**
Assumes conflicts are rare. Each transaction runs in three phases:
- **Read phase** — read from the database, make all updates in a private local workspace.
- **Validation phase** — check whether committing would violate serializability against concurrently running transactions.
- **Write phase** — if validation succeeds, apply the local copies to the database; otherwise **abort and restart**.

Excellent for read-heavy, low-conflict workloads (no locking overhead); poor when conflicts are frequent (wasted work).

**4. Multiversion Concurrency Control (MVCC)**
The system keeps **multiple versions** of each data item. A read is directed to the appropriate committed version according to its timestamp, so **readers never block writers and writers never block readers**. Used by Oracle and PostgreSQL as *snapshot isolation*. Cost: extra storage for old versions and version-cleanup (vacuum) work.

**5. Multiple Granularity Locking**
Locks can be taken at database, file, page or record level using intention locks (IS, IX, SIX), letting a big transaction take one coarse lock while small transactions take fine locks — balancing overhead against concurrency.

**6. Deadlock handling (part of CC)**
- **Prevention** — ordering resources, or timestamp schemes: **wait-die** (older waits, younger dies) and **wound-wait** (older wounds/preempts younger, younger waits).
- **Detection** — build a **wait-for graph**; a cycle means deadlock; choose a victim (least work done, fewest locks, avoid repeated victimisation) and roll it back.
- **Timeout** — abort any transaction that waits too long. Simple but may abort innocent transactions.

**Comparison of the main techniques**

| Basis | Lock-based (2PL) | Timestamp | Optimistic (OCC) | MVCC |
|---|---|---|---|---|
| Approach | Pessimistic | Pessimistic ordering | Optimistic | Versioned |
| Waiting | Yes (blocking) | No | No | Readers never wait |
| Deadlock | Possible | Impossible | Impossible | Rare |
| Rollbacks | Few | Many | Many if conflicts high | Few |
| Overhead | Lock table | Timestamp fields | Validation | Version storage |
| Best for | General, write-heavy | Short transactions | Read-heavy, low conflict | Mixed read/write OLTP |

**Isolation levels (practical CC in SQL)**

| Level | Dirty read | Unrepeatable read | Phantom |
|---|---|---|---|
| Read Uncommitted | Possible | Possible | Possible |
| Read Committed | Prevented | Possible | Possible |
| Repeatable Read | Prevented | Prevented | Possible |
| Serializable | Prevented | Prevented | Prevented |

**Summary:** Concurrency control is the DBMS mechanism that keeps interleaved transaction execution equivalent to some serial execution. It is implemented through lock-based (2PL), timestamp-based, optimistic and multiversion protocols, together with deadlock prevention/detection, and is exposed to the programmer as SQL isolation levels.

---

### Q12. How Concurrency Control supports the database transaction process

**The transaction process**

A **transaction** is a logical unit of work moving the database from one consistent state to another, delimited by `BEGIN` … `COMMIT`/`ROLLBACK`, and must satisfy **ACID**. Its states are:

```
   BEGIN
     |
     v
  ACTIVE ---------> PARTIALLY COMMITTED ---------> COMMITTED
     |                      |
     |                      | failure
     v                      v
   FAILED ------------> ABORTED (rolled back)
```

**Where concurrency control fits**

CC is invoked on **every read and write** of every active transaction. The transaction manager passes each operation to the **scheduler** (the CC module), which decides to *execute*, *delay* or *reject (abort)* it:

```
   Transaction  --op-->  Transaction Manager  --op-->  Scheduler (CC)
                                                          |
                             execute / delay / reject     |
                                                          v
                                                  Data / Buffer Manager
                                                          |
                                                  Recovery Manager (log)
```

**How CC supports each ACID property**

| Property | Contribution of Concurrency Control |
|---|---|
| **Atomicity** | Strict/rigorous 2PL holds exclusive locks until commit, so no other transaction sees partial effects; a rollback is therefore invisible to others and cascading aborts are avoided |
| **Consistency** | By enforcing serializability, CC guarantees that a set of individually consistency-preserving transactions leaves the database consistent when interleaved |
| **Isolation** | This is CC's central job: locks, timestamps, validation or versions make each transaction behave as if it ran alone; SQL isolation levels expose tunable degrees of it |
| **Durability** | CC cooperates with the recovery manager — locks are released only after the commit log record is force-written, so the committed state that others observe is the state that survives a crash |

**Specific support provided**

1. **Prevents the concurrency anomalies** — lost update, dirty read, unrepeatable read, phantom and incorrect summary (see Q10 table), each of which would otherwise corrupt the database.
2. **Guarantees serializability** — the schedule is provably equivalent to a serial one, so correctness reasoning about a single transaction remains valid under concurrency.
3. **Guarantees recoverability and avoids cascading rollback** — by not letting a transaction read uncommitted data, CC ensures an abort never forces a chain of other aborts.
4. **Maximises throughput** — instead of running transactions strictly one at a time, CC allows the maximum safe interleaving, so CPU and disk stay busy and response time falls.
5. **Enables fair resource sharing** — the lock manager's queues prevent starvation and ensure every transaction eventually proceeds.
6. **Handles deadlocks** — detection via the wait-for graph, or prevention via wait-die/wound-wait, so the transaction process never freezes permanently.
7. **Supports distributed transactions** — distributed CC (distributed 2PL, a global lock manager, or timestamp ordering) works together with the 2PC commit protocol so that multi-site transactions remain isolated as well as atomic (see Q9).
8. **Lets applications trade correctness for speed deliberately** — a reporting query can run at `READ COMMITTED` while a payment runs at `SERIALIZABLE`.

**Illustrative example — a lost update prevented**

Two customers buy the last unit of a product concurrently:

| Time | T1 (Customer A) | T2 (Customer B) | Without CC | With CC (2PL) |
|---|---|---|---|---|
| t1 | read stock = 1 | | 1 | X-lock granted to T1, reads 1 |
| t2 | | read stock = 1 | 1 | T2 requests X-lock → **waits** |
| t3 | stock = 0, write | | 0 | T1 writes 0 |
| t4 | | stock = 0, write | 0 | T1 commits, releases lock |
| t5 | commit | commit | **Both orders accepted — oversell!** | T2 now reads 0 → order rejected correctly |

**Summary:** Concurrency control is the enforcement arm of the transaction process — it sits between the transaction manager and the data, permitting only those interleavings that preserve isolation and consistency, cooperating with the recovery manager for atomicity and durability, while still allowing the parallelism that makes a multi-user DBMS fast.

---

## 31 Aug 2026 — OOPS

### Q13. OODBMS vs RDBMS with a real-world example

**Definitions**

- An **RDBMS (Relational DBMS)** stores data as **relations (tables)** of rows and columns, based on relational algebra and set theory. Relationships are expressed through **foreign keys**, and data is manipulated with **SQL**. Examples: Oracle, MySQL, PostgreSQL, SQL Server.
- An **OODBMS (Object-Oriented DBMS)** stores data as **objects**, exactly as they exist in an object-oriented programming language. An object bundles **state (attributes)** with **behaviour (methods)**, has a system-generated **OID (object identifier)**, and supports **classes, inheritance, encapsulation and polymorphism**. Relationships are expressed as direct **object references**, and data is manipulated with OQL or the host language. Examples: ObjectDB, db4o, ObjectStore, Versant.
- (An **ORDBMS**, e.g. Oracle or PostgreSQL with user-defined types, is the hybrid that adds object features on top of the relational model.)

**Comparison table**

| Basis | RDBMS | OODBMS |
|---|---|---|
| Basic unit | Table (relation), row, column | Object, class |
| Data model | Relational (tables) | Object-oriented (objects, classes) |
| Identity | Primary key — value-based | OID — system-generated, immutable, independent of values |
| Behaviour | Data only; logic lives in the application (or limited stored procedures) | Data **and** methods stored together (encapsulation) |
| Relationships | Foreign keys, resolved by joins at query time | Direct object references / pointers — navigation, no join needed |
| Data types | Fixed, simple, atomic (1NF) — INT, VARCHAR, DATE | Complex and user-defined — arrays, nested objects, multimedia, CAD models |
| Inheritance | Not supported natively | Supported (class hierarchy, polymorphism) |
| Query language | SQL (declarative, standardised, mature) | OQL / language-native queries (less standardised) |
| Impedance mismatch | Present — objects must be mapped to tables (ORM like Hibernate) | Absent — objects are stored directly |
| Performance profile | Excellent for large volumes of simple, structured, tabular data and ad-hoc queries | Excellent for complex, deeply nested, richly linked data |
| Normalisation | Central concept (1NF–BCNF) | Not applicable in the same way |
| Maturity & tooling | Very mature, huge ecosystem, abundant skills | Niche, smaller ecosystem and talent pool |
| Best suited to | Banking, ERP, payroll, inventory, reporting | CAD/CAM, GIS, multimedia, telecom networks, scientific and engineering data |

**Real-world example — a CAD / car design system (or the same case as a bank)**

*Scenario:* An automobile company stores car designs. A `Car` is composed of an `Engine`, a `Chassis` and many `Wheel`s; an `Engine` is composed of `Cylinder`s, `Piston`s and a `FuelInjector`; each part has a 3D geometry, material properties and a `computeWeight()` / `simulateStress()` operation. Parts are also specialised: `ElectricEngine` and `PetrolEngine` both *are* `Engine`s.

**In an RDBMS:**
- The design must be flattened into tables: `CAR`, `ENGINE`, `CYLINDER`, `PISTON`, `WHEEL`, `MATERIAL`, `GEOMETRY`, plus link tables — often 20+ tables for one conceptual object.
- Retrieving one complete car requires a long chain of **joins** across all of them, which is slow for deeply nested structures.
- Inheritance (`ElectricEngine` vs `PetrolEngine`) has to be simulated by a type column plus nullable columns, or by extra tables with 1:1 joins.
- 3D geometry does not fit the atomic-column requirement of 1NF; it ends up in a BLOB the database cannot interpret.
- `computeWeight()` cannot be stored with the data — it lives in the application, so different applications may implement it inconsistently.
- The programmer writes ORM mapping code to convert rows back into `Car` objects — the **impedance mismatch**.

**In an OODBMS:**
- The `Car` object is stored *as an object*, with its `Engine` object referenced directly. Fetching the car and navigating `car.engine.cylinders[0].material` follows pointers — **no joins**.
- `ElectricEngine extends Engine` is stored natively; a query for all `Engine`s returns both kinds through **polymorphism**.
- The 3D geometry is a user-defined type the database understands.
- `computeWeight()` is stored **with** the class, so every application computes weight the same way (encapsulation).
- No mapping layer is needed — the object the program builds is the object the database stores.

**Contrasting example where RDBMS wins:** a bank's `ACCOUNT`/`TRANSACTION` data is simple, flat, uniform and queried with heavy ad-hoc aggregation ("total deposits per branch this month"). SQL, indexes and mature optimisers make an RDBMS clearly the better choice — an OODBMS would add complexity with no benefit.

**Conclusion / Summary:** RDBMS models the world as tables of atomic values linked by keys and excels at large volumes of simple, uniform data with ad-hoc querying; OODBMS models the world as objects that carry both state and behaviour, support inheritance and direct references, and excel at complex, nested, multimedia or engineering data such as a CAD car-design system, where it removes joins and the object-relational impedance mismatch.

---

### Q14. Object-oriented structure — Attributes, Methods, Relationships

**The object-oriented structure**

In the object-oriented data model, the real world is modelled as a set of **objects**. An **object** is a self-contained entity that combines:

```
        +-------------------------------------------+
        |            OBJECT : Student               |
        +-------------------------------------------+
        |  OID  : #10024   (system-generated)       |   Identity
        +-------------------------------------------+
        |  ATTRIBUTES (state)                       |
        |    prn      = 24MCA1042                   |
        |    name     = Vidit                       |
        |    address  = Address object (complex)    |
        |    marks[]  = {78, 85, 91}   (multivalued)|
        +-------------------------------------------+
        |  METHODS (behaviour)                      |
        |    calculateCGPA()                        |
        |    registerCourse(c)                      |
        |    getAge()                               |
        +-------------------------------------------+
```

A **class** is the template/definition; an **object (instance)** is one occurrence of it. Every object has three parts: **identity (OID)**, **state (attributes)** and **behaviour (methods)**. **Encapsulation** means the state is accessible only through the methods — the object's interface is public, its implementation private.

**1. Attributes (state / instance variables)**

Attributes describe the properties of an object. In the object model they are richer than relational columns:

| Type of attribute | Meaning | Example |
|---|---|---|
| **Simple / Atomic** | A single indivisible value | `age = 22`, `name = "Vidit"` |
| **Composite** | Made of sub-attributes | `address = {street, city, pin}` |
| **Multivalued (set/list/bag/array)** | Holds a collection | `phone_numbers = {98…, 91…}` |
| **Derived** | Computed from other attributes | `age` derived from `dob` |
| **Reference (relationship) attribute** | Points to another object via its OID | `student.department → Department object` |
| **Class / static attribute** | Belongs to the class, shared by all objects | `total_students` |

Attributes may be `private`, `protected` or `public`; good OO design keeps them private and exposes them through accessor methods.

**2. Methods (behaviour / operations)**

A method is a function defined inside a class that operates on the object's state. It has a **signature** (name, parameter types, return type) — the public interface — and a **body** (implementation), which can be changed without affecting users of the class.

Common kinds:
- **Constructor** — creates and initialises a new object: `Student(prn, name)`.
- **Destructor** — releases the object.
- **Accessor (getter)** — returns state without changing it: `getName()`.
- **Mutator (setter)** — modifies state: `setAddress(a)`.
- **Business/processing method** — the real logic: `calculateCGPA()`, `computeWeight()`.
- **Class (static) method** — operates on the class rather than one object: `getTotalStudents()`.

Related concepts: **overloading** (same method name, different signatures — compile-time polymorphism), **overriding** (a subclass redefines an inherited method — run-time polymorphism), and **dynamic binding** (the correct implementation is chosen at run time based on the object's actual class).

In an OODBMS the methods are stored in the database along with the data, so the behaviour is shared by every application that uses the class.

**3. Relationships**

Relationships express how objects are associated. They are implemented by **reference attributes (OIDs)**, usually as an **inverse pair** so both directions stay consistent.

| Relationship | Meaning | Verb test | Example |
|---|---|---|---|
| **Association** | A general structural link between independent objects | "uses / works for" | `Student` ↔ `Course` |
| **Aggregation** | "has-a" / whole–part, where the part can exist independently | "has-a" | `Department` has `Professor`s — the professor survives if the department closes |
| **Composition** | Strong "part-of": the part cannot exist without the whole; deleting the whole deletes the parts | "part-of" | `Car` is composed of an `Engine`; `Book` composed of `Chapter`s |
| **Inheritance (generalisation / specialisation)** | "is-a": a subclass inherits attributes and methods of a superclass and may add or override | "is-a" | `ElectricEngine` **is-a** `Engine`; `Manager` **is-a** `Employee` |
| **Dependency** | One class temporarily uses another (e.g. as a parameter) | "depends-on" | `ReportGenerator` uses a `Printer` |

**Cardinality** applies as in the ER model: **1:1**, **1:N** and **M:N**. A 1:N relationship is stored as a single reference on one side and a set of references on the other.

**Class diagram (UML-style example)**

```
                +---------------------+
                |      Person         |   superclass
                |---------------------|
                | - name : String     |
                | - dob  : Date       |
                |---------------------|
                | + getAge() : int    |
                +----------+----------+
                           ^  (inheritance : is-a)
              +------------+------------+
              |                         |
   +----------+---------+     +---------+----------+
   |     Student        |     |     Professor      |
   |--------------------|     |--------------------|
   | - prn : String     |     | - empId : String   |
   | - marks : int[]    |     | - salary : double  |
   |--------------------|     |--------------------|
   | + calculateCGPA()  |     | + assignGrade()    |
   +----------+---------+     +---------+----------+
              |  M:N enrolls (association)  | 1:N teaches
              |                             |
        +-----v-----------------------------v-----+
        |                Course                    |
        |------------------------------------------|
        | - code : String                          |
        | - credits : int                          |
        |------------------------------------------|
        | + addStudent(s)                          |
        +------------------------------------------+
                  ^ composition (1 : N)
                  |
        +---------+---------+
        |      Module       |   cannot exist without its Course
        +-------------------+
```

**The four OO pillars, in one line each**

- **Encapsulation** — bind attributes and methods together and hide the internal state behind an interface.
- **Abstraction** — expose only what a user of the object needs to know (the method signatures).
- **Inheritance** — reuse and specialise an existing class, avoiding duplication.
- **Polymorphism** — one interface, many implementations, resolved at run time.

**Summary:** An object-oriented structure models the world as objects that carry an immutable identity (OID), a state defined by simple, composite, multivalued, derived and reference **attributes**, behaviour defined by constructor, accessor, mutator and business **methods**, and links to other objects through **relationships** — association, aggregation, composition and inheritance — with encapsulation, abstraction, inheritance and polymorphism as the underlying principles.

---

## Quick revision sheet

**Unit-wise questions**

| Q | One-line answer |
|---|---|
| U1-Q1 | Query processor (DDL interpreter, DML compiler, evaluation engine) + storage manager (authorisation, transaction, file, buffer managers) over data files, data dictionary, indices and statistics |
| U1-Q2 | See Q2 — clients request, a DBMS server responds with result sets |
| U1-Q3 | Server system = the server's internal design; client-server = division of work between client and server machines |
| U1-Q4 | Transaction server: server processes + lock manager, DB writer, log writer, checkpoint and process monitor around shared memory; a data server ships pages/objects |
| U1-Q5 | Server = one machine; parallel = many processors at one site, for speed; distributed = autonomous sites over a network, for availability |
| U1-Q6 | See Q4 — one logical database over many sites; local vs global transactions |
| U2-Q1 | Round-robin (even scans), hash (point queries) and range (range queries) partitioning across disks; skew is the main limit |
| U2-Q2 | One disk caps bandwidth; n disks cut scan time to about 1/n (100 s → 25 s on 4 disks) |
| U2-Q3 | Inter-query = many queries at once (throughput); intra-query = one query split up (response time) |
| U2-Q4 | Different transactions on different processors — raises OLTP throughput; needs cache coherency on shared-disk/shared-nothing |
| U2-Q5 | Intra-operation (parallel sort/join over partitions) + inter-operation (pipelined and independent) |
| U2-Q6 | Fragmentation, replication, allocation; consistency through 2PC, replica control (eager, ROWA, primary copy, quorum, lazy), distributed CC and recovery |
| U2-Q7 | Commit only on unanimous `ready` votes, otherwise abort everywhere — all-or-nothing across sites |
| U2-Q8 | See Q9 — a multi-site transaction kept atomic by 2PC |
| U2-Q9 | See Q11 — serializable schedules keep the database consistent and no committed update is lost |
| U2-Q10 | Serial, non-serial, serializable (conflict/view), recoverable/cascadeless/strict; the scheduler executes, delays or rejects operations to keep the precedence graph acyclic |
| U3-Q1 | See Q13 — tables + keys + SQL vs objects + OIDs + methods + inheritance |
| U3-Q2 | OID = unique, system-generated, immutable, value-independent; object = (OID, type constructor, state) |
| U3-Q3 | Atom, tuple, set, bag, list, array, dictionary — nested to build complex objects; `ROW(...)` and `ARRAY[...]` in SQL |
| U3 — 8 marks | Structured types as classes, `ROW(...)` as the constructor, `CREATE TABLE … OF` as the object table, display functions as methods |

**Questions by lecture date**

| Q | One-line answer |
|---|---|
| 1 | Database system architecture = levels of data abstraction (ANSI/SPARC); client-server = distribution of work across machines |
| 2 | Clients request, a server running the DBMS responds with result sets — centralised data, security and administration |
| 3 | Presentation + Application + Data tiers; clients never touch the DB directly, giving scalability and security |
| 4 | One logical database over many networked sites with location, fragmentation and replication transparency |
| 5 | A maintained copy of data at another site — availability and read speed vs update cost and consistency |
| 6 | An intermediary that caches, filters, secures, logs and load-balances traffic between clients and servers |
| 7 | Client-server = the model; server system architecture = the server's internals; client system architecture = thin vs fat client |
| 8 | Shared-nothing parallelism gives e-commerce throughput, sub-second search, peak-load scale-up and availability |
| 9 | Fragmentation + replication + allocation for storage; 2PC (prepare/vote → commit/abort) for atomic multi-site transactions |
| 10 | Concurrency raises throughput but risks anomalies; shared, exclusive, update and intention locks under 2PL fix them |
| 11 | CC enforces serializability via lock-based, timestamp, optimistic and multiversion protocols plus deadlock handling |
| 12 | CC is the scheduler between transaction manager and data — it enforces isolation and consistency while allowing interleaving |
| 13 | RDBMS = tables + keys + SQL (banking); OODBMS = objects + methods + inheritance + OIDs (CAD car design) |
| 14 | Object = OID + attributes (state) + methods (behaviour), linked by association, aggregation, composition and inheritance |
