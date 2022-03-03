import paramiko
import sys
import concurrent.futures

try:
    host = sys.argv[1]
    port = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]
except:
    print('Usage:\npython3 cfiptables.py host port username pass\n\nExample usage:\npython3 cfiptables 123.123.123.123 22 root root')

def Server(host=host,port=port,username=username,password=password,*,cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port, username, password)
    except:
        sys.exit('Invalid host port username password')
    stdin, stdout, stderr = ssh.exec_command(cmd)
    return 0


def Main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        executor.submit(Server(cmd='sudo rm -r cloudflare.sh'))
        executor.submit(Server(cmd='wget https://gist.githubusercontent.com/Manouchehri/cdd4e56db6596e7c3c5a/raw/be3c3ef3459a39e97aad4e643c9e0992d49cef96/cloudflare.sh'))
        executor.submit(Server(cmd='sudo apt update -y'))
        executor.submit(Server(cmd='sudo apt install curl -y'))
        executor.submit(Server(cmd='chmod +x cloudflare.sh && sudo ./cloudflare.sh'))
    print("\033[32m\033[1mInstalled Successfully Iptables Ruleset\033[0m")

if __name__ == '__main__':
    Main()
