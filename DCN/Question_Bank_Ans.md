# Computer Networks — Answers to Question Bank

Structured, exam-oriented answers to every question in [Question_Bank.md](Question_Bank.md). Numbering matches the question bank exactly and restarts inside each unit, so Unit 2 question 7 here answers Unit 2 question 7 there.

Unit 1 Q1–Q9 and Unit 2 Q1–Q3 are carried over from the earlier `DCN Question Bank Answers.pdf`, which this file replaces, with text-extraction slips and a few technical errors fixed. The remaining answers follow the same shape: **Definition → Explanation / Diagram → Key points or comparison table → Advantages & limitations → One-line summary**.

> Student-written notes. Cross-check terminology against your class notes and the lecture slides in [Slides/](Slides/) before an exam.

## Contents

- [Unit 1 — Introduction and Physical Layer](#unit-1--introduction-and-physical-layer)
  - [Q1. Types of computer networks](#q1-types-of-computer-networks)
  - [Q2. Network topologies](#q2-network-topologies)
  - [Q3. Overview of computer networks — components, advantages, applications](#q3-overview-of-computer-networks--components-advantages-applications)
  - [Q4. OSI reference model](#q4-osi-reference-model)
  - [Q5. TCP/IP model](#q5-tcpip-model)
  - [Q6. OSI vs TCP/IP](#q6-osi-vs-tcpip)
  - [Q7. Guided transmission media](#q7-guided-transmission-media)
  - [Q8. Unguided transmission media](#q8-unguided-transmission-media)
  - [Q9. Guided vs unguided media](#q9-guided-vs-unguided-media)
  - [Q10. Analog and digital communication](#q10-analog-and-digital-communication)
  - [Q11. Shannon's capacity theorem](#q11-shannons-capacity-theorem)
  - [Q12. Encoding and modulation](#q12-encoding-and-modulation)
  - [Q13. TDM and FDM](#q13-tdm-and-fdm)
  - [Q14. Switching techniques](#q14-switching-techniques)
- [Unit 2 — Data Link Layer](#unit-2--data-link-layer)
  - [Q1. Character stuffing in character-oriented framing](#q1-character-stuffing-in-character-oriented-framing)
  - [Q2. Bit stuffing in bit-oriented framing](#q2-bit-stuffing-in-bit-oriented-framing)
  - [Q3. VRC and LRC](#q3-vrc-and-lrc)
  - [Q4. VRC numerical — checking the received bytes](#q4-vrc-numerical--checking-the-received-bytes)
  - [Q5. LRC numerical — checking the received blocks](#q5-lrc-numerical--checking-the-received-blocks)
  - [Q6. Hamming code — single-bit error detection and correction](#q6-hamming-code--single-bit-error-detection-and-correction)
  - [Q7. Constructing the Hamming codeword for 1010010101](#q7-constructing-the-hamming-codeword-for-1010010101)
  - [Q8. Locating and correcting the error in 01100101001011](#q8-locating-and-correcting-the-error-in-01100101001011)
  - [Q9. Stop-and-Wait protocol](#q9-stop-and-wait-protocol)
  - [Q10. Sliding Window protocol](#q10-sliding-window-protocol)
  - [Q11. Go-Back-N ARQ](#q11-go-back-n-arq)
  - [Q12. Selective-Reject ARQ vs Go-Back-N ARQ](#q12-selective-reject-arq-vs-go-back-n-arq)
  - [Q13. HDLC protocol](#q13-hdlc-protocol)
  - [Q14. Channel allocation methods — static and dynamic](#q14-channel-allocation-methods--static-and-dynamic)
  - [Q15. ALOHA — efficiency and applications](#q15-aloha--efficiency-and-applications)
  - [Q16. CSMA protocols — persistent vs non-persistent](#q16-csma-protocols--persistent-vs-non-persistent)

---

## Unit 1 — Introduction and Physical Layer

### Q1. Types of computer networks

A **computer network** is a collection of interconnected computers and devices that communicate with each other to share data, resources, and services.

Computer networks can be classified mainly according to their **geographical coverage, size, and purpose**.

**1. PAN (Personal Area Network)**

A **Personal Area Network (PAN)** is a small network used to connect devices around a single person.

**Range:** Usually a few meters.

**Examples:**

- Smartphone connected to wireless earbuds through Bluetooth.
- Laptop connected to a wireless mouse.
- Smartphone sharing Internet with a laptop through hotspot.

**Advantages:**

- Easy to set up.
- Low cost.
- Requires little infrastructure.

**Applications:**

- Connecting personal devices.
- File transfer between nearby devices.
- Bluetooth peripherals.

**2. LAN (Local Area Network)**

A **Local Area Network (LAN)** connects computers and devices within a limited geographical area such as a room, home, office, school, or laboratory.

**Examples:**

- Computers connected in a college computer laboratory.
- Devices connected to a Wi-Fi router in a home.

**Characteristics:**

- High data transmission speed.
- Covers a relatively small area.
- Usually owned and managed by a single organization or person.

**Applications:**

- Sharing printers and files.
- Internet access.
- Communication between employees.
- Sharing centralized servers.

**3. MAN (Metropolitan Area Network)**

A **Metropolitan Area Network (MAN)** covers a larger area than a LAN, generally extending across a city or metropolitan region.

**Example:** A network connecting different branches of a bank located throughout a city.

**Characteristics:**

- Larger coverage than LAN.
- Usually connects multiple LANs.
- Can be operated by organizations, telecom providers, or governments.

**Applications:**

- Connecting offices within a city.
- Cable television networks.
- City-wide Internet infrastructure.

**4. WAN (Wide Area Network)**

A **Wide Area Network (WAN)** covers a very large geographical area such as a country, continent, or the entire world.

The **Internet** is the largest example of a WAN.

**Examples:**

- A multinational company connecting offices in India, Germany, and the USA.
- Banking networks connecting branches across countries.

**Characteristics:**

- Covers very large geographical areas.
- Uses leased lines, fiber-optic links, satellites, microwave links, etc.
- Generally has higher latency than LAN.

**Applications:**

- International business communication.
- Internet services.
- Online banking.
- Cloud computing.

**Comparison**

| Network | Full Form | Coverage | Example |
|---|---|---|---|
| PAN | Personal Area Network | Few meters | Bluetooth devices |
| LAN | Local Area Network | Building/campus | College lab |
| MAN | Metropolitan Area Network | City | City-wide network |
| WAN | Wide Area Network | Country/world | Internet |

**Summary:** Networks are classified by coverage — PAN (a few meters around one person), LAN (a room, building or campus), MAN (a city) and WAN (a country or the whole world, e.g. the Internet).

---

### Q2. Network topologies

**Network topology** refers to the physical or logical arrangement of computers, network devices, and communication links in a network.

The major types are:

**1. Bus Topology**

In a **bus topology**, all devices are connected to a single main communication cable called the **backbone**.

```
Computer A ─┐
Computer B ─┼──────── Backbone ────────┬─ Computer C
Computer D ─┘                          └─ Computer E
```

**Advantages:**

- Simple to install.
- Requires less cable.
- Relatively inexpensive.

**Disadvantages:**

- Failure of backbone can affect the entire network.
- Difficult to troubleshoot.
- Performance decreases as more devices are added.
- Limited cable length.

**Example:** Older Ethernet networks.

**2. Star Topology**

In a **star topology**, every device is connected to a central device such as a switch or hub.

```
             Computer A
                 |
                 |
Computer B ─── Switch ─── Computer C
                 |
                 |
             Computer D
```

**Advantages:**

- Easy to install and manage.
- Failure of one cable affects only one device.
- Easy to add or remove devices.
- Easy troubleshooting.

**Disadvantages:**

- Failure of central switch can affect the entire network.
- Requires more cable than bus topology.
- Central device increases cost.

**Example:** Modern Ethernet LANs.

**3. Ring Topology**

In a **ring topology**, each device is connected to two other devices, forming a closed loop.

```
Computer A ─── Computer B
     |              |
     |              |
Computer D ─── Computer C
```

**Advantages:**

- Data transmission can be organized systematically.
- No central device is required.

**Disadvantages:**

- Failure of one device/link may disrupt communication.
- Adding or removing devices can be difficult.
- Troubleshooting is comparatively difficult.

**Example:** Token Ring networks.

**4. Mesh Topology**

In a **mesh topology**, devices are connected to multiple or all other devices.

```
A ───── B
|\     /|
| \   / |
|  \ /  |
|  / \  |
| /   \ |
C ───── D
```

There are two forms:

- **Full Mesh:** Every device connects directly to every other device.
- **Partial Mesh:** Only selected devices have multiple connections.

**Advantages:**

- Highly reliable.
- Multiple paths are available.
- Failure of one link does not necessarily stop communication.

**Disadvantages:**

- Expensive.
- Requires large amounts of cabling.
- Complex installation and maintenance.

**Example:** Internet backbone networks.

**5. Tree Topology**

A **tree topology** combines characteristics of star and bus topologies. Devices are organized hierarchically.

```
                Core
              /      \
         Switch      Switch
         /    \      /    \
        A      B    C      D
```

**Advantages:**

- Scalable.
- Easy to manage hierarchically.
- Suitable for large networks.

**Disadvantages:**

- Failure of a higher-level device can affect connected segments.
- More complex than star topology.

**Example:** Large organizational networks.

**6. Hybrid Topology**

A **hybrid topology** combines two or more different topologies.

For example, an organization may use star topology within individual departments and connect departments using a mesh or tree structure.

**Advantages:**

- Flexible.
- Scalable.
- Can be designed according to organizational requirements.

**Disadvantages:**

- Expensive.
- Complex design and maintenance.

**Summary:** Topology is the layout of devices and links — bus (one backbone), star (central switch), ring (closed loop), mesh (multiple/all links), tree (hierarchy of stars) and hybrid (a mix) — each trading cost and cabling against reliability and ease of management.

---

### Q3. Overview of computer networks — components, advantages, applications

A **computer network** is a system in which two or more computers or devices are interconnected to communicate and exchange information.

Networks allow devices to **share data, hardware, software, Internet connectivity, and other resources**.

**Basic Components of a Computer Network**

**1. Sender and Receiver**

The **sender** generates and transmits data, while the **receiver** receives the data.

Example: A computer sending a file to another computer.

**2. Transmission Medium**

The transmission medium carries data from one device to another.

Examples:

- Ethernet cable
- Fiber-optic cable
- Radio waves
- Microwave

**3. Network Interface Card**

A **Network Interface Card (NIC)** allows a computer or device to connect to a network.

Modern computers commonly have Ethernet and/or Wi-Fi network interfaces.

**4. Switch**

A **switch** connects multiple devices in a LAN and forwards data to the appropriate destination.

**5. Router**

A **router** connects different networks and determines appropriate paths for forwarding packets.

For example, a home router connects the home LAN to the Internet.

**6. Protocols**

Protocols are rules that define how devices communicate.

Examples:

- TCP
- IP
- HTTP
- DNS
- Ethernet

**Advantages of Computer Networks**

1. **Resource sharing:** Printers, storage, and Internet connections can be shared.
2. **File sharing:** Users can exchange files easily.
3. **Communication:** Email, messaging, and video conferencing are possible.
4. **Centralized management:** Data and applications can be managed centrally.
5. **Cost reduction:** Shared resources reduce infrastructure costs.
6. **Remote access:** Users can access systems from different locations.
7. **Scalability:** Additional devices can be connected when required.

**Applications**

Computer networks are used in:

- Banking
- Education
- Healthcare
- E-commerce
- Cloud computing
- Social media
- Online gaming
- Government services
- Industrial automation
- Remote work

**Example:** In a university, computers in laboratories can connect to a central server, share printers, access the Internet, and access common educational resources.

**Summary:** A computer network interconnects devices through sender/receiver, transmission media, NICs, switches, routers and protocols, so that data, hardware and Internet access can be shared — which is why networks underpin banking, education, healthcare, e-commerce and cloud services.

---

### Q4. OSI reference model

The **OSI (Open Systems Interconnection) model** is a conceptual reference model developed by the **International Organization for Standardization (ISO)**.

It divides network communication into **seven layers**, with each layer performing specific functions.

```
+---------------------------+
| 7. Application            |
+---------------------------+
| 6. Presentation           |
+---------------------------+
| 5. Session                |
+---------------------------+
| 4. Transport              |
+---------------------------+
| 3. Network                |
+---------------------------+
| 2. Data Link              |
+---------------------------+
| 1. Physical               |
+---------------------------+
```

**1. Physical Layer**

The Physical Layer is responsible for transmitting **raw bits** over the communication medium.

**Functions:**

- Bit transmission.
- Electrical/optical/radio signaling.
- Defines cables, connectors, frequencies, and transmission characteristics.

**Examples:**

- Ethernet cables.
- Fiber-optic cables.
- Radio signals.
- Network connectors.

**2. Data Link Layer**

The Data Link Layer provides **node-to-node delivery** and organizes bits into frames.

**Functions:**

- Framing.
- MAC addressing.
- Error detection.
- Flow control.
- Medium access control.

**Examples:**

- Ethernet.
- Wi-Fi MAC.
- Switches.

**3. Network Layer**

The Network Layer is responsible for **logical addressing and routing**.

**Functions:**

- IP addressing.
- Routing.
- Packet forwarding.
- Path determination.

**Example:** IP protocol.

Routers primarily operate at this layer.

**4. Transport Layer**

The Transport Layer provides **end-to-end communication** between applications.

**Functions:**

- Segmentation.
- Flow control.
- Error recovery.
- Reliable delivery.
- Port addressing.

**Examples:**

- TCP
- UDP

**5. Session Layer**

The Session Layer establishes, manages, and terminates communication sessions between applications.

**Functions:**

- Session establishment.
- Session management.
- Synchronization.
- Session termination.

**Example:** Maintaining a logical communication session between applications.

**6. Presentation Layer**

The Presentation Layer deals with the **format and representation of data**.

**Functions:**

- Data translation.
- Encryption/decryption.
- Compression/decompression.
- Character encoding.

**Examples:**

- JPEG
- ASCII
- UTF-8
- Encryption formats

**7. Application Layer**

The Application Layer provides network services directly to user applications.

**Functions:**

- Web communication.
- Email.
- File transfer.
- Name resolution.

**Examples:**

- HTTP/HTTPS
- FTP
- SMTP
- DNS

**Data Flow**

At the sender:

**Application → Presentation → Session → Transport → Network → Data Link → Physical**

At the receiver, the reverse process occurs.

**Summary:** The ISO OSI model splits communication into seven layers — Physical, Data Link, Network, Transport, Session, Presentation, Application — each with its own functions; data passes down the layers at the sender and back up at the receiver.

---

### Q5. TCP/IP model

The **TCP/IP model** is the networking model used as the foundation of the Internet.

It consists of **four layers**:

```
+-----------------------------+
| Application                 |
+-----------------------------+
| Transport                   |
+-----------------------------+
| Internet                    |
+-----------------------------+
| Network Access / Link       |
+-----------------------------+
```

**1. Application Layer**

The Application Layer provides network services to user applications.

It combines the functions of the OSI **Application, Presentation, and Session layers**.

**Functions:**

- Web communication.
- Email.
- File transfer.
- Domain-name resolution.
- Remote access.

**Protocols:**

- HTTP/HTTPS
- DNS
- FTP
- SMTP
- SSH

**2. Transport Layer**

This layer provides communication between applications running on different hosts.

**Functions:**

- Segmentation.
- Port addressing.
- Flow control.
- Error control.
- Reliable or unreliable delivery.

**Protocols:**

- TCP
- UDP

**TCP** provides reliable, connection-oriented communication.

**UDP** provides faster, connectionless communication without TCP's reliability mechanisms.

**3. Internet Layer**

The Internet Layer handles logical addressing and routing of packets.

**Functions:**

- IP addressing.
- Routing.
- Packet forwarding.
- Internetworking.

**Protocols:**

- IPv4
- IPv6
- ICMP

Routers primarily operate at this layer.

**4. Network Access / Link Layer**

This layer handles communication over the physical network.

**Functions:**

- Framing.
- MAC addressing.
- Physical transmission.
- Access to the transmission medium.

**Examples:**

- Ethernet
- Wi-Fi
- Fiber networks

**Example**

When a user opens a website:

1. Application Layer uses HTTPS.
2. Transport Layer uses TCP.
3. Internet Layer adds IP addressing.
4. Link Layer places the packet into an Ethernet/Wi-Fi frame.
5. Data is transmitted over the physical medium.

**Summary:** TCP/IP is the Internet's four-layer model — Application (HTTP, DNS, SMTP), Transport (TCP, UDP), Internet (IPv4/IPv6, ICMP) and Network Access/Link (Ethernet, Wi-Fi).

---

### Q6. OSI vs TCP/IP

| Feature | OSI Model | TCP/IP Model |
|---|---|---|
| Full form | Open Systems Interconnection | Transmission Control Protocol/Internet Protocol |
| Number of layers | 7 | 4 |
| Developed by | ISO | DARPA/DoD research ecosystem |
| Nature | Reference/conceptual model | Practical protocol suite and model |
| Application layers | Application, Presentation, Session | Application |
| Transport | Transport | Transport |
| Network | Network | Internet |
| Data Link + Physical | Separate | Combined into Link/Network Access |
| Protocol dependency | Protocol-independent | Built around TCP/IP protocols |
| Practical use | Mainly educational/reference | Widely used in real networks |
| Development approach | Model first, protocols later | Protocols and architecture evolved together |

**Layer Mapping**

```
OSI                              TCP/IP

Application  ─┐
Presentation  ├───────────────── Application
Session      ─┘

Transport ────────────────────── Transport
Network ──────────────────────── Internet

Data Link ───┐
Physical  ───┴────────────────── Network Access
```

**Conclusion**

The OSI model provides a more detailed conceptual separation of networking functions, while TCP/IP is the practical architecture underlying modern Internet communication.

**Summary:** OSI is ISO's seven-layer, protocol-independent reference model; TCP/IP is the four-layer practical model of the Internet that merges OSI's top three layers into Application and its bottom two into Network Access.

---

### Q7. Guided transmission media

**Guided transmission media** are communication media in which signals travel through a **physical path or cable** from sender to receiver.

The major types are:

1. Twisted Pair Cable
2. Coaxial Cable
3. Fiber-Optic Cable

**1. Twisted Pair Cable**

It consists of two insulated copper wires twisted together to reduce electromagnetic interference.

Types:

- **UTP:** Unshielded Twisted Pair
- **STP:** Shielded Twisted Pair

**Advantages:**

- Low cost.
- Easy installation.
- Flexible.
- Widely available.

**Disadvantages:**

- Limited distance.
- Susceptible to interference, especially UTP.
- Lower bandwidth than fiber.

**Applications:**

- Telephone networks.
- Ethernet LANs.
- Office networks.

**2. Coaxial Cable**

A coaxial cable consists of:

- Central conductor.
- Insulating layer.
- Metallic shield.
- Outer protective covering.

```
+-------------------------+
| Protective outer layer  |
| +---------------------+ |
| | Metallic shield     | |
| | +-----------------+ | |
| | | Insulator       | | |
| | | +-------------+ | | |
| | | | Conductor   | | | |
| | | +-------------+ | | |
| | +-----------------+ | |
| +---------------------+ |
+-------------------------+
```

**Advantages:**

- Better shielding than twisted pair.
- Higher bandwidth than basic twisted pair.
- More resistant to interference.

**Disadvantages:**

- More expensive than twisted pair.
- Less flexible.
- Installation is more difficult.

**Applications:**

- Cable television.
- Broadband networks.
- CCTV systems.

**3. Fiber-Optic Cable**

Fiber-optic cable transmits information using **light signals** through thin strands of glass or plastic.

Types:

- Single-mode fiber.
- Multimode fiber.

**Advantages:**

- Very high bandwidth.
- Long-distance transmission.
- Low signal loss.
- Immune to electromagnetic interference.
- More secure against electromagnetic interception.

**Disadvantages:**

- Higher installation cost.
- Fragile compared with copper.
- Requires specialized equipment and expertise.

**Applications:**

- Internet backbone.
- Long-distance telecommunications.
- Data centers.
- Submarine communication cables.

**Summary:** Guided media carry signals along a physical cable — twisted pair (cheap, short-range LANs and telephones), coaxial (better shielded, cable TV and broadband) and fiber-optic (light signals, very high bandwidth, long-distance backbones).

---

### Q8. Unguided transmission media

**Unguided transmission media**, also called **wireless transmission media**, transmit signals through air or space without requiring a physical cable.

Major types include:

1. Radio waves
2. Microwaves
3. Infrared
4. Satellite communication

**1. Radio Waves**

Radio waves can travel through air and can cover relatively large areas.

**Advantages:**

- No physical cable required.
- Can cover large areas.
- Suitable for mobile communication.

**Disadvantages:**

- Interference.
- Security concerns.
- Signal quality may vary.

**Applications:**

- Radio broadcasting.
- Wi-Fi.
- Mobile communication.
- IoT devices.

**2. Microwaves**

Microwaves use high-frequency electromagnetic waves for communication. Terrestrial microwave communication generally requires **line of sight**.

**Advantages:**

- High bandwidth.
- Suitable for long-distance communication.
- No physical cable required.

**Disadvantages:**

- Requires line of sight.
- Buildings and terrain can obstruct signals.
- Weather can affect some microwave links.

**Applications:**

- Cellular networks.
- Point-to-point communication.
- Television transmission.

**3. Infrared**

Infrared communication uses infrared light for short-range communication.

**Advantages:**

- Low interference between rooms.
- Relatively secure over short distances.
- Inexpensive.

**Disadvantages:**

- Short range.
- Cannot normally pass through walls.
- Requires suitable alignment in many applications.

**Applications:**

- Remote controls.
- Short-range device communication.
- Sensors.

**4. Satellite Communication**

Satellite communication uses satellites as communication relays between ground stations.

```
Ground Station A
       ↑
       |
  [Satellite]
       |
       ↓
Ground Station B
```

**Advantages:**

- Very large coverage area.
- Useful for remote regions.
- Suitable for broadcasting.

**Disadvantages:**

- High cost.
- Higher propagation delay.
- Weather and atmospheric conditions can affect certain frequency bands.

**Applications:**

- Satellite TV.
- GPS/GNSS services.
- Weather monitoring.
- Remote communication.
- Global telecommunications.

**Summary:** Unguided (wireless) media send electromagnetic waves through air or space — radio waves (wide-area, mobile, Wi-Fi), microwaves (line-of-sight, high bandwidth), infrared (short range, remotes) and satellites (very wide coverage, higher delay).

---

### Q9. Guided vs unguided media

| Feature | Guided Media | Unguided Media |
|---|---|---|
| Meaning | Uses physical path | Uses air/space |
| Transmission | Through cables | Through electromagnetic waves |
| Examples | Twisted pair, coaxial, fiber | Radio, microwave, infrared |
| Mobility | Limited | High |
| Installation | Requires physical cabling | Usually no physical cable |
| Interference | Generally lower, especially fiber | More susceptible |
| Security | Generally easier to physically control | Wireless signals can be intercepted |
| Bandwidth | Fiber provides extremely high bandwidth | Depends on frequency and technology |
| Coverage | Cable-dependent | Can cover large areas |
| Cost | Cabling can be expensive | Deployment may be cheaper for some applications |
| Example | Ethernet cable | Wi-Fi |

**Conclusion**

Guided media are suitable where a stable physical connection and high reliability are required, while unguided media are useful when **mobility, flexibility, and wide-area wireless connectivity** are important.

**Summary:** Guided media confine the signal to a cable (more secure, less interference, limited mobility); unguided media radiate it through air or space (mobility and wide coverage, but more interference and easier interception).

---

### Q10. Analog and digital communication

**Data and signals**

- **Data** is the information to be communicated — text, numbers, voice, images or video.
- A **signal** is the electrical, optical or electromagnetic form of the data that actually travels over the transmission medium. To be transferred, data must first be converted into a signal.
- Both data and signals can be **analog** or **digital**.

**Analog and digital data**

- **Analog data** is continuous — it changes smoothly and can take any value. Example: an analog clock, whose hour, minute and second hands move continuously; the human voice.
- **Digital data** has discrete states. Example: a digital clock that jumps suddenly from 8:05 to 8:06; text and numbers stored in a computer as 0s and 1s.

**Analog and digital signals**

- An **analog signal** is continuous and can have an **infinite number of values** in a range (e.g., a sine wave). It is described by its amplitude (volts), frequency (Hz) and phase.
- A **digital signal** can have only a **limited number of values** (levels), e.g., +5 V for 1 and 0 V for 0. With L levels, each level carries log2(L) bits — a 4-level signal carries 2 bits per level. It is described by its bit rate (bps), where bit rate = 1 ÷ bit interval.

**Diagram**

```
 Analog signal - continuous, any value in a range
  value
    |     .-'''-.                   .-'''-.
    |   .'       '.               .'       '.
    |--'-----------'.-----------.'-----------'.-----------.---> time
    |                '.       .'               '.       .'
    |                  '-...-'                   '-...-'

 Digital signal - discrete, only a limited set of values (here +5 V and 0 V)
   value
  +5 V   |         _______         _______________
         |        |       |       |               |
   0 V   |________|       |_______|               |_______  ---> time
              0       1       0       1       1       0
```

**Analog communication and digital communication**

- **Analog communication** — the information is carried by an analog signal whose amplitude, frequency or phase varies continuously with the message (AM, FM, PM). Examples: AM/FM radio, analog TV broadcasting, the traditional landline telephone.
- **Digital communication** — the information is carried as discrete symbols (bits), sent either as a digital signal (line coding, e.g., Manchester on Ethernet) or by keying a carrier (ASK, FSK, PSK, QAM). Examples: the Internet and Ethernet LANs, Wi-Fi, 4G/5G mobile, digital TV, VoIP calls. The four data-to-signal conversion methods are covered in Q12.

**Converting analog data to digital (A/D)**

```
 analog   +----------+  discrete-time  +------------------+  digital
 signal ->| Sampling |---------------->| Quantization and |-> signal
          +----------+     signal      | coding into bits |   (PCM)
                                       +------------------+
```

- **Sampling** — the signal is measured at regular time intervals (at least twice its highest frequency).
- **Quantization** — each sample is rounded to one of a finite number of levels, and each level is coded as bits.
- Example: telephone voice (up to 4 kHz) is sampled 8,000 times per second with 8 bits per sample, giving 8,000 × 8 = 64 kbps (PCM).

**Comparison**

| Basis | Analog communication | Digital communication |
|---|---|---|
| Signal | Continuous; infinite values in a range | Discrete; limited set of levels (e.g., 0 and 1) |
| Typical waveform | Sine wave | Square pulses |
| Effect of noise | Noise adds to the signal and cannot be separated from it | Small noise does not change the detected bit; errors can be detected and corrected |
| Long distance | Amplifiers boost the noise along with the signal, so noise accumulates | Regenerative repeaters recreate clean pulses |
| Bandwidth | Less — a voice channel needs about 4 kHz | More — 64 kbps PCM voice needs at least 32 kHz with two-level signaling (Nyquist) |
| Security | Difficult to encrypt | Easily encrypted |
| Multiplexing | FDM | TDM (and FDM) |
| Hardware | Analog circuits that drift with temperature and age | Cheap, programmable ICs and processors |
| Storage and copying | Quality degrades with every copy | Exact copies; easy storage and processing |
| Conversion error | None (no quantization) | Quantization error (reduced by using more bits) |
| Examples | AM/FM radio, analog TV, landline telephone | Internet, Ethernet, Wi-Fi, 4G/5G, digital TV |

**Advantages of analog communication**

- Natural representation of real-world signals such as voice; no A/D conversion and no quantization error.
- Needs less bandwidth for the same message.
- Simple, cheap transmitters and receivers for basic uses (AM/FM radio).
- Degrades gracefully — a weak signal is noisy but still usable.

**Limitations of analog communication**

- Noise and distortion accumulate with distance and cannot be removed.
- No error detection or correction; difficult to encrypt.
- Hard to store, process and multiplex many signals; components drift.

**Advantages of digital communication**

- High noise immunity — regenerative repeaters allow long distances without loss of quality.
- Error detection and correction (parity, CRC, Hamming code).
- Security through encryption.
- Easy multiplexing (TDM) and integration of voice, video and data on one network; compression.
- Cheap, reliable VLSI hardware; easy storage, processing and exact copying.

**Limitations of digital communication**

- Needs more bandwidth than the analog original.
- Sender and receiver clocks must be synchronized.
- A/D conversion adds quantization error and some delay.
- More complex systems; when the signal falls below a threshold, quality collapses suddenly (cliff effect) instead of degrading gradually.

**Summary:** Analog communication carries information as continuous signals (AM/FM radio, landline telephone) — simple and bandwidth-efficient, but noise accumulates; digital communication carries discrete bits (Internet, Wi-Fi, 4G/5G, digital TV) — it needs more bandwidth and synchronization but gives noise immunity, regeneration, error control, encryption and easy multiplexing, which is why modern networks are digital.

---

### Q11. Shannon's capacity theorem

**Definition**

**Shannon's capacity theorem** (Claude Shannon, 1948) gives the **theoretical maximum bit rate — the channel capacity — of a noisy channel**, i.e., the highest rate at which data can be sent with an arbitrarily small error rate:

**C = B × log2(1 + SNR)**

- **C** — capacity of the channel in bits per second (bps)
- **B** — bandwidth of the channel in hertz (Hz)
- **SNR** — signal-to-noise ratio = average signal power ÷ average noise power (a plain ratio, not dB)

**SNR in decibels**

- SNR(dB) = 10 × log10(SNR), and back: SNR = 10^(SNR(dB) ÷ 10).
- Examples: SNR = 1000 → 30 dB; SNR = 3162 → 35 dB; 36 dB → SNR = 10^3.6 ≈ 3981.
- Always convert dB back to the plain ratio before using the formula.

**Key points**

- It is an **upper limit**: no modulation or coding scheme can send error-free data faster than C; real systems operate below it.
- Unlike the Nyquist formula, it does **not** depend on the number of signal levels — the noise decides how many levels can be told apart.
- C grows **linearly with bandwidth** but only **logarithmically with SNR** (signal power).
- Extreme cases: SNR = 0 (only noise) → C = 0; SNR = 1 (0 dB) → C = B.

**Worked examples**

1. **Class example** — B = 3000 Hz, SNR = 300:
   - C = 3000 × log2(301) = 3000 × 8.234 ≈ 24,701 bps ≈ **24.7 kbps**.
   - The slide rounds log2(301) to 8.23 and gets 24,690 bps.
2. **Telephone line** — B = 3000 Hz (300–3300 Hz), SNR = 3162 (35 dB):
   - C = 3000 × log2(3163) = 3000 × 11.627 ≈ 34,881 bps ≈ **34.9 kbps**.
   - Dial-up (V.34) modems reached 33.6 kbps — just under this limit.
3. **Shannon and Nyquist together** — B = 1 MHz, SNR = 63:
   - Shannon: C = 10^6 × log2(64) = **6 Mbps** (the upper limit).
   - Choose a safer rate below the limit, e.g., 4 Mbps.
   - Nyquist: 4 Mbps = 2 × 1 MHz × log2(L) → log2(L) = 2 → **L = 4 signal levels**.

**Nyquist bit rate (noiseless channel) — for contrast**

- BitRate = 2 × B × log2(L), where L = number of signal levels.
- Class example: B = 5000 Hz, L = 2 → 2 × 5000 × log2(2) = **10,000 bps**.
- B = 3000 Hz: L = 2 → 6,000 bps; L = 4 → 12,000 bps — without noise, more levels would always mean more bits per second.

| Basis | Nyquist bit rate | Shannon capacity |
|---|---|---|
| Channel | Noiseless (ideal) | Noisy (real) |
| Formula | 2 × B × log2(L) | B × log2(1 + SNR) |
| Depends on | Bandwidth and number of levels | Bandwidth and SNR |
| Result | Bit rate for a chosen number of levels | Absolute upper limit for any scheme |
| Use in design | Choose the number of levels for a target rate | Check that the target rate is achievable |

**How it influences the design of modern communication systems**

1. **Benchmark** — engineers compare a system's spectral efficiency (bits per second per hertz) with log2(1 + SNR) to see how much improvement is still possible; no design can beat the limit.
2. **Bandwidth versus power** — capacity can be raised with more bandwidth (linear gain) or more SNR (logarithmic gain). For B = 1 MHz and SNR = 1000 (30 dB), C ≈ 9.97 Mbps; doubling the bandwidth (same SNR) gives ≈ 19.93 Mbps, while doubling the SNR (≈ 33 dB) gives only ≈ 10.97 Mbps. Hence Wi-Fi channel bonding (20 → 40 → 80 → 160 MHz) and wide 5G carriers (up to 100 MHz below 6 GHz, 400 MHz in mmWave bands).
3. **More levels need more SNR** — packing more levels into the same voltage range puts them closer together, so noise confuses them. Equating Nyquist and Shannon gives the largest useful number of levels, L = √(1 + SNR): 4 levels need SNR ≥ 15 (≈ 11.8 dB); SNR = 63 allows 8 levels.
4. **Adaptive modulation and coding** — Wi-Fi, 4G LTE and 5G measure the SNR continuously and switch between QPSK (2 bits/symbol) at low SNR and 16-QAM (4), 64-QAM (6) or 256-QAM (8 bits/symbol) at high SNR; Wi-Fi 6 adds 1024-QAM. The data rate follows the channel quality, as the theorem predicts.
5. **Error-correcting codes** — the theorem promises error-free transmission up to C with suitable coding; Turbo codes (3G/4G), LDPC codes (Wi-Fi, 5G data) and Polar codes (5G control) come close to the Shannon limit.
6. **Raising SNR and adding channels** — fiber instead of copper, shielding, low-noise amplifiers and repeaters raise the SNR; MIMO uses several antennas to create parallel channels that multiply capacity.
7. **Realistic targets** — a 3 kHz voice channel cannot carry more than about 35 kbps, so DSL obtains megabits per second by using a much wider band (about 1 MHz) of the same copper pair.

**Limitations of the theorem**

- It gives the limit but not the method to reach it.
- It assumes random (white Gaussian) noise; interference, fading and impulse noise reduce the practical rate further.
- Approaching the limit needs long codes, which add delay and complexity.

**Summary:** Shannon's theorem C = B × log2(1 + SNR) gives the maximum error-free bit rate of a noisy channel (≈ 34.9 kbps for a 3 kHz, 35 dB telephone line); unlike Nyquist's 2 × B × log2(L) it caps every scheme whatever the number of levels, and it shapes modern design — wider bandwidth, higher SNR, adaptive QAM and near-capacity error-correcting codes in Wi-Fi, 4G and 5G.

---

### Q12. Encoding and modulation

**Definition**

Data must be converted into a signal before it can travel over a medium.

- **Encoding** (digital-to-digital conversion, **line coding**) converts a sequence of bits into a **digital signal** — a pattern of voltage levels — that is sent directly on a wire (baseband transmission). Example: Manchester encoding on 10 Mbps Ethernet.
- **Modulation** varies one characteristic of a high-frequency **carrier** — amplitude, frequency or phase — according to the message, so that the signal suits the medium (radio, telephone line, optical fiber). For digital data it is **digital modulation**: ASK, FSK, PSK and QAM.

**Conversion methods (class slides)**

| Conversion | Name | Techniques | Example |
|---|---|---|---|
| Digital data → digital signal | Encoding | Line coding, block coding, scrambling | Ethernet LAN |
| Analog data → digital signal | Pulse modulation | PAM, PWM, PPM; PCM (sampling + quantization) | Digital telephony |
| Digital data → analog signal | Digital modulation | ASK, FSK, PSK, QAM | Modem, Wi-Fi, mobile phone |
| Analog data → analog signal | Analog modulation | AM, FM, PM | AM/FM radio |

**Block diagram — where encoding and modulation sit**

```
                              TRANSMITTER
 +-------------+    +------------+    +--------------------------------+
 | Source      |--->| A/D (PCM)  |--->| Line encoder (baseband)        |
 | data        |    | only if    |    |       - or -                   |
 | 01001110    |    | analog     |    | Modulator (+ carrier)          |
 +-------------+    +------------+    +----------------+---------------+
                                                       |  signal
                                                       v
                                      +--------------------------------+
                                      | CHANNEL: cable / fiber / radio |
                                      |          (+ noise)             |
                                      +----------------+---------------+
                                                       |  noisy signal
                              RECEIVER                 v
 +-------------+    +------------+    +--------------------------------+
 | Destination |<---| D/A only   |<---| Line decoder  - or -           |
 +-------------+    | if analog  |    | Demodulator: recover clock,    |
                    +------------+    | regenerate the bits            |
                                      +--------------------------------+
```

**The process**

1. The source produces data; analog data such as voice is first digitized by sampling and quantization (PCM).
2. **Encoding** maps the bits to signal levels (line coding). Block coding (e.g., 4B/5B) or scrambling (e.g., B8ZS, HDB3) may be added to guarantee enough transitions.
3. **Modulation** is used when the channel is band-pass (radio, telephone line): the bits key a high-frequency carrier.
4. The channel attenuates the signal and adds noise.
5. The receiver demodulates or decodes, recovers the clock from the transitions and regenerates the bits.

**Line coding schemes (class slides)**

```
                         Line coding
                              |
        +---------------------+----------------------+
        |                     |                      |
    Unipolar                Polar                 Bipolar
                              |                    (AMI)
          +-------------------+--------------------+
          |                   |                    |
         NRZ                 RZ                 Biphase
      +---+---+                              +-----+------+
      |       |                              |            |
    NRZ-L   NRZ-I                       Manchester   Differential
                                                     Manchester
```

**Rules used in the waveforms**

| Scheme | Rule |
|---|---|
| Unipolar (NRZ) | 1 = +V; 0 = 0 V |
| NRZ-L (polar) | 0 = +V; 1 = −V — the level decides the bit |
| NRZ-I (polar) | 1 = invert the level at the start of the bit; 0 = no change (line assumed at +V before the first bit) |
| RZ (polar) | 1 = +V for the first half, then 0 V; 0 = −V for the first half, then 0 V |
| Manchester (biphase) | Transition in the middle of every bit: 1 = low-to-high, 0 = high-to-low |
| Differential Manchester (biphase) | Transition in the middle of every bit; 0 = an extra transition at the start of the bit, 1 = no transition at the start (line assumed at +V before the first bit) |
| Bipolar AMI | 0 = 0 V; 1 = alternately +V and −V (first 1 = +V) |

**Waveforms for 01001110 (the class example)**

```
Bits             0       1       0       0       1       1       1       0
             :       :       :       :       :       :       :       :       :

                      _______                 _______________________
Unipolar             |       |               |                       |
              _______|       |_______________|                       |_______

              _______         _______________                         _______
NRZ-L                |       |               |                       |
                     |_______|               |_______________________|

           __________                         _______         _______________
NRZ-I                |                       |       |       |
                     |_______________________|       |_______|

                      ___                     ___     ___     ___
                     |   |                   |   |   |   |   |   |
RZ                ___|   |___     ___     ___|   |___|   |___|   |___     ___
                 |           |   |   |   |                           |   |
              ___|           |___|   |___|                           |___|

              ___         _______     ___         ___     ___     _______
Manchester       |       |       |   |   |       |   |   |   |   |       |
                 |_______|       |___|   |_______|   |___|   |___|       |___

           __     _______     ___     ___         _______         ___     ___
Diff. Man.   |   |       |   |   |   |   |       |       |       |   |   |
             |___|       |___|   |___|   |_______|       |_______|   |___|

                      _______                         _______
                     |       |                       |       |
AMI           _______|       |_______________        |       |        _______
                                             |       |       |       |
                                             |_______|       |_______|
```

Top line = +V and bottom line = −V (0 V for unipolar); RZ and AMI use three lines: +V, 0 V and −V. The short stub before NRZ-I and Differential Manchester shows the line level before the first bit.

**Comparison of line codes**

| Scheme | Levels | Synchronization | DC component | Bandwidth | Use / drawback |
|---|---|---|---|---|---|
| Unipolar | 2 (+V, 0) | Poor — no transitions in long runs of 0s or 1s | Yes | Low | Wastes power; not used today |
| NRZ-L | 2 (+V, −V) | Poor — long runs of 0s or 1s | Yes | Low | Polarity reversal inverts every bit |
| NRZ-I | 2 (+V, −V) | Good for runs of 1s, poor for runs of 0s | Yes | Low | Used with 4B/5B block coding (FDDI, 100BASE-FX) |
| RZ | 3 (+V, 0, −V) | Good — a transition in every bit | Yes, but smaller | High (two changes per bit) | Three levels; replaced by Manchester |
| Manchester | 2 (+V, −V) | Excellent — mid-bit transition in every bit | None | High (twice NRZ) | 10 Mbps Ethernet (IEEE 802.3) |
| Differential Manchester | 2 (+V, −V) | Excellent | None | High (twice NRZ) | Token Ring (IEEE 802.5); immune to polarity reversal |
| Bipolar AMI | 3 (+V, 0, −V) | Poor for long runs of 0s (fixed by B8ZS/HDB3 scrambling) | None | Same as NRZ | T1/E1 telephone lines |

**Digital modulation (digital data → analog signal)**

Why a carrier is needed (class slides):

- Low-frequency baseband signals (audio is 20 Hz–20 kHz) cannot travel far through air; a high-frequency carrier can.
- Antenna size: an antenna is about λ/4 long — 25 km for a 3 kHz signal but only 0.75 m for a 100 MHz carrier.
- Different carrier frequencies let many signals share one medium without interfering (FDM).
- It matches the signal to band-pass channels such as radio and telephone lines.

The techniques:

- **ASK (Amplitude Shift Keying)** — the carrier's amplitude changes with the data; frequency and phase stay constant. Class convention: 1 = carrier at full amplitude, 0 = zero amplitude (on-off keying). Simple, but noise easily corrupts the amplitude. Used in optical fiber (light on/off) and RFID.
- **FSK (Frequency Shift Keying)** — the carrier's frequency changes: one frequency for 1 and another for 0; amplitude and phase stay constant. More noise-resistant than ASK but needs more bandwidth. Used in early 300 bps modems, caller ID and Bluetooth (GFSK).
- **PSK (Phase Shift Keying)** — the carrier's phase changes; amplitude and frequency stay constant. Binary PSK: 1 = phase 0°, 0 = phase shifted by 180°. QPSK uses four phases 90° apart to send 2 bits per symbol. Robust against noise, but the receiver needs a phase reference. Used in satellite links, GPS and Wi-Fi at low rates.
- **QAM (Quadrature Amplitude Modulation)** — combines ASK and PSK: both amplitude and phase change, so each symbol carries several bits (16-QAM = 4 bits, 64-QAM = 6 bits, 256-QAM = 8 bits). Most bits per hertz, but needs a high SNR. Used in Wi-Fi, 4G/5G, cable modems and DSL.

**Waveforms for 1010 (as in the class slide)**

```
Bits             1               0               1               0
          :               :               :               :               :
          ________________                 _______________
Data                      |_______________|               |_______________

Carrier   /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\
            \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/

ASK       /\  /\  /\  /\  ________________/\  /\  /\  /\  ________________
            \/  \/  \/  \/                  \/  \/  \/  \/

                           __      __                      __      __
FSK       /\  /\  /\  /\  /  \    /  \    /\  /\  /\  /\  /  \    /  \
            \/  \/  \/  \/    \__/    \__/  \/  \/  \/  \/    \__/    \__/

PSK       /\  /\  /\  /\    /\  /\  /\  /\/\  /\  /\  /\    /\  /\  /\  /\
            \/  \/  \/  \/\/  \/  \/  \/    \/  \/  \/  \/\/  \/  \/  \/
```

In this sketch FSK uses the higher frequency for 1 and the lower frequency for 0, as in the slide's figure. Which frequency stands for which bit is only a convention (the slide's text states the reverse), so state the convention you use. In PSK the sudden reversal at each 1 → 0 and 0 → 1 boundary is the 180° phase shift.

**16-QAM constellation** — each dot is one amplitude-phase combination, so 16 dots = 16 symbols = 4 bits per symbol.

```
                 Q
                 |
       o    o    |    o    o
                 |
       o    o    |    o    o
  ---------------+---------------  I
       o    o    |    o    o
                 |
       o    o    |    o    o
                 |
```

**Comparison of digital modulation techniques**

| Basis | ASK | FSK | PSK | QAM |
|---|---|---|---|---|
| Carrier property changed | Amplitude | Frequency | Phase | Amplitude and phase |
| Bits per symbol | 1 | 1 | 1 (BPSK), 2 (QPSK) | 4, 6, 8 (16-, 64-, 256-QAM) |
| Noise immunity | Poor | Good | Very good | Lower — needs a high SNR |
| Bandwidth efficiency | Moderate | Low (uses two frequencies) | Moderate (BPSK), good (QPSK) | Highest |
| Receiver complexity | Simple | Simple | Complex (phase reference) | Most complex |
| Typical use | Optical fiber, RFID | Early modems, Bluetooth | Satellite, GPS, Wi-Fi (low rates) | Wi-Fi, 4G/5G, cable modems |

**Advantages and limitations**

- **Encoding** — simple and cheap, with no carrier needed on cables; self-clocking codes (Manchester, Differential Manchester) keep sender and receiver synchronized and remove the DC component. But it suits only baseband (low-pass) wired channels, and self-clocking codes need more bandwidth.
- **Modulation** — makes long-distance and wireless transmission possible, allows small antennas and FDM of many signals, and higher-order schemes carry many bits per symbol. But it needs oscillators, mixers and phase-locked receivers (more complex), and higher-order schemes need a high SNR (Shannon limit, Q11).

**Summary:** Encoding (line coding) turns bits into a digital baseband signal — unipolar, NRZ-L, NRZ-I, RZ, Manchester, Differential Manchester and bipolar AMI, which differ in levels, synchronization, DC component and bandwidth — while modulation keys a high-frequency carrier (ASK, FSK, PSK, QAM) so that digital data can travel over band-pass channels such as radio and telephone lines.

---

### Q13. TDM and FDM

**Multiplexing**

**Multiplexing** is the process of combining several signals into one signal over a shared medium. It divides one physical link into several **logical channels**, one for each signal. The device that combines the signals is the **multiplexer (MUX)**; the device at the receiver that separates them again is the **demultiplexer (DEMUX)**. One high-capacity link then replaces many separate links. The two classic techniques are **Frequency Division Multiplexing (FDM)** and **Time Division Multiplexing (TDM)**.

```
              +-------+                          +---------+
 Input 1 ---->|       |                          |         |----> Output 1
 Input 2 ---->|       |     one shared link      |         |----> Output 2
 Input 3 ---->|  MUX  |==========================|  DEMUX  |----> Output 3
   ...        |       |  (n logical channels)    |         |        ...
 Input n ---->|       |                          |         |----> Output n
              +-------+                          +---------+
```

**1. Frequency Division Multiplexing (FDM)**

**Definition:** In FDM the bandwidth of the link is divided into separate frequency bands (channels). Each signal is given its own band, and all signals are transmitted **at the same time**. Narrow unused strips called **guard bands** separate adjacent channels so that they do not overlap.

**Working**

- Sender: each source modulates a carrier of a different frequency (f1, f2, f3); the modulated signals are added and sent on the link.
- Receiver: band-pass filters (BPF) separate the bands, and each band is demodulated.
- Every user feels it owns its band all the time. FDM is basically an analog technique.

```
  amplitude
      ^
      |    +----------+      +----------+      +----------+
      |    | Channel 1|      | Channel 2|      | Channel 3|
      |    |  band f1 |      |  band f2 |      |  band f3 |
      +----+----------+------+----------+------+----------+-----> frequency
                       \____/            \____/
                     guard band        guard band
```

```
          SENDER (MUX)                          RECEIVER (DEMUX)
 S1 --> [Mod f1] --+                          +--> [BPF f1] --> [Demod] --> D1
 S2 --> [Mod f2] --+--> ( + ) ==== link ====>-+--> [BPF f2] --> [Demod] --> D2
 S3 --> [Mod f3] --+                          +--> [BPF f3] --> [Demod] --> D3
```

S = source, D = destination, Mod = modulator (carrier f1, f2 or f3), BPF = band-pass filter, Demod = demodulator.

**Example:** Five channels of 100 kHz each are multiplexed with a 10 kHz guard band between neighbors. Five channels need four guard bands, so the link needs at least 5 × 100 + 4 × 10 = **540 kHz**.

**Advantages**

- All signals are sent simultaneously; no time synchronization is needed between the sources.
- Simple for analog signals and ideal for broadcasting.
- Each channel is independent — a slow or idle source does not delay the others.

**Limitations**

- Guard bands waste bandwidth.
- Crosstalk and intermodulation between adjacent channels.
- A modulator and a filter are needed per channel — complex and costly.
- An idle channel still occupies its band, and each user's bandwidth is fixed.

**2. Time Division Multiplexing (TDM)**

**Definition:** In TDM the users share the **whole bandwidth** of the link **in turns**: time is divided into recurring slots of fixed length, and each signal is given a slot in round-robin order. One round of slots forms a **frame**. TDM is used mainly for digital signals. It has two types — synchronous and asynchronous.

**Synchronous TDM**

- Slots are pre-assigned and fixed — each input always gets its own slot in every frame.
- A slot is sent **empty** if its source has no data at that moment.
- Framing (synchronization) bits mark the start of each frame so the DEMUX stays in step.
- Used for multiplexing digitized voice.

```
 A: AAAA --+    +-----+   Frame 4     Frame 3     Frame 2     Frame 1
 B: BB   --+    |     |  +-+-+-+-+   +-+-+-+-+   +-+-+-+-+   +-+-+-+-+
 C: C    --+--->| MUX |--| | | |A|---|D| | |A|---|D| |B|A|---|D|C|B|A|--->
 D: DDD  --+    |     |  +-+-+-+-+   +-+-+-+-+   +-+-+-+-+   +-+-+-+-+
                +-----+
```

Frames move to the right, so Frame 1 — and slot A within each frame — is sent first. The 16 slots carry only 10 data units: 6 slots (37.5%) travel empty.

**Asynchronous (statistical) TDM**

- Slots are allocated dynamically to the inputs that have data, so a frame has fewer slots than there are inputs (here 3 slots for 4 inputs).
- Each slot carries the address of its source (A1 = data from line 1), so the DEMUX can deliver it.
- It saves channel capacity: the same 10 data units need only 12 slots (83% used) instead of 16.

```
 A: AAAA --+    +-----+   Frame 4      Frame 3      Frame 2      Frame 1
 B: BB   --+    |     |  +--+--+--+   +--+--+--+   +--+--+--+   +--+--+--+
 C: C    --+--->| MUX |--|  |  |A1|---|D4|A1|D4|---|B2|A1|D4|---|C3|B2|A1|--->
 D: DDD  --+    |     |  +--+--+--+   +--+--+--+   +--+--+--+   +--+--+--+
                +-----+
```

**Example — T1 line (digital telephony):** 24 voice channels of 64 kbps each are time-division multiplexed. Each frame holds 24 × 8 = 192 bits plus 1 framing bit = 193 bits, and 8,000 frames are sent per second: 193 × 8,000 = **1.544 Mbps** (= 24 × 64 kbps + 8 kbps of framing). The E1 line used in Europe and India carries 32 slots × 64 kbps = 2.048 Mbps.

**Advantages**

- Each user gets the full bandwidth of the link during its slot; no guard bands are needed.
- Low interference — only one signal is on the link at a time.
- Simpler, cheaper digital circuitry; suits computers and digital data.
- Statistical TDM adapts to bursty traffic.

**Limitations**

- Needs precise synchronization (sync pulses, framing bits).
- Synchronous TDM wastes empty slots.
- Buffering adds delay; statistical TDM needs addresses (overhead) and may queue data when many inputs are busy.

**Comparison (class slide, with extra points)**

| Basis | TDM | FDM |
|---|---|---|
| Basic | Time is shared | Frequency is shared |
| Used with | Digital and analog signals | Analog signals |
| Necessary requirement | Synchronization pulse | Guard band |
| Interference | Low or negligible | High (crosstalk between adjacent bands) |
| Circuitry | Simpler | Complex |
| Utilization | Efficient | Less efficient |
| How signals are sent | One after another, each in its own time slot using the full bandwidth | All at the same time, each in its own frequency band |
| Wasted resource | Empty slots (synchronous TDM) | Guard bands and idle bands |

**Applications compared**

| Area | FDM | TDM |
|---|---|---|
| Broadcasting and cable TV | Radio stations and TV channels each occupy their own frequency band; one coaxial cable carries hundreds of 6–8 MHz channels | Digital TV interleaves several programs in time within one channel's bit stream |
| Telephone network | Older analog trunks (12 voice channels per group) | Digital trunks: T1 (1.544 Mbps), E1 (2.048 Mbps), SONET/SDH backbones |
| Mobile networks | 1G (AMPS): each call on its own 30 kHz channel | 2G GSM: each 200 kHz carrier split into 8 time slots (FDM and TDM together) |
| Access and fiber | ADSL: separate bands for voice, upload and download; WDM in fiber is FDM of light wavelengths | Statistical TDM on packet links; SONET/SDH on fiber |

- FDM suits continuous analog signals that must be sent all the time (broadcasting); TDM suits digital data that can be buffered and sent in turns.
- Modern systems combine both, e.g., GSM; OFDM in Wi-Fi, 4G and 5G is an advanced form of FDM that uses overlapping (orthogonal) subcarriers instead of guard bands.

**Summary:** FDM divides the link's bandwidth into frequency bands separated by guard bands so that all signals travel at once (radio/TV broadcasting, cable TV, 1G cellular, ADSL); TDM gives each source the whole bandwidth in turns through time slots grouped into frames — fixed in synchronous TDM, on demand in statistical TDM — and suits digital traffic such as T1 (24 × 64 kbps + 8 kbps framing = 1.544 Mbps), E1 and GSM time slots.

---

### Q14. Switching techniques

**Definition**

**Switching** is the technique of forwarding data from an input link to the correct output link through intermediate devices called **switches** (switching nodes), so that many devices can communicate over shared links. Without switching, every pair of devices would need its own link — a full mesh of n devices needs n(n − 1)/2 links, e.g., 4,950 links for 100 devices.

**Classification**

```
                        Switching techniques
                                  |
         +------------------------+------------------------+
         |                        |                        |
 Circuit switching        Message switching        Packet switching
                                                           |
                                                 +---------+----------+
                                                 |                    |
                                             Datagram          Virtual circuit
                                         (connectionless)       (connection-
                                                                  oriented)
```

**1. Circuit switching**

A dedicated path (circuit) between sender and receiver is set up **before** data transfer and stays reserved for the whole communication. On each link the circuit occupies one channel — an **FDM frequency band or a TDM time slot** — which is why the syllabus places TDM and FDM under switching techniques (see Q13).

**Phases**

1. **Connection setup** — a path is found and resources are reserved on every link (A requests, the switches allocate a channel, B accepts).
2. **Data transfer** — data flows continuously along the reserved path; the switches do no addressing or queuing.
3. **Connection teardown** — the path is released for other users.

```
          +----+          +----+          +----+
  A ======| S1 |==========| S2 |==========| S4 |====== B
          +----+          +----+          +----+
            |               |               |
          +----+          +----+            |
  C ------| S3 |----------| S5 |------------+
          +----+          +----+
```

The path A–S1–S2–S4–B (`====`) is reserved for the whole call, even while A and B are silent; the other links (`----`) are not used by this call.

- **Example:** the traditional telephone network (PSTN).
- **Advantages:** guaranteed bandwidth; constant, low delay; data arrives in order; no per-packet headers — good for continuous real-time traffic such as voice.
- **Disadvantages:** setup delay; reserved capacity is wasted while the users are silent; fixed bandwidth; calls are blocked when no path is free; a link failure drops the call.

**2. Message switching**

There is no dedicated path. The **whole message**, with the destination address in its header, is sent to the next switch, which **stores** it completely and then **forwards** it when the next link is free (**store-and-forward**).

```
  A ----> [ S1 ] ----> [ S2 ] ----> [ S4 ] ----> B
          stores       stores       stores
          the whole    the whole    the whole
          message,     message,     message,
          then sends   then sends   then sends
```

- **Example:** telegraph networks and early email systems.
- **Advantages:** no setup phase; links are shared, so they are used better than in circuit switching; messages can be stored while the receiver is busy and can be given priorities.
- **Disadvantages:** switches need large storage (disks) for whole messages; long, variable delays make it unsuitable for interactive or real-time traffic; one long message can occupy a link for a long time.

**3. Packet switching**

The message is divided into small **packets**, each with a header (addresses, sequence number). Packets are stored and forwarded one by one, and link capacity is shared on demand among all users (**statistical multiplexing**). There are two approaches:

- **Datagram approach (connectionless):** each packet is routed independently using the destination address in its header; packets of one message may take different routes, arrive out of order or be lost; there is no setup phase. Example: IP in the Internet.
- **Virtual-circuit approach (connection-oriented):** a setup phase fixes one route; every packet carries a short virtual-circuit identifier (VCI), follows the same route and arrives in order; the circuit is torn down at the end. Resources can be reserved, but links are still shared with other circuits. Examples: X.25, Frame Relay, ATM, MPLS.

```
          +----+   1, 3   +----+   1, 3   +----+   1, 3
  A ------| S1 |----------| S2 |----------| S4 |------ B
          +----+          +----+          +----+        receives 1, 3, 2
            |  2            |               |  2        and reorders them
          +----+    2     +----+     2      |
  C ------| S3 |----------| S5 |------------+
          +----+          +----+
```

Datagram approach: A sends packets 1, 2 and 3; packets 1 and 3 go via S2, while packet 2 goes via S3 and S5 and arrives last, so B puts them back in order. In a virtual circuit all three packets would follow one fixed route and arrive in order.

- **Advantages:** efficient link use — no capacity is reserved while idle; no setup delay (datagram); traffic is rerouted around failures; many users with bursty traffic can be supported.
- **Disadvantages:** variable delay (queuing) and jitter; packets may be lost or reordered (datagram); header overhead; congestion when many users send at once.

**Comparison**

| Basis | Circuit switching | Message switching | Packet switching (datagram) | Packet switching (virtual circuit) |
|---|---|---|---|---|
| Path | Dedicated path set up first | No fixed path; hop by hop | No fixed path; each packet routed separately | One logical path set up first |
| Setup and teardown | Yes | No | No | Yes |
| Unit of transfer | Continuous bit stream | Whole message | Packet | Packet |
| Store-and-forward | No | Yes (whole message) | Yes (per packet) | Yes (per packet) |
| Resource reservation | Yes, for the whole session | No | No | Optional |
| Link utilization | Low for bursty data | Better | Highest (statistical multiplexing) | High |
| Delay | Setup delay, then constant and low | Long and variable | Variable (queuing) | Setup delay, then less variable |
| Order of delivery | In order | In order | May be out of order | In order |
| Address carried | Only during setup | Full address in each message | Full address in each packet | Short VC identifier in each packet |
| Effect of a link failure | Call dropped | Message rerouted | Packets rerouted | Circuit must be set up again |
| Example | Telephone network (PSTN) | Telegraph, early email | Internet (IP) | X.25, Frame Relay, ATM, MPLS |

**Role in efficient resource utilization**

- **Dedicated versus shared links:** circuit switching reserves capacity for the whole session — fine for continuous voice, but computer data is bursty, so most of the reserved capacity sits idle. Message and packet switching occupy a link only while data is actually being sent.
- **Statistical multiplexing:** packets from many users share a link on demand. Example (Kurose & Ross): a 1 Mbps link; each user sends at 100 kbps when active and is active 10% of the time. Circuit switching supports only 1 Mbps ÷ 100 kbps = 10 users. Packet switching can serve 35 users, because the probability that more than 10 of them are active at the same time is only about 0.0004.
- **Store-and-forward pipelining:** small packets let all links work at the same time. A 3 Mb message sent from A to B through two switches over three 1 Mbps links (ignoring propagation delay and headers) takes 3 × 3 s = 9 s with message switching, but only (3 + 3 − 1) × 1 s = 5 s when split into three 1 Mb packets.
- **Buffer space:** packet switches need only small buffers; message switches need disks for whole messages.
- **Virtual circuits** combine both ideas — shared links with ordered delivery and optional reservation for quality of service.
- **Matching the technique to the traffic:** circuit switching for constant-rate, delay-sensitive traffic (classic telephony); packet switching for bursty data — the reason the Internet, and today's 4G/5G mobile networks (voice over LTE), are packet switched.

**Summary:** Switching connects many users through shared nodes — circuit switching reserves a dedicated path (a TDM slot or FDM band on each link) through setup, transfer and teardown, guaranteeing quality but wasting idle capacity; message switching stores and forwards whole messages; packet switching (datagram or virtual circuit) stores and forwards small packets and shares links by statistical multiplexing, giving the best utilization for bursty data, which is why the Internet is packet switched.

---

## Unit 2 — Data Link Layer

### Q1. Character stuffing in character-oriented framing

**Character stuffing** is a technique used in **character-oriented framing** to distinguish control characters from actual data.

In character-oriented protocols, special characters are used to indicate the **beginning and end of a frame**.

Suppose:

- `FLAG` indicates the beginning/end of a frame.
- `ESC` is an escape character.

If the actual data contains `FLAG` or `ESC`, the sender inserts an `ESC` before it. This process is called **character stuffing**.

**Example**

Suppose the frame delimiter is: `FLAG`

Original data: `A B FLAG C`

The receiver could incorrectly interpret `FLAG` as the end of the frame.

Therefore, the sender stuffs an escape character:

`FLAG A B ESC FLAG C FLAG`

At the receiver, when `ESC FLAG` is encountered, it understands that `FLAG` is **data**, not a frame delimiter.

The receiver removes the extra `ESC` character and reconstructs:

`A B FLAG C`

**Process**

**Sender:** Data → Search for special characters → Insert ESC → Send frame

**Receiver:** Receive frame → Detect ESC → Remove ESC → Recover original data

**Advantages**

- Simple technique.
- Prevents confusion between control characters and data.
- Useful for character-oriented protocols.

**Disadvantage**

The size of the transmitted frame increases when data contains many special characters.

**Summary:** In character-oriented framing a `FLAG` character marks the start and end of each frame; character (byte) stuffing makes the sender insert an `ESC` before every `FLAG` or `ESC` that appears in the data, and the receiver removes each `ESC` and treats the next character as data — e.g. data `A B FLAG C` is sent as `FLAG A B ESC FLAG C FLAG`.

---

### Q2. Bit stuffing in bit-oriented framing

**Bit stuffing** is a framing technique used in **bit-oriented protocols** to ensure that a special bit pattern used as a frame delimiter does not accidentally appear in the data.

A common flag pattern is: `01111110`

The sender follows this rule:

Whenever five consecutive `1`s occur in the data, the sender inserts a `0`.

The receiver removes the inserted `0` after detecting five consecutive `1`s.

**Example**

Suppose original data is: `011111101`

The data contains five consecutive `1`s, followed by a sixth `1`:

`0 11111 1 0 1`

The sender inserts `0` after the five `1`s:

`0111110101` (grouped: `0 11111 0 1 0 1`)

The frame can then be transmitted as:

```
FLAG       Stuffed Data   FLAG
01111110   0111110101     01111110
```

At the receiver, after five consecutive `1`s, the inserted `0` is removed.

```
0111110101
      ↑
  stuffed 0
```

The original data is recovered: `011111101`

**Advantages**

- Prevents accidental occurrence of the flag pattern in data.
- Provides reliable frame boundary detection.
- Used in bit-oriented protocols such as HDLC.

**Difference from Character Stuffing**

Character stuffing works with **characters/bytes**, whereas bit stuffing works at the **individual bit level**.

**Summary:** In bit-oriented framing (e.g. HDLC) the flag `01111110` marks the frame boundaries; bit stuffing makes the sender insert a `0` after every five consecutive `1`s in the data so the flag pattern can never appear inside a frame, and the receiver deletes that `0` — e.g. data `011111101` is sent as `0111110101`.

---

### Q3. VRC and LRC

**Vertical Redundancy Check (VRC)**

**VRC**, commonly called **parity checking**, adds one extra parity bit to each transmitted data unit.

The parity bit makes the total number of `1`s either:

- **Even** for even parity.
- **Odd** for odd parity.

**Example: Even Parity**

Suppose data is: `1011001`

Number of 1s = 4, which is already even.

Therefore:

| Data | Parity bit | Transmitted |
|---|---|---|
| `1011001` | `0` | `10110010` |

If the receiver receives `10110011`, there are now 5 ones, which is odd.

Therefore, an error is detected.

**Advantages**

- Simple.
- Low overhead.
- Easy to implement.

**Disadvantage**

VRC may fail to detect errors involving an **even number of bit changes**.

**Longitudinal Redundancy Check (LRC)**

**LRC** calculates parity across multiple data units, usually arranged in rows and columns.

An additional parity row is generated so that each column satisfies the selected parity condition.

For example:

```
        1 0 1 1
        1 0 1 0
        1 1 1 1
        1 0 1 0
        -------
LRC     0 1 0 0
```

The LRC bits are calculated column-wise.

For even parity:

| Column | Bits (rows 1–4) | Number of 1s | LRC bit |
|---|---|---|---|
| Column 1 | `1 1 1 1` | 4 | 0 |
| Column 2 | `0 0 1 0` | 1 | 1 |
| Column 3 | `1 1 1 1` | 4 | 0 |
| Column 4 | `1 0 1 0` | 2 | 0 |

Therefore: LRC = `0100`

LRC can detect many errors that simple VRC cannot, particularly when the errors affect different columns — for example, a burst error that changes several bits of the same row.

**Summary:** VRC (parity check) adds one parity bit per data unit so that its number of `1`s is even (or odd) — it detects any odd number of flipped bits but misses an even number; LRC arranges the data units in rows and adds a parity row computed column by column (e.g. LRC `0100`), which also catches burst errors that VRC misses.

---

### Q4. VRC numerical — checking the received bytes

**Given** (bits numbered 1–8 from the left):

| Sr No | Sender side | Receiver side |
|---|---|---|
| 1 | `1 0 1 1 1 0 1 0` | `1 0 1 1 1 0 1 1` |
| 2 | `1 1 1 1 1 0 1 0` | `1 1 0 1 1 0 1 0` |
| 3 | `1 1 0 0 1 0 1 0` | `1 1 1 0 1 0 1 1` |
| 4 | `0 1 0 0 1 0 1 0` | `0 1 0 0 1 0 1 0` |

**Method (even parity)**

1. The sender bytes have mixed parity (5, 6, 4 and 3 `1`s), so their last bit is not already a parity bit and each 8-bit row is treated as data. The sender counts the `1`s in each byte and adds a VRC (parity) bit in front of it — 1 if the count is odd, 0 if it is even — so the 9 transmitted bits always contain an even number of `1`s.
2. The VRC bit travels with the byte (assumed to arrive intact); the receiver-side column shows the 8 data bits that arrived.
3. The receiver recomputes the parity of the received data bits and compares it with the received VRC bit. Equivalently, it counts the `1`s in all 9 received bits: an odd count means an error.

As in the class slides, the VRC bit is written in front of the data (the example in Q3 appends it at the end instead); its position does not change the check.

**Step 1 — Sender: generate the VRC bits**

| Sr No | Sender data | Number of 1s | VRC bit (even) | Transmitted (VRC + data) |
|---|---|---|---|---|
| 1 | `10111010` | 5 (odd) | 1 | `1 10111010` |
| 2 | `11111010` | 6 (even) | 0 | `0 11111010` |
| 3 | `11001010` | 4 (even) | 0 | `0 11001010` |
| 4 | `01001010` | 3 (odd) | 1 | `1 01001010` |

**Step 2 — Receiver: recompute the parity and compare**

| Sr No | Received data | Number of 1s | Recomputed parity | Received VRC | 1s in all 9 bits | Result |
|---|---|---|---|---|---|---|
| 1 | `10111011` | 6 | 0 | 1 | 7 (odd) | 0 ≠ 1 → **error detected** |
| 2 | `11011010` | 5 | 1 | 0 | 5 (odd) | 1 ≠ 0 → **error detected** |
| 3 | `11101011` | 6 | 0 | 0 | 6 (even) | 0 = 0 → accepted (error **not** detected) |
| 4 | `01001010` | 3 | 1 | 1 | 4 (even) | 1 = 1 → accepted (no error) |

**Step 3 — Which bits actually changed (sender vs receiver)**

| Sr No | Changed bit(s) | Flipped bits | Why VRC does or does not catch it |
|---|---|---|---|
| 1 | bit 8 (0 → 1) | 1 (odd) | One flip changes the parity → detected |
| 2 | bit 3 (1 → 0) | 1 (odd) | One flip changes the parity → detected |
| 3 | bit 3 (0 → 1) and bit 8 (0 → 1) | 2 (even) | The two flips cancel; parity stays even → missed |
| 4 | none | 0 | Byte arrived unchanged → correctly accepted |

**Conclusion**

- **Rows 1 and 2:** the recomputed parity disagrees with the VRC bit, so VRC demonstrates that an error has occurred.
- **Row 3:** the byte *is* corrupted (bits 3 and 8 flipped), but because an even number of bits changed, the number of `1`s stays even and VRC accepts it. This is VRC's limitation — it detects only an odd number of bit errors in a data unit.
- **Row 4:** the sent and received bytes are identical, so there is no error to detect.

So the question's "demonstrate that an error has occurred" holds only for rows 1 and 2: row 3 contains an error that VRC cannot detect, and row 4 contains no error. With odd parity every VRC bit is inverted (0, 1, 1, 0), but the verdicts are exactly the same.

**Summary:** With even parity the sender's VRC bits are 1, 0, 0, 1; the receiver's recomputed parity disagrees in rows 1 and 2 (single-bit errors in bit 8 and bit 3 → error detected), row 3 passes even though bits 3 and 8 both flipped (VRC misses an even number of errors), and row 4 arrived unchanged.

---

### Q5. LRC numerical — checking the received blocks

**Method (even parity)**

1. Each block of four 4-bit data units is written as rows (rows 1–4 from the top, columns C1–C4 from the left).
2. The sender counts the `1`s in each **column** and sets that column's LRC bit to 1 if the count is odd and 0 if it is even. The 4-bit LRC row is sent after the block.
3. The receiver recomputes the LRC over the received rows, column by column, and compares it with the LRC row it received. Any mismatch means an error. (Equivalently, every column together with its LRC bit must contain an even number of `1`s.)

**Block 1**

| Row | Sender | Receiver |
|---|---|---|
| 1 | `1 0 1 1` | `1 0 1 1` |
| 2 | `1 0 1 0` | `1 0 1 0` |
| 3 | `1 1 1 1` | `1 1 0 1` |
| 4 | `1 0 1 0` | `1 0 1 0` |
| 1s per column (C1–C4) | `4 1 4 2` | `4 1 3 2` |
| LRC (even) | `0 1 0 0` (sent) | `0 1 1 0` (recomputed) |

Sender LRC `0100` ≠ recomputed LRC `0110` → column 3 mismatches → **error detected**. (Row 3, column 3 changed 1 → 0, so column 3 now has an odd number of `1`s.)

**Block 2**

| Row | Sender | Receiver |
|---|---|---|
| 1 | `1 1 0 0` | `1 1 0 0` |
| 2 | `1 0 1 0` | `1 0 1 0` |
| 3 | `0 1 0 1` | `0 1 0 1` |
| 4 | `0 1 0 1` | `0 1 1 1` |
| 1s per column (C1–C4) | `2 3 1 2` | `2 3 2 2` |
| LRC (even) | `0 1 1 0` (sent) | `0 1 0 0` (recomputed) |

Sender LRC `0110` ≠ recomputed LRC `0100` → column 3 mismatches → **error detected**. (Row 4, column 3 changed 0 → 1.)

**Block 3**

| Row | Sender | Receiver |
|---|---|---|
| 1 | `1 1 0 1` | `1 1 0 1` |
| 2 | `1 0 1 0` | `1 0 1 0` |
| 3 | `0 1 0 1` | `0 1 0 1` |
| 4 | `1 1 0 1` | `1 1 0 1` |
| 1s per column (C1–C4) | `3 3 1 3` | `3 3 1 3` |
| LRC (even) | `1 1 1 1` (sent) | `1 1 1 1` (recomputed) |

Sender LRC `1111` = recomputed LRC `1111` → **no error** — the received block is identical to the sent block.

**Result**

| Sr No | Sender LRC | Receiver's recomputed LRC | Mismatch | Result |
|---|---|---|---|---|
| 1 | `0100` | `0110` | column 3 | Error detected |
| 2 | `0110` | `0100` | column 3 | Error detected |
| 3 | `1111` | `1111` | none | No error |

So LRC demonstrates an error in blocks 1 and 2; block 3 was received exactly as sent, so there is no error to detect.

**Notes**

- LRC shows *which column* is wrong but not which row, so on its own it only detects the error. Adding a VRC bit to every row (two-dimensional parity) locates the bit: in block 1 the parity of row 3 also changes (`1111` → `1101`), and row 3 × column 3 is exactly the flipped bit.
- **Limitation:** if two bits in the *same column* flip, that column's count of `1`s stays even and LRC misses the error.

**Summary:** Even-parity LRC computed column by column gives sender LRCs `0100`, `0110` and `1111`; the receiver recomputes `0110`, `0100` and `1111`, so column 3 mismatches in blocks 1 and 2 (error detected) while block 3 matches (no error).

---

### Q6. Hamming code — single-bit error detection and correction

**Definition**

The **Hamming code** is an error-correcting code, devised by R. W. Hamming, that adds redundant (parity) bits to the data at the bit positions that are powers of 2 (1, 2, 4, 8, …). Each parity bit gives even (or odd) parity over a particular group of positions, so the receiver can not only detect a single-bit error but also find its position and correct it.

**Role in error detection and correction**

- **Detection:** the receiver recomputes every parity check on the received word; if any check fails, an error has occurred.
- **Correction:** the results of the checks, written as a binary number (the **syndrome**), give the position of the wrong bit, and the receiver flips that bit. Syndrome 0 means no error.
- This is **forward error correction** — the receiver corrects the error itself, without asking the sender to retransmit.

**Number of redundant bits**

For m data bits, the number of redundant bits r is the smallest value that satisfies

2^r ≥ m + r + 1

and the codeword has n = m + r bits. The r checks must be able to point to any of the n positions or report "no error" — n + 1 possibilities.

| Data bits m | Redundant bits r | Codeword n = m + r | Check |
|---|---|---|---|
| 4 | 3 | 7 | 2^3 = 8 ≥ 4 + 3 + 1 = 8 |
| 7 | 4 | 11 | 2^4 = 16 ≥ 7 + 4 + 1 = 12 |
| 10 | 4 | 14 | 2^4 = 16 ≥ 10 + 4 + 1 = 15 |

**Bit positions (class convention)**

Positions are numbered from the **right** (position 1 = rightmost bit). Parity bits sit at positions 1, 2, 4 (and 8, 16, … in longer words); data bits fill the remaining positions, with the leftmost data bit at the highest position. For the (7,4) code:

```
Position:   7    6    5    4    3    2    1
Bit:        D4   D3   D2   P4   D1   P2   P1
```

Parity bits are named here by their position (P1, P2, P4, P8). The slides number them in order, so the slides' **P3** is the bit at position 4 (P4 here).

**Parity-bit coverage**

Each parity bit checks every position whose binary number has a 1 in that parity bit's place:

| Position | Binary | Checked by |
|---|---|---|
| 1 | 001 | P1 |
| 2 | 010 | P2 |
| 3 | 011 | P1, P2 |
| 4 | 100 | P4 |
| 5 | 101 | P1, P4 |
| 6 | 110 | P2, P4 |
| 7 | 111 | P1, P2, P4 |

| Parity bit | Positions checked | Even-parity rule |
|---|---|---|
| P1 | 1, 3, 5, 7 | P1 = D1 ⊕ D2 ⊕ D4 |
| P2 | 2, 3, 6, 7 | P2 = D1 ⊕ D3 ⊕ D4 |
| P4 | 4, 5, 6, 7 | P4 = D2 ⊕ D3 ⊕ D4 |

In longer words the pattern continues — P1 also checks 9, 11, 13, …, and P8 checks positions 8–15 (see Q7).

**Worked example (class example)**

*Encoding:* data `1010` (m = 4 → r = 3, a (7,4) code). D4 = 1, D3 = 0, D2 = 1 and D1 = 0 go to positions 7, 6, 5 and 3.

| Position | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|---|---|
| Bit | D4 | D3 | D2 | P4 | D1 | P2 | P1 |
| Value | 1 | 0 | 1 | ? | 0 | ? | ? |

| Parity bit | Data positions | Data bits | Number of 1s | Parity (even) |
|---|---|---|---|---|
| P1 | 3, 5, 7 | 0, 1, 1 | 2 | 0 |
| P2 | 3, 6, 7 | 0, 0, 1 | 1 | 1 |
| P4 | 5, 6, 7 | 1, 0, 1 | 2 | 0 |

Transmitted codeword (positions 7 … 1): `1010010`.

*Detection and correction:* suppose `1110010` is received (bit 6 has flipped). The receiver recomputes each check over its whole group, parity bit included:

| Check | Positions | Received bits | Number of 1s | Result |
|---|---|---|---|---|
| c1 | 1, 3, 5, 7 | 0, 0, 1, 1 | 2 | 0 |
| c2 | 2, 3, 6, 7 | 1, 0, 1, 1 | 3 | 1 |
| c4 | 4, 5, 6, 7 | 0, 1, 1, 1 | 3 | 1 |

Syndrome (c4 c2 c1) = `110` = 6 → bit 6 is wrong. Flipping bit 6 turns `1110010` back into `1010010`, and the data `1010` is recovered. Had the word arrived unchanged, all three checks would give 0 (syndrome `000`, no error).

The slides reach the same syndrome another way: recompute each parity bit from the received data bits and compare it with the received parity bit — P1: 0 vs 0 → 0; P2: 0 vs 1 → 1; P4: 1 vs 0 → 1 → `110` = 6.

**Hamming distance and d_min**

- The **Hamming distance** d(x, y) between two words is the number of bit positions in which they differ, i.e. the number of `1`s in x ⊕ y. Example: d(`10101`, `11110`) = 3, because `10101` ⊕ `11110` = `01011`.
- The **minimum Hamming distance** d_min is the smallest Hamming distance between any two codewords of a code.
- A code detects up to **d_min − 1** errors (d_min = s + 1 to detect s errors) and corrects up to **⌊(d_min − 1)/2⌋** errors (d_min = 2t + 1 to correct t errors). Example: d_min = 9 → detects 8 errors, corrects 4.
- Every Hamming code has **d_min = 3**, so it corrects any single-bit error or, if used only for detection, detects any 2-bit error. It cannot do both at once: a 2-bit error gives a non-zero syndrome that points to a wrong bit. Adding one overall parity bit (extended Hamming code, d_min = 4) gives single-error correction with double-error detection.
- **Note — the slides' formula:** the slides give d_min = n − k + 1 for an (n, k) Hamming code, so their exercise "(11,7) Hamming code" works out as d_min = 11 − 7 + 1 = 5 → detects 4 errors and corrects 2; use that working if a question asks for the slide formula. Strictly, n − k + 1 is only an upper limit (the Singleton bound): every Hamming code has d_min = 3 — for (7,4), data `0000` → `0000000` and data `0001` → `0000111` differ in only 3 bits — so a Hamming code really detects 2 errors or corrects 1.

**Summary:** Hamming code places r parity bits (2^r ≥ m + r + 1) at positions 1, 2, 4, 8, …, each giving even parity over the positions whose binary number contains it; the receiver's recomputed checks form a syndrome equal to the position of a single-bit error (e.g. `1110010` → syndrome `110` = 6 → corrected `1010010`), and with d_min = 3 it corrects any 1-bit error.

---

### Q7. Constructing the Hamming codeword for 1010010101

**Convention (class):** positions are numbered from the right (position 1 = rightmost bit); parity bits sit at positions 1, 2, 4 and 8; the data bits fill the other positions with the leftmost data bit at the highest position, so the codeword reads D10 … P8 … D1 P2 P1. Even parity is used.

**Step 1 — Number of parity bits**

m = 10 data bits.

- r = 3: 2^3 = 8 ≥ 10 + 3 + 1 = 14? No.
- r = 4: 2^4 = 16 ≥ 10 + 4 + 1 = 15? Yes.

So r = 4 parity bits and n = 10 + 4 = 14 bits — a (14,10) Hamming code.

**Step 2 — Place the data bits**

Parity positions: 1, 2, 4, 8. Data positions, from the top: 14, 13, 12, 11, 10, 9, 7, 6, 5, 3. The data `1010010101` is written into them from left to right:

| Position | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bit | D10 | D9 | D8 | D7 | D6 | D5 | P8 | D4 | D3 | D2 | P4 | D1 | P2 | P1 |
| Value | 1 | 0 | 1 | 0 | 0 | 1 | ? | 0 | 1 | 0 | ? | 1 | ? | ? |

(In the slides' numbering, P1, P2, P4 and P8 are called P1, P2, P3 and P4.)

**Step 3 — Calculate the parity bits (even parity)**

| Parity bit | Checks positions | Data bits at those positions | Number of 1s | Parity bit value |
|---|---|---|---|---|
| P1 | 3, 5, 7, 9, 11, 13 | 1, 0, 0, 1, 0, 0 | 2 (even) | 0 |
| P2 | 3, 6, 7, 10, 11, 14 | 1, 1, 0, 0, 0, 1 | 3 (odd) | 1 |
| P4 | 5, 6, 7, 12, 13, 14 | 0, 1, 0, 1, 0, 1 | 3 (odd) | 1 |
| P8 | 9, 10, 11, 12, 13, 14 | 1, 0, 0, 1, 0, 1 | 3 (odd) | 1 |

**Step 4 — Hamming codeword**

| Position | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bit | D10 | D9 | D8 | D7 | D6 | D5 | P8 | D4 | D3 | D2 | P4 | D1 | P2 | P1 |
| Value | 1 | 0 | 1 | 0 | 0 | 1 | **1** | 0 | 1 | 0 | **1** | 1 | **1** | **0** |

**Hamming codeword = `10100110101110`**

**Check:** recomputing the four checks on `10100110101110`, each group now including its own parity bit, finds 2, 4, 4 and 4 `1`s in the groups of P1, P2, P4 and P8 — all even, so the syndrome is 0.

**Note:** if positions are numbered from the left instead (position 1 = leftmost), the same method gives the codeword `10110101010101`.

**Summary:** m = 10 needs r = 4 parity bits (2^4 = 16 ≥ 15), giving a 14-bit code; with positions numbered from the right and even parity, P1 = 0, P2 = 1, P4 = 1 and P8 = 1, so the Hamming codeword is `10100110101110`.

---

### Q8. Locating and correcting the error in 01100101001011

**Convention (class):** positions are numbered from the right (position 1 = rightmost bit); parity bits are at positions 1, 2, 4 and 8; even parity is used; the syndrome is read as c8 c4 c2 c1.

**Step 1 — Write the received bits against their positions**

The word has 14 bits, so r = 4 (parity bits at 1, 2, 4, 8) and m = 10.

| Position | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bit | D10 | D9 | D8 | D7 | D6 | D5 | P8 | D4 | D3 | D2 | P4 | D1 | P2 | P1 |
| Received | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 1 |

**Step 2 — Even-parity checks (each group includes its parity bit)**

| Check | Positions | Received bits | Number of 1s | Result |
|---|---|---|---|---|
| c1 | 1, 3, 5, 7, 9, 11, 13 | 1, 0, 0, 1, 1, 0, 1 | 4 (even) | 0 |
| c2 | 2, 3, 6, 7, 10, 11, 14 | 1, 0, 0, 1, 0, 0, 0 | 2 (even) | 0 |
| c4 | 4, 5, 6, 7, 12, 13, 14 | 1, 0, 0, 1, 1, 1, 0 | 4 (even) | 0 |
| c8 | 8, 9, 10, 11, 12, 13, 14 | 0, 1, 0, 0, 1, 1, 0 | 3 (odd) | 1 |

**Step 3 — Syndrome**

Syndrome = c8 c4 c2 c1 = `1000` = 8 → the bit at **position 8** is in error. Position 8 is the parity bit **P8**, so only a check bit was corrupted; the data bits arrived intact.

**Step 4 — Correct the codeword**

Flip bit 8 (0 → 1):

| Position | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Received | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 1 |
| Corrected | 0 | 1 | 1 | 0 | 0 | 1 | **1** | 1 | 0 | 0 | 1 | 0 | 1 | 1 |

**Corrected codeword = `01100111001011`**

Recomputing the checks on the corrected word gives c8 c4 c2 c1 = `0000` (the c8 group now holds four `1`s). The data bits (positions 14, 13, 12, 11, 10, 9, 7, 6, 5, 3) are `0110011000`, the same as received.

**Note:** with positions numbered from the left, the syndrome comes out as 7 (a data bit), and flipping it gives the same corrected codeword `01100111001011`, because position 8 from the right is position 7 from the left in a 14-bit word.

**Summary:** Recomputing the even-parity checks on `01100101001011` (positions 14 … 1) gives c8 c4 c2 c1 = `1000` = 8, so bit 8 — the parity bit P8 — is in error; flipping it gives the corrected codeword `01100111001011`, and the data `0110011000` is unaffected.

---

### Q9. Stop-and-Wait protocol

**Definition**

Stop-and-Wait is the simplest flow-control protocol of the data link layer: the sender transmits **one frame**, then **stops and waits** for an acknowledgment (ACK) from the receiver before sending the next frame. Because the receiver sends the ACK only when it is ready, it controls how fast the sender transmits (flow control).

In the slides' taxonomy, plain Stop-and-Wait is a protocol for a **noiseless channel** — flow control but no error control. For a **noisy channel** it is extended to **Stop-and-Wait ARQ** (Automatic Repeat reQuest):

**Stop-and-Wait ARQ = Stop-and-Wait + timeout timer + sequence numbers**

**Working principle (Stop-and-Wait ARQ)**

1. The sender numbers the frame (0 or 1), keeps a **copy**, sends it and **starts a timer**.
2. The receiver checks the frame for errors (e.g. with a CRC). A damaged frame is silently discarded.
3. A correct frame with the expected number is delivered to the network layer, and an ACK is returned carrying the number of the **next frame expected** (frame 0 → ACK 1, frame 1 → ACK 0).
4. If the ACK arrives before the timer expires, the sender stops the timer, discards the copy and sends the next frame.
5. If the timer expires (frame lost or damaged, or ACK lost), the sender **retransmits the copy**.
6. A frame with the wrong number is a **duplicate** (its ACK was lost): the receiver discards it but sends the ACK again.

**Diagram — Stop-and-Wait ARQ timeline**

```
        Sender                                  Receiver
          |                                        |
          |----- Frame 0 ------------------------->|  expects 0: accept,
          |<---------------------------- ACK 1 ----|  deliver, expect 1
          |                                        |
  timer   |----- Frame 1 -------------X            |  frame 1 lost
  starts  |       ... no ACK arrives ...           |
  timeout |----- Frame 1 (copy resent) ----------->|  expects 1: accept,
          |<---------------------------- ACK 0 ----|  deliver, expect 0
          |                                        |
          |----- Frame 0 ------------------------->|  accept, expect 1
          |              X-------------- ACK 1 ----|  ACK lost
  timeout |----- Frame 0 (copy resent) ----------->|  expects 1, got 0:
          |<---------------------------- ACK 1 ----|  duplicate - discard
          v                                        v  it, send ACK again
```

**Why the sequence numbers 0/1 are needed**

- When an ACK is lost, the sender times out and resends the same frame. Without numbers the receiver would accept it twice (duplicate data).
- With a 1-bit number the receiver knows which frame it expects next, so it can tell a new frame from a copy. Two numbers (counting modulo 2) are enough because only one frame is outstanding at a time.
- Numbered ACKs also solve the slides' "delayed ACK" problem: a late ACK carries an old number and is ignored instead of being taken as the ACK of a newer frame.

**Efficiency (link utilization)**

Let Tt = transmission time of a frame = frame length L ÷ bandwidth B, and Tp = propagation time = distance ÷ signal speed. Only one frame is sent per cycle of Tt + 2Tp (ignoring the ACK's own transmission time and processing time):

**U = Tt / (Tt + 2Tp) = 1 / (1 + 2a)**, where **a = Tp / Tt**

*Worked example:* B = 1 Mbps, L = 1000 bits, Tp = 10 ms (about 2000 km of fiber).

- Tt = 1000 bits ÷ 10^6 bps = 1 ms, so a = 10 ms ÷ 1 ms = 10.
- U = 1 / (1 + 2 × 10) = 1/21 ≈ 0.048 — only **4.8%** of the link is used (about 47.6 kbps of the 1 Mbps).
- On a 1 km LAN at 10 Mbps with the same frame (Tp = 5 μs, Tt = 100 μs, a = 0.05), U = 1/1.1 ≈ 91%. Stop-and-Wait is acceptable only when a is small.

**Advantages**

- Very simple to implement; each side needs a buffer for only one frame.
- Built-in flow control — the receiver paces the sender through its ACKs.
- Needs only 1-bit sequence numbers.

**Limitations**

1. **Poor utilization when a is large** — on long, fast or satellite links the sender sits idle for 2Tp after every frame; there is no pipelining (slides).
2. Throughput is at most one frame per round trip, however high the bandwidth.
3. **Without a timer and sequence numbers** (plain Stop-and-Wait), a lost frame or lost ACK leaves both sides waiting forever, and a delayed ACK can be mistaken for the ACK of another frame — the three problems listed on the slides.
4. **Timeout choice is critical** — too short causes needless duplicates ("the timeout fires too soon"); too long slows recovery after a loss.
5. Every frame needs its own ACK, and every loss costs a whole timeout period, which is wasteful on noisy links.

**Summary:** Stop-and-Wait sends one frame and waits for its ACK; with a timer and 0/1 sequence numbers (Stop-and-Wait ARQ) it recovers lost frames and ACKs and rejects duplicates, but its utilization U = 1 / (1 + 2a) is very low on long or fast links.

---

### Q10. Sliding Window protocol

**Definition**

A sliding window protocol lets the sender transmit **several frames — up to the window size W — before it receives an acknowledgment**. Every frame carries a sequence number; with an m-bit sequence-number field the numbers run from 0 to 2^m − 1 and then repeat (modulo 2^m). The **window** is the range of sequence numbers the sender may send without waiting, and it **slides forward** as acknowledgments arrive.

As the slides put it:

- Send multiple frames at a time.
- The number of frames to be sent is based on the window size.
- Each frame is numbered → sequence number.

The two noisy-channel ARQ protocols built on it are **Go-Back-N ARQ** (Q11) and **Selective-Reject (Selective Repeat) ARQ** (Q12). Stop-and-Wait is the special case W = 1.

**Diagram — sender window (W = 4, 3-bit sequence numbers 0–7)**

```
                  Sf      Sn
                   |       |
                   v       v
     +---+---+---+---+---+---+---+---+---+---+---+
 ... | 5 | 6 | 7 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | ...
     +---+---+---+---+---+---+---+---+---+---+---+
                 |<--- W = 4 --->|
                 |       |       |
      sent and   | sent, | can   |  cannot be sent
      ACKed      | not   | be    |  until the window
                 | ACKed | sent  |  slides
```

- **Sf** = first outstanding (unacknowledged) frame; **Sn** = next frame to send.
- When the ACK for frame 0 arrives, Sf moves to 1 and the right edge moves to 4 — the window **slides** one slot and frame 4 may now be sent.
- The receiver keeps its own window of the frame numbers it will accept: size 1 in Go-Back-N, size W in Selective-Reject.

**Diagram — why pipelining helps (link of Q9: Tt = 1 ms, Tp = 10 ms, a = 10)**

The ACK for F0 returns at t = Tt + 2Tp = 21 ms.

```
  time (ms)   0     1     2     3     4    //   21    22    23
              |     |     |     |     |         |     |     |
  W = 1       [ F0 ] idle: waiting for ACK      [ F1 ] idle ...
  (S&W)
  W = 4       [ F0 ][ F1 ][ F2 ][ F3 ] idle     [ F4 ][ F5 ] ...
  W >= 21     [ F0 ][ F1 ][ F2 ][ F3 ][...F20]  [F21 ][F22 ] ...
```

**Efficiency**

The first ACK comes back after Tt + 2Tp, i.e. after (1 + 2a) frame times, and in that time the sender can transmit W frames:

- If **W ≥ 1 + 2a**, the first ACK arrives before the window is used up, so the sender never stops: **U = 1 (100%)**.
- If **W < 1 + 2a**, the sender sends W frames and then waits: **U = W / (1 + 2a)**.

**U = min(1, W / (1 + 2a))** — with W = 1 this reduces to Stop-and-Wait's 1 / (1 + 2a).

*Worked example* (same link, 1 + 2a = 21):

| Window W | Utilization U | Gain over Stop-and-Wait |
|---|---|---|
| 1 (Stop-and-Wait) | 1/21 ≈ 4.8% | — |
| 4 | 4/21 ≈ 19% | 4 times |
| 7 (largest Go-Back-N window with 3-bit numbers) | 7/21 ≈ 33% | 7 times |
| 21 or more | 100% | link kept full |

A window of 21 needs at least 5-bit sequence numbers with Go-Back-N (largest window 2^5 − 1 = 31).

**How it improves efficiency compared with Stop-and-Wait**

1. **Pipelining** — several frames are in flight at once, so the link is not idle during the round-trip delay ("pipelining improves the efficiency of the transmission" — slides).
2. **Utilization grows W times**, up to 100% once W ≥ 1 + 2a ("keeping the pipe full").
3. **Cumulative ACKs** — one ACK can acknowledge several frames, so fewer ACK frames are needed and a lost ACK is covered by the next one.
4. **Piggybacking** — in two-way traffic the ACK travels inside a data frame going the other way (slides), saving bandwidth.
5. **Flow control is kept** — the receiver sizes the window to its buffer space and can hold back ACKs to stop the sender.

**Comparison**

| Basis | Stop-and-Wait | Sliding Window |
|---|---|---|
| Frames outstanding | 1 | Up to W |
| Sequence numbers | 0 and 1 | 0 to 2^m − 1 (m-bit field) |
| Utilization | 1 / (1 + 2a) | min(1, W / (1 + 2a)) |
| Pipelining | No | Yes |
| Acknowledgments | One per frame | Cumulative, can be piggybacked |
| Buffers | One frame at each end | W frames at the sender (and at the receiver in Selective-Reject) |
| Complexity | Very simple | Higher — windows, timers, retransmission rules |
| Suitable for | Short links (small a) | Long or high-speed links (large a) |
| Examples | TFTP, simple half-duplex links | HDLC, TCP |

**Limitations**

- The sender must buffer up to W unacknowledged frames.
- The window is limited by the sequence-number field: at most 2^m − 1 for Go-Back-N and 2^(m−1) for Selective-Reject.
- Error recovery is more complex — the protocol must decide which frames to resend (Q11, Q12).

**Summary:** Sliding window lets the sender pipeline up to W numbered frames before an ACK and slides the window forward as cumulative or piggybacked ACKs arrive, raising utilization from 1 / (1 + 2a) to min(1, W / (1 + 2a)) — 100% once W ≥ 1 + 2a.

---

### Q11. Go-Back-N ARQ

**Definition**

Go-Back-N ARQ is a sliding-window error-control protocol in which the sender may have up to **N unacknowledged frames** outstanding ("N is the sender window size" — slides), while the receiver accepts frames **only in order** (receiver window = 1). If a frame is lost or damaged, the receiver discards it and every frame after it; when the sender's timer expires, the sender **goes back** to that frame and retransmits it **and all frames sent after it**.

Key points from the slides:

- It uses pipelining — the sender can send several frames before the ACK for the first one arrives.
- Frames are numbered sequentially, modulo 2^m (m = bits in the sequence-number field).
- The number of frames that can be sent depends on the sender's window size.
- If the ACK of a frame is not received within the agreed time, all frames in the current window are retransmitted.

**Working**

*Sender*

- Keeps a copy of every outstanding frame, from **Sf** (first outstanding) to **Sn − 1** (Sn = next to send), and may send while fewer than N frames are outstanding.
- Runs a timer for the oldest outstanding frame.
- **ACK n** is cumulative — it means "all frames up to n − 1 received, next expected is n". The sender purges those frames and slides the window (Sf = n).
- **On timeout**: resends every outstanding frame, from Sf up to Sn − 1.

*Receiver* (window size 1; **Rn** = number of the next frame expected)

- Correct frame numbered Rn → deliver it to the network layer, set Rn = Rn + 1 and send ACK Rn.
- Damaged or out-of-order frame → discard it; nothing is buffered. (In HDLC the receiver can also send a REJ frame to start the go-back before the timer expires.)

**Example — N = 4, 3-bit sequence numbers, frame 2 lost**

```
        Sender                                  Receiver
    (window W = 4)                           (window 1, expects Rn)
          |                                        |
          |---- F0 ------------------------------->|  Rn = 0: accept, Rn = 1
          |---- F1 ------------------------------->|  Rn = 1: accept, Rn = 2
          |---- F2 ----------X                     |  F2 lost
          |---- F3 ------------------------------->|  Rn = 2, got F3: discard
          |<---------------------------- ACK 1 ----|
          |---- F4 ------------------------------->|  got F4: discard
          |<---------------------------- ACK 2 ----|
          |---- F5 ------------------------------->|  got F5: discard
          |  window 2..5 full, no ACK 3            |
timeout   |---- F2 (go back to 2) ---------------->|  Rn = 2: accept, ACK 3
of F2     |---- F3 ------------------------------->|  accept, ACK 4
          |---- F4 ------------------------------->|  accept, ACK 5
          |---- F5 ------------------------------->|  accept, ACK 6
          v                                        v
```

- F0 and F1 are accepted; F2 is lost, so F3, F4 and F5 arrive **out of order** and are discarded even though they are correct.
- ACK 1 and ACK 2 slide the window to frames 2–5. All four are sent, so the sender must wait; no ACK 3 arrives and the timer for F2 expires.
- The sender **goes back to 2** and resends F2, F3, F4 and F5 — four frames sent again to recover one lost frame.
- If an **ACK** is lost instead (the case animated on the slides), a later cumulative ACK normally covers it. If none arrives before the timeout, the sender again resends the whole window and the receiver discards the duplicates.

**Window sizes — sender window ≤ 2^m − 1, receiver window = 1**

The slides' example with m = 2 (sequence numbers 0, 1, 2, 3) shows why the send window must be **less than 2^m**:

| Step | W = 3 (less than 2^m) | W = 4 (equal to 2^m) |
|---|---|---|
| Sender sends | 0, 1, 2 | 0, 1, 2, 3 |
| Receiver accepts all and now expects | 3 | 0 (numbers wrap around) |
| All ACKs lost; sender times out and resends | old frame 0 | old frame 0 |
| Receiver's decision | expects 3 → **correctly discards** it | expects 0 → **wrongly accepts** the duplicate as new data |

So with m-bit sequence numbers, **sender window ≤ 2^m − 1** (7 for m = 3, 127 for m = 7), and the **receiver window is always 1**.

**Advantages**

1. **Much better utilization than Stop-and-Wait** — pipelining gives U = min(1, N / (1 + 2a)) on an error-free link.
2. **Simple receiver** — a window of one frame, no buffering or reordering; frames are delivered in order as they arrive.
3. **Cumulative ACKs** — fewer ACK frames, a lost ACK is covered by a later one, and ACKs can be piggybacked on data frames.
4. **One timer** at the sender (for the oldest outstanding frame), as in the slides' algorithm.
5. **Larger window for the same sequence-number field** than Selective-Reject (2^m − 1 vs 2^(m−1)).
6. Works well on **low-error links**, where retransmissions are rare; HDLC supports it with the REJ frame.

**Disadvantages**

- A single error makes the sender resend up to N frames, wasting bandwidth — "Go-Back-N ARQ is inefficient on a noisy link" (slides).
- Correct frames that arrive out of order are thrown away.
- The larger the window (large a), the more frames are resent per error; the sender must also buffer N frames.

**Summary:** Go-Back-N pipelines up to N = 2^m − 1 frames with cumulative ACKs and an in-order receiver (window 1); a lost or damaged frame makes the sender go back and resend that frame and every frame after it, which is simple and efficient on clean links but wasteful on noisy ones.

---

### Q12. Selective-Reject ARQ vs Go-Back-N ARQ

**Definition**

Selective-Reject ARQ (called **Selective Repeat ARQ** on the slides) is a sliding-window error-control protocol in which **only the frames that are lost or damaged are retransmitted**. The receiver has a window as large as the sender's: it accepts correct frames that arrive **out of order**, **buffers** them, and hands them to the network layer in order once the missing frame arrives.

Why it is needed (slides):

- Go-Back-N ARQ is inefficient on a **noisy** link — frames are damaged more often, so many frames are resent, which consumes bandwidth and slows transmission.
- Selective Repeat resends **only the damaged frame**.
- It defines a **negative acknowledgment (NAK)** that reports the sequence number of a damaged frame before the timer expires.
- Correct frames are received and buffered.
- It is more efficient for noisy links, but the processing at the receiver is more complex.

**Working**

*Sender* (window Ssize = 2^(m−1))

- Sends frames while its window is not full and starts a **separate timer for each frame**.
- **NAK n** or the **timeout of frame n** → resends **only frame n**.
- **ACK n** (cumulative: frames up to n − 1 received) → purges those frames and slides the window.

*Receiver* (window Rsize = 2^(m−1); Rn = first frame not yet received)

- Accepts and **stores** any correct frame whose number lies inside its window.
- When a damaged frame arrives, or a later frame arrives while frame Rn is still missing, it sends **NAK Rn** (only once).
- When frame Rn arrives, it delivers Rn and every consecutive buffered frame, slides the window and sends one cumulative ACK.

**Example — same situation as Q11 (W = 4, 3-bit numbers, frame 2 lost)**

```
        Sender                                  Receiver
   (window 4, a timer                        (window 4, buffers
    for each frame)                          out-of-order frames)
          |                                        |
          |---- F0 ------------------------------->|  in order: deliver F0
          |---- F1 ------------------------------->|  in order: deliver F1
          |---- F2 ----------X                     |  F2 lost
          |---- F3 ------------------------------->|  out of order: buffer F3
          |<---------------------------- ACK 1 ----|
          |---- F4 ------------------------------->|  buffer F4
          |<---------------------------- ACK 2 ----|
          |---- F5 ------------------------------->|  buffer F5
          |<---------------------------- NAK 2 ----|  (sent when F3 arrived)
resend    |---- F2 ------------------------------->|  deliver F2, F3, F4, F5
F2 only   |<---------------------------- ACK 6 ----|  one cumulative ACK
          |---- F6 ------------------------------->|  window has moved on
          v                                        v
```

- To deliver F0–F5, Selective-Reject transmits **7 frames** (one resent); Go-Back-N transmitted **10** (four resent).
- If the NAK itself is lost, F2's own timer expires and still only F2 is resent.

**Window size — at most 2^(m−1)**

The sender's and receiver's windows must never overlap in sequence-number space, so **Ssize + Rsize ≤ 2^m**; with equal windows each is **≤ 2^(m−1)**. Example with m = 2 (numbers 0–3):

| Step | W = 2 (= 2^(m−1)) | W = 3 (more than 2^(m−1)) |
|---|---|---|
| Sender sends | 0, 1 | 0, 1, 2 |
| Receiver accepts all; its window becomes | {2, 3} | {3, 0, 1} |
| All ACKs lost; sender times out and resends | old frame 0 | old frame 0 |
| Receiver's decision | 0 is outside the window → **discarded** (correct) | 0 is inside the window → **accepted as new data** (error) |

**Efficiency comparison**

On an error-free link both protocols give U = min(1, W / (1 + 2a)). The difference appears when frames are lost. With P = probability that a frame is lost or damaged (Stallings' standard results):

| Protocol | U when W ≥ 1 + 2a | U when W < 1 + 2a |
|---|---|---|
| Go-Back-N | (1 − P) / (1 + 2aP) | W(1 − P) / ((1 + 2a)(1 − P + WP)) |
| Selective-Reject | 1 − P | W(1 − P) / (1 + 2a) |

For comparison, Stop-and-Wait ARQ gives U = (1 − P) / (1 + 2a).

*Example:* a = 10, large window (W ≥ 21). With P = 0.01, Selective-Reject gives U = 0.99 and Go-Back-N 0.99 / 1.2 ≈ 0.83 (Stop-and-Wait only ≈ 0.047). With P = 0.1, they give 0.90 and 0.30. Each error costs Go-Back-N about 1 + 2a frame times but costs Selective-Reject only one frame.

**Comparison — efficiency and complexity**

| Basis | Go-Back-N ARQ | Selective-Reject ARQ |
|---|---|---|
| Frames resent after an error | The lost frame **and all frames after it** (up to N) | **Only** the lost or damaged frame |
| Receiver window | 1 | Same as the sender's |
| Largest window, m-bit numbers | 2^m − 1 | 2^(m−1) |
| Out-of-order frames | Discarded | Buffered, delivered in order later |
| Receiver buffer | None | Up to W frames |
| Timers | One (oldest outstanding frame) | One per outstanding frame |
| Control frames | Cumulative ACK (REJ in HDLC) | ACK plus NAK (SREJ in HDLC) |
| Utilization on a noisy link | Lower — bandwidth wasted on resent frames | Higher — close to 1 − P |
| Sender logic | Simple — resend the whole window | Complex — track and resend individual frames |
| Receiver logic | Very simple | Complex — buffer, mark, reorder, send NAKs |
| Best suited to | Low error rates, small a | Noisy or long-delay links (wireless, satellite) |

**Advantages of Selective-Reject**

- Only lost or damaged frames are resent, so it gives the best throughput of the sliding-window schemes on noisy links and on links with a large bandwidth-delay product.
- Correct frames are never thrown away.

**Limitations of Selective-Reject**

- Receiver needs buffers for up to W frames plus reordering logic; the sender needs a timer per frame.
- Only half the sequence-number space can be used (2^(m−1)), so more sequence-number bits are needed for the same window.
- Frames that follow a gap wait in the buffer until the missing frame arrives, which delays delivery.

**Summary:** Selective-Reject ARQ resends only the lost or damaged frame (triggered by a NAK or its own timer) and buffers out-of-order frames, with both windows ≤ 2^(m−1); it uses bandwidth far better than Go-Back-N on noisy links — U ≈ 1 − P vs (1 − P) / (1 + 2aP) — at the cost of a more complex sender and receiver.

---

### Q13. HDLC protocol

**Definition**

**HDLC (High-Level Data Link Control)** is a **bit-oriented** data link layer protocol. It is an **ISO standard** developed from IBM's **SDLC (Synchronous Data Link Control)**. As the slides describe it:

- It embeds control information in each frame that lets devices **control data flow and correct errors**.
- Its role is to ensure that data is received **without loss or errors and in the correct order**.
- It works on **point-to-point and multipoint** links and uses **ARQ** (sliding window) for full-duplex communication.

**Station types**

| Station | Role |
|---|---|
| Primary | Controls the link — establishes and releases it and manages data flow; its frames are **commands** |
| Secondary | Works under the primary's control; its frames are **responses** |
| Combined | Acts as both primary and secondary; sends commands and responses |

**Link configurations**

- **Unbalanced** — one primary and one or more secondaries, point-to-point or multipoint.
- **Balanced** — two combined stations on a point-to-point link.

**Data transfer modes** (the slides call them "transfer models")

| Mode | Configuration | How it works |
|---|---|---|
| **NRM** — Normal Response Mode | Unbalanced: a primary with secondaries, point-to-point or multipoint | The primary sends commands; a secondary transmits only when the primary polls it (P bit) |
| **ABM** — Asynchronous Balanced Mode | Balanced: two combined stations, point-to-point | Either station can start transmitting at any time without permission — the most widely used mode |
| **ARM** — Asynchronous Response Mode | Unbalanced | A secondary may transmit without permission, but the primary keeps responsibility for line initialization, error recovery and logical disconnect; rarely used |

**Frame structure**

```
              |<---- header ----->|<-- data --->|<- trailer ->|
  +----------+---------+---------+-------------+-------------+----------+
  |   Flag   | Address | Control | Information |     FCS     |   Flag   |
  | 01111110 |         |         |  (payload)  |    (CRC)    | 01111110 |
  +----------+---------+---------+-------------+-------------+----------+
     8 bits     8 bits    8 bits     variable   16 or 32 bits   8 bits
```

| Field | Size | Purpose |
|---|---|---|
| Flag | 8 bits, `01111110` | Marks the beginning and end of every frame; keeps the receiver synchronized |
| Address | 8 bits (extendable) | Address of the **secondary** station — the destination of a command from the primary, the source of a response from a secondary |
| Control | 8 bits (16 in extended mode) | Frame type, sequence numbers and the P/F bit — used for flow and error control |
| Information | Variable | User data from the network layer (I-frames) or management data (some U-frames); absent in S-frames |
| FCS | 16 or 32 bits | Frame Check Sequence — a CRC (CRC-CCITT 16-bit or CRC-32) over the address, control and information fields, for error detection |
| Flag | 8 bits, `01111110` | Ends the frame |

**Frame types — identified by the first bits of the control field**

| Frame | First bit(s) | Purpose |
|---|---|---|
| **I-frame** (Information) | `0` | Carries user data; also carries a piggybacked ACK in N(R) |
| **S-frame** (Supervisory) | `10` | Error and flow control; has no information field |
| **U-frame** (Unnumbered) | `11` | Link management — set up, reset and release the link, report errors |

```
  bit         1   2   3   4   5   6   7   8
            +---+---+---+---+---+---+---+---+
  I-frame   | 0 |    N(S)   |P/F|    N(R)   |
            +---+---+---+---+---+---+---+---+
  S-frame   | 1 | 0 |   S   |P/F|    N(R)   |
            +---+---+---+---+---+---+---+---+
  U-frame   | 1 | 1 |   M1  |P/F|     M2    |
            +---+---+---+---+---+---+---+---+
```

- **N(S)** — send sequence number of this frame. **N(R)** — receive sequence number: the number of the next frame expected, i.e. an acknowledgment of all frames up to N(R) − 1. Both are 3 bits (window up to 7) or 7 bits in extended mode (window up to 127).
- **P/F** — *Poll* in a command from the primary (the secondary must respond); *Final* in a response from a secondary (last frame of its response).
- **S-frame codes** (2-bit S field, from the slides):

| S | Name | Meaning |
|---|---|---|
| `00` | RR — Receive Ready | Positive ACK up to N(R) − 1; ready for more I-frames |
| `10` | RNR — Receive Not Ready | ACK up to N(R) − 1, but stop sending (flow control) |
| `01` | REJ — Reject | Go-Back-N: resend everything from frame N(R) |
| `11` | SREJ — Selective Reject | Resend only frame N(R) |

- **U-frame commands and responses** (M1 and M2 bits) include SNRM / SABM / SABME (set the mode — NRM, ABM, extended ABM), DISC (disconnect), UA (unnumbered acknowledgment), RSET (reset sequence numbers) and FRMR (frame reject).

**Bit stuffing — data transparency**

The flag `01111110` must never appear between the two flags of a frame. So the sender inserts a `0` after every five consecutive `1`s in the frame contents, and the receiver deletes the `0` that follows five `1`s (see Q2). For example, data `01111110` is sent as `011111010`, and the slides' example `0001111111001111101000` is sent as `000111110110011111001000` (two stuffed `0`s). Any bit pattern can therefore be carried.

**Example — data transfer in ABM**

```
      Station A                                Station B
          |                                        |
          |---- U: SABM -------------------------->|  set up the link in ABM
          |<---------------------------- U: UA ----|  link accepted
          |---- I: N(S)=0, N(R)=0 ---------------->|  A sends data frame 0
          |---- I: N(S)=1, N(R)=0 ---------------->|  A sends data frame 1
          |<---------------- I: N(S)=0, N(R)=2 ----|  B's data + ACKs A's 0, 1
          |---- S: RR, N(R)=1 -------------------->|  A ACKs B's frame 0
          |---- U: DISC -------------------------->|  release the link
          |<---------------------------- U: UA ----|
          v                                        v
```

**Role in reliable communication**

1. **Framing and synchronization** — flags mark every frame, and bit stuffing keeps the flag pattern out of the data.
2. **Error detection** — the FCS (CRC) lets the receiver discard damaged frames.
3. **Error control (ARQ)** — N(S) numbers each frame; N(R) acknowledges frames (piggybacked in I-frames or sent in RR); REJ asks for Go-Back-N and SREJ for Selective-Reject retransmission; timers resend lost frames; sequence numbers detect duplicates and keep frames in order.
4. **Flow control** — a sliding window of up to 7 (or 127) frames; RNR stops the sender and RR lets it resume.
5. **Link management** — U-frames set up the link (SABM or SNRM, answered by UA), reset it, release it (DISC, answered by UA) and report errors (FRMR).
6. **Access control on multipoint lines** — in NRM the primary polls each secondary with the P bit, so only one secondary transmits at a time.
7. **Basis of many protocols** — LAPB (X.25), LAPD (ISDN) and the HDLC-like framing of PPP are derived from it.

**Summary:** HDLC is ISO's bit-oriented data link protocol (from IBM's SDLC); its frame is Flag (`01111110`) | Address | Control | Information | FCS | Flag, with I-, S- and U-frames told apart by the control field; primary, secondary and combined stations work in NRM, ABM or ARM, and flags with bit stuffing, CRC, N(S)/N(R) sequence numbers, RR/RNR/REJ/SREJ and U-frame link management make delivery error-free, in order and flow-controlled.

---

### Q14. Channel allocation methods — static and dynamic

**Definition**

In a broadcast network — a LAN, a wireless LAN, a satellite link — many stations share **one channel**. **Channel allocation** is the problem of deciding how that single channel is divided among the competing stations. It is the job of the **MAC (Medium Access Control) sublayer** of the data link layer. There are two approaches: **static (fixed)** and **dynamic** allocation.

**Classification**

```
                              Channel allocation
                                       |
                  +--------------------+-------------------+
                  |                                        |
           Static (fixed)                         Dynamic (on demand)
                  |                                        |
          +-------+-------+                    +-----------+-----------+
          |               |                    |                       |
         FDM             TDM             Random access         Controlled access
                                         (contention)          (collision-free)
                                         - ALOHA               - Reservation
                                         - CSMA                - Polling
                                         - CSMA/CD             - Token passing
                                         - CSMA/CA
```

**1. Static (fixed) channel allocation**

The channel's capacity is divided permanently into N fixed parts, one per user, whether or not that user has anything to send.

- **FDM (Frequency Division Multiplexing)** — the bandwidth is split into N frequency bands separated by guard bands; each user owns one band all the time. *Examples:* FM radio and TV broadcasting, cable TV channels, first-generation analog cellular.
- **TDM (Time Division Multiplexing)** — time is split into frames of N slots; each user owns one slot in every frame. *Examples:* T1/E1 digital telephone trunks, the 8 time slots of a GSM carrier.

*Works well when* there are a few users, each with steady, continuous traffic (e.g. voice calls): there is no contention and no collision, and each user gets a guaranteed share.

*Works badly for computer data, because:*

- Data traffic is **bursty** — an idle user's band or slot is wasted while busy users cannot borrow it.
- N is fixed — with more users than N some are refused; with fewer, capacity is wasted.
- **Delay is N times worse.** With capacity C bps, arrival rate λ frames/s and mean frame length 1/μ bits, the mean delay on one shared channel is T = 1 / (μC − λ). Splitting it into N subchannels (capacity C/N, arrivals λ/N each) gives T_N = 1 / (μC/N − λ/N) = N / (μC − λ) = **N × T**.
- *Example:* C = 100 Mbps, 1/μ = 10,000 bits, λ = 5000 frames/s → μC = 10,000 frames/s, so T = 1 / (10,000 − 5000) s = 200 μs; with N = 10 fixed subchannels, T_N = 2 ms.

**2. Dynamic channel allocation**

The channel is given to stations **on demand**: only stations that have data compete for it, and the whole capacity goes to whoever is active. This suits many users with bursty data traffic.

*Assumptions used to model dynamic allocation* (Tanenbaum):

1. **Station model (independent traffic)** — N independent stations generate frames at random (a Poisson process with rate λ); a station waits until its frame has been sent before generating the next.
2. **Single channel** — one channel carries all communication; every station can send and receive on it.
3. **Collision assumption** — two frames that overlap in time are garbled (a collision); all stations can detect collisions; collided frames are sent again; there are no other errors.
4. **Continuous or slotted time** — a frame may start at any instant, or only at the start of a time slot.
5. **Carrier sense or no carrier sense** — stations either can or cannot tell whether the channel is busy before they transmit.

*Methods of dynamic allocation*

| Class | Idea | Protocols | Examples |
|---|---|---|---|
| **Random access** (contention) | No station has priority; a station sends when it has data, collisions can happen, and collided frames are resent after a random wait | Pure and slotted ALOHA (Q15); CSMA — 1-persistent, non-persistent, p-persistent; CSMA/CD; CSMA/CA (Q16) | ALOHAnet, classic Ethernet (CSMA/CD), Wi-Fi (CSMA/CA) |
| **Controlled access** (collision-free) | Stations take turns — by reserving in advance, by being polled, or by holding a token — so frames never collide | Reservation (e.g. the bit-map protocol), polling, token passing | Token Ring (IEEE 802.5), FDDI, polling of secondaries in HDLC's NRM, Bluetooth (the central device polls the others) |

**Comparison**

| Basis | Static (fixed) allocation | Dynamic allocation |
|---|---|---|
| How the channel is shared | A fixed band or slot per user, permanently | On demand, only to stations with data |
| Techniques | FDM (FDMA), TDM (TDMA) | Random access (ALOHA, CSMA family), controlled access (reservation, polling, token passing) |
| Best suited to | Few users with steady traffic (voice) | Many users with bursty traffic (data) |
| Channel utilization | Wasted whenever a user is idle | High — capacity goes to active stations |
| Collisions | None | Possible in random access; none in controlled access |
| Delay | Predictable, but about N times higher for bursty traffic | Low at light load; grows with load (contention or waiting for a turn) |
| Number of users | Fixed (N) | Can vary |
| Complexity | Simple | Needs a MAC protocol |
| Examples | FM radio, cable TV, GSM time slots, T1/E1 lines | Ethernet, Wi-Fi, ALOHA, Token Ring |

**Summary:** Channel allocation decides how one shared broadcast channel is divided: static allocation (FDM, TDM) gives each of N users a fixed band or slot — simple and collision-free, but wasteful and N times slower for bursty traffic — while dynamic allocation hands the channel out on demand through random-access (ALOHA, CSMA) or controlled-access (reservation, polling, token passing) protocols.

---

### Q15. ALOHA — efficiency and applications

**Definition**

**ALOHA** is the earliest **random-access** protocol. It was developed in the early 1970s by Norman Abramson's group at the University of Hawaii (ALOHAnet) to connect terminals on different islands to a central computer over one shared radio channel. Its rule is simple: **a station transmits whenever it has a frame**. If two frames overlap, they collide and are destroyed; the senders notice because no acknowledgment comes back, wait a **random back-off time**, and transmit again.

**Pure ALOHA — working**

1. A station sends a frame as soon as it has one.
2. It waits for an ACK for one round-trip time (2 × the maximum propagation time).
3. If the ACK arrives, the frame was delivered; if not, the station assumes a collision.
4. It waits a random back-off time — e.g. R × Tfr, with R chosen at random from 0 to 2^K − 1 after the K-th attempt — and retransmits; after a maximum number of attempts (typically 15) it gives up.

**Vulnerable time — pure ALOHA**

Let **Tfr** be the time to transmit one frame. A frame A sent at time t is destroyed by any other frame that starts between t − Tfr and t + Tfr:

```
            B starts just after           C starts just before
            t - Tfr: hits A's start       t + Tfr: hits A's end
            +---------------+             +---------------+
            |       B       |             |       C       |
            +---------------+             +---------------+
                          +---------------+
                          |       A       |
                          +---------------+
  --------+---------------+---------------+-------------------> time
       t - Tfr            t            t + Tfr
          |<- vulnerable time = 2 x Tfr ->|
```

**Pure ALOHA vulnerable time = 2 × Tfr.**

**Slotted ALOHA**

Time is divided into **slots of length Tfr**, and a station may start sending **only at the beginning of a slot** (all stations share a common clock). A frame that becomes ready in the middle of a slot waits for the next one. Two frames can now collide only if they start in the same slot:

```
        slot k-1         slot k         slot k+1
  --+---------------+---------------+---------------+--> time
                    [====== A ======]                 A and B start in the
                    [====== B ======]                 same slot: collision
    [====== D ======]               [====== C ======] D and C cannot overlap A
                    |<---- Tfr ---->|
                    vulnerable time = Tfr
```

**Slotted ALOHA vulnerable time = Tfr.**

**Derivation of efficiency (throughput)**

*Assumptions*

- All frames have the same length, so each takes one frame time Tfr.
- There are very many stations, and the frames offered to the channel (new ones plus retransmissions) arrive as a **Poisson process**. **G** = mean number of frames offered per frame time (the offered load).
- **S** = throughput = mean number of frames *successfully* sent per frame time (0 ≤ S ≤ 1). S is the efficiency of the channel.

*Step 1 — Poisson probability.* In an interval of n frame times the mean number of frames offered is nG, so the probability of exactly k frames is

P(k) = (nG)^k × e^(−nG) / k!, and the probability of **no** frame is P(0) = e^(−nG).

*Step 2 — condition for success.* A frame gets through only if no other frame is offered during its vulnerable time, so **S = G × P0**, where P0 = probability of no other frame in the vulnerable time.

*Step 3 — pure ALOHA* (vulnerable time 2 frame times, n = 2):

P0 = e^(−2G), so **S = G × e^(−2G)**

*Step 4 — maximum.* dS/dG = e^(−2G) − 2G × e^(−2G) = e^(−2G)(1 − 2G) = 0 gives **G = 1/2**, and

**Smax = (1/2) × e^(−1) = 1/(2e) ≈ 0.184** — at best **18.4%** of the channel time carries successful frames.

*Step 5 — slotted ALOHA* (vulnerable time 1 frame time, n = 1):

P0 = e^(−G), so **S = G × e^(−G)**; dS/dG = e^(−G)(1 − G) = 0 gives **G = 1**, and

**Smax = 1 × e^(−1) = 1/e ≈ 0.368** — **36.8%**, twice pure ALOHA. At G = 1, about 36.8% of slots are empty, 36.8% carry exactly one frame (success) and 26.4% hold a collision.

*Worked example:* 200-bit frames on a 200 kbps channel, so Tfr = 200 / 200,000 s = 1 ms and the channel can carry at most 1000 frames/s.

| Frames offered per second | G | Pure ALOHA S = G × e^(−2G) | Successful frames/s | Slotted ALOHA S = G × e^(−G) | Successful frames/s |
|---|---|---|---|---|---|
| 250 | 0.25 | 0.152 | 152 | 0.195 | 195 |
| 500 | 0.5 | 0.184 (maximum) | 184 | 0.303 | 303 |
| 1000 | 1 | 0.135 | 135 | 0.368 (maximum) | 368 |

Successful frames/s = S × 1000 (equivalently, frames offered × P0). Some textbook examples instead multiply the offered frames by S (e.g. 500 × 0.184 = 92); that counts G twice — the correct figure is 184.

**Comparison**

| Basis | Pure ALOHA | Slotted ALOHA |
|---|---|---|
| Time | Continuous | Divided into slots of one frame time |
| When a station may send | At any time | Only at the start of a slot |
| Vulnerable time | 2 × Tfr | Tfr |
| Throughput | S = G × e^(−2G) | S = G × e^(−G) |
| Maximum throughput | 1/(2e) ≈ 0.184 at G = 0.5 | 1/e ≈ 0.368 at G = 1 |
| Synchronization | Not needed | All stations need a common clock |
| Collisions | Partial or complete overlap | Complete overlap only (same slot) |
| Delay at light load | Lowest — a frame is sent at once | A frame may wait up to one slot |

**Applications in modern wireless networks**

ALOHA survives wherever many devices send short, occasional messages and cannot coordinate or sense the channel first:

- **Cellular random access** — a phone's first message to the base station (initial access, call setup, a request for resources) goes on a random-access channel. GSM's RACH uses slotted ALOHA; LTE and 5G NR use the same idea on the PRACH — the phone sends a randomly chosen preamble in a random-access slot, and collisions are resolved in the following steps.
- **RFID** — a reader identifies many tags with **framed slotted ALOHA** (e.g. the "Q" anti-collision algorithm of EPC Gen2): each tag replies in a randomly chosen slot.
- **Satellite networks** — VSAT terminals send short requests in contention slots with slotted ALOHA (newer standards such as DVB-RCS2 use improved variants like CRDSA). Carrier sensing is useless here because a signal needs about a quarter of a second to go up to the satellite and back down.
- **IoT and LPWAN** — LoRaWAN (Class A) devices send uplink frames whenever they have data, i.e. pure ALOHA, and Sigfox works similarly; the low duty cycle keeps collisions rare and saves battery because devices never have to listen first.
- **Basis of CSMA in Wi-Fi and Ethernet** — CSMA is ALOHA plus carrier sensing (Q16), and the random back-off after a collision in Ethernet (CSMA/CD) and Wi-Fi (CSMA/CA) comes straight from ALOHA.

**Advantages**

- Extremely simple — no coordination, no carrier sensing, no central controller.
- Works even when stations cannot hear one another or the propagation delay is long.
- Lowest delay at light load (pure ALOHA sends at once).

**Limitations**

- Low maximum throughput — 18.4% (pure) or 36.8% (slotted).
- Unstable under heavy load: more collisions cause more retransmissions, which cause still more collisions.
- Slotted ALOHA needs clock synchronization among all stations.

**Summary:** In ALOHA a station sends whenever it has a frame and retransmits after a random back-off if no ACK comes; with Poisson traffic of G frames per frame time, pure ALOHA (vulnerable time 2 × Tfr) gives S = G × e^(−2G), at most 1/(2e) ≈ 18.4% at G = 0.5, and slotted ALOHA (vulnerable time Tfr) gives S = G × e^(−G), at most 1/e ≈ 36.8% at G = 1 — still the basis of random access in cellular RACH/PRACH, RFID, satellite and IoT uplinks, and of CSMA.

---

### Q16. CSMA protocols — persistent vs non-persistent

**Definition**

**CSMA (Carrier Sense Multiple Access)** is a random-access protocol based on **"listen before talk"**: a station first **senses the medium** (the carrier) and transmits only if the channel is **idle**. This avoids most of the collisions that ALOHA suffers, but not all of them. Because of propagation delay, a station may sense the channel idle although another station has already started sending and its signal has not reached it yet.

- **Vulnerable time = propagation time Tp** — the time a signal needs to travel from one end of the medium to the other.
- CSMA works best when **a = Tp / Tfr** is small (short medium, long frames).

**Persistence methods — what a station does after sensing the channel**

**1. 1-persistent CSMA**

The station senses the channel. If it is busy, the station **keeps sensing continuously**; the moment the channel becomes idle it **transmits immediately (with probability 1)**. After a collision it waits a random time and starts again.

```
     +-----------------+
     |  Sense channel  |<----+
     +--------+--------+     |
              |              |  busy: keep sensing
        +-----v-----+        |  continuously
        |   Idle?   |--------+
        +-----+-----+
              | idle
     +--------v--------+
     | Transmit at once|
     | (probability 1) |
     +-----------------+
```

**2. Non-persistent CSMA**

If the channel is idle, the station transmits immediately. If it is busy, the station **does not keep sensing**: it **waits a random time** and then senses again.

```
     +-----------------+
     |  Sense channel  |<--------------+
     +--------+--------+               |
              |                        |
        +-----v-----+  busy   +--------+--------+
        |   Idle?   |-------->| Wait a random   |
        +-----+-----+         | time            |
              | idle          +-----------------+
     +--------v--------+
     | Transmit at once|
     +-----------------+
```

**3. p-persistent CSMA** (for slotted channels, with a slot at least as long as the maximum propagation time)

The station senses until the channel is idle. Then it **transmits with probability p**, or with probability **q = 1 − p** it waits for the next slot and senses again. If that slot is idle it repeats the choice; if it is busy, the station acts as if a collision had occurred and backs off.

```
     +-----------------+
     |  Sense channel  |<--- busy: keep sensing until idle
     +--------+--------+
              | idle
     +--------v--------+                 idle
     | Draw random r,  |<---------------------------------+
     | 0 <= r < 1      |                                  |
     +--------+--------+                                  |
              |                                           |
        +-----v-----+  no (prob. q = 1 - p)     +---------+--------+
        |  r < p ?  |-------------------------->| Wait for the next|
        +-----+-----+                           | slot, sense again|
              | yes (prob. p)                   +---------+--------+
     +--------v--------+                                  | busy
     | Transmit frame  |                                  v
     +-----------------+                       act as if a collision
                                               occurred: back off and
                                               start again
```

**CSMA/CD — Collision Detection (classic Ethernet, IEEE 802.3)**

- Uses 1-persistent sensing, and the station **keeps listening while it transmits**.
- When it detects a collision it **stops at once** and sends a short **jam signal** so that every station notices the collision.
- It then waits using **binary exponential back-off**: after the n-th collision it waits K slot times, with K chosen at random from 0 to 2^min(n, 10) − 1 (one slot = 512 bit times = 51.2 μs at 10 Mbps), and gives up after 16 attempts.
- A frame must last at least one round trip (Tfr ≥ 2Tp) so the sender is still transmitting when the collision news returns — hence Ethernet's 64-byte (512-bit) minimum frame.

**CSMA/CA — Collision Avoidance (Wi-Fi, IEEE 802.11)**

- A wireless station cannot listen while it transmits, and hidden stations may not hear each other, so collisions cannot be detected reliably — they are **avoided** instead.
- The station waits until the channel has been idle for an interframe space (DIFS), then counts down a **random back-off** chosen from a **contention window**; the countdown pauses whenever the channel is busy. At zero it transmits.
- The receiver returns an **ACK** after a short interframe space (SIFS). No ACK means a collision: the contention window is doubled and the frame is resent.
- An optional **RTS/CTS** exchange reserves the channel and solves the hidden-station problem.

**Comparison — persistent vs non-persistent CSMA (performance)**

| Basis | 1-persistent | Non-persistent | p-persistent |
|---|---|---|---|
| Channel busy | Keeps sensing continuously | Waits a random time, then senses again | Keeps sensing until it is idle |
| Channel idle | Sends at once (probability 1) | Sends at once | Sends with probability p, else defers one slot |
| Idle channel time wasted | None | Can be high — the channel may sit idle while stations wait | Small |
| Collision probability | Highest — all stations waiting for a transmission to end send together | Low — random waits spread the stations out | Low; the smaller p, the lower |
| Delay at low load | Lowest | Higher — needless random waits | Moderate — may defer even when alone |
| Throughput at high load (a = 0.01) | Poor — peaks at S ≈ 0.53 near G = 1, then collapses | High — S ≈ 0.81 near G = 9 | High; rises as p is made smaller, at the cost of delay |

*Key points* (throughput figures are the standard Kleinrock–Tobagi results for a = Tp / Tfr = 0.01)

- **Low load — 1-persistent is better.** Few stations compete, so sending at once rarely collides and gives the smallest delay; non-persistent stations sometimes wait although the channel is already free. With a = 0.01 and G = 0.5, throughput is about 0.41 for 1-persistent and 0.33 for non-persistent.
- **High load — non-persistent is better.** In 1-persistent CSMA every station that became ready during a transmission waits for it to end and then all transmit together, so collisions become almost certain (S ≈ 0.04 at G = 5). Non-persistent stations come back at random times, so usually only one finds the channel idle (S ≈ 0.79 at G = 5), at the cost of longer delays. The two curves cross near G ≈ 1.1.
- **p-persistent is the compromise** — it spreads stations out like non-persistent without leaving the channel idle as long; a smaller p means fewer collisions but more delay.
- **All CSMA variants beat ALOHA** (maximum 0.184 / 0.368), but they degrade as a grows: with a = 0.1 the peaks fall to about 0.45 (1-persistent) and 0.52 (non-persistent).

**Summary:** CSMA senses the channel before sending (vulnerable time = Tp): 1-persistent sends as soon as the channel is idle — lowest delay at light load but many collisions at heavy load (peak S ≈ 0.53 for a = 0.01) — non-persistent waits a random time when the channel is busy — fewer collisions and higher throughput at heavy load (≈ 0.81) but more delay — and p-persistent sends with probability p as a compromise; Ethernet adds collision detection (CSMA/CD) and Wi-Fi collision avoidance (CSMA/CA).

---

## Quick revision sheet

| Q | One-line answer |
|---|---|
| U1-Q1 | PAN (a few meters, one person), LAN (building or campus), MAN (city), WAN (country or world — the Internet) |
| U1-Q2 | Bus (one backbone), star (central switch), ring (closed loop), mesh (many or all links), tree (hierarchy), hybrid (a mix) |
| U1-Q3 | Components: sender/receiver, transmission medium, NIC, switch, router, protocols; benefits: sharing, communication, central management, lower cost, scalability |
| U1-Q4 | ISO's seven layers — Physical, Data Link, Network, Transport, Session, Presentation, Application; data goes down at the sender and up at the receiver |
| U1-Q5 | Four layers — Application (HTTP, DNS), Transport (TCP, UDP), Internet (IP, ICMP), Network Access (Ethernet, Wi-Fi) |
| U1-Q6 | OSI = seven-layer, protocol-independent reference model; TCP/IP = four-layer practical Internet model (OSI's top three layers → Application, bottom two → Network Access) |
| U1-Q7 | Cables: twisted pair (cheap, LANs and phones), coaxial (shielded, cable TV), fiber optic (light, very high bandwidth, backbones) |
| U1-Q8 | Wireless: radio (Wi-Fi, mobile), microwave (line of sight), infrared (short range), satellite (wide coverage, high delay) |
| U1-Q9 | Guided: physical path, less interference, easier to secure, little mobility; unguided: air or space, mobility and coverage, more interference |
| U1-Q10 | Analog = continuous signal with infinite values (AM/FM radio, landline phone); digital = discrete levels/bits (Internet, 4G/5G, digital TV); digital wins on noise immunity, regeneration, error control, encryption and TDM, at the cost of more bandwidth and synchronization. |
| U1-Q11 | C = B × log2(1 + SNR), SNR(dB) = 10 × log10(SNR) — upper limit for a noisy channel (3 kHz line at 35 dB ≈ 34.9 kbps), unlike Nyquist's noiseless 2 × B × log2(L); it drives wider bandwidth, higher SNR, adaptive QAM and near-capacity error-correcting codes. |
| U1-Q12 | Encoding = bits → digital signal (unipolar, NRZ-L, NRZ-I, RZ, Manchester, Differential Manchester, bipolar AMI); modulation = bits vary a carrier's amplitude, frequency or phase (ASK, FSK, PSK, QAM) for band-pass channels such as radio. |
| U1-Q13 | FDM shares frequency — bands separated by guard bands, all sent at once (radio/TV, cable TV, 1G, ADSL); TDM shares time — slots in frames, synchronous or statistical (T1 = 24 × 64 kbps + 8 kbps = 1.544 Mbps, E1, GSM's 8 slots). |
| U1-Q14 | Circuit switching reserves a dedicated path (setup–transfer–teardown, PSTN); message switching stores and forwards whole messages; packet switching (datagram or virtual circuit) shares links by statistical multiplexing — the best utilization for bursty data (Internet). |
| U2-Q1 | Character stuffing: in character-oriented framing the sender puts `ESC` before every `FLAG` or `ESC` in the data and the receiver removes it — `A B FLAG C` → `FLAG A B ESC FLAG C FLAG`. |
| U2-Q2 | Bit stuffing: with flag `01111110` (HDLC), insert a `0` after every five consecutive 1s and delete it at the receiver — `011111101` → `0111110101`. |
| U2-Q3 | VRC = one parity bit per data unit (misses an even number of flipped bits); LRC = a parity row computed column by column over a block (e.g. `0100`), which also catches burst errors within a row. |
| U2-Q4 | Even VRC bits 1, 0, 0, 1; rows 1 and 2 fail the parity check (error detected), row 3 passes despite two flipped bits (VRC limitation), row 4 is error-free. |
| U2-Q5 | Sender LRCs `0100`, `0110`, `1111` vs receiver's `0110`, `0100`, `1111` → column 3 mismatch in blocks 1 and 2 (error detected); block 3 has no error. |
| U2-Q6 | Hamming code: parity bits at positions 1, 2, 4, 8 …, 2^r ≥ m + r + 1, syndrome = error position, d_min = 3 (corrects 1 bit); e.g. `1010` → `1010010`, received `1110010` → syndrome 6. |
| U2-Q7 | m = 10 → r = 4, n = 14; P1 = 0, P2 = 1, P4 = 1, P8 = 1 → codeword `10100110101110`. |
| U2-Q8 | Syndrome c8 c4 c2 c1 = `1000` = 8 → parity bit P8 is wrong → corrected codeword `01100111001011` (data `0110011000`). |
| U2-Q9 | Stop-and-Wait: send one frame, then wait for its ACK; Stop-and-Wait ARQ adds a timeout timer and 0/1 sequence numbers (resend on timeout, discard duplicates); U = 1 / (1 + 2a) with a = Tp / Tt — e.g. a = 10 → 1/21 ≈ 4.8%. |
| U2-Q10 | Sliding window: up to W numbered frames (0 to 2^m − 1) in flight, and the window slides on cumulative or piggybacked ACKs; U = min(1, W / (1 + 2a)) — W = 7, a = 10 → 33%; 100% once W ≥ 1 + 2a. |
| U2-Q11 | Go-Back-N: sender window ≤ 2^m − 1, receiver window 1, cumulative ACKs, one timer; a lost frame makes the receiver discard all later frames and the sender resend it and everything after it (W = 4, F2 lost → F2–F5 resent). |
| U2-Q12 | Selective-Reject (Selective Repeat): resend only the lost frame (on NAK/SREJ or its own timer); the receiver buffers out-of-order frames; both windows ≤ 2^(m−1); U ≈ 1 − P vs Go-Back-N's (1 − P) / (1 + 2aP) — more efficient but more complex. |
| U2-Q13 | HDLC: ISO bit-oriented protocol derived from SDLC; frame = Flag (`01111110`), Address, Control, Information, FCS (CRC-16/32), Flag; I- (`0`), S- (`10`: RR, RNR, REJ, SREJ) and U-frames (`11`); primary, secondary and combined stations; NRM, ABM, ARM; bit stuffing for transparency. |
| U2-Q14 | Channel allocation: static — a fixed FDM band or TDM slot per user (no collisions, but idle capacity is wasted and delay is N × T for bursty traffic); dynamic — on demand via random access (ALOHA, CSMA, CSMA/CD, CSMA/CA) or controlled access (reservation, polling, token passing). |
| U2-Q15 | ALOHA: send at any time, random back-off after a collision; with Poisson load G, pure S = G × e^(−2G) (vulnerable time 2 × Tfr), max 1/(2e) ≈ 0.184 at G = 0.5; slotted S = G × e^(−G) (vulnerable time Tfr), max 1/e ≈ 0.368 at G = 1; used in cellular RACH/PRACH, RFID, satellite and LoRaWAN uplinks. |
| U2-Q16 | CSMA (listen before talk, vulnerable time Tp): 1-persistent sends as soon as the channel is idle (lowest delay, but many collisions at high load, peak S ≈ 0.53 for a = 0.01); non-persistent waits a random time when busy (fewer collisions, S ≈ 0.81 at high load, more delay); p-persistent sends with probability p; CSMA/CD (Ethernet), CSMA/CA (Wi-Fi). |
