import logging
import subprocess as sp
import sys
'''
Programmed by Z3NTL3
'''

logging.basicConfig(filename='logs.log', level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def main():
    
    ipv6 = "curl -s https://www.cloudflare.com/ips-v6"
    ipv4 = "curl -s https://www.cloudflare.com/ips-v4"

    contentipv4 = sp.getoutput(ipv4).strip()
    contentipv6 = sp.getoutput(ipv6).strip()


    sp.run("sudo rm -r ipv4.txt", shell=True, stderr=sp.DEVNULL)
    sp.run("sudo rm -r ipv6.txt", shell=True, stderr=sp.DEVNULL)

    readableipv4 = contentipv4.split("\n")

    readableipv6 = contentipv6.split("\n")

 

    try:
        for ipv4s in readableipv4:
            sp.run("iptables -I INPUT -p tcp -m multiport --dports http,https -s {} -j ACCEPT".format(ipv4s),shell=True)
    except:   
        pass
    
    try:

        for ipv6s in readableipv6:
            sp.run("ip6tables -I INPUT -p tcp -m multiport --dports http,https -s {} -j ACCEPT".format(ipv6s),shell=True)
    
    except:
        pass
    


    try:
        sp.run("iptables -A INPUT -p tcp --dport http,https -j DROP",shell=True)
        sp.run("ip6tables -A INPUT -p tcp --dport http,https -j DROP",shell=True)
    except:
        pass
    
    logging.info("Successfully set IPTABLE RULES")
    print("Successfully allowed ONLY CLOUDFLARE IPs REVERSE PROXY TECHNOLOGY and disallowed all requests from other.\nAllowed only IP requests which came from the cloudflare cdn reverse proxy end")

    


if __name__ == '__main__':
    main()
