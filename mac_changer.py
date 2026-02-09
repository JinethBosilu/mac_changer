import subprocess

interface = "eth0"
new_mac = "00:11:22:33:44:55"

print("[+] Changing MAC address for "+interface+" to "+new_mac)

subprocess.run("ifconfig "+interface+" down", shell=True)
subprocess.run("ifconfig "+interface+" hw ether "+new_mac, shell=True)
subprocess.run("ifconfig "+interface+" up", shell=True)