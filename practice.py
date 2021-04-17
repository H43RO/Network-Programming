import ipaddress
addr4 = ipaddress.ip_address('192.0.2.1')
print(addr4)

net = ipaddress.ip_network('114.71.220.0/24')
for x in net.hosts():
    print(x)

addr = ipaddress.ip_address('114.71.220.95')
print(addr in net)
addr = ipaddress.ip_address('192.168.0.1')
print(addr in net)

import socket
name = socket.gethostname()
print(name)
print(socket.gethostbyname(name))
print(socket.gethostbyname('homepage.sch.ac.kr'))
print(socket.gethostbyname_ex('homepage.sch.ac.kr'))
print(socket.gethostbyaddr('220.69.189.98'))
print(socket.getfqdn('220.69.189.98'))
print(socket.getfqdn('www.google.com'))

import socket

HOSTS = [
    'www.sch.ac.kr',
    'homepage.sch.ac.kr',
    'www.daum.net',
    'www.google.com',
    'iot'
]

for host in HOSTS:
    try:
        print('{} : {}'.format(host, socket.gethostbyname(host)))
    except socket.error as msg:
        print('{} : {}'.format(host, msg))

print(socket.getservbyname('http'))
print(socket.getservbyname('ftp'))
print(socket.getservbyname('ssh'))
print(socket.getservbyname('https'))

print(socket.getservbyport(80))
print(socket.getservbyport(25))
print(socket.getservbyport(1123))

for port in [80, 443, 21, 25, 143, 993, 110, 995]:
    url = '{}://example.co.kr/'.format(socket.getservbyport(port))
    print('{:4d}'.format(port), url)

import binascii
import sys

for string_address in ['114.71.220.95']:
    packed = socket.inet_aton(string_address)
    print('Original : ', string_address)
    print('Packed : ', binascii.hexlify(packed))
    print('Unpacked : ', socket.inet_ntoa(packed))

a = 1234
print(hex(a))
b = socket.htons(a)
print(hex(b))

c = socket.ntohs(b)
print(hex(c))