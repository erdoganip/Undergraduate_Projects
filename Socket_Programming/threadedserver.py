from socket import *
import threading

class ThreadedServer():

    def sendToClient(self, client, username, message):

        while True:

            for c in clientset:
                c.sendall(username)
                c.sendall(message)


    def listenToClient(self, client, addr):
        
        while True:

            clientUsername= client.recv(1024)
            clientMessage= client.recv(1024)
            if message == "exit":
                clientset.remove(client)
                client.close()
            threading.Thread(target = self.listenToClient,args = (connectionSocket, clientUsername, clientMessage)).start()

    def __init__(self,serverPort):
        clientset= set()

        try:
            serverSocket=socket(AF_INET,SOCK_STREAM)

        except:
    
            print ("Socket cannot be created!!!")
            exit(1)
            
        print ("Socket is created...")

        try:
            serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        except:
    
            print ("Socket cannot be used!!!")
            exit(1)

        print ("Socket is being used...")

        try:
            serverSocket.bind(('',serverPort))
        except:
        
            print ("Binding cannot be done!!!")
            exit(1)

        print ("Binding is done...")

        try:
            serverSocket.listen(45)
        except:
    
            print ("Server cannot listen!!!")
            exit(1)

        print ("The server is ready to receive")


        while True:

            connectionSocket,addr=serverSocket.accept()
            clientset.add(client)
            
            threading.Thread(target = self.listenToClient,args = (connectionSocket,addr)).start()
            

if __name__=="__main__":
    serverPort=12000
    ThreadedServer(serverPort)