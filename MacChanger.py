import os

def mac_changer():
    interface=input("Enter Interface:")
    new_mac=input("New_MAC:")
    os.system("ifconfig "+ interface + " down")
    os.system("ifconfig "+ interface + " hw ether " +new_mac)
    os.system("ifconfig "+ new_mac + " up")
print(mac_changer())
