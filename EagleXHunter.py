import requests
import argparse
import os
import signal
import json
from concurrent.futures import ThreadPoolExecutor

#colors_Template
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Custom Banner with ASCII Art
BANNER = f"{CYAN}"
BANNER += "\n                               /T /I"
BANNER += "\n                              / |/ | .-~/"
BANNER += "\n                          T\\ Y  I  |/  /  _"
BANNER += "\n         /T               | \\I  |  I  Y.-~/"
BANNER += "\n        I l   /I       T\\ |  |  l  |  T  /"
BANNER += "\n     T\\ |  \\ Y l  /T   | \\I  l   \\   l Y"
BANNER += "\n __  | \\l   \\l  \\I l __l  l   \\     _. |"
BANNER += "\n \\ ~-l  \\   \\  \\  \\ ~\\  \\   . .-~   |"
BANNER += "\n  \\   ~-. \"-.    \\  ^._ ^. \"-.  /  \\   |"
BANNER += "\n.--~-._  ~-    _  ~-_.-\".-\" ._ /._ .\" ./"
BANNER += "\n &gt;--.  ~-.   ._  ~&gt;-\"    \"\\   7   7   ]"
BANNER += "\n^.___~\"--._    ~-{  .-~ .  \\ Y . /    |"
BANNER += "\n &lt;__ ~\"-.  ~       /_/   \\   \\I  Y   : |"
BANNER += "\n   ^-.__           ~(_/   \\   &gt;._:   | l______   Eagle X Hunter"
BANNER += "\n       ^--.,___.-~\"  /_/   !  -.~\"--l_ /     ~\"-. @napoli1372      "
BANNER += "\n              (_/ .  ~(   /'     \"~\"--,Y   -=b-. _)"
BANNER += "\n               (_/ .  \\  :           / l      c\"~o \\"
BANNER += "\n                \\ /    .    .     .^   \\_.-~\"~--.  )"
BANNER += "\n                 (_/ .     /     /       !       )/"
BANNER += "\n                  / / _.   '.   .':      /        '"
BANNER += "\n                  ~(_/ .   /    _    .-&lt;_"
BANNER += "\n                    /_/ . ' .-~\" .  / \\  \\          ,z=."
BANNER += "\n                    ~( /   '  :   | K   \"-.______//"
BANNER += "\n                      \"-.    l   I/ \\_    __{---&gt;._(==."
BANNER += "\n                       //(     \\  &lt;    ~\"~\"     //"
BANNER += "\n                      /' /\\     \\  \\     ,v=.  (("
BANNER += "\n                    .^. / /\\     \"  }__ //===-  "
BANNER += "\n                   / / ' '  \"-.,__ {---(==-"
BANNER += "\n                 .^ '       :  T  ~\"   ll       "
BANNER += "\n                / .  .  . : | :!        \\"
BANNER += "\n               (_/  /   | | j-\"          ~^"
BANNER += "\n                 ~-&lt;_(_.^-~\"\n"
BANNER += "\nHunterXCVE v~1.0 - Created by @napoli1372\n{RESET}"

# API KEYS (Add your own keys)
#------------------------------------------
SHODAN_API_KEY = "your_shodan_api_key"
CENSYS_API_ID = "your_censys_id"
CENSYS_API_SECRET = "your_censys_secret"
BINARYEDGE_API_KEY = "your_binaryedge_api_key"
VULNERS_API_KEY = "your_vulners_api_key"
#-------------------------------------------
def exit():
    print(f"\n{YELLOW}[+]Terminating...{RESET}")
    exit(0)

signal.signal(signal.SIGINT, exit)
#Fast IP Lookups for Open Ports and Vulnerabilities
def query_shodan(ip):
    if not SHODAN_API_KEY:
        return {"{RED}[-]error": "API Key not found{RESET} "}
    host = f"https://internetdb.shodan.io/{ip}"
    response = requests.get(host)
    return response.json() if response.status_code == 200 else print("N/A")

def query_censys(ip):
    if not CENSYS_API_ID or not CENSYS_API_SECRET:
        return {"{RED}[-]error": "API Key not found{RESET}"}
    url = f"https://search.censys.io/api/v2/hosts/{ip}"
    response = requests.get(url, auth=(CENSYS_API_ID, CENSYS_API_SECRET))
    return response.json() if response.status_code == 200 else print("N/A")

def query_binaryedge(ip):
    if not BINARYEDGE_API_KEY:
        return {"{RED}[-]error": "API Key not found{RESET}"}
    url = f"https://api.binaryedge.io/v2/query/ip/{ip}"
    headers = {"X-Key": BINARYEDGE_API_KEY}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else print("N/A")

def query_vulnerabilities(cve_id):
    if not VULNERS_API_KEY:
        return {"{RED}[+]error": "API Key not found{RESET}"}
    url = f"https://vulners.com/api/v3/search/id/?id={cve_id}&apiKey={VULNERS_API_KEY}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else print("N/A")

def scan_ip(ip, services_to_use):
    print(f"{YELLOW}[INFO]{RESET} Scanning {ip}...")
    service_methods = {
        "shodan": query_shodan,
        "censys": query_censys,
        "binaryedge": query_binaryedge
    }
    
    with ThreadPoolExecutor() as executor:
        future_results = {name: executor.submit(func, ip) for name, func in service_methods.items() if name in services_to_use}
    
    results = {key: future.result() for key, future in future_results.items()}
    
    print(f"{GREEN}\n[RESULT] IP: {ip}{RESET}")
    for service, data in results.items():
        print(f"{BLUE}[{service.upper()}]{RESET}: {json.dumps(data, indent=2)}")

def main():
    os.system("clear")
    print(BANNER)
    
    
    parser = argparse.ArgumentParser(description="------EagleXHunter Recon Tool------")
    parser.add_argument("-ip", help="Single IP (eg : 192.x.x.x)")
    parser.add_argument("-file", help="File with IPs (eg : Ips.txt)")
    parser.add_argument("-services", help="Comma-separated list of services to use ( eg :shodan,censys,binaryedge)", default="shodan,censys,binaryedge")
    args = parser.parse_args()
    
    selected_services = args.services.split(",")
    
    if args.ip:
        scan_ip(args.ip, selected_services)
    elif args.file:
        with open(args.file, "r") as file:
            ip_list = file.read().splitlines()
            for ip in ip_list:
                scan_ip(ip, selected_services)
    else:
        print(f"{RED}[ERROR]{RESET} No input provided.")
    
if __name__ == "__main__":
    main()
