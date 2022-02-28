import logging
import subprocess as sp
import sys
'''
Programmed by Z3NTL3
'''

logging.basicConfig(filename='logs.log', level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def main():
    try:
        ipv6 = "curl -s https://www.cloudflare.com/ips-v6"
        ipv4 = "curl -s https://www.cloudflare.com/ips-v4"

        contentipv4 = sp.getoutput(ipv4)
        contentipv6 = sp.getoutput(ipv6)

        sp.run("sudo rm -r ipv4.txt", shell=True, stderr=sp.DEVNULL)
        sp.run("sudo rm -r ipv6.txt", shell=True, stderr=sp.DEVNULL)

        with open("ipv4.txt", "a+")as f:
            f.write(contentipv4)
        with open("ipv6.txt", "a+")as q:
            q.write(contentipv6)

        read_ipv4 = open("ipv4.txt","r").read()
        cleanipv4 = read_ipv4.strip()
        readableipv4 = cleanipv4.split("\n")

        read_ipv6 = open("ipv6.txt","r").read()
        cleanipv6 = read_ipv4.strip()
        readableipv6 = cleanipv6.split("\n")


        try:
            for ipv4s in readableipv4:
                sp.run("sudo iptables -I INPUT -p tcp -m multiport --dports http,https -s {} -j ACCEPT".format(ipv4s),shell=True)
        except:
            read_ipv4.close()
            logging.critical("Cannot execute commands run me as sudo")
            sys.exit("Error occured look into logs.log for details")
        
        try:

            for ipv6s in readableipv4:
                sp.run("sudo ip6tables -I INPUT -p tcp -m multiport --dports http,https -s {} -j ACCEPT".format(ipv6s),shell=True)
        
        except:
            
            logging.critical("Cannot execute commands run me as sudo")
            sys.exit("Error occured look into logs.log for details")
        


        try:
            sp.run("sudo iptables -A INPUT -p tcp --dport http,https -j DROP",shell=True)
            sp.run("sudo ip6tables -A INPUT -p tcp --dport http,https -j DROP",shell=True)
        except:
            logging.critical("Cannot execute commands run me as sudo")
            sys.exit("Error occured look into logs.log for details")
        
        logging.info("Successfully set IPTABLE RULES")
        print("Successfully allowed ONLY CLOUDFLARE IPs REVERSE PROXY TECHNOLOGY and disallowed all requests from other.\nAllowed only IP requests which came from the cloudflare cdn reverse proxy end")

    except:
        logging.critical("I cannot connect to cloudflare, please check your internet")
        sys.exit("Error occured look into logs.log for details")


if __name__ == '__main__':
    main()
