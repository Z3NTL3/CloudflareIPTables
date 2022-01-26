import logging
import subprocess as sp
import sys
'''
Programmed by Z3NTL3
'''
logging.basicConfig(filename='logs.log', level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class installer:
    try:
        curl_install = sp.run("sudo apt-get install curl", shell=True)
    except:
        print("\033[31mPlease run manually:\033[0m\nsudo apt-get install curl")
        logging.error("Cannot run sudo apt-get install curl")
        sys.exit()

installer.curl_install

class Cloudflare_IPS:
    try:
        ipv6 = "curl -s https://www.cloudflare.com/ips-v6"
        ipv4 = "curl -s https://www.cloudflare.com/ips-v4"

        contentipv4 = sp.getoutput(ipv4)
        contentipv6 = sp.getoutput(ipv6)

        iplist_ipv4 = {contentipv4}
        iplist_ipv6 = {contentipv6}

    except:
        logging.critical("Cannot run IPTABLES commands please run me as root and be sure you have iptables")
        sys.exit("Error occured look into logs.log for details")


for ipv_4s in Cloudflare_IPS.iplist_ipv4:
    try:        
        sp.run(f"sudo iptables -I INPUT -p tcp -m multiport --dports http,https -s {ipv_4s} -j ACCEPT",shell=True)
    except:
        logging.critical("Cannot run IPTABLES commands please run me as root and be sure you have iptables")
        sys.exit("Error occured look into logs.log for details")
        

for ipv_6s in Cloudflare_IPS.iplist_ipv6:
    try:      
         sp.run(f"sudo ip6tables -I INPUT -p tcp -m multiport --dports http,https -s {ipv_6s} -j ACCEPT", shell=True)
    
    except:
        logging.critical("Cannot run IPTABLES commands please run me as root and be sure you have iptables")
        sys.exit("Error occured look into logs.log for details")


try:
    sp.run(f"sudo iptables -A INPUT -p tcp --dport http,https -j DROP",shell=True)
    sp.run(f"sudo ip6tables -A INPUT -p tcp --dport http,https -j DROP",shell=True)
except:
    logging.critical("Cannot run IPTABLES commands please run me as root and be sure you have iptables")
    sys.exit("Error occured look into logs.log for details")

logging.info("Successfully set IPTABLE RULES")
print("Successfully allowed ONLY CLOUDFLARE IPs REVERSE PROXY TECHNOLOGY and disallowed all requests from other.\nAllowed only IP requests which came from the cloudflare cdn reverse proxy end")
