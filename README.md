# Industrial Protocol Lab


A hands-on lab for learning industrial communication protocols from first principles, starting with **Modbus TCP** and expanding to SCADA networking and automation systems.

---

# Modbus TCP Lab

## Overview

This project is designed to build a deep understanding of the **Modbus TCP protocol** by implementing both Modbus servers and clients from scratch. Rather than relying on higher-level SCADA software, the focus is on understanding the protocol itself—function codes, register maps, addressing, and communication between industrial devices.

The project serves as a foundation for future work involving:

- SCADA systems
- Industrial networking
- Distributed control systems
- Aerospace automation
- Additional industrial protocols (DNP3, EtherNet/IP, OPC UA, etc.)

---

## Objectives

- Learn the Modbus TCP protocol at the packet and register level.
- Simulate multiple industrial field devices.
- Build a Modbus client capable of polling and controlling devices.
- Understand how SCADA systems communicate with PLCs and remote devices.
- Create a foundation for larger industrial automation projects.

---

## System Architecture

```text
                 Ethernet / TCP/IP Network

        ┌───────────────────────────────────────┐
        │             Raspberry Pi 5            │
        │                                       │
        │  Modbus TCP Server #1 (Pump)          │
        │  Port 1502                            │
        │                                       │
        │  Modbus TCP Server #2 (Tank)          │
        │  Port 1503                            │
        │                                       │
        │  Modbus TCP Server #3 (Valve)         │
        │  Port 1504                            │
        └───────────────────────────────────────┘
                     ▲
                     │
             Modbus TCP Requests
                     │
                     ▼
        ┌───────────────────────────────────────┐
        │            MacBook Pro                │
        │                                       │
        │      Modbus TCP Client / Master       │
        │                                       │
        │ • Poll device registers               │
        │ • Read sensor values                  │
        │ • Toggle coils                        │
        │ • Write holding registers             │
        └───────────────────────────────────────┘
```

---

## Hardware

### Raspberry Pi 5

Acts as the **field device layer**, hosting multiple simulated Modbus TCP servers.

Each server represents an independent industrial device with its own register map.

Examples include:

- Pump controller
- Tank level sensor
- Valve actuator

---

### MacBook Pro

Acts as the **Modbus TCP client (SCADA master)**.

Responsibilities include:

- Polling all devices
- Reading register values
- Writing coils
- Updating holding registers
- Logging device data

---

## Technology Stack

| Component | Purpose |
|-----------|---------|
| Python | Primary programming language |
| pymodbus | Modbus TCP server/client implementation |
| Raspberry Pi 5 | Simulated field devices |
| MacBook Pro | Modbus client / SCADA master |
| FastAPI *(planned)* | REST API / control interface |
| InfluxDB *(planned)* | Time-series historian |
| Grafana *(planned)* | Dashboards and visualization |
| Ignition Perspective *(planned)* | Industrial HMI |

---

# Understanding Modbus TCP

Modbus TCP is one of the most widely used industrial communication protocols.

It operates over standard TCP/IP networks (default port **502**) and allows a client (master) to communicate with remote devices (servers/slaves).

---

## Data Types

### Coils

- 1-bit values
- Read/Write
- Typically represent outputs

Examples:

- Motor ON/OFF
- Valve OPEN/CLOSED

---

### Discrete Inputs

- 1-bit values
- Read-only

Examples:

- Limit switch
- Emergency stop
- Sensor status

---

### Holding Registers

- 16-bit values
- Read/Write

Examples:

- Temperature setpoint
- Motor speed
- Pressure threshold

---

### Input Registers

- 16-bit values
- Read-only

Examples:

- Temperature
- Pressure
- Tank level
- Voltage

---

## Function Codes

| Function | Description |
|----------|-------------|
| 01 | Read Coils |
| 02 | Read Discrete Inputs |
| 03 | Read Holding Registers |
| 04 | Read Input Registers |
| 05 | Write Single Coil |
| 06 | Write Single Holding Register |
| 15 | Write Multiple Coils |
| 16 | Write Multiple Holding Registers |

---

## Addressing

Each Modbus server owns its own register map.

In this lab, multiple devices are simulated by assigning each server a different TCP port.

Example:

| Device | Port |
|---------|------|
| Pump Controller | 1502 |
| Tank Sensor | 1503 |
| Valve Controller | 1504 |

---

# Project Roadmap

## Phase 1 — Basic Communication

- Single Modbus server
- Single holding register
- Read/write using Function Codes 03, 05, 06, and 16
- Verify communication between Raspberry Pi and MacBook

---

## Phase 2 — Dynamic Data

Replace static register values with simulated sensor behavior.

Examples:

- Tank level rising and falling
- Temperature changes
- Pressure fluctuations

---

## Phase 3 — Multiple Devices

Create multiple Modbus servers representing independent field devices.

Example devices:

- Pump controller
- Tank level sensor
- Valve actuator

Each device maintains its own register map.

---

## Phase 4 — SCADA Polling

Develop a polling application that:

- Connects to every device
- Reads registers periodically
- Logs values
- Detects communication failures

---

## Phase 5 — Device Control

Implement a control interface using either:

- Command-line interface
- FastAPI web application

Features:

- Toggle coils
- Modify setpoints
- Change holding register values

---

## Phase 6 — Historian & Visualization

Connect the Modbus network to:

- InfluxDB
- Grafana
- Ignition Perspective

This recreates the architecture of a real SCADA system while maintaining a complete understanding of the underlying protocol.

---

# Future Expansion

This repository is intended to grow into a comprehensive industrial communications lab.

Planned additions include:

- Modbus RTU
- DNP3
- EtherNet/IP
- OPC UA
- MQTT
- CAN Bus
- Industrial networking exercises
- SCADA architecture examples
- Protocol analyzers
- Packet captures (Wireshark)

---

## Repository Structure

```text
industrial-protocol-lab/
│
├── modbus-tcp/
│   ├── servers/
│   ├── client/
│   ├── register_maps/
│   ├── examples/
│   └── docs/
│
├── dnp3/                 (future)
├── ethernet-ip/          (future)
├── opc-ua/               (future)
├── mqtt/                 (future)
└── docs/
```

---

## Learning Goals

By the completion of this project, you should be comfortable with:

- Designing Modbus register maps
- Implementing Modbus TCP servers
- Building Modbus clients
- Reading and writing industrial data
- Understanding SCADA polling strategies
- Simulating industrial field devices
- Preparing for more advanced industrial protocols
- Building larger SCADA and automation systems from first principles
