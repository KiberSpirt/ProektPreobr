import socket
import random

host = "127.0.0.1"
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
print("socket binded to port", port)
client = []

def get_client(addr):
    if addr == client[0]:
        return 0
    return 1

def wait_player():
    players = 0
    while players < 2:
        s.settimeout(None)
        data, addr = s.recvfrom(1024)
        players += 1
        client.append(addr)
        print(addr, 'connected')
    s.sendto('1'.encode('ascii'), client[0])
    s.sendto('1'.encode('ascii'), client[1])

while True:
    wait_player()