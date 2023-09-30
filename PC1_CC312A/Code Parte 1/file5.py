import time
from paramiko.client import SSHClient
# Credentials here are for a always-on Sandbox from Cisco DevNet
SSH_USER = "developer"
SSH_PASSWORD = "lastorangerestoreball8876"
SSH_HOST = "sandbox-iosxe-recomm-1.cisco.com"
SSH_PORT = 22 # Change this if your SSH port is different


client = SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


client.connect(SSH_HOST, port=SSH_PORT,
                         username=SSH_USER,
                         password=SSH_PASSWORD,
                         look_for_keys=False)

channel = client.get_transport().open_session()
shell = client.invoke_shell()

commands = [
	"configure terminal",
	"hostname test"
]

for cmd in commands:
      shell.send(cmd + "\n")
      out = shell.recv(1024)
      print(out)
      time.sleep(5)
