# Herencia y poliformismo

class Figura:
        # #atributos
        def __init__(self, lado, tamanio):
            self.nLados = lado
            self.tLado = tamanio

        # metodos
        def mostarNlados(self):
            print('El numero de ', type, ' es:', self.nLados)

        def mostrarTlados(self):
            print('El tamaño del lado es:', self.tLado)

        def perimetro(self):
            print('El perimetro es:', self.nLados * self.tLado)

class Rectangulo(Figura):
    pass

class Triangulo(Figura):
    pass

# Encapsulación
class Estudiante:
    # Atributos
    __nombre = ' '
    __correo = ' '
    __password = ' '

    def __init__(self):
        self.__nombre = ' '
        self.__correo = ' '
        self.__password = ' '

    def inNombre(self, nombre):
        self.__nombre = nombre

    def inCorreo(self, correo):
        self.__correo = correo

    def inPassword(self, password):
        self.__password = password

    def mostrarNombre(self):
        print('El nombre es: ')
        return self.__nombre

    def mostrarCorreo(self):
        print(f'El correo es: ')
        return self.__correo

    def mostrarPassword(self):
        print(f'La contraseña es: ')
        return self.__password

if __name__ == '__main__':
    r1 = Rectangulo(4,2)
    t1 = Triangulo(3,10)
    r1.perimetro()
    t1.perimetro()

    e = Estudiante()
    e.inNombre('Alfonso Sanchez')
    e.inCorreo('correo@prueba.com')
    e.inPassword('1234')
    print(e.mostrarNombre())
    print(e.mostrarCorreo())
    print(e.mostrarPassword())


