import httpx
import subprocess

try:
    # clear first
    p = subprocess.Popen("ufw reset", shell=True, stdin=subprocess.PIPE)
    p.communicate(input='y\n'.encode())

    p = subprocess.Popen("ufw default reject incoming",
                         shell=True, stdin=subprocess.PIPE)
    p.communicate(input='y\n'.encode())

    with httpx.Client(headers={"Cache-Control": "must-revalidate", "Content-Type": "text/plain"}) as client:
        ipv4s = client.get("https://www.cloudflare.com/ips-v4").text
        ipv6s = client.get("https://www.cloudflare.com/ips-v6").text

        ipv4s = ipv4s.strip().split("\n")
        ipv6s = ipv6s.strip().split("\n")

        for ipv4 in ipv4s:
            p = subprocess.Popen(
                f"ufw allow proto tcp from {ipv4} comment 'CF IP'", shell=True, stdin=subprocess.PIPE)
            p.communicate(input='y\n'.encode())
        for ipv6 in ipv6s:
            p = subprocess.Popen(
                f"ufw allow proto tcp from {ipv6} comment 'CF IP'", shell=True, stdin=subprocess.PIPE)
            p.communicate(input='y\n'.encode())

        p = subprocess.Popen("ufw limit ssh",
                             shell=True)
        p.communicate(input='y\n'.encode())
        p = subprocess.Popen("ufw reload", shell=True, stdin=subprocess.PIPE)
        p.communicate(input='y\n'.encode())
        p = subprocess.Popen("ufw enable", shell=True, stdin=subprocess.PIPE)
        p.communicate(input='y\n'.encode())
except:
    print("Failed")
