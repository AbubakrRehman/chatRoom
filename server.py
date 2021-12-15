import socket
import threading



def broadcast(msg):
    for i in client_list:
        i.send(msg.encode('utf-8'))



def handle_client(client):
    while True:
        try:
            msg=client.recv(1024).decode('utf-8')
            broadcast(msg)
        except:
            index=client_list.index(client)
            client_list.remove(client)
            client.close()
            nickname=client_name_list[index]
            broadcast(f'{nickname} left the chat')
            client_name_list.remove(nickname)
            break
    

if __name__=="__main__":
    host=""
    port=4001

    s=socket.socket()
    s.bind((host,port))
    s.listen(5)

    client_list=[]
    client_name_list=[]
    print('listening for the clients !!! ')
    while True:
        client,addr=s.accept()
        print(f'connected to {str(addr[0])} | {str(addr[1])}')
        client_list.append(client)
        client.send('NICKNAME'.encode('utf-8'))
        client_name=client.recv(1024).decode('utf-8')
        print(f'Client name is {client_name}')
        broadcast(f'{client_name} joined the chat room')
        client_name_list.append(client_name)
        t=threading.Thread(target=handle_client,args=(client,))
        t.start()


    




