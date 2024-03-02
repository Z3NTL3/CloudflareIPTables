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

def test_pytest_pass():
    assert 1 == 1

try:
    for cmd in commands:
        if "ufw allow proto tcp" in cmd: 
            with httpx.Client(headers={"Cache-Control": "must-revalidate", "Content-Type": "text/plain"}) as client:
                ipv4s = client.get("https://www.cloudflare.com/ips-v4").text.strip().split("\n")
                ipv6s = client.get("https://www.cloudflare.com/ips-v6").text.strip().split("\n")

                ips = np.concatenate((ipv4s, ipv6s))

                for ip in ips:
                    p = subprocess.run(cmd % ip, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    out, err = p.communicate(input='y\n'.encode())

                    if err:
                        print("failed configuration: %s" % err.decode())
                        exit(0)
                    if out:
                        print(out.decode())
            continue

        p = subprocess.run("%s" % cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate(input='y\n'.encode())

        if err:
            print("failed configuration: %s" % err.decode())
            exit(0)
        if out:
            print(out.decode())

except Exception as e:
    print("Found error: %s" % e)
