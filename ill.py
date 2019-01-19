import csv
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Firewall:
    fwall = {}
    IT = {}
    IU = {}
    OT = {}
    OU = {}
    def __init__(self, path):
        file = open(path)
        f_csv = csv.DictReader(file)
        for row in f_csv:
            if row["direction"] == "inbound" and row["protocol"] == "tcp":
                self.inithelper(self.IT, row["port"],row["ip_address"])
            elif row["direction"] == "inbound" and row["protocol"] == "udp":
                self.inithelper(self.IU, row["port"],row["ip_address"])
            elif row["direction"] == "outbound" and row["protocol"] == "tcp":
                self.inithelper(self.OT, row["port"],row["ip_address"])
            elif row["direction"] == "outbound" and row["protocol"] == "udp":
                self.inithelper(self.OU, row["port"],row["ip_address"])
        self.fwall["IT"] = self.IT
        self.fwall["IU"] = self.IU
        self.fwall["OT"] = self.OT
        self.fwall["OU"] = self.OU
    def inithelper(self, typedic, port, ip):
        ports = port.split('-')
        for i in range(len(ports)):
            ports[i] = int(ports[i])
        if len(ports) == 1:
            ports.append(ports[0])
        #print (ip)
        ips = ip.split('-')
        for i in range(len(ips)):
            l = ips[i].split('.')
            ipnum = 0
            for ll in l:
                ipnum *= 256
                ipnum += int(ll)
            ips[i] = ipnum
        if len(ips) == 1:
            ips.append(ips[0])
        for p in range(ports[0],ports[1]+1):
            if p in typedic: #port aleady in dic
                head = typedic[p] #head [ip1,ip2]. typedic[p] [[ip1,ip2],[ip3,ip4]...]
                dummy = ListNode([-1,-1])
                dummy.next = head
                pre = dummy
                cur = pre.next
                while cur != None:
                    if ips[0] > cur.val[1]:
                        pre = cur
                        cur = cur.next
                        continue
                    if ips[0] > pre.val[1] and ips[1] < cur.val[0]:
                        newnode =  ListNode(ips)
                        pre.next = newnode
                        newnode.next = cur
                        break
                    else:
                        if ips[0] > pre.val[1] and ips[0] < cur.val[0]:
                            cur.val[0] = ips[0]
                        if ips[1] <= cur.val[1]:
                            break #overlap with record
                        pre2 = cur
                        cur2 = cur.next
                        while cur2 != None:
                            if ips[1] > cur2.val[1]:
                                pre2 = cur2
                                cur2 = cur2.next
                                continue
                            if ips[1] > pre2.val[1] and ips[1] < cur2.val[0]:
                                cur.val[1] = ips[1]
                                cur.next = cur2
                                pre2.next = None
                                break
                            else:
                                cur.val[1] = cur2.val[1]
                                cur.next = cur2.next
                                cur2.next = None
                                break
                        if cur2 == None:
                            cur.val[1] = ips[1]
                            cur.next = None
                        break
                if cur == None:
                    newnode = ListNode(ips)
                    pre.next = newnode
                typedic[p] = dummy.next
            else: #port not in dic
                typedic[p] = ListNode(ips)
    def accept_helper(self,typedic,port,ip_address):
        if port not in typedic:
            return False
        else:
            head = typedic[port]
            cur = head
            l = ip_address.split('.')
            ipnum = 0
            for ll in l:
                ipnum *= 256
                ipnum += int(ll)
            while cur != None:
                if ipnum > cur.val[1]:
                    cur = cur.next
                    continue
                if ipnum < cur.val[0]:
                    return False
                else:
                    #print(cur.val)
                    return True
            return False

    def accept_packet(self, direction, protocol, port, ip_address):
        if direction == "inbound" and protocol == "tcp":
            return self.accept_helper(self.fwall["IT"], port, ip_address)
        elif direction == "inbound" and protocol == "udp":
            return self.accept_helper(self.fwall["IU"], port, ip_address)
        elif direction == "outbound" and protocol == "tcp":
            return self.accept_helper(self.fwall["OT"], port, ip_address)
        elif direction == "outbound" and protocol == "udp":
            return self.accept_helper(self.fwall["OU"], port, ip_address)



path = ["overlap.csv","given.csv","norange.csv","rangeport.csv","rangeipport.csv"]

for pa in path:
    print("data loading ......")
    fw = Firewall(pa)
    print("=========data load finish=========")
    """ #for show all ip range in IT
    for p in fw.fwall["IT"]:
        head = fw.fwall["IT"][p]
        while head!=None:
            print(p,head.val)
            head = head.next
        print("\n")
    """
    #given data test
    if (pa == "given.csv"):
        if ((fw.accept_packet("inbound", "tcp", 80, "192.168.1.2") == True) and
           (fw.accept_packet("inbound", "udp", 53, "192.168.2.1") == True) and
           (fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11") == True) and
           (fw.accept_packet("inbound", "tcp", 81, "192.168.1.2") == False) and
           (fw.accept_packet("inbound", "udp", 24, "52.12.48.92") == False)):
            print("given test pass")
        else:
            print("given test  Failed")


    #ip overlap test
    elif (pa == "overlap.csv"):
        if ((fw.accept_packet("inbound", "tcp", 80, "192.168.1.3") == False) and
           (fw.accept_packet("inbound", "tcp", 80, "192.168.1.2") == True) and
           (fw.accept_packet("inbound", "tcp", 800, "192.168.1.3") == False) and
           (fw.accept_packet("inbound", "tcp", 800, "192.168.1.2") == True) and
           (fw.accept_packet("inbound", "tcp", 8000, "192.168.1.2") == True) and
           (fw.accept_packet("inbound", "tcp", 8000, "192.168.3.3") == False) and
           (fw.accept_packet("inbound", "tcp", 10, "192.168.3.4") == True) and
           (fw.accept_packet("inbound", "tcp", 10, "192.168.3.5") == False) and
           (fw.accept_packet("inbound", "tcp", 100, "192.168.1.3") == True) and
           (fw.accept_packet("inbound", "tcp", 100, "192.168.1.0") == False) and
           (fw.accept_packet("inbound", "tcp", 1000, "192.168.1.3") == False) and
           (fw.accept_packet("inbound", "tcp", 1000, "192.168.3.3") == True) and
           (fw.accept_packet("inbound", "tcp", 1000, "192.168.4.3") == False)):
            print("overlap test pass")
        else:
            print("overlap test  Failed")

    #ips and ports are both single value instead of range
    elif (pa == "norange.csv"):
       if ((fw.accept_packet("inbound", "tcp", 1, "0.0.0.0") == True) and 
           (fw.accept_packet("inbound", "udp", 10001, "80.80.85.80") == False) and
           (fw.accept_packet("outbound", "tcp", 21006, "160.80.160.240") == False) and
           (fw.accept_packet("inbound", "tcp", 65005, "240.160.80.0") == False) and
           (fw.accept_packet("inbound", "udp", 55006, "240.160.79.0") == False)):
           print("norange test pass")
       else:
            print("norange test  Failed")
    #ports are ranged and ips are single
    elif (pa == "rangeport.csv"):
        if ((fw.accept_packet("inbound", "tcp", 1, "0.0.0.0") == True) and 
           (fw.accept_packet("inbound", "udp", 10001, "80.80.85.80") == False) and
           (fw.accept_packet("outbound", "tcp", 21006, "160.80.160.240") == True) and
           (fw.accept_packet("inbound", "tcp", 65005, "240.160.80.0") == True) and
           (fw.accept_packet("inbound", "udp", 55006, "240.160.86.0") == False)):
           print("rangeport test pass")
        else:
            print("rangeport test  Failed")
    #both ips and ports are ranged
    elif (pa == "rangeipport.csv"):
        if ((fw.accept_packet("inbound", "tcp", 1, "0.0.0.0") == True) and 
           (fw.accept_packet("inbound", "udp", 10001, "80.80.85.80") == True) and
           (fw.accept_packet("outbound", "tcp", 21006, "160.80.176.240") == False) and
           (fw.accept_packet("inbound", "tcp", 65020, "240.160.80.10") == False) and
           (fw.accept_packet("inbound", "udp", 55006, "240.160.86.0") == True)):
           print("rangeipport test pass")
        else:
            print("rangeipport test  Failed")

    


