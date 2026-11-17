# YEAGER — Cybersecurity Toolkit

**YEAGER** is a Python-based cybersecurity toolkit designed to organize security analysis tools through an interactive command-line interface.

The project focuses on modularity, usability, and the integration of tools commonly used in cybersecurity and penetration testing.

> **Project Status:** Early Development

## Features

### Currently Implemented
- Interactive command-line interface
- Modular Python project structure
- Network Analysis navigation menu
- Nmap configuration menu and target input
- Custom terminal banners and colored output

### Planned Features
- Network discovery and port scanning
- Service and version detection
- Operating system identification
- Web reconnaissance and enumeration
- Vulnerability assessment
- Integration with external security tools
- Scan history and report generation

**Note:** Scanning operations are not yet implemented. The current Nmap interface provides menu navigation and informational messages.

## Technologies

- Python
- Rich
- Questionary
- Pyfiglet

## Installation

Clone the repository:

```bash
git clone https://github.com/JohnMedeirosOnlyONe/YEAGER.git
cd YEAGER
```

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the main application:

```bash
python main.py
```

Navigate through the interactive menu to explore the available modules.

## Project Structure

```text
YEAGER/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── interface/
    ├── interface_YEAGER.py
    ├── menu_YEAGER.py
    ├── components/
    │   └── banners.py
    ├── menus/
    │   ├── network_menu.py
    │   └── utilities_menu.py
    └── screens/
        └── network/
            └── nmap_screen.py
```

## Disclaimer

YEAGER is intended for educational purposes and authorized security testing only.

Users are responsible for ensuring they have explicit permission before performing security assessments against any system or network.

## Development

YEAGER is an ongoing project. Additional modules, tool integrations, and security analysis features will be implemented progressively.

Contributions and suggestions are welcome.
