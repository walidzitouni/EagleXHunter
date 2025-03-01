# EagleXHunter

<p align="center">
  <img src="https://raw.githubusercontent.com/walidzitouni/eaglexhunter/main/logo.png" alt="EagleXHunter Logo" width="200"/>
</p>

<p align="center">
  <em>Advanced multi-source reconnaissance tool for security professionals</em>
</p>

<p align="center">
  <a href="https://github.com/username/eaglexhunter/releases">
    <img src="https://img.shields.io/github/v/release/walidzitouni/eaglexhunter" alt="Release">
  </a>
  <a href="https://github.com/username/eaglexhunter/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/walidzitouni/eaglexhunter" alt="License">
  </a>
  <a href="https://github.com/username/eaglexhunter/stargazers">
    <img src="https://img.shields.io/github/stars/walidzitouni/eaglexhunter" alt="Stars">
  </a>
</p>

## Overview

EagleXHunter is a powerful reconnaissance tool that aggregates intelligence from multiple sources including Shodan, Censys, and BinaryEdge. Designed for security professionals, penetration testers, and researchers, it streamlines the process of gathering critical intelligence about IP addresses and potential vulnerabilities.

## Features

- **Multi-Source Intelligence**: Seamlessly integrates with Shodan, Censys, and BinaryEdge
- **Concurrent Processing**: Utilizes threading for faster results
- **Flexible Targeting**: Scan individual IPs or process lists from files
- **Service Selection**: Choose which intelligence services to use for each scan
- **Vulnerability Lookup**: Integrated CVE details through Vulners API
- **Clean Visualization**: Color-coded output for improved readability

## Installation

```bash
# Clone the repository
git clone https://github.com/username/eaglexhunter.git

# Navigate to the directory
cd eaglexhunter

# Install dependencies
pip install -r requirements.txt
```

## Configuration

Edit the API keys section in the script to add your own keys:

```python
# API KEYS
SHODAN_API_KEY = "your_shodan_api_key"
CENSYS_API_ID = "your_censys_id"
CENSYS_API_SECRET = "your_censys_secret"
BINARYEDGE_API_KEY = "your_binaryedge_api_key"
VULNERS_API_KEY = "your_vulners_api_key"
```

## Usage

### Basic Command Syntax

```bash
python EagleXHunter.py [options]
```

### Options

- `-ip <IP_ADDRESS>`: Scan a single IP address
- `-file <FILENAME>`: Process multiple IPs from a file (one IP per line)
- `-services <SERVICE_LIST>`: Comma-separated list of services to use (default: shodan,censys,binaryedge)

### Examples

Scan a single IP using all services:
```bash
python EagleXHunter.py -ip 8.8.8.8
```

Scan a single IP using only Shodan:
```bash
python EagleXHunter.py -ip 8.8.8.8 -services shodan
```

Scan multiple IPs from a file:
```bash
python EagleXHunter.py -file targets.txt
```

## Output Example

```
[INFO] Scanning 8.8.8.8...

[RESULT] IP: 8.8.8.8
[SHODAN]: {
  "ip": "8.8.8.8",
  "ports": [53, 443],
  "hostnames": ["dns.google"],
  "tags": ["cdn", "dns"],
  "vulnerabilities": []
}
[CENSYS]: {
  "result": {
    "ip": "8.8.8.8",
    "services": [
      {
        "port": 53,
        "service_name": "DNS"
      }
    ]
  }
}
```

## Dependencies

- requests
- argparse
- concurrent.futures

## Roadmap

- [ ] Add support for additional intelligence sources
- [ ] Implement export functionality (CSV, JSON, PDF)
- [ ] Create a web interface
- [ ] Add historical data comparison
- [ ] Integrate with threat intelligence feeds

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspiration from various OSINT tools in the security community
- Thanks to the developers of Shodan, Censys, and BinaryEdge for their APIs

## Contact

Creator: [@napoli1372](https://twitter.com/napoli1372)

Project Link: [https://github.com/username/eaglexhunter](https://github.com/username/eaglexhunter)
