import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER , PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

print(SERVER)
#make socket for connnection
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

#bind to address-->  means we bind this socket to this address so anything that connnect 
#to this address now that hits to this socket
server.bind(ADDR)


#for handle the client when any one is connected to this client
def handle_clients(conn ,addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while(connected):
        msg_lenght = conn.recv(HEADER).decode(FORMAT)
        if msg_lenght:
            msg_lenght = int(msg_lenght)
            #msg = conn.recv()  #blocking line mean this is stop tilll any message is recieved from client so it is not allow to other client
            msg = conn.recv(msg_lenght).decode(FORMAT)
            #print(f"[{addr}] {msg}")
            #now try for disconnection 
            if(msg == DISCONNECT_MESSAGE):
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Message Recived".encode(FORMAT))

    conn.close()



#for starting the server  to start listing for any clients and 
#then send it to handle_client where a each new client is handle by new thread
def start():

    server.listen()
    print(f"[SERVER] Server is listining on {SERVER}")
    while True:
        conn , addr = server.accept() #blocking line
        thread =  threading.Thread(target=handle_clients , args=(conn , addr))
        thread.start()
        #here we are going to fond the number of active connection but 
        # there is always 1 thread of this funtion so we subttract that
        print(f"[ACTIVE CONNECTION] {threading.activeCount()-1}")



print("[STARTING] server is starting...")
start()
 