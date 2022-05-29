import socket
import select
import tkinter as tk

window = tk.Tk()
host = '127.0.0.1'
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = (host, port)
s.connect(server)

def up_while_not_data():
    ready = select.select([s], [], [], 0.1)
    while not ready[0]:
        window.update()
        ready = select.select([s], [], [], 0.1)

def start():
    send_cell('1'.encode('ascii'))
    up_while_not_data()
    data = s.recvfrom(1024)

def send_cell(data):
    s.sendto(str(data).encode('ascii'), server)