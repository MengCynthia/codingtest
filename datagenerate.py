s = "direction,protocol,port,ip_address\n"
#norange

for d in ["inbound","outbound"]:
	for pro in ["tcp","udp"]:
		for p in range(1,65536,1000):
		    for ip1 in range(0,256,80):
		        for ip2 in range(0,256,80):
		        	for ip3 in range(0,256,80):
		        		for ip4 in range(0,256,80):
		        			print(p," ",ip1," ",ip2," ",ip3," ",ip4)
		        			s += d + ","+pro + ","+str(p) + ","+str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' +str(ip4) +"\n"
file1 = open("norange.csv","w")
file1.write(s)
#range port
s = "direction,protocol,port,ip_address\n"
for d in ["inbound","outbound"]:
	for pro in ["tcp","udp"]:
		for p in range(1,65536,1000):
		    for ip1 in range(0,256,80):
		        for ip2 in range(0,256,80):
		        	for ip3 in range(0,256,80):
		        		for ip4 in range(0,256,80):
		        			print(p," ",ip1," ",ip2," ",ip3," ",ip4)
		        			s += d + ","+pro + ","+str(p) + "-"+str(p+10)+","+str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' +str(ip4) +"\n"
file2 = open("rangeport.csv","w")
file2.write(s)

#range ip
s = "direction,protocol,port,ip_address\n"
for d in ["inbound","outbound"]:
	for pro in ["tcp","udp"]:
		for p in range(1,65536,1000):
		    for ip1 in range(0,256,80):
		        for ip2 in range(0,256,80):
		        	for ip3 in range(0,256,80):
		        		for ip4 in range(0,256,80):
		        			print(p," ",ip1," ",ip2," ",ip3," ",ip4)
		        			s += d + ","+pro + ","+str(p) + "-"+str(p+10)+","+str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' +str(ip4) +"-"+str(ip1) + '.' + str(ip2) + '.' + str(ip3+10) + '.' +str(ip4)+"\n"
file3 = open("rangeipport.csv","w")
file3.write(s)

#overlapped ip
s = "direction,protocol,port,ip_address\n"

s+="inbound,tcp,80,192.168.1.2\n"
s+="inbound,tcp,80,192.168.0.2-192.168.1.1\n"

s+="inbound,tcp,800,192.168.1.2\n"
s+="inbound,tcp,800,192.168.0.2-192.168.1.2\n"

s+="inbound,tcp,8000,192.168.1.2\n"
s+="inbound,tcp,8000,192.168.2.2-192.168.3.2\n"
s+="inbound,tcp,8000,192.168.0.2-192.168.3.1\n"

s+="inbound,tcp,10,192.168.1.2\n"
s+="inbound,tcp,10,192.168.2.2-192.168.3.2\n"
s+="inbound,tcp,10,192.168.0.2-192.168.3.4\n"

s+="inbound,tcp,100,192.168.1.2\n"
s+="inbound,tcp,100,192.168.1.2-192.168.3.4\n"

s+="inbound,tcp,1000,192.168.1.2\n"
s+="inbound,tcp,1000,192.168.2.2-192.168.3.4\n"

file4 = open("overlap.csv","w")
file4.write(s)

s = "direction,protocol,port,ip_address\n"
s += "inbound,tcp,80,192.168.1.2\n" 
s += "outbound,tcp,10000-20000,192.168.10.11\n" 
s += "inbound,udp,53,192.168.1.1-192.168.2.5\n" 
s += "outbound,udp,1000-2000,52.12.48.92\n"
file5 = open("given.csv","w")
file5.write(s)


