# written by z3ntl3
import httpx
import subprocess
import numpy as np

commands = [
    "ufw reset",
    "ufw default reject incoming",
    "ufw allow proto tcp from %s comment 'CF IP'",
    "ufw limit ssh",
    "ufw reload",
    "ufw enable"
]

try:
    for cmd in commands:
        if "ufw allow proto tcp" in cmd: 
            with httpx.Client(headers={"Cache-Control": "must-revalidate", "Content-Type": "text/plain"}) as client:
                ipv4s = client.get("https://www.cloudflare.com/ips-v4").text.strip().split("\n")
                ipv6s = client.get("https://www.cloudflare.com/ips-v6").text.strip().split("\n")

                ips = np.concatenate((ipv4s, ipv6s))

                for ip in ips:
                    p = subprocess.Popen(cmd % ip, shell=True, stdin=subprocess.PIPE)
                    p.communicate(input='y\n'.encode()) 
            continue

        p = subprocess.Popen("%s" % cmd, shell=True, stdin=subprocess.PIPE)
        p.communicate(input='y\n'.encode())

except Exception as e:
    print("Found error: %s" % e)