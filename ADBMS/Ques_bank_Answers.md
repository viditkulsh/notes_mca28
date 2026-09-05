# ADBMS — Answers to Important Questions

Structured, exam-oriented answers to every question in [Ques_bank.md](Ques_bank.md). Numbering matches the question bank exactly, so question 9 here answers question 9 there.

Each answer follows the same shape: **Definition → Explanation / Diagram → Key points or comparison table → Advantages & limitations → One-line summary**, so it can be reproduced under exam time pressure.

> Student-written notes. Cross-check terminology against your class notes and the prescribed textbook (Silberschatz, Korth & Sudarshan, *Database System Concepts*) before an exam.

## Contents

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
  - [Q12. How Concurrency Control supports the transaction process](#q12-how-concurrency-control-supports-the-transaction-process)
- [31 Aug 2026 — OOPS](#31-aug-2026--oops)
  - [Q13. OODBMS vs RDBMS with a real-world example](#q13-oodbms-vs-rdbms-with-a-real-world-example)
  - [Q14. Object-oriented structure — Attributes, Methods, Relationships](#q14-object-oriented-structure--attributes-methods-relationships)

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
