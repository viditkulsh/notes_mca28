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

8. Explain Unguided transmission media. Describe its types, advantages, disadvantages, and applications with suitable examples.

9. Differentiate between guided and unguided transmission media.

10. Explain the concept of analog and digital communication with examples. Discuss their advantages and limitations.

11. Describe Shannon’s Capacity Theorem. How does it influence the design of modern communication systems?

12. Explain the process of encoding and modulation in digital communication. Illustrate with a neat diagram.

13. Discuss Time Division Multiplexing (TDM) and Frequency Division Multiplexing (FDM). Compare their applications in communication networks.

14. Explain switching techniques used in communication networks. Highlight their role in efficient resource utilization.

---

## Unit 2 — Data Link Layer (15 Sessions)

1. Define character stuffing in computer networks. Explain how it is used in characteroriented framing with a suitable example.

2. Define bit stuffing in computer networks. Explain how it is used in bitsoriented framing with a suitable example.

3. Describe Vertical Redundancy Check (VRC), Longitudinal Redundancy Check (LRC) with examples.

4. The sender transmits the following byte code to the receiver. Using the Vertical Redundancy Check (VRC) method, demonstrate that an error has occurred in the received byte code.

| Sr No | Sender side | Receiver side |
|---|---|---|
|1| 1   0   1   1   1   0   1    0 | 1   0   1   1   1   0   1    1 |
|2| 1   1   1   1   1   0   1    0 | 1   1   0   1   1   0   1    0 |
|3| 1   1   0   0   1   0   1    0 | 1   1   1   0   1   0   1    1 |
|4| 0   1   0   0   1   0   1    0 | 0   1   0   0   1   0   1    0 |

5. The sender transmits the following byte code to the receiver. Using the **Longitudinal Redundancy Check (LRC)** method, demonstrate that an error has occurred in the received byte code.

| Sr No | Sender side | Receiver side |
|---|---|---|
|1 | 1   0   1   1 <br> 1 0 1 0 <br> 1 1 1 1 <br> 1 0 1 0 | 1 0 1 1 <br> 1 0 1 0 <br> 1 1 0 1 <br> 1 0 1 0 |
|2 | 1   1   0   0 <br> 1 0 1 0 <br> 0 1 0 1 <br> 0 1 0 1 | 1 1 0 0 <br> 1 0 1 0 <br> 0 1 0 1 <br> 0 1 1 1 |
|3 | 1   1   0   1 <br> 1 0 1 0 <br> 0 1 0 1 <br> 1 1 0 1 | 1 1 0 1 <br> 1 0 1 0 <br> 0 1 0 1 <br> 1 1 0 1 |

6. Define Hamming Code. Explain its role in error detection and correction. Illustrate with a suitable example how singlebit errors can be detected and corrected using Hamming Code.

7. The given data bits are 1010010101. Construct the Hamming Codeword using even parity.

8. The received Hamming codeword is 01100101001011. Identify the position of the error using even parity checks and correct the codeword accordingly.

9. Explain the StopandWait protocol. Discuss its working principle and limitations in reliable data transmission.

10. Describe the Sliding Window protocol. How does it improve efficiency compared to StopandWait?

11. Explain the GoBackN ARQ technique. Illustrate its operation with an example and discuss its advantages.

12. Describe SelectiveReject ARQ. Compare it with GoBackN ARQ in terms of efficiency and complexity.

13. Explain the HDLC protocol. Discuss its frame structure and role in reliable communication.

14. Discuss channel allocation methods in computer networks. Explain fixed and dynamic allocation with examples.

15. Explain the ALOHA system. Derive its efficiency and discuss its applications in modern wireless networks.

16.Describe CSMA protocols. Compare persistent and nonpersistent CSMA in terms of performance.

 

 