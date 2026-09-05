# Computer Networks — Question Bank (by Unit)

Official question bank, segregated unit-wise. Numbering restarts inside each unit, matching the way the questions were handed out.

> Student-transcribed. Verify against the copy given in class before relying on it for an exam.

## Contents

- [Unit 1 — Introduction and Physical Layer](#unit-1--introduction-and-physical-layer-15-sessions)
- [Unit 2 — Data Link Layer](#unit-2--data-link-layer-15-sessions)

---

## Unit 1 — Introduction and Physical Layer (15 Sessions)

1. Explain the different types of computer networks with suitable examples.
2. Explain the different types of network topologies with suitable examples.
3. Give an overview of computer networks. Explain their basic components, advantages, and applications with suitable examples.
4. Explain the OSI (Open Systems Interconnection) reference model. Describe its seven layers and their functions with suitable examples.
5. Explain the TCP/IP model. Describe its four layers, their functions, and give suitable examples.
6. Compare the OSI and TCP/IP reference models.
7. Explain guided transmission media. Describe its types, advantages, disadvantages, and applications with suitable examples.
8. Explain unguided transmission media. Describe its types, advantages, disadvantages, and applications with suitable examples.
9. Differentiate between guided and unguided transmission media.

---

## Unit 2 — Data Link Layer (15 Sessions)

1. Define character stuffing in computer networks. Explain how it is used in character-oriented framing with a suitable example.
2. Define bit stuffing in computer networks. Explain how it is used in bit-oriented framing with a suitable example.
3. Describe Vertical Redundancy Check (VRC) and Longitudinal Redundancy Check (LRC) with examples.
4. The sender transmits the following byte code to the receiver. Using the **Vertical Redundancy Check (VRC)** method, demonstrate that an error has occurred in the received byte code.

   | Sr. No. | Sender side | Receiver side |
   | --- | --- | --- |
   | 1 | `1 0 1 1 1 0 1 0` | `1 0 1 1 1 0 1 1` |
   | 2 | `1 1 1 1 1 0 1 0` | `1 1 0 1 1 0 1 0` |
   | 3 | `1 1 0 0 1 0 1 0` | `1 1 1 0 1 0 1 1` |
   | 4 | `0 1 0 0 1 0 1 0` | `0 1 0 0 1 0 1 0` |

5. The sender transmits the following byte code to the receiver. Using the **Longitudinal Redundancy Check (LRC)** method, demonstrate that an error has occurred in the received byte code.

   | Sr. No. | Sender side | Receiver side |
   | --- | --- | --- |
   | 1 | `1 0 1 1`<br>`1 1 1 1`<br>`1 0 1 1`<br>`1 1 0 1` | `1 0 1 0`<br>`1 0 1 0`<br>`1 0 1 0`<br>`1 0 1 0` |
   | 2 | `1 1 0 0`<br>`0 1 0 1`<br>`1 1 0 0`<br>`0 1 0 1` | `1 0 1 0`<br>`0 1 0 1`<br>`1 0 1 0`<br>`0 1 1 1` |
   | 3 | `1 1 0 1`<br>`0 1 0 1`<br>`1 1 0 1`<br>`0 1 0 1` | `1 0 1 0`<br>`1 1 0 1`<br>`1 0 1 0`<br>`1 1 0 1` |

> Unit 2 is incomplete here — the source text ends at Q5. Add the remaining questions when you have them.
