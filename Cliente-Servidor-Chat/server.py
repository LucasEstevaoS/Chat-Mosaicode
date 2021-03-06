import socket 
import select 
import sys 
from thread import *
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
  
IP_address = "192.168.0.104"
Port = 5500
  
server.bind((IP_address, Port))   

server.listen(100) 
  
list_of_clients = [] 
  
def clientthread(conn, addr): 
  
    
    conn.send("Welcome to this chatroom!") 
  
    while True: 
            try: 
                message = conn.recv(2048) 
                if message: 
                    print "<" + addr[0] + "> " + message 
                    #chama broadcast para enviar mensagem para todos                   
                    message_to_send = "<" + addr[0] + "> " + message 
                    broadcast(message_to_send, conn)   
                else: 
                    remove(conn)   
            except: 
                continue
  
#Envia mensagem para todos, exceto o remetente
def broadcast(message, connection): 
    for clients in list_of_clients: 
        if clients!=connection: 
            try: 
                clients.send(message) 
            except: 
                clients.close() 
  
                # if the link is broken, we remove the client 
                remove(clients) 
  

def remove(connection): 
    if connection in list_of_clients: 
        list_of_clients.remove(connection) 
  
while True: 
  
    conn, addr = server.accept() 
    #Mantém uma lista de clientes, para facilitar a transmissão uma mensagem para todas as pessoas disponíveis na sala de bate-papo
    list_of_clients.append(conn) 
  
    # print do endereco + conectado 
    print addr[0] + " connected"
  
    # criacao de thread 
   
    start_new_thread(clientthread,(conn,addr))     
  
conn.close() 
server.close() 
