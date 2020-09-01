import socket

HEADER = 64
PORT = 5050
SERVER = "192.168.0.109"
FORMAT = "utf-8"
ADDR =(SERVER ,PORT)
DISCONNECT_MESSAGE = "!DISCONNECT" 

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    #now making the message 64 bit
    send_length += b' ' * (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)
    print("[SERVER]" + client.recv(2048).decode(FORMAT))

send("hallo kevin")
send(input())
send(input())
send(DISCONNECT_MESSAGE) 