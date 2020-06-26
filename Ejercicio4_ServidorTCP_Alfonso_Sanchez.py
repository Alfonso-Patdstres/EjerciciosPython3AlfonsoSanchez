import socket


class ServidorTCP:
    host = None
    puerto = None
    server = None
    clienteConexion = None
    clienteDireccion = None
    contador = 0
    mensaje = None
    salir = False

    def __init__(self, ip, port):
        self.host = ip
        self.puerto = port
        self.server = socket.socket()
        print('Se a creado un soket para el servidot')
        self.server.bind((self.host, self.puerto))
        self.server.listen()
        while not self.salir:
            self.clienteConexion, self.clienteDireccion = self.server.accept()
            self.contador += 1
            # print('Connection {} accepted of {}'.format(self.contador, self.clienteDireccion))
            print(f'Conexion numero {self.contador} de {self.clienteDireccion}')
            self.leer()
            if self.data == b'Cerrar':
                self.salir = True
        self.server.close()

    def leer(self):
        self.data = self.clienteConexion.recv(1024)
        print(self.data)
        if self.data != b'':
            self.mandarM('Mensaje recibido')

    def mandarM(self, mensaje):
        self.mensaje = mensaje
        b_bytes = self.mensaje.encode()
        self.clienteConexion.send(b_bytes)
        print('Conexion cerrada')
        self.clienteConexion.close()


ServidorTCP('127.0.0.1', 35491)
