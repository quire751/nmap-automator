import shutil as shu
import sys
import subprocess as sub
import ipaddress as ipad
passer = False

if shu.which("nmap"): # Checks Whether you even have nmap Installed.
    passer = True
else:
    passer = False

if not passer:
    print("nmap not found!")
    sys.exit(1)
try:
   network = ipad.ip_network(input("Please Enter an IP Network Address: "), strict=False) # Turns off strict mode & lets you input a network Address.
except ValueError:
    print("Not a network Address.")
    sys.exit(1)

sub.run(["nmap", "-sn", str(network)]) # pyright: ignore[reportUnusedCallResult]
# Runs nmap with a Host discovery scan with the given Address. this does **Skip** the port scan.
