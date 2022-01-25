import logging
import subprocess as sp
import sys

logging.basicConfig(filename='logs.log', level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class installer:
    try:
        curl_install = sp.run("sudo apt-get install curl", shell=True)
    except:
        print("\033[31mPlease run manually:\033[0m\nsudo apt-get install curl")
        logging.error("Cannot run sudo apt-get install curl")
        sys.exit()

class Cloudflare_IPS:
    ipv6 = "curl https://www.cloudflare.com/ips-v6"
    ipv4 = "curl https://www.cloudflare.com/ips-v4"

    contentipv4 = sp.getoutput(ipv4)
    contentipv6 = sp.getoutput(ipv6)


for ipv_4s in Cloudflare_IPS.contentipv4:
    try:        
        sp.run(f"iptables -I INPUT -p tcp -m multiport --dports http,https -s {ipv_4s} -j ACCEPT",shell=True)
    except:
        logging.critical("Cannot run IPTABLES commands please run me as root and be sure you have iptables")
        sys.exit("Error occured look into logs.log for details")
        

for ipv_6s in Cloudflare_IPS.contentipv6:
    try:      
         sp.run(f"ip6tables -I INPUT -p tcp -m multiport --dports http,https -s {ipv_6s} -j ACCEPT", shell=True)
    
    except:
        logging.critical("Cannot run IPTABLES commands please run me as root and be sure you have iptables")
        sys.exit("Error occured look into logs.log for details")


try:
    sp.run(f"iptables -A INPUT -p tcp --dport http,https -j DROP",shell=True)
    sp.run(f"ip6tables -A INPUT -p tcp --dport http,https -j DROP",shell=True)
except:
    logging.critical("Cannot run IPTABLES commands please run me as root and be sure you have iptables")
    sys.exit("Error occured look into logs.log for details")

logging.info("Successfully set IPTABLE RULES")
print("Successfully allowed ONLY CLOUDFLARE IPs REVERSE PROXY TECHNOLOGY and disallowed all requests from other.\nAllowed only IP requests which came from the cloudflare cdn reverse proxy end")
