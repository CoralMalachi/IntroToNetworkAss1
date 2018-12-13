import sys
from socket import socket, AF_INET, SOCK_DGRAM

# get inputs
ip_server, port_server = sys.argv[1], sys.argv[2]

#create a socket udp
s = socket(AF_INET, SOCK_DGRAM)

dst_ip = ip_server
dst_port = int(port_server)
#get addresfrom the user that want to get its ip address
webAddress = raw_input()

#as long as we didnt exit the script keep asking from the user fo more input
while not webAddress == 'quit':
	#use sendto function 
	s.sendto(webAddress, (dst_ip,dst_port))
	ans, sender_info = s.recvfrom(2048)
	print ans
	#get from the user input again
	webAddress = raw_input()
s.close()
