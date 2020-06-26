import socket
import time


class ClienteTCP:
    cliente = None
    mensaje = None
    host = None
    puerto = None
    salir = False

    def __init__(self, ip, port):
        self.host = ip
        self.puerto = port
        self.cliente = socket.socket()
        self.cliente.connect((self.host, self.puerto))
        print(f'Conectado al servidor {self.host} en el puerto {self.puerto}')

    def mandarM(self, mensaje):
        # while True:
        while not self.salir:
            # msg = 'Test3 send'
            msg = mensaje
            b_bytes = msg.encode()
            self.cliente.send(b_bytes)
            data = self.cliente.recv(1024)
            print(data)
            if data == b'Mensaje recibido':
                self.salir = True
            time.sleep(2)
        self.cliente.close()


c1 = ClienteTCP('127.0.0.1', 35491)
# ClienteTCP.mandarM(c1, 'hola')
ClienteTCP.mandarM(c1, 'Cerrar')
