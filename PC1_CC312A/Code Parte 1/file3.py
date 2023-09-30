import time
from paramiko.client import SSHClient,AutoAddPolicy

# Credentials here are for a always-on Sandbox from Cisco DevNet
SSH_USER = "developer"
SSH_PASSWORD = "lastorangerestoreball8876"
SSH_HOST = "sandbox-iosxe-recomm-1.cisco.com"
SSH_PORT = 22 # Change this if your SSH port is different

client = SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(AutoAddPolicy())

client.connect(SSH_HOST, port=SSH_PORT,
                         username=SSH_USER,
                         password=SSH_PASSWORD,
                         look_for_keys=False)



CMD = "show ip interface brief" # You can issue any command you want
stdin, stdout, stderr = client.exec_command(CMD)
output = stdout.readlines()
with open("backup.txt", "w") as out_file:
    for line in output:
        out_file.write(line)

client.close()
