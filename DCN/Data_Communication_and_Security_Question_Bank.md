# Data Communication and Security

## Question Bank

**Course units:** Unit 1 --- Introduction and Physical Layer; Unit 2 ---
Data Link Layer\
**Purpose:** Clean, consistently numbered study copy of the supplied
question bank.

> **Editorial notes** - The original repeats the label "Q16" in Unit 1.
> The CSMA question is numbered Q21 here so numbering remains unique. -
> Unit 2's original numbering restarts and then continues into an
> unnumbered practice set. These are organized as Q1--Q15 and Practice
> Problems P1--P12. - The CRC questions in the supplied source omit the
> generator polynomial. The polynomial must be obtained from the
> instructor or original question paper before a unique CRC answer can
> be calculated. - Some source tables have damaged spacing. The bit
> strings below preserve the visible values as closely as possible;
> verify them against the original paper before submitting numerical
> work.

------------------------------------------------------------------------

# Unit 1: Introduction and Physical Layer (15 Sessions)

### Q1. Types of computer networks

Explain the different types of computer networks with suitable examples.

### Q2. Network topologies

Explain the different types of network topologies with suitable
examples.

### Q3. Overview of computer networks

Give an overview of computer networks. Explain their basic components,
advantages, and applications with suitable examples.

### Q4. OSI reference model

Explain the OSI (Open Systems Interconnection) reference model. Describe
its seven layers and their functions with suitable examples.

### Q5. TCP/IP model

Explain the TCP/IP model. Describe its four layers, their functions, and
give suitable examples.

### Q6. OSI vs TCP/IP

Compare the OSI and TCP/IP reference models.

### Q7. Guided transmission media

Explain guided transmission media. Describe its types, advantages,
disadvantages, and applications with suitable examples.

### Q8. Unguided transmission media

Explain unguided transmission media. Describe its types, advantages,
disadvantages, and applications with suitable examples.

### Q9. Guided vs unguided media

Differentiate between guided and unguided transmission media.

### Q10. Analog and digital communication

Explain analog and digital communication with examples. Discuss their
advantages and limitations.

### Q11. Shannon's Capacity Theorem

Describe Shannon's Capacity Theorem. How does it influence the design of
modern communication systems?

### Q12. Encoding and modulation

Explain the process of encoding and modulation in digital communication.
Illustrate with a neat diagram.

### Q13. Multiplexing and TDM

Explain multiplexing in data communication. Detail the working principle
of Time Division Multiplexing (TDM), and differentiate between
Synchronous TDM and Asynchronous (Statistical) TDM with neat block
diagrams.

### Q14. Switching techniques

Explain switching techniques used in communication networks. Highlight
their role in efficient resource utilization.

### Q15. Transmission impairments and noise

What are the three different transmission impairments? Explain the
different types of noise.

### Q16. Bit stuffing and byte stuffing

Explain bit stuffing and byte stuffing with appropriate examples. Which
method is preferable in a given situation, and why?

### Q17. CSMA protocols

Describe CSMA protocols. Compare persistent and non-persistent CSMA in
terms of performance.

### Q18. Nyquist bit rate: maximum bit rate

What is the maximum bit rate of a noiseless channel with a bandwidth of
5000 Hz transmitting a signal with two signal levels?

### Q19. Nyquist bit rate: number of signal levels

A noiseless channel of bandwidth (B=5`\text{ kHz}`{=tex}) must support a
bit rate of (C=90`\text{ kbps}`{=tex}). What is the required number of
signal levels (L)?

### Q20. Nyquist bit rate: required bandwidth

A noiseless channel with a bit rate of 96 kbps and 4 signal levels is
given. Determine the required bandwidth.

### Q21. Shannon capacity calculation

A noisy channel has a bandwidth of 4 kHz and a signal-to-noise ratio of
30 dB. Calculate the maximum data rate using Shannon's capacity theorem.

### Q22. Line coding waveforms

Encode each bit stream using the specified line-coding scheme. Draw a
labelled waveform and state the voltage/transition convention used. 1.
`110110010` using Unipolar NRZ. 2. `101101010` using Polar NRZ-L. 3.
`101101010` using Polar NRZ-I (assume the initial level is Low). 4.
`1011011010` using Return-to-Zero (RZ). 5. `101110010` using Manchester
encoding. 6. `101101010` using Differential Manchester encoding (assume
the initial level is Low).

------------------------------------------------------------------------

# Unit 2: Data Link Layer (15 Sessions)

### Q1. Character stuffing

Define character stuffing in computer networks. Explain how it is used
in character-oriented framing with a suitable example.

### Q2. Bit stuffing

Define bit stuffing in computer networks. Explain how it is used in
bit-oriented framing with a suitable example.

### Q3. VRC and LRC

Describe Vertical Redundancy Check (VRC) and Longitudinal Redundancy
Check (LRC), with examples.

### Q4. VRC error detection table

The sender transmits the following byte codes to the receiver. Using
VRC, demonstrate whether an error has occurred in each received byte.
**Assume even parity unless the instructor specifies otherwise.**

    Row Sender byte   Received byte
  ----- ------------- ---------------
      1 `10111010`    `10111011`
      2 `11111010`    `11011010`
      3 `11001010`    `11101011`
      4 `01001010`    `01001010`

### Q5. LRC error detection tables

For each group below, compare the sender-side and receiver-side rows
using LRC. Recalculate the column parity at the receiver and identify
any mismatch. The source document's spacing is damaged, so verify the
exact grouping and parity convention before using this as a graded
numerical question.

**Group 1**

  Sender row   Receiver row
  ------------ --------------
  `1011`       `1011`
  `1010`       `1010`
  `1111`       `1101`
  `1010`       `1010`

**Group 2**

  Sender row   Receiver row
  ------------ --------------
  `1100`       `1100`
  `1010`       `1010`
  `0101`       `0101`
  `0101`       `0111`

**Group 3**

  Sender row   Receiver row
  ------------ --------------
  `1101`       `1101`
  `1010`       `1010`
  `0101`       `0101`
  `1101`       `1101`

### Q6. Hamming code: concept

Define Hamming Code. Explain its role in error detection and correction.
Illustrate with an example how a single-bit error is detected and
corrected.

### Q7. Hamming code construction

The data bits are `1010010101`. Construct the Hamming codeword using
even parity.

### Q8. Hamming code correction

The received Hamming codeword is `01100101001011`. Identify the error
position using even-parity checks and correct the codeword accordingly.
State the bit-position convention you use.

### Q9. Flow control and Stop-and-Wait ARQ

Explain flow control at the data link layer. Explain the working of the
Stop-and-Wait ARQ protocol.

### Q10. Sliding Window protocol

Describe the Sliding Window protocol. How does it improve efficiency
compared with Stop-and-Wait?

### Q11. Go-Back-N ARQ

Explain Go-Back-N ARQ. Illustrate its operation with an example and
discuss its advantages.

### Q12. Selective-Repeat ARQ

Describe Selective-Repeat (Selective-Reject) ARQ. Compare it with
Go-Back-N ARQ in terms of efficiency and complexity.

### Q13. HDLC

Explain the High-Level Data Link Control (HDLC) protocol. Explain
I-frames, S-frames, and U-frames, and the significance of each field in
the HDLC frame structure with a neat diagram.

### Q14. Channel allocation

Discuss channel allocation methods in computer networks. Explain fixed
and dynamic allocation with examples.

### Q15. MAC channel allocation and ALOHA

Discuss the channel-allocation problem in Medium Access Control (MAC).
Explain static versus dynamic channel allocation. Explain the working
principles, collision handling, and throughput performance of Pure ALOHA
and Slotted ALOHA.

------------------------------------------------------------------------

# Additional Numerical Practice Problems

### P1. Hamming code for four data bits

A sender transmits the 4-bit data `1011`. Construct the Hamming code,
show parity-bit placement, and write the final codeword.

### P2. 1's-complement checksum

A sender has the following four data words: `110010100`, `101001010`,
`111100100`, and `001101100`. Calculate the checksum using
1's-complement addition and write the transmitted data with checksum.
**Note:** these strings contain 9 bits, despite the source describing
them as 8-bit words. Confirm the intended word size.

### P3. Hamming code repeated exercise

A sender transmits the 4-bit data `1011`. Construct the Hamming code,
show parity-bit placement, and write the final codeword.

### P4. Correct a 7-bit Hamming code

A 7-bit Hamming codeword `1011011` is received. Detect and correct the
error, if any, using the Hamming method. Show all steps.

### P5. CRC encoding

Encode the dataword `10010110` using CRC with the specified generator
polynomial. Perform the division and determine the transmitted codeword.
**The generator polynomial is missing from the supplied source.**

### P6. CRC verification

The receiver receives `10010110101`. Using the same generator polynomial
as P5, check whether the data should be accepted or rejected. **The
generator polynomial is missing from the supplied source.**

### P7. Checksum at sender and receiver

A sender transmits the message `11001100`. Compute the checksum at the
sender and verify it at the receiver. Show all steps. State the word
segmentation and word size used.

### P8. VRC for a message

A message `10101010` is transmitted using VRC. Show how an error can be
detected at the receiver. State whether even or odd parity is used.

### P9. LRC for a message

Encode the message `10101010` using LRC. Construct the matrix and show
how errors are detected. State how the message is divided into rows and
columns.

### P10. VRC versus LRC

Compare the effectiveness of VRC and LRC in detecting single-bit and
burst errors.

### P11. Hamming code and correction

A sender transmits the data `11100011`. Construct the Hamming code and
demonstrate how a single-bit error is corrected at the receiver. State
the parity convention and bit-position convention.

------------------------------------------------------------------------

## Source-quality checklist

Before treating this as the final examination version, confirm: - the
missing CRC generator polynomial in P5 and P6; - whether P2 contains
8-bit or 9-bit words; - parity convention for VRC/LRC/Hamming
exercises; - the precise intended layout of the damaged LRC tables; -
the instructor's NRZ-L, NRZ-I, RZ, Manchester, and Differential
Manchester voltage conventions.
