import socket


class ServidorUTP:
    server = None
    host = None
    puerto = None
    contador = 0
    direccion = None
    data = None
    mensaje = None
    salir = False

    def __init__(self, ip, port):
        self.host = ip
        self.puerto = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print('Se ha creado el socket para el servidor UDP')
        self.server.bind((self.host, self.puerto))
        print('Esperando por paquetes')
        self.leer()

    def leer(self):
        while not self.salir:
            self.data, self.direccion = self.server.recvfrom(1024)
            self.contador += 1
            print(f'[{self.contador}] Memsaje: {self.data} de {self.direccion}')
            # self.mensaje = 'Mensaje recibido'
            # self.server.sendto(self.mensaje.encode(), self.direccion)
            self.mandarM('Mensaje recibido')
            if self.data == b'Cerrar':
                self.salir = True
                self.mandarM('Cerrar')
                self.server.close()

    def mandarM(self, msg):
        self.mensaje = msg
        self.server.sendto(self.mensaje.encode(), self.direccion)


ServidorUTP('127.0.0.1', 35491)
