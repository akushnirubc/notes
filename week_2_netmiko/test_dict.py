from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'cisco1.lasthop.io', 
    "username": 'pyclass', 
    "password": getpass(), 
    "device_type": 'cisco_ios', 
    #"session_log": 'my_session.txt'
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

command = 'delete flash:/testx.txt'

# output = net_connect.send_command_timing(command,
#     strip_prompt=False, strip_command=False)
# output += net_connect.send_command_timing('y', 
#     strip_prompt=False, strip_command=False)
# print(output)

output = net_connect.send_command(
    command, expect_string=r'Delete filename', strip_prompt=False, strip_command=False)
output += net_connect.send_command(
    '\n', expect_string=r'confirm', strip_prompt=False, strip_command=False)
output += net_connect.send_command(
    'y', expect_string=r'#', strip_prompt=False, strip_command=False)
print(output)
net_connect.disconnect()

