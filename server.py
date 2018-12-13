import sys
from socket import socket, AF_INET, SOCK_DGRAM

# get arguments - parent server port and file
port_dad, input_file = int(sys.argv[3]), sys.argv[4]
#now get  parent server ip and port
m_port, ip_parent = int(sys.argv[1]), sys.argv[2]


#create a dictionary to save the ip address
adds = {}
m_file = open(input_file, "r+")
for raw in m_file:
	ip_add, webAddress = raw.partition(",")[::-2]
	adds[webAddress] = ip_add.strip()

s = socket(AF_INET, SOCK_DGRAM)
port_src = int(m_port)
ip_src = '0.0.0.0'

s.bind((ip_src, port_src))

#as long as true
while True:
	i, sender_info = s.recvfrom(2048)
	if i in adds.keys() :
		#get answer from server
		answer = adds.get(i, 0)
		#send answer to sender
		s.sendto(answer, sender_info)
	else :
		s.sendto(i, (ip_parent, port_dad))
		answer, fatherServerInfo = s.recvfrom(2048)
		s.sendto(answer, sender_info)	
		#save answer - ip address into son server dictionary	
		adds[i] = answer
		#write in file
		m_file.write(i+","+answer)
		m_file.close()
		m_file = open(input_file, "r+")
