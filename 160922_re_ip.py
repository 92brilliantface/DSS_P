import re

ip1 = '192.168.0.114'
ip2 = '192.168.112.'

ip = [ip1, ip2]

ip_correct = re.compile(r'\w+.\w+.\w+.\w+$')

for address in ip:
    if ip_correct.search(address) != None:
        print ip_correct.search(address).group()