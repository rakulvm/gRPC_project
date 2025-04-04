# gRPC_project

# Distributed Test Executor using gRPC

Distributed Test Executor is a Python-based test automation tool designed to simulate remote command execution in distributed environments. Built using gRPC and Protocol Buffers, this project demonstrates how a client can securely dispatch shell-based test commands to a centralized server and receive real-time results.

It serves as a scalable foundation for network device test automation, telecom-grade CLI validations, or DevOps testing workflows, particularly in systems requiring fast, structured, and bidirectional communication.

## Project Objectives
- Demonstrate a practical implementation of a gRPC client-server architecture
- Enable remote execution of shell commands with minimal overhead
- Provide a real-time feedback mechanism for command outputs
- Showcase how Protocol Buffers enable efficient message serialization
- Emulate a simplified version of a distributed test infrastructure often used in embedded, network, or CI/CD environments

## Tech Stack
- Language: Python
- Communication Protocol: gRPC
- Serialization Format: Protocol Buffers (.proto)
- Process Execution: Python's subprocess module
- Other Tools: Git, pip, gRPC tools for Python

## Features
- Client-server architecture using gRPC
- Runs CLI test commands (e.g., ping, curl)
- Real-time output return and success flag
- Scalable base for distributed automation

## Setup & Usage Instructions
1. Install dependencies: `pip install -r requirements.txt`
2. Generate gRPC code:
   ```bash
   python -m grpc_tools.protoc -Iproto --python_out=. --grpc_python_out=. proto/testexecutor.proto
3. Start the Server
   ```bash
   python server.py
4. Start the Client
   ```bash
   python server.py
