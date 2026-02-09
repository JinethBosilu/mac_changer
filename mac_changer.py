import subprocess

interface = input("Enter the interface you want to change the MAC address for: ")
new_mac = input("Enter the new MAC address: ")

print("[+] Changing MAC address for "+interface+" to "+new_mac)

subprocess.run("ifconfig "+interface+" down", shell=True)
subprocess.run("ifconfig "+interface+" hw ether "+new_mac, shell=True)
subprocess.run("ifconfig "+interface+" up", shell=True)