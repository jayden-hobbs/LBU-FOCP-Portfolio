import socket
import threading

def handle_client(client, addr):
    print(f"New connection from {addr}")
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(f"Message: {message}")
        except:
            print(f"Connection closed by {addr}.")
            client.close()
            break

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            client.send(message)
            try:
                client.send(message.encode('utf-8'))
            except:
                clients.remove(client)
                client.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555))
server.listen()

clients = []

print("Server is listening...")
client_socket, addr = server.accept()
print(f"Connection from {addr} has been established.")
clients.append(client_socket)
threading.Thread(target=handle_client, args=(client_socket, addr)).start()