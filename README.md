# Python Socket Programming Examples

A collection of Python socket programming examples demonstrating different server implementations and client connections. This project showcases basic socket communication patterns including single-client servers, multi-client servers using selectors, and interactive client applications.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Server](#basic-server)
  - [Multi-Client Server](#multi-client-server)
  - [Client](#client)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Examples](#examples)
- [Contributing](#contributing)

## 🔍 Overview

This project contains practical implementations of TCP socket programming in Python, featuring:

1. **Basic Server** (`server.py`) - A simple echo server that handles one client at a time
2. **Multi-Client Server** (`multi_server.py`) - An advanced server using selectors to handle multiple clients concurrently
3. **Interactive Client** (`client.py`) - A command-line client that can connect to either server

## ✨ Features

- **Single-client echo server** with basic TCP socket implementation
- **Multi-client server** using Python's `selectors` module for concurrent connections
- **Interactive client** with command-line interface
- **Non-blocking I/O** implementation in the multi-client server
- **Clean connection handling** with proper resource cleanup
- **Easy-to-use CLI commands** via project scripts

## 📦 Requirements

- Python 3.13+
- No external dependencies required (uses only Python standard library)

## 🚀 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd python-websockets
```

2. Install the project using uv (recommended) or pip:
```bash
# Using uv
uv sync

# Or using pip
pip install -e .
```

## 💻 Usage

### Basic Server

Start the basic echo server that handles one client at a time:

```bash
# Using the installed script
uv run server

# Or run directly
python servers/server.py
```

The server will start on `127.0.0.1:65432` and wait for a single client connection.

### Multi-Client Server

Start the advanced server that can handle multiple clients simultaneously:

```bash
# Using the installed script
uv run multi-server

# Or run directly
python servers/multi_server.py
```

This server uses selectors for efficient handling of multiple concurrent connections.

### Client

Connect to either server using the interactive client:

```bash
# Using the installed script
uv run client

# Or run directly
python clients/client.py
```

The client will prompt you to enter messages. Type 'exit' to disconnect.

## 📁 Project Structure

```
python-websockets/
├── pyproject.toml          # Project configuration and dependencies
├── README.md              # This file
├── uv.lock                # Lock file for dependencies
├── clients/
│   ├── client.py          # Interactive TCP client
│   └── __pycache__/
├── servers/
│   ├── server.py          # Basic single-client echo server
│   ├── multi_server.py    # Multi-client server with selectors
│   └── __pycache__/
└── scripts/               # Additional scripts (empty)
```

## 🔧 How It Works

### Basic Server (`server.py`)
- Creates a TCP socket and binds to `127.0.0.1:65432`
- Listens for incoming connections
- Accepts one client connection at a time
- Echoes back any received data
- Closes connection when client disconnects

### Multi-Client Server (`multi_server.py`)
- Uses Python's `selectors` module for I/O multiplexing
- Handles multiple client connections concurrently
- Non-blocking socket operations
- Event-driven architecture with callback functions
- Efficient resource management with automatic cleanup

### Client (`client.py`)
- Connects to server on `127.0.0.1:65432`
- Interactive command-line interface
- Sends user input to server and displays responses
- Graceful disconnection with 'exit' command

## 🎯 Examples

### Example 1: Basic Echo Communication

1. Start the basic server:
```bash
uv run server
```

2. In another terminal, start the client:
```bash
uv run client
```

3. Type messages in the client terminal:
```
Client: Hello, Server!
Server b'Hello, Server!'
Client: How are you?
Server b'How are you?'
Client: exit
```

### Example 2: Multiple Clients with Multi-Server

1. Start the multi-client server:
```bash
uv run multi-server
```

2. Open multiple terminals and start clients in each:
```bash
# Terminal 1
uv run client

# Terminal 2  
uv run client

# Terminal 3
uv run client
```

3. All clients can communicate with the server simultaneously!

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Notes

- The servers bind to `localhost` (`127.0.0.1`) on port `65432`
- Make sure the port is not in use by other applications
- The multi-client server can handle up to 100 concurrent connections
- All socket operations include proper error handling and resource cleanup

---

*This project is designed for learning socket programming concepts in Python. It demonstrates fundamental networking patterns and can serve as a foundation for more complex networked applications.*
