# Python Network Port Scanner

A lightweight and customizable **Python-based port scanner** built using the `python-nmap` library.  
This tool automates common Nmap scan types and parses the results into a clean, readable format.

## Features
- Performs service/version detection using `-sV`
- Runs default Nmap scripts using `-sC`
- Displays open ports, services, and protocol information
- Simple and beginner-friendly code structure
- Fully compatible with Windows, Linux, and macOS
- Great for learning Python + Nmap automation

## Technologies Used
- **Python 3**
- **python-nmap**
- **Nmap**

## Installation

### 1. Install Nmap
Download Nmap:  
https://nmap.org/download.html  
Ensure you check **Add Nmap to PATH** during installation.

Verify installation:
```bash
nmap --version
```

### 2. Install python-nmap
```bash
pip install python-nmap
```
## Usage
Run the script:
```bash
python port_scanner.py
```

Modify the Target: 
For demonstration and learning purposes, this project uses the safe, publicly provided test IP from Nmap:
```bash
45.33.32.156
```
This IP is officially published by Nmap for beginner-friendly scanning practice and is safe to use in training projects.
```bash
target = "45.33.32.156"
```
## **IMPORTANT**
**You should only scan IP addresses that you own or have explicit permission to scan.
Unauthorized scanning of networks or systems you do not control may violate laws or terms of service.
Always follow safe and ethical cybersecurity practices.**

## Output
```bash
Host: 45.33.32.156 (scanme.nmap.org)
State: up
Protocol: tcp
Port: 22        State: open
Port: 80        State: open
Port: 9929      State: open
Port: 31337     State: open
```


