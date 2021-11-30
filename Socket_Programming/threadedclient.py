from socket import *
import threading

class ClientServer():

	def listenOtherClients(self, server):

		while True:
			clientUsername=server.recv(1024)
			clientMessage=server.recv(1024)
			if clientMessage=="exit":
				print (clientUsername , " is closed")
			else:
				print (clientUsername , " says: ", clientMessage.decode("utf-8"))

	def __init__(self,serverport, servername, clientserverport):

		try:
			clientSocket=socket(AF_INET,SOCK_STREAM)
		except:
			print ("Socket cannot be created!!!")
			exit(1)
		
		print ("Socket is created...")

		try:
			clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		except:
			print ("Socket cannot be used!")
			exit(1)

		print ("Socket can be used well")

		try:
			clientSocket.bind(('', clientserverport))
		except:
			print ("Binding is unsuccessfull!")
			exit(1)

		print ("Binding is successfull.")

		clientSocket.listen(45)

		clientSocket.connect((servername,serverport))

		while True:
			username=input('Username:')
			message=input('Type message:')

			clientSocket.send(username.encode())
			clientSocket.send(message.encode())
			if message=="exit":
				clientSocket.close()
				exit(0)
			else:
				print("Message is sent.")

			connectionSocket,addr=clientSocket.accept()
			threading.Thread(target = self.listenOtherClients,args = (connectionSocket) ).start()
            


if __name__=="__main__":

	serverName="192.168.0.33"
	serverPort=12000
	clientServerPort=13000
	ClientServer(serverPort, serverName, clientServerPort)