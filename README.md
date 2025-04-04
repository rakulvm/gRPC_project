# Distributed Test Executor using gRPC

A Python-based distributed test automation tool that uses gRPC and Protocol Buffers to simulate execution of remote test commands. The client sends shell commands to a gRPC server, which runs them and returns the output.

## Features
- Client-server architecture using gRPC
- Runs CLI test commands (e.g., ping, curl)
- Real-time output return and success flag
- Scalable base for distributed automation

## Tech Stack
Python, gRPC, Protocol Buffers, subprocess

## Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Generate gRPC code:
   ```bash
   python -m grpc_tools.protoc -Iproto --python_out=. --grpc_python_out=. proto/testexecutor.proto
