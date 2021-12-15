import socket
import threading


def receive():
    while True:
        try:
            msg=s.recv(1024).decode('utf-8')
            if(msg=='NICKNAME'):
                s.send(NICKNAME.encode('utf-8'))
            else:
                print(msg)
        except:
            print('An error occured')
            s.close()
            break
def write():
    while True:
        msg=input()
        s.send(f"{NICKNAME} : {msg}".encode('utf-8'))

if __name__=="__main__":
    NICKNAME=input('Enter a nickname: ')
    host='139.59.28.214'
    port=4001
    s=socket.socket()
    s.connect((host,port))

    t1=threading.Thread(target=receive)
    t2=threading.Thread(target=write)

    t1.start()
    t2.start()




    