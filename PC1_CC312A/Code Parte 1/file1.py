from paramiko.client import SSHClient
from paramiko.client import SSHClient, AutoAddPolicy

# Credentials here are for a always-on Sandbox from Cisco DevNet
SSH_USER = "developer"
SSH_PASSWORD = "lastorangerestoreball8876"
SSH_HOST = "sandbox-iosxe-recomm-1.cisco.com"
SSH_PORT = 22 # Change this if your SSH port is different

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())
client.load_system_host_keys()
try:
    client.connect(SSH_HOST, port=SSH_PORT,
                             username=SSH_USER,
                             password=SSH_PASSWORD,
                             look_for_keys=False)
    print("Connected succesfully!")
except Exception:
    print("Failed to establish connection.")
finally:
    client.close()