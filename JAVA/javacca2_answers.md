# Java CCA-2: Exception Handling & Input/Output — Answers

Answers to [javacca2_questions.pdf](javacca2_questions.pdf): 5 questions × 10 marks (Q1–Q3 theory, Q4–Q5 practical). Each answer follows the question's mark breakdown.

Every program here was compiled and run on JDK 25. Each **Output** or **Sample run** block is the real output of that run. All code also compiles with `javac --release 8`. File-error messages such as *(No such file or directory)* come from macOS/Linux. On Windows the same errors read *(The system cannot find the file specified)* or *(The system cannot find the path specified)*.

## Contents

- [Q1. How Java handles exceptional situations](#q1-how-java-handles-exceptional-situations)
- [Q2. Tracing exception control flow and propagation](#q2-tracing-exception-control-flow-and-propagation)
- [Q3. Choosing the right stream for the data](#q3-choosing-the-right-stream-for-the-data)
- [Q4. Resilient student-record file reader](#q4-resilient-student-record-file-reader)
- [Q5. Copying a binary file safely and efficiently](#q5-copying-a-binary-file-safely-and-efficiently)
- [Quick revision sheet](#quick-revision-sheet)

---

## Q1. How Java handles exceptional situations

*Theory · 10 marks: hierarchy & concepts 3 · checked vs unchecked 3 · keywords + example 4*

An **exception** is an event that disrupts the normal flow of a program while it runs, such as a missing file, a division by zero or a `null` reference. Java represents it as an **object**. The code that detects the problem *throws* that object, and the JVM carries it back up the call stack until some code *catches* it. If no code catches it, the thread terminates with a stack trace.

### 1.1 The exception hierarchy

Everything that can be thrown extends `java.lang.Throwable`. A `Throwable` carries a **message** (`getMessage()`), an optional **cause** (`getCause()`, for chained exceptions) and the **stack trace** captured when it was created (`printStackTrace()`). Below `Throwable` the tree splits into two branches:

```text
java.lang.Object
└── java.lang.Throwable                               message + cause + stack trace
    ├── java.lang.Error                               the JVM or its environment has failed
    │   ├── VirtualMachineError
    │   │   ├── OutOfMemoryError
    │   │   └── StackOverflowError
    │   └── LinkageError
    │       └── NoClassDefFoundError
    └── java.lang.Exception                           conditions a program may want to handle
        ├── IOException                               ┐
        │   ├── FileNotFoundException                 │
        │   └── EOFException                          │  CHECKED
        ├── SQLException                              │  (compiler enforces handling)
        ├── InterruptedException                      │
        ├── user-defined (extends Exception)          ┘
        └── RuntimeException                          ┐
            ├── NullPointerException                  │
            ├── ArithmeticException                   │
            ├── ClassCastException                    │  UNCHECKED
            ├── IllegalArgumentException              │  (compiler does not enforce handling)
            │   └── NumberFormatException             │
            └── IndexOutOfBoundsException             │
                └── ArrayIndexOutOfBoundsException    ┘
```

- **`Error`**: a serious problem in the JVM itself, not in the program's logic, such as running out of memory or overflowing the stack. Applications are not expected to catch errors.
- **`Exception`**: a condition that a well-written program might anticipate and handle.
- **`RuntimeException`**: the subclass of `Exception` for problems that usually come from bugs in the code itself.

The rule that decides checked vs unchecked: **`RuntimeException`, `Error` and their subclasses are unchecked. Every other `Throwable` is checked.**

### 1.2 Errors vs checked vs unchecked exceptions

| Decision point | `Error` | Checked exception | Unchecked exception |
|---|---|---|---|
| Classes | `Error` and its subclasses | `Exception` and its subclasses, **except** the `RuntimeException` branch | `RuntimeException` and its subclasses |
| What it signals | The JVM or its environment has failed | A **foreseeable failure outside the program's control**: a missing file, a network outage, a database that is down | A **programming mistake or broken precondition**: `null`, a bad index, an illegal argument |
| What the **compiler** enforces | Nothing | The **catch-or-declare rule**: each checked exception a method can throw must be caught inside it or listed in its `throws` clause, or the code does not compile | Nothing. Catching or declaring is optional |
| What happens at **runtime** | It propagates up the stack and normally terminates the thread | It propagates until a matching `catch`. If there is none, the thread terminates with a stack trace | Exactly the same as for a checked exception. The JVM treats all throwables alike, because "checked" is a compile-time idea only |
| Who is responsible for **recovery** | No one inside the program. At most, log it and shut down | The **caller that can act**: ask for another file, retry, or fall back to a default. A `throws` clause hands that responsibility to the caller | The **programmer**, who fixes the code or validates input before using it. Catch it only where untrusted input enters the program (for example, a `NumberFormatException` from user input) |
| Examples | `OutOfMemoryError`, `StackOverflowError` | `IOException`, `FileNotFoundException`, `SQLException`, `InterruptedException` | `NullPointerException`, `ArithmeticException`, `ArrayIndexOutOfBoundsException`, `NumberFormatException` |

**What the compiler enforces, in practice.** If a method calls `loadMarks()`, which declares `throws IOException`, and neither catches nor declares that exception, `javac` rejects it:

```java
import java.io.IOException;

public class CompileCheck {
    static int loadMarks(String fileName) throws IOException {
        throw new IOException("cannot read " + fileName);
    }

    public static void main(String[] args) {
        int marks = loadMarks("marks.pdf");          // checked exception neither caught nor declared
        System.out.println(marks);
    }
}
```

```text
$ javac CompileCheck.java
CompileCheck.java:9: error: unreported exception IOException; must be caught or declared to be thrown
        int marks = loadMarks("marks.pdf");          // checked exception neither caught nor declared
                             ^
1 error
```

The compiler also checks two more things about `catch` clauses for checked exceptions:

```java
import java.io.FileNotFoundException;
import java.io.IOException;

public class CompileCheck2 {
    public static void main(String[] args) {
        try {
            System.out.println("no I/O here");
        } catch (IOException e) {                    // nothing in the try can throw it
            System.out.println("never");
        }

        try {
            throw new FileNotFoundException("x");
        } catch (IOException e) {
            System.out.println("general");
        } catch (FileNotFoundException e) {          // subclass after its superclass
            System.out.println("specific");
        }
    }
}
```

```text
$ javac CompileCheck2.java
CompileCheck2.java:8: error: exception IOException is never thrown in body of corresponding try statement
        } catch (IOException e) {                    // nothing in the try can throw it
          ^
CompileCheck2.java:16: error: exception FileNotFoundException has already been caught
        } catch (FileNotFoundException e) {          // subclass after its superclass
          ^
2 errors
```

None of these checks apply to unchecked exceptions. Code such as `int x = 10 / 0;` compiles cleanly and fails only at runtime.

### 1.3 How `try`, `catch`, `finally`, `throw` and `throws` work together

| Keyword | Where it appears | What it does |
|---|---|---|
| `try { … }` | Around statements that may fail | Marks the guarded region. It must be followed by at least one `catch` or a `finally`, unless it is a try-with-resources |
| `catch (Type e) { … }` | After `try` | Handles an exception whose class is `Type` or a subclass of it. Clauses are tested top to bottom and **only the first match runs**. `e` is the thrown object |
| `finally { … }` | After `try`/`catch` | **Always** runs when control leaves the `try`: after normal completion, a caught exception, an uncaught exception, or a `return`/`break`. It is used for clean-up |
| `throw expr;` | Statement inside a method | Throws **one** exception object, as in `throw new IOException("…")`. The current block stops immediately |
| `throws T1, T2` | Method header | **Declares** the checked exceptions the method passes on to its caller. It satisfies the compiler and has no effect at runtime |

The sequence at runtime:

1. **`throw`** creates an exception object (recording the stack trace at that moment) and throws it. The rest of the current block is skipped.
2. The JVM searches the **current method** for an enclosing `try` whose `catch` type matches, testing the clauses in order.
3. If none matches, the method **ends abruptly**. Any `finally` blocks on the way out run first, the method's stack frame is popped, and the exception reappears at the **call site in the caller**. The search repeats there. This is **propagation**, and a checked exception needs a **`throws`** clause to travel this way.
4. When a matching **`catch`** is found, control jumps into it with `e` referring to the same object. After the `catch`, the **`finally`** block runs, and execution continues with the statement after the whole `try` statement.
5. If the exception passes `main()` without being caught, the JVM's default handler prints `Exception in thread "main" …` and the stack trace, and the thread dies (the program exits with status 1).

Since Java 7, **try-with-resources** (`try (Resource r = …) { … }`) adds automatic clean-up. Every resource declared in the parentheses is closed when the block ends, even after an exception. Q4 and Q5 use it.

### 1.4 Example

`loadMarks()` throws a **checked** `IOException` and must declare it. `percentage()` throws an **unchecked** `IllegalArgumentException` and needs no `throws`. `main()` recovers from the checked exception but deliberately leaves the unchecked one uncaught.

```java
import java.io.IOException;

public class ExceptionBasics {
    // throws: loadMarks() may pass a CHECKED exception on to its caller
    static int loadMarks(String fileName) throws IOException {
        if (!fileName.endsWith(".txt")) {
            throw new IOException("cannot read " + fileName);       // throw: raise the exception
        }
        return 72;
    }

    // An UNCHECKED exception needs no throws clause
    static double percentage(int marks, int total) {
        if (total <= 0) {
            throw new IllegalArgumentException("total must be positive, got " + total);
        }
        return marks * 100.0 / total;
    }

    public static void main(String[] args) {
        String[] files = {"marks.txt", "marks.pdf"};
        for (String file : files) {
            try {
                int marks = loadMarks(file);                         // may throw IOException
                System.out.println(file + " -> " + percentage(marks, 80) + "%");
            } catch (IOException e) {                                // the caller recovers
                System.out.println(file + " -> recovered: " + e.getMessage());
            } finally {
                System.out.println(file + " -> finally: cleanup done");
            }
        }
        System.out.println(percentage(72, 0));                       // unchecked and not caught
    }
}
```

**Output**

```text
marks.txt -> 90.0%
marks.txt -> finally: cleanup done
marks.pdf -> recovered: cannot read marks.pdf
marks.pdf -> finally: cleanup done
Exception in thread "main" java.lang.IllegalArgumentException: total must be positive, got 0
	at ExceptionBasics.percentage(ExceptionBasics.java:15)
	at ExceptionBasics.main(ExceptionBasics.java:32)
```

How each part of the output shows a decision point:

- **`marks.txt`**: nothing is thrown. The `try` block completes, `catch` is skipped and `finally` still runs.
- **`marks.pdf`**: `throw` raises the `IOException` inside `loadMarks()`. The `throws` clause lets it propagate to `main()`, where `catch` **recovers**, and then `finally` runs. The compiler insisted on this handling (§1.2).
- **`percentage(72, 0)`**: the `IllegalArgumentException` is unchecked, so the code compiled without any `try` or `throws`. At runtime **nobody recovers**: the default handler prints the stack trace (thrown at line 15, called from line 32) and the program exits with status 1.

---

## Q2. Tracing exception control flow and propagation

*Theory · 10 marks: output 3 · reasoning 4 · finally 3*

### 2.1 Output

```text
B
C
```

`A` is never printed, and neither is the message `"data"`. The question's code is shown below as a complete program (with an `import` and a class around it), followed by its real output:

```java
import java.io.IOException;

public class TraceDemo {
    static void read() throws IOException {
        throw new IOException("data");
    }

    public static void main(String[] args) {
        try { read(); System.out.println("A"); }
        catch (IOException e) { System.out.println("B"); }
        finally { System.out.println("C"); }
    }
}
```

```text
$ java TraceDemo
B
C
```

The program ends normally with exit status 0, because the exception was handled.

### 2.2 Why each line does, or does not, execute

| Step | Statement | Executes? | Reason |
|---|---|---|---|
| 1 | `try {` … `read();` | **Yes** | `main()` enters the `try` block and calls `read()` |
| 2 | `throw new IOException("data");` | **Yes** | It creates an `IOException` with the message `"data"`, records the current stack trace and throws it. `read()` ends abruptly at this point |
| 3 | `System.out.println("A");` | **No** | Once `read()` throws, control never returns normally to the statement after the call. The rest of the `try` block is abandoned |
| 4 | `catch (IOException e)` → `println("B")` | **Yes** | The thrown object is an `IOException`, so this clause matches. `e` refers to that object. It prints **B** |
| 5 | `finally` → `println("C")` | **Yes** | `finally` always runs when control leaves the `try` statement. It prints **C** |
| 6 | End of `main()` | **Yes** | The exception was handled, so the program ends normally. No stack trace appears, and `"data"` is never printed because the `catch` block does not print `e.getMessage()` |

### 2.3 Propagation: how the `IOException` reaches the `catch`

When `read()` is running, the call stack holds two frames:

```text
  read()   ← exception thrown here (no try/catch in this method)
  main()   ← read() was called from inside a try block
```

1. The JVM first looks **inside `read()`** for an enclosing `try` with a matching `catch`. There is none.
2. `read()` therefore **completes abruptly**. Its frame is popped and the same exception object is re-thrown at the **call site**, the `read();` statement in `main()`.
3. That call site is inside `main()`'s `try`, so the JVM tests `main()`'s `catch` clauses. `catch (IOException e)` matches, and control transfers there.

The compiler's role: `IOException` is **checked**, so `read()` *must* declare `throws IOException`. That declaration both allows the exception to leave `read()` and tells every caller to deal with it. If `main()` had neither the `catch` nor its own `throws IOException`, the program would not compile (see the compiler error in [Q1](#12-errors-vs-checked-vs-unchecked-exceptions)).

The stack trace stored in the exception records this path. Adding `e.printStackTrace(System.out);` to the `catch` makes it visible:

```java
import java.io.IOException;

public class TracePath {
    static void read() throws IOException {
        throw new IOException("data");
    }

    public static void main(String[] args) {
        try { read(); System.out.println("A"); }
        catch (IOException e) { System.out.println("B"); e.printStackTrace(System.out); }
        finally { System.out.println("C"); }
    }
}
```

```text
$ java TracePath
B
java.io.IOException: data
	at TracePath.read(TracePath.java:5)
	at TracePath.main(TracePath.java:9)
C
```

The top line of the trace is where the exception was **thrown** (`read`, line 5). The line below it is the caller it **propagated** into (`main`, line 9), where it was caught.

### 2.4 The role of `finally` in this execution

In this run, `finally` executes **after the `catch` block** and prints `C`. The order is: part of the `try` → `catch` → `finally` → the statement after the `try` statement. `finally` is Java's guaranteed exit point from a `try`, which makes it the place for clean-up such as closing a file or releasing a lock. It runs **whether or not** an exception occurred and **whether or not** it was caught. The variant below shows `C` printed in every case:

```java
import java.io.IOException;

public class FinallyCases {
    static void read(boolean fail) throws IOException {
        if (fail) {
            throw new IOException("data");
        }
    }

    // Case 1: read() succeeds
    static void noException() {
        try { read(false); System.out.println("A"); }
        catch (IOException e) { System.out.println("B"); }
        finally { System.out.println("C"); }
    }

    // Case 2: catch returns early
    static void returnInCatch() {
        try { read(true); System.out.println("A"); }
        catch (IOException e) { System.out.println("B"); return; }
        finally { System.out.println("C"); }
        System.out.println("after try");                 // skipped by the return
    }

    // Case 3: no matching catch, so the exception keeps travelling
    static void notCaught() {
        try { throw new IllegalStateException("bug"); }
        catch (IllegalArgumentException e) { System.out.println("B"); }
        finally { System.out.println("C"); }
    }

    public static void main(String[] args) {
        System.out.println("-- case 1: no exception --");
        noException();
        System.out.println("-- case 2: return inside catch --");
        returnInCatch();
        System.out.println("-- case 3: catch does not match --");
        try {
            notCaught();
        } catch (IllegalStateException e) {
            System.out.println("main caught: " + e.getMessage());
        }
    }
}
```

```text
$ java FinallyCases
-- case 1: no exception --
A
C
-- case 2: return inside catch --
B
C
-- case 3: catch does not match --
C
main caught: bug
```

| Case | What happens | Does `finally` print `C`? |
|---|---|---|
| Question's program | Exception thrown and caught: `B`, then `C` | Yes, after the `catch` |
| 1. No exception | `try` completes: `A`, then `C` | Yes, after the `try` |
| 2. `return` inside `catch` | `B`, then `C`, then the method returns. `"after try"` is skipped | Yes, **before** the method actually returns |
| 3. No matching `catch` | `C`, then the exception continues to the caller (`main caught: bug`) | Yes, **before** the exception propagates |

`finally` is skipped only if the JVM stops inside the `try` or `catch`, for example through `System.exit()` or a crash. Avoid `return` or `throw` inside `finally`, because either one silently discards the original exception.

---

## Q3. Choosing the right stream for the data

*Theory · 10 marks: comparison 4 · selection & reasoning 4 · buffering 2*

### 3.1 Byte streams vs character streams

A file on disk contains **only bytes**. The real question is whether those bytes **represent text**. Text bytes must be **decoded with a character set** (UTF-8, ISO-8859-1, …) before they mean anything. Bytes of an image, PDF or ZIP must **not** be decoded at all.

- **Byte streams** (`InputStream` / `OutputStream`) move raw 8-bit bytes with no interpretation.
- **Character streams** (`Reader` / `Writer`) move 16-bit `char` values. Internally, a character stream is a byte stream plus a **charset decoder/encoder**: `FileReader` is an `InputStreamReader` over a `FileInputStream`.

```text
BYTE STREAMS (binary data)                 CHARACTER STREAMS (text)
InputStream (abstract)                     Reader (abstract)
├── FileInputStream                        ├── InputStreamReader   ← bridge: bytes → chars (charset)
├── ByteArrayInputStream                   │   └── FileReader
└── FilterInputStream                      ├── BufferedReader      (adds readLine())
    ├── BufferedInputStream                └── StringReader
    └── DataInputStream
OutputStream (abstract)                    Writer (abstract)
├── FileOutputStream                       ├── OutputStreamWriter  ← bridge: chars → bytes (charset)
├── ByteArrayOutputStream                  │   └── FileWriter
└── FilterOutputStream                     ├── BufferedWriter      (adds newLine())
    ├── BufferedOutputStream               ├── PrintWriter
    ├── DataOutputStream                   └── StringWriter
    └── PrintStream  (System.out)
```

| Basis | Byte streams | Character streams |
|---|---|---|
| Abstract base classes | `InputStream`, `OutputStream` | `Reader`, `Writer` |
| Unit of data | 8-bit byte. `read()` returns 0–255, or −1 at end of stream | 16-bit `char`. `read()` returns 0–65535, or −1 at end of stream |
| Encoding | None: bytes pass through unchanged | Bytes are **decoded** on input and **encoded** on output using a charset |
| Suitable data | Binary: images (JPEG, PNG), audio, video, PDF, ZIP, `.class` files, serialised objects | Text: `.txt`, `.csv`, `.properties`, `.json`, `.xml`, `.html`, source code |
| File classes | `FileInputStream`, `FileOutputStream` | `FileReader`, `FileWriter` |
| Buffered wrappers | `BufferedInputStream`, `BufferedOutputStream` | `BufferedReader` (`readLine()`), `BufferedWriter` (`newLine()`) |
| Array used with `read(…)` | `byte[]` | `char[]` |
| Cost of the wrong choice | For text, you must decode bytes yourself, and multi-byte characters break if handled one byte at a time | For binary data, byte sequences that are invalid in the charset are **replaced**, which corrupts the file |

### 3.2 Decision task

**(a) Reading a UTF-8 configuration file → a character stream: `BufferedReader` with the charset stated explicitly**

```java
try (BufferedReader reader = Files.newBufferedReader(Paths.get("app.properties"), StandardCharsets.UTF_8)) {
    String line;
    while ((line = reader.readLine()) != null) {
        // parse "key=value"
    }
}
// For key=value files, Properties can read through the same Reader:  props.load(reader);
```

Justification:

- A configuration file is **text**. The program needs characters and whole lines (`readLine()`), not raw bytes.
- **UTF-8 is a variable-length encoding.** ASCII characters take 1 byte, `é` takes 2 bytes (`C3 A9`) and `₹` takes 3. A decoder must see each whole byte sequence, so reading byte by byte and casting each byte to `char` corrupts every non-ASCII character. A `Reader` does this decoding correctly.
- **State the charset.** `new FileReader("app.properties")` uses the platform's default charset. That default is UTF-8 only from JDK 18 onwards. Before that it depended on the operating system (for example, windows-1252 on Windows), so the same file could read differently on different machines. Alternatives that name the charset: `new FileReader(file, StandardCharsets.UTF_8)` (Java 11+) or `new BufferedReader(new InputStreamReader(new FileInputStream(file), StandardCharsets.UTF_8))`.
- `Files.newBufferedReader` is also **strict**: bytes that are not valid UTF-8 cause a `MalformedInputException` instead of being silently replaced with `�`. That suits a configuration file, where it is better to fail than to misread a setting.
- Do **not** pass an `InputStream` to `Properties.load()`. That overload decodes as ISO-8859-1, and the demo below shows the resulting garbled text.

**(b) Copying a JPEG → a byte stream: `BufferedInputStream` + `BufferedOutputStream` with a `byte[]` chunk**

```java
try (InputStream in = new BufferedInputStream(new FileInputStream("photo.jpg"));
     OutputStream out = new BufferedOutputStream(new FileOutputStream("photo_copy.jpg"))) {
    byte[] buffer = new byte[8192];
    int n;
    while ((n = in.read(buffer)) != -1) {
        out.write(buffer, 0, n);
    }
}
```

(Q5 is the full command-line version of this. In production code, `Files.copy(source, target)` does the same job.)

Justification:

- A JPEG is **compressed binary data**. Its bytes can take any value from 0 to 255, and they are not characters. The file even begins with `FF D8 FF E0`, which is not valid UTF-8.
- A `Reader` would decode the file and replace every invalid sequence with U+FFFD (`�`). The `Writer` would then encode each replacement as `EF BF BD`. The copy comes out **larger and corrupted**: in the demo, 25,676 bytes became 48,886.
- Byte streams pass every byte through **unchanged**, so the copy is byte-for-byte identical. The task needs no text conversion, so none should take place.

### 3.3 What buffering changes

- **Without buffering**, every `read()` or `write()` on a `FileInputStream` or `FileOutputStream` is a native call into the operating system. Reading a file one byte at a time therefore makes one system call per byte.
- **With buffering**, `BufferedInputStream` and `BufferedReader` fetch a whole block (8,192 bytes or chars by default) into an internal array and serve later `read()` calls from memory. They go back to the file only when the array is empty. `BufferedOutputStream` and `BufferedWriter` collect output in memory and write a whole block when the array fills up, when `flush()` is called, or when the stream is closed.
- Buffering changes **how often the program touches the disk** and therefore how fast it runs. It does **not** change the data. The character-stream buffers also add the line methods `readLine()` and `newLine()`.
- The gain is largest for many small operations, such as `read()`, `readLine()` or `write(int)`. A program that already moves data in large chunks itself (Q5 uses `byte[8192]`) gains less, because it already makes only one call per 8 KB.
- **Caveat:** output still waiting in a buffer is lost if the stream is never flushed or closed. Close streams with try-with-resources, and call `flush()` when the data must reach the file before the stream is closed.

In the demo below, reading a 25,676-byte JPEG byte by byte asked the file for data **25,677 times** without a buffer, but only **5 times** with one (⌈25,676 ÷ 8,192⌉ = 4 block reads, plus 1 read that reports end of file).

### 3.4 Demo program: proving each choice

This program writes a UTF-8 configuration file and reads it both ways. It then creates a small JPEG, copies it with each kind of stream, and counts the reads made with and without a buffer.

```java
import java.awt.image.BufferedImage;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Properties;
import javax.imageio.ImageIO;

public class StreamChoiceDemo {
    public static void main(String[] args) throws IOException {
        // ---------- (a) UTF-8 configuration file ----------
        Path config = Paths.get("app.properties");
        String line = "app.name=Café Billing";
        Files.write(config, Arrays.asList(line, "owner=Zoë"), StandardCharsets.UTF_8);
        System.out.println("(a) \"" + line + "\" = " + line.length() + " characters but "
                + line.getBytes(StandardCharsets.UTF_8).length + " bytes in UTF-8");

        Properties viaReader = new Properties();
        try (BufferedReader reader = Files.newBufferedReader(config, StandardCharsets.UTF_8)) {
            viaReader.load(reader);                              // character stream, charset stated
        }
        Properties viaBytes = new Properties();
        try (InputStream in = new BufferedInputStream(new FileInputStream("app.properties"))) {
            viaBytes.load(in);                                   // byte stream: decoded as ISO-8859-1
        }
        System.out.println("    BufferedReader (UTF-8) : " + viaReader.getProperty("app.name")
                + ", " + viaReader.getProperty("owner"));
        System.out.println("    InputStream (bytes)    : " + viaBytes.getProperty("app.name")
                + ", " + viaBytes.getProperty("owner"));

        // ---------- (b) JPEG file ----------
        File photo = new File("photo.jpg");
        createTestJpeg(photo);
        copyWithByteStreams(photo, new File("copy_bytes.jpg"));
        copyWithCharStreams(photo, new File("copy_chars.jpg"));
        System.out.println();
        System.out.println("(b) photo.jpg          : " + photo.length() + " bytes");
        report("copy_bytes.jpg", photo);
        report("copy_chars.jpg", photo);

        // ---------- buffering ----------
        CountingInputStream direct = new CountingInputStream(new FileInputStream(photo));
        try (InputStream in = direct) {
            while (in.read() != -1) { }                          // one byte per call
        }
        CountingInputStream underBuffer = new CountingInputStream(new FileInputStream(photo));
        try (InputStream in = new BufferedInputStream(underBuffer)) {
            while (in.read() != -1) { }                          // same loop, buffered
        }
        System.out.println();
        System.out.println("Reading photo.jpg one byte at a time:");
        System.out.println("    FileInputStream alone         : " + direct.calls + " reads from the file");
        System.out.println("    wrapped in BufferedInputStream: " + underBuffer.calls + " reads from the file");
    }

    // Recommended: byte streams with a fixed-size chunk
    static void copyWithByteStreams(File src, File dst) throws IOException {
        try (InputStream in = new BufferedInputStream(new FileInputStream(src));
             OutputStream out = new BufferedOutputStream(new FileOutputStream(dst))) {
            byte[] buffer = new byte[8192];
            int n;
            while ((n = in.read(buffer)) != -1) {
                out.write(buffer, 0, n);
            }
        }
    }

    // Wrong tool: decodes the bytes as UTF-8 text and encodes them again
    static void copyWithCharStreams(File src, File dst) throws IOException {
        try (Reader in = new BufferedReader(new InputStreamReader(new FileInputStream(src), StandardCharsets.UTF_8));
             Writer out = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(dst), StandardCharsets.UTF_8))) {
            char[] buffer = new char[8192];
            int n;
            while ((n = in.read(buffer)) != -1) {
                out.write(buffer, 0, n);
            }
        }
    }

    static void report(String name, File original) throws IOException {
        byte[] a = Files.readAllBytes(original.toPath());       // small test file, fine to compare in memory
        byte[] b = Files.readAllBytes(Paths.get(name));
        System.out.printf("    %-18s : %d bytes, identical = %b%n", name, b.length, Arrays.equals(a, b));
    }

    static void createTestJpeg(File file) throws IOException {
        BufferedImage img = new BufferedImage(320, 240, BufferedImage.TYPE_INT_RGB);
        for (int x = 0; x < 320; x++) {
            for (int y = 0; y < 240; y++) {
                img.setRGB(x, y, ((x * 7) % 256) << 16 | ((y * 13) % 256) << 8 | ((x * y) % 256));
            }
        }
        ImageIO.write(img, "jpg", file);
    }

    // Counts how many times the stream underneath is actually asked for data
    static class CountingInputStream extends FilterInputStream {
        int calls;

        CountingInputStream(InputStream in) {
            super(in);
        }

        @Override
        public int read() throws IOException {
            calls++;
            return super.read();
        }

        @Override
        public int read(byte[] b, int off, int len) throws IOException {
            calls++;
            return super.read(b, off, len);
        }
    }
}
```

**Output**

```text
(a) "app.name=Café Billing" = 21 characters but 22 bytes in UTF-8
    BufferedReader (UTF-8) : Café Billing, Zoë
    InputStream (bytes)    : CafÃ© Billing, ZoÃ«

(b) photo.jpg          : 25676 bytes
    copy_bytes.jpg     : 25676 bytes, identical = true
    copy_chars.jpg     : 48886 bytes, identical = false

Reading photo.jpg one byte at a time:
    FileInputStream alone         : 25677 reads from the file
    wrapped in BufferedInputStream: 5 reads from the file
```

Looking inside the two copies with `xxd` shows exactly what the character stream did to the JPEG header:

```text
$ xxd -l 16 photo.jpg
00000000: ffd8 ffe0 0010 4a46 4946 0001 0200 0001  ......JFIF......
$ xxd -l 16 copy_chars.jpg
00000000: efbf bdef bfbd efbf bdef bfbd 0010 4a46  ..............JF
```

The four bytes `FF D8 FF E0` became four replacement characters (`EF BF BD` × 4), so `copy_chars.jpg` no longer opens as an image. The JPEG size can vary slightly between JDK versions, but every result holds.

---

## Q4. Resilient student-record file reader

*Practical · 10 marks: logic 4 · exceptions & resources 3 · output/logging 2 · clarity 1*

### 4.1 Approach

| Requirement | How the program meets it |
|---|---|
| Use `BufferedReader` / `BufferedWriter` | `BufferedReader` over a `FileReader` reads `students.txt` line by line with `readLine()`. Two `BufferedWriter`s over `FileWriter`s write the output files, using `newLine()` |
| 01 Validate the format and a 0–100 score | `parse()` checks for exactly two comma-separated fields, a non-empty name, a whole-number score (`Integer.parseInt`) and the range 0–100. Each failure throws an `InvalidRecordException` that states the reason |
| 02 Score ≥ 40 → `passed.txt` | Valid records with `score >= PASS_MARK` are written in the clean form `name,score` |
| 03 Malformed or out-of-range lines → `errors.txt` | Each bad line is logged with its line number, the original text and the reason |
| Do not stop at an invalid line | The `try`/`catch` for `InvalidRecordException` sits **inside** the loop, so a bad line is logged and the loop moves on to the next one |
| 04 Handle file errors and close every resource | All three files are opened in one **try-with-resources**, so they are closed automatically in reverse order, even after an exception. `FileNotFoundException` (a file cannot be opened or created) and other `IOException`s (a failure part-way) are reported separately |

Valid records **below 40** (such as `Meera,35`) go to neither file, because they are neither passes nor errors. The console log and the summary count them.

### 4.2 Program

```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

// Thrown for one bad line; it is caught per line, so processing continues
class InvalidRecordException extends Exception {
    InvalidRecordException(String message) {
        super(message);
    }
}

public class StudentRecordProcessor {
    static final String INPUT_FILE = "students.txt";
    static final String PASSED_FILE = "passed.txt";
    static final String ERRORS_FILE = "errors.txt";
    static final int PASS_MARK = 40;

    static class Student {
        final String name;
        final int score;

        Student(String name, int score) {
            this.name = name;
            this.score = score;
        }
    }

    // Validates one "name,score" line and returns the record, or throws with the reason
    static Student parse(String line) throws InvalidRecordException {
        String[] parts = line.split(",", -1);                  // -1 keeps empty fields such as "Asha,"
        if (parts.length != 2) {
            throw new InvalidRecordException("expected name,score but found " + parts.length + " field(s)");
        }
        String name = parts[0].trim();
        String scoreText = parts[1].trim();
        if (name.isEmpty()) {
            throw new InvalidRecordException("name is empty");
        }
        int score;
        try {
            score = Integer.parseInt(scoreText);
        } catch (NumberFormatException e) {
            throw new InvalidRecordException("score \"" + scoreText + "\" is not a whole number");
        }
        if (score < 0 || score > 100) {
            throw new InvalidRecordException("score " + score + " is outside 0-100");
        }
        return new Student(name, score);
    }

    public static void main(String[] args) {
        int lineNo = 0, passed = 0, belowPassMark = 0, errors = 0, blank = 0;

        // try-with-resources closes all three files (in reverse order), even if an exception occurs
        try (BufferedReader reader = new BufferedReader(new FileReader(INPUT_FILE));
             BufferedWriter passedOut = new BufferedWriter(new FileWriter(PASSED_FILE));
             BufferedWriter errorOut = new BufferedWriter(new FileWriter(ERRORS_FILE))) {

            String line;
            while ((line = reader.readLine()) != null) {
                lineNo++;
                if (line.trim().isEmpty()) {
                    blank++;
                    continue;
                }
                try {
                    Student s = parse(line);
                    if (s.score >= PASS_MARK) {
                        passedOut.write(s.name + "," + s.score);
                        passedOut.newLine();
                        passed++;
                        System.out.printf("Line %2d  PASSED    %s%n", lineNo, line);
                    } else {
                        belowPassMark++;
                        System.out.printf("Line %2d  BELOW %d  %s%n", lineNo, PASS_MARK, line);
                    }
                } catch (InvalidRecordException e) {         // log it and move on to the next line
                    errorOut.write("Line " + lineNo + ": " + line + " -> " + e.getMessage());
                    errorOut.newLine();
                    errors++;
                    System.out.printf("Line %2d  ERROR     %s (%s)%n", lineNo, line, e.getMessage());
                }
            }
        } catch (FileNotFoundException e) {                   // a file could not be opened or created
            System.err.println("Cannot open file: " + e.getMessage());
            System.exit(1);
        } catch (IOException e) {                             // a read or write failed part-way
            System.err.println("I/O error after line " + lineNo + ": " + e.getMessage());
            System.exit(1);
        }

        System.out.println();
        System.out.println(lineNo + " lines read: " + passed + " passed, " + belowPassMark + " below "
                + PASS_MARK + ", " + errors + " errors, " + blank + " blank");
        System.out.println("Wrote " + PASSED_FILE + " and " + ERRORS_FILE);
    }
}
```

### 4.3 Sample run 1: the input given in the question

`students.txt`

```text
Asha,78
Ravi,abc
Meera,35
Dev,105
```

```text
$ javac StudentRecordProcessor.java
$ java StudentRecordProcessor
Line  1  PASSED    Asha,78
Line  2  ERROR     Ravi,abc (score "abc" is not a whole number)
Line  3  BELOW 40  Meera,35
Line  4  ERROR     Dev,105 (score 105 is outside 0-100)

4 lines read: 1 passed, 1 below 40, 2 errors, 0 blank
Wrote passed.txt and errors.txt
```

`passed.txt`

```text
Asha,78
```

`errors.txt`

```text
Line 2: Ravi,abc -> score "abc" is not a whole number
Line 4: Dev,105 -> score 105 is outside 0-100
```

The invalid line 2 did not stop the program. Lines 3 and 4 were still processed.

### 4.4 Sample run 2: edge cases

This `students.txt` adds a blank line, a missing comma, extra spaces, an empty name, a negative score, an extra field, a decimal score, a non-ASCII name and the boundary scores 40, 100 and 0:

```text
Asha,78
Ravi,abc
Meera,35
Dev,105

Kiran
 Neha , 40 
,55
Arjun,-5
Sara,88,extra
Vikram,7.5
Zoë,100
Om,0
```

```text
$ java StudentRecordProcessor
Line  1  PASSED    Asha,78
Line  2  ERROR     Ravi,abc (score "abc" is not a whole number)
Line  3  BELOW 40  Meera,35
Line  4  ERROR     Dev,105 (score 105 is outside 0-100)
Line  6  ERROR     Kiran (expected name,score but found 1 field(s))
Line  7  PASSED     Neha , 40 
Line  8  ERROR     ,55 (name is empty)
Line  9  ERROR     Arjun,-5 (score -5 is outside 0-100)
Line 10  ERROR     Sara,88,extra (expected name,score but found 3 field(s))
Line 11  ERROR     Vikram,7.5 (score "7.5" is not a whole number)
Line 12  PASSED    Zoë,100
Line 13  BELOW 40  Om,0

13 lines read: 3 passed, 2 below 40, 7 errors, 1 blank
Wrote passed.txt and errors.txt
```

`passed.txt`. Note that `" Neha , 40 "` is trimmed to `Neha,40`:

```text
Asha,78
Neha,40
Zoë,100
```

`errors.txt`

```text
Line 2: Ravi,abc -> score "abc" is not a whole number
Line 4: Dev,105 -> score 105 is outside 0-100
Line 6: Kiran -> expected name,score but found 1 field(s)
Line 8: ,55 -> name is empty
Line 9: Arjun,-5 -> score -5 is outside 0-100
Line 10: Sara,88,extra -> expected name,score but found 3 field(s)
Line 11: Vikram,7.5 -> score "7.5" is not a whole number
```

### 4.5 Sample runs 3 and 4: file errors

**Run 3: `students.txt` does not exist**

```text
$ java StudentRecordProcessor
Cannot open file: students.txt (No such file or directory)
```

The reader is the first resource in the try-with-resources, so when it fails, the two writers are never created. No empty `passed.txt` or `errors.txt` is left behind, and the program exits with status 1.

**Run 4: an output file cannot be created** (here `passed.txt` is a folder)

```text
$ java StudentRecordProcessor
Cannot open file: passed.txt (Is a directory)
```

The reader was already open when `passed.txt` failed. Try-with-resources closed it automatically before the `catch` block ran.

**Notes**

- **Resource safety:** try-with-resources calls `close()` on every resource that was opened successfully, in reverse order (`errorOut` → `passedOut` → `reader`). Closing a `BufferedWriter` also flushes its last block to disk. If `close()` itself fails while another exception is already in flight, the second exception is attached to the first as a *suppressed* exception (`e.getSuppressed()`) rather than replacing it.
- **Why a custom checked exception:** `parse()` declares `throws InvalidRecordException`, so the compiler forces the loop to handle bad records. `NumberFormatException` (unchecked) is caught inside `parse()` and turned into a clear message. Every validation failure therefore reaches `errors.txt` through a single `catch`.
- **Charset:** `FileReader` and `FileWriter` use the platform's default charset, which is UTF-8 on JDK 18+ (that is why `Zoë` worked). On older JDKs, use `new FileReader(INPUT_FILE, StandardCharsets.UTF_8)` (Java 11+) or `new InputStreamReader(new FileInputStream(INPUT_FILE), StandardCharsets.UTF_8)`, as explained in [Q3](#32-decision-task).

---

## Q5. Copying a binary file safely and efficiently

*Practical · 10 marks: copy logic 4 · resources 2 · error handling 2 · CLI & reporting 2*

### 5.1 Acceptance check

| Requirement | How the program meets it |
|---|---|
| 01 Read paths from `args[]` | `args[0]` is the source and `args[1]` the destination. Any other number of arguments prints a usage message and exits with status 1 |
| 02 Copy in chunks with buffered byte streams | `BufferedInputStream(FileInputStream)` → `BufferedOutputStream(FileOutputStream)`, through a fixed `byte[8192]` |
| 03 Report bytes copied | A running total of the bytes actually read is printed on success |
| 03 Handle a missing source and a write failure separately | Nested try-with-resources: the outer `catch (FileNotFoundException)` can only mean the **source** failed to open (exit 2). The inner catches mean the **destination** could not be created, or writing failed part-way (exit 3) |
| ✓ Uses `InputStream` / `OutputStream` | Variables are typed as the abstract `InputStream` / `OutputStream` |
| ✓ Wraps streams for buffering | `BufferedInputStream` / `BufferedOutputStream` |
| ✓ Uses try-with-resources | Both streams are closed automatically on every path, including the early `return`s |
| ✓ Never loads the full file into memory | Only one 8 KB chunk and the streams' small internal buffers are in memory at any time, whatever the file size. Sample run 2 copies 200 MB with a 16 MB heap |
| ✓ Produces a byte-for-byte copy | `write(buffer, 0, bytesRead)` writes exactly the bytes that were read. `cmp` confirms the copies are identical |

### 5.2 Program

```java
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

public class BinaryFileCopy {
    static final int CHUNK_SIZE = 8 * 1024;                 // fixed-size buffer: 8 KB per read

    public static void main(String[] args) {
        if (args.length != 2) {
            System.err.println("Usage: java BinaryFileCopy <source-file> <destination-file>");
            System.exit(1);
        }
        File source = new File(args[0]);
        File destination = new File(args[1]);

        if (isSameFile(source, destination)) {              // opening the output would empty the source
            System.err.println("Source and destination are the same file: " + source);
            System.exit(1);
        }
        System.exit(copy(source, destination));
    }

    // Returns the exit code: 0 = copied, 2 = source problem, 3 = write problem
    static int copy(File source, File destination) {
        long bytesCopied = 0;

        try (InputStream in = new BufferedInputStream(new FileInputStream(source))) {
            try (OutputStream out = new BufferedOutputStream(new FileOutputStream(destination))) {
                byte[] buffer = new byte[CHUNK_SIZE];
                int bytesRead;
                while ((bytesRead = in.read(buffer)) != -1) {    // read up to 8 KB
                    out.write(buffer, 0, bytesRead);           // write exactly the bytes that were read
                    bytesCopied += bytesRead;
                }
            } catch (FileNotFoundException e) {                // destination could not be created
                System.err.println("Write failed: cannot create " + e.getMessage());
                return 3;
            } catch (IOException e) {                          // failed part-way, e.g. disk full
                System.err.println("Copy failed after " + bytesCopied + " bytes: " + e.getMessage());
                destination.delete();                          // do not leave a half-written copy behind
                return 3;
            }
        } catch (FileNotFoundException e) {                    // source missing or not readable
            System.err.println("Source not found: " + e.getMessage());
            return 2;
        } catch (IOException e) {                              // closing the source failed
            System.err.println("Read failed: " + e.getMessage());
            return 2;
        }

        System.out.println("Copied " + bytesCopied + " bytes from " + source + " to " + destination);
        return 0;
    }

    static boolean isSameFile(File a, File b) {
        try {
            return a.getCanonicalFile().equals(b.getCanonicalFile());
        } catch (IOException e) {
            return false;                                      // let copy() report the real problem
        }
    }
}
```

**Key points of the copy logic**

- `in.read(buffer)` returns **how many bytes** it actually read (1 to 8,192), or −1 at the end of the file.
- `out.write(buffer, 0, bytesRead)` writes only those bytes. Calling plain `out.write(buffer)` would append leftover bytes from the previous chunk after the last, shorter chunk, so the copy would be wrong.
- The **nested** try-with-resources separates the two failures. A `FileNotFoundException` that reaches the **outer** `catch` can only come from opening the source. Anything the **inner** catches comes from the destination side or from the copy itself.
- If a copy fails part-way, the half-written destination is deleted. The inner try-with-resources has already closed it by the time the `catch` runs.
- `isSameFile()` guards against `java BinaryFileCopy a.jpg a.jpg`. Opening a `FileOutputStream` truncates the file, so without this check the source would be emptied before it was read.

### 5.3 Sample runs

**Run 1: copy a PDF and a JPEG, then verify them** (`photo.jpg` is the test image created by the Q3 demo)

```text
$ javac BinaryFileCopy.java
$ java BinaryFileCopy javacca2_questions.pdf questions_copy.pdf
Copied 113163 bytes from javacca2_questions.pdf to questions_copy.pdf
$ cmp javacca2_questions.pdf questions_copy.pdf && echo "byte-for-byte identical"
byte-for-byte identical
$ java BinaryFileCopy photo.jpg backup.jpg
Copied 25676 bytes from photo.jpg to backup.jpg
```

`cmp` prints nothing when the two files are identical. On Windows, use `fc /b file1 file2` instead.

**Run 2: a 200 MB file with only 16 MB of heap** (shows the whole file is never loaded into memory)

```text
$ dd if=/dev/urandom of=big.bin bs=1048576 count=200
$ java -Xmx16m BinaryFileCopy big.bin big_copy.bin
Copied 209715200 bytes from big.bin to big_copy.bin
$ cmp big.bin big_copy.bin && echo "byte-for-byte identical"
byte-for-byte identical
```

**Run 3: wrong number of arguments**

```text
$ java BinaryFileCopy photo.jpg
Usage: java BinaryFileCopy <source-file> <destination-file>
```

**Run 4: missing source** (exit status 2, and no destination file is created)

```text
$ java BinaryFileCopy missing.jpg copy.jpg
Source not found: missing.jpg (No such file or directory)
```

**Run 5: the destination cannot be created** (the folder does not exist; exit status 3)

```text
$ java BinaryFileCopy photo.jpg no_such_folder/photo.jpg
Write failed: cannot create no_such_folder/photo.jpg (No such file or directory)
```

**Run 6: writing fails part-way** (a full disk, simulated with a 1 MB file-size limit using `ulimit`; exit status 3)

```text
$ (ulimit -f 2048; java BinaryFileCopy big.bin limited_copy.bin)
Copy failed after 1048576 bytes: File too large
$ ls limited_copy.bin
ls: limited_copy.bin: No such file or directory
```

The partial copy was deleted after the failure.

**Run 7: source and destination are the same file**

```text
$ java BinaryFileCopy photo.jpg ./photo.jpg
Source and destination are the same file: photo.jpg
```

`photo.jpg` is left untouched at 25,676 bytes.

| Exit status | Meaning |
|---|---|
| 0 | Copied successfully |
| 1 | Usage error, or source and destination are the same file |
| 2 | The source is missing or cannot be read |
| 3 | The destination cannot be created, or writing failed part-way |

---

## Quick revision sheet

**Exceptions**

- `Throwable` → `Error` (the JVM has failed; do not catch) and `Exception`. `Exception` → `RuntimeException` (**unchecked**: usually a bug) and everything else (**checked**: catch it or declare it).
- **The compiler** enforces catch-or-declare for checked exceptions only. **At runtime**, every throwable propagates up the call stack until a matching `catch` handles it. **Recovery** belongs to the caller that can act (checked exceptions) or to the programmer who fixes the bug (unchecked exceptions).
- `throw new X("msg");` throws one object, inside a method. `throws X, Y` declares exceptions, in the method header.
- `catch` clauses are tested top to bottom and only the first match runs, so list subclasses before superclasses. `finally` always runs, unless the JVM exits.
- An uncaught exception ends the current method, pops its frame and re-appears at the caller's call site. If it passes `main()`, the program prints `Exception in thread "main"` and the stack trace, and exits with status 1.
- Try-with-resources: `try (R r = …) { }` closes `r` automatically, in reverse order of declaration, and keeps any `close()` failure as a *suppressed* exception.

**Streams**

| Data | Use | Example |
|---|---|---|
| Text (config, CSV, logs) | Character streams with an explicit charset | `Files.newBufferedReader(path, StandardCharsets.UTF_8)` |
| Binary (JPEG, PDF, ZIP) | Byte streams | `BufferedInputStream` + `BufferedOutputStream` + `byte[8192]` |
| Text from bytes (bridge) | `InputStreamReader` / `OutputStreamWriter` | `new InputStreamReader(new FileInputStream(f), StandardCharsets.UTF_8)` |

- Buffering means fewer OS calls (one per 8 KB block instead of one per byte). The data is unchanged. Close or `flush()` output streams so the last block is written.
- Copy loop: `while ((n = in.read(buf)) != -1) out.write(buf, 0, n);`
