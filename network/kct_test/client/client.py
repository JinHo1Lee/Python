from socket import *
from time import sleep


sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('172.16.0.107', 5000))

print sock
while 1:
	sock.send("hello")
	print "Send packet"
	sleep(1)

