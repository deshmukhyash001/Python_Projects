# 🌀 Python TCP Load Balancer

A simple **TCP Load Balancer** built with Python. It uses a round-robin algorithm to distribute incoming client connections across multiple backend servers, with fault tolerance for unavailable servers.

---

## 📦 Features

- 🔁 Round-robin load balancing across backend servers
- 🛑 Skips unreachable backend servers (basic failover)
- 🔄 Bi-directional data forwarding between client and backend
- 🧵 Multi-threaded handling of traffic
- 🧹 Clean socket management

---

## 🏗️ Architecture

```text
  Client
    |
    v
+-----------+           +------------------+
| Load      |---------> | Backend Server 1 |
| Balancer  |---------> | Backend Server 2 |
| (Port 2000)|--------->| Backend Server 3 |
+-----------+           +------------------+
