#!/usr/bin/python
import sys, socket

if len(sys.argv) < 2 :
    print "Usage : %s PORT" % (sys.argv[0])
    sys.exit(1)

UDP_PORT = int(sys.argv[1])
print "listening on port: " + UDP_PORT

sock = socket.socket(	socket.AF_INET, # Internet
			socket.SOCK_DGRAM) # UDP
sock.bind(("", UDP_PORT))

print sock
while True:
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	print "received message:", data
