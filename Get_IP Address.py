


# Python3 Simple program to Get IP Address


import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


print("Your Computer Name is: " + hostname)
print("Your Computer IP Address is: " + IPAddr)




# ================= OUTPUT =================

# Your Computer Name is: Infinity-1337
# Your Computer IP Address is: 192.168.51.652
