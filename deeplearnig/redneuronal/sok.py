import SocketServer
import threading 


class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        # se lanza automaticamente al hacer un request
        self.data = self.request.recv(1024).strip()
        #datos de donde corre
        #print "{} wrote:".format(self.client_address[0])
        #print "-------------------------"
        #los datos
        #print self.data
        # responde al clienete con las mismas lineas que le envio pero en mayusculas
        self.request.sendall(self.data.upper())

class servidor(threading.Thread):
    def __init__(self,direccion, puerto):
        threading.Thread.__init__(self)  
        HOST, PORT = direccion,puerto
        global estado
        estado=1
        global server
        server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    def run(self):
        # Lanzamos el server
        server.serve_forever()