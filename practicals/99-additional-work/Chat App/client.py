#!/usr/bin/env python3

import socket
import threading

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Connection closed by the server.")
            client.close()
            break

def send():
    while True:
        message = input("")
        client.send(message.encode('utf-8'))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

threading.Thread(target=receive).start()
threading.Thread(target=send).start()