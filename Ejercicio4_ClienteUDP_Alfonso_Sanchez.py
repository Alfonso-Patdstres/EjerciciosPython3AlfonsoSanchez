import socket
import time


class ClienteUDP:
    clienteUDP = None
    host = None
    puerto = None
    direccion = None
    data = None
    mensaje = None
    salir = False

    def __init__(self, ip, port):
        self.host = ip
        self.puerto = port
        self.clienteUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.direccion = self.host, self.puerto
        # self.mandarM('Mensaje cliente')

    def mandarM(self, msg):
        contador = 0
        self.mensaje = msg
        while not self.salir:
            b_bytes = self.mensaje.encode()
            self.clienteUDP.sendto(b_bytes, self.direccion)
            self.leer()
            contador += 1
            if contador > 10:
                self.mensaje = 'Cerrar'
        self.clienteUDP.close()

    def leer(self):
        self.data, self.direccion = self.clienteUDP.recvfrom(1024)
        print(f'Mensaje: {self.data} de {self.direccion}')
        if self.data == b'Cerrar':
            self.salir = True
        time.sleep(2)


c1 = ClienteUDP('127.0.0.1', 35491)
c1.mandarM('Hola')