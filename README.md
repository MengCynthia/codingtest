# Coding Assignment
1. The data loaded are orignized like the following:
fwall{
    "IT":{
        port1:[ip1,ip2]->[ip3,ip4]->... , //Linked List
        port2:[ip1,ip2]->[ip3,ip4]->... , //Linked List
        port3:[ip1,ip2]->[ip3,ip4]->... , //Linked List
        ...
    },
    "IU":{...},
    "OT":{...},
    "OU":{...}
}

Ports do not contain range, all the ports in range form like "10-20" will be expanded to be 10,11,12...20,
so that if the file contains overlaped ports, it just needs to add ip address instead of cut down the port range
and create something new.

Ip address will be managed by a linked list of each port. All the value of a listnode is a two-value list:[ip1,ip2].
All the ip value is recaculated to a single int: 
       192.168.2.1. ----> 192*256^3 + 168*256^2 + 2*256 + 1
and all the node are linked by an ascending order of the first value in the two-value list.
So that, the space can be saved and the time to tranverse will be decreased as well.

2. To test the solution, I generated 5 files.
  1) the given data and test in the assignment
  2) all the ips and ports have no range
  3) ports have range
  4) both ports and ips have range
  5) the ips of same ports are overlaped. this test aims to test if the data processing is able to deal with ip overlapping or not.
  
  Each file has their own testcase.
3. All the test are passed immediately are the data are loaded.
4. If I have more time, I will generate more testfile and testcase. Also I will try to find more efficient solutions.
#Team Interested
First is data team
Second is platform team
