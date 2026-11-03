import shutil as shu
import sys
import subprocess as sub
import ipaddress as ipad
import psutil as util
import socket as sock
passer = False

if shu.which("nmap"): # Checks Whether you even have nmap Installed.
    passer = True
else:
    passer = False

if not passer:
    print("nmap not found!")
    sys.exit(1)

# Send a UDP Packet to find out what your Address is.
mes = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)
addres = util.net_if_addrs().items()
mes.connect(("8.8.8.8", 80))

mask = None

ip = mes.getsockname()[0]

# Get your Subnet
for i_name, address in addres:
    print(i_name, address)
    for addr in address:
        if addr.address == ip:
            mask = addr.netmask

network = ipad.ip_interface(f"{ip}/{mask}").network

sub.run(["nmap", "-sn", str(network)]) # pyright: ignore[reportUnusedCallResult]
# Runs nmap with a Host discovery scan with the subnet. this does **Skip** the port scan.
