import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
(options, arguments) = parser.parse_args()

interface = input("Enter the interface you want to change the MAC address for: ")
new_mac = input("Enter the new MAC address: ")

print("[+] Changing MAC address for "+interface+" to "+new_mac)

subprocess.run(["ifconfig", interface, "down"], shell=True)
subprocess.run(["ifconfig", interface, "hw", "ether", new_mac], shell=True)
subprocess.run(["ifconfig", interface, "up"], shell=True)