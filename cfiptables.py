import paramiko
import sys
from concurrent.futures import ThreadPoolExecutor
'''
By Z3NTL3
'''
procnum = 0
try:
    host = sys.argv[1]
    port = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]
except:
    print('Usage:\npython3 cfiptables.py host port username pass\n\nExample usage:\npython3 cfiptables 123.123.123.123 22 root root')


def Server(host=host,port=port,username=username,password=password,*,cmd):
    global procnum
    procnum += 1
    print("\033[35mProcess: \033[32m{} \033[36mstarted\033[0m".format(procnum))
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port, username, password)
    except:
        sys.exit('\033[31mERROR: \033[35mInvalid host port username password\033[0m')
    stdin, stdout, stderr = ssh.exec_command(cmd)
    return 0


def Main():
    with ThreadPoolExecutor(max_workers=6) as executor:
        executor.submit(Server(cmd='sudo rm -r cloudflare.sh'))
        executor.submit(Server(cmd='wget https://raw.githubusercontent.com/Z3NTL3/CloudflareIPTables/main/anti_ddos_cf_iptables.py'))
        executor.submit(Server(cmd='sudo apt update -y'))
        executor.submit(Server(cmd='sudo apt install curl -y'))
        executor.submit(Server(cmd='chmod +x anti_ddos_cf_iptables.py && sudo python3 anti_ddos_cf_iptables.py'))
    print("\033[32m\033[1mInstalled Successfully Iptables Ruleset\033[0m")

if __name__ == '__main__':
    Main()
