import os
import re

directory = "/etc/NetworkManager/system-connections/"
files = os.listdir(directory)

for file in files:
    with open(os.path.join(directory, file), "r") as f:
        contents = f.read()
        connection_name = re.search('ssid=(\w+)', contents)
        password = re.search('psk=(\w+)', contents)

        if connection_name and password:
            print(f"Device Name: {connection_name.group(1)}")
            print(f"Password: {password.group(1)}")
            print("-" * 20)