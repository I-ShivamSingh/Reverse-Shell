# Reverse Shell using Python and Socket Programming

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)

## Project Description

This project demonstrates how to create a reverse shell using Python and socket programming. A reverse shell is a powerful tool that allows a remote user to establish a connection to a target system, gaining full control over it. The project includes two main components: the client and the server.

- `client.py`: This script runs on the target system (the victim) and connects back to the server. It listens for commands from the server, executes them, and sends the results back to the server.

- `serverformultipleclients.py`: The server script that can handle connections from multiple clients simultaneously. It allows you to manage and control multiple remote systems from a single interface.

- `serverforsingleclient.py`: An alternative server script that handles connections from a single client, ideal for scenarios where you only need to control one system.

## Features

- Establish a reverse connection to the client's computer.
- Execute commands on the remote system.
- Handle multiple client connections simultaneously.
- Send and receive data in an interactive manner.

## Setup and Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/I-ShivamSingh/Reverse-Shell.git
   ```

2. Run the server script to set up a listening server:

   ```bash
   python serverformultipleclients.py
   ```

   Alternatively, you can use `serverforsingleclient.py` for a single-client scenario.

3. Update the `client.py` script with the server's IP address and run it on the target system:

   ```python
   host = "your-server-ip"
   ```

4. Once the client connects to the server, you can interact with the remote system through the server's command prompt.


## Acknowledgments

- Inspired by ethical hacking and penetration testing tools.
- Built for educational and informational purposes.

## Contact

If you have any questions or suggestions, feel free to reach out to me at [shivamsinghsemail@gmail.com](mailto:shivamsinghsemail@gmail.com).
