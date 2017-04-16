import binascii
import re

def dec_to_bin(x):
    return int(bin(x)[2:])

#Input IP and Subnet
ip  = raw_input("Enter a valid ip: ")
subnet = raw_input("Etner a valid subnet mask: ")

#creates lists for ip
ip = ip.replace('.', ' ')
ip = ip.split()
ip = [int(i) for i in ip]
#creates lists for subnet
subnet = subnet.replace('.', ' ')
subnet = subnet.split()
subnet = [int(i) for i in subnet]

#creates binary lists
# old code = ipbinary = ["{0:b}".format(i) for i in ip]
#fixes missing leading zeroes issue
ipbinary = [bin(i)[2:].zfill(8) for i in ip]
subnetbinary = [bin(i)[2:].zfill(8) for i in subnet]

#separate groups and regroup
ipbinary1 = [int(i) for i in str(ipbinary[0])]
ipbinary2 = [int(i) for i in str(ipbinary[1])]
ipbinary3 = [int(i) for i in str(ipbinary[2])]
ipbinary4 = [int(i) for i in str(ipbinary[3])]
ipbinary = ipbinary1 + ipbinary2 + ipbinary3 + ipbinary4
subnetbinary1 = [int(i) for i in str(subnetbinary[0])]
subnetbinary2 = [int(i) for i in str(subnetbinary[1])]
subnetbinary3 = [int(i) for i in str(subnetbinary[2])]
subnetbinary4 = [int(i) for i in str(subnetbinary[3])]
subnetbinary = subnetbinary1 + subnetbinary2 + subnetbinary3 + subnetbinary4

networkipTF = list(i[0] == i[1] == 1 for i in zip(subnetbinary, ipbinary))

networkip = []

for i in networkipTF:
    if i == True:
        networkip.append(1)
    else:
        networkip.append(0)


networkip1 = str(networkip[0]) + str(networkip[1]) + str(networkip[2]) + str(networkip[3]) + str(networkip[4]) + str(networkip[5]) + str(networkip[6]) + str(networkip[7])
networkip2 = str(networkip[8]) + str(networkip[9]) + str(networkip[10]) + str(networkip[11]) + str(networkip[12]) + str(networkip[13]) + str(networkip[14]) + str(networkip[15])
networkip3 = str(networkip[16]) + str(networkip[17]) + str(networkip[18]) + str(networkip[19]) + str(networkip[20]) + str(networkip[21]) + str(networkip[22]) + str(networkip[23])
networkip4 = str(networkip[24]) + str(networkip[25]) + str(networkip[26]) + str(networkip[27]) + str(networkip[28]) + str(networkip[29]) + str(networkip[30]) + str(networkip[31])
ni1 = str(int(networkip1, 2))
ni2 = str(int(networkip2, 2))
ni3 = str(int(networkip3, 2))
ni4 = str(int(networkip4, 2))
print "Your network ip is %s" % (ni1+"."+ni2+"."+ni3+"."+ni4)
usable_hosts = 2 ** subnetbinary.count(0) - 2
print "You have %s usable hosts." % (usable_hosts)
