# Importar libreria Pickle
try:
    import cPpickle as pickle
except ImportError:
    import pickle
# Importar Shelve
import shelve


class Estudiante:
    # Atributos
    __nombre = ' '
    __apellido = ' '
    __correo = ' '
    __password = ' '

    def __init__(self, n, a, c, p):
        self.__nombre = n
        self.__apellido = a
        self.__correo = c
        self.__password = p

    def inNombre(self, nombre):
        self.__nombre = nombre

    def inApellido(self, apellido):
        self.__apellido = apellido

    def inCorreo(self, correo):
        self.__correo = correo

    def inPassword(self, password):
        self.__password = password

    def mostrarNombre(self):
        return self.__nombre

    def mostrarApellido(self):
        return self.__apellido

    def mostrarCorreo(self):
        print(f'El correo es: ')
        return self.__correo

    def mostrarPassword(self):
        print(f'La contraseña es: ')
        return self.__password

    def __str__(self):
        return f'Nombre: {self.__nombre}\n'\
               f'Apellido: {self.__apellido}\n'\
               f'Correo: {self.__correo}\n'\
               f'Contraseña: {self.__password}\n'


# Clase pickle
class Spickle:
    # Guardar en Pikel
    def saveStudentP(student):
        # Creacion archivo para pickle
        archivoP = open('studenp.db', 'ab')
        pickle.Pickler(archivoP, 4).dump(student)
        archivoP.close()

    # Leer en Pickle
    def readStudentP(nombre, apellido):
        error = False
        # Carga todos los tados en una lista
        datos = list(Spickle.loadall('studenp.db'))
        # Buscar donde esta el objeto
        for i in datos:
            if Estudiante.mostrarNombre(i) == nombre \
                    and Estudiante.mostrarApellido(i) == apellido:
                error = False
                return i
            else:
                error = True
        if error == True:
            return (f"Error, estudiante \"{nombre} {apellido}\" no encontrado")

    # Actualizar en Pickle
    def updateStudentP(student):
        error = False
        ii= 0
        # Carga todos los datos en una lista
        datos = list(Spickle.loadall('studenp.db'))
        # Variables para buscar el antiguo objeto
        nombre = Estudiante.mostrarNombre(student)
        apellido = Estudiante.mostrarApellido(student)
        # Buscar donde esta el objeto
        for i in datos:
            if Estudiante.mostrarNombre(i) == nombre\
            and Estudiante.mostrarApellido(i) == apellido:
                error = False
                print(f'\tDato anterior\n{i}')
                break
            else:
                error = True
                ii += 1
        if error == True:
            print(f'Error, estudiante no encontrado')
        else:
            del datos[ii]
            datos.insert(ii,student)
            # Borramos archivo
            archivoP = open('studenp.db', 'wb')
            archivoP.close()
            # Guardamos datos actualizado
            for i in datos:
                Spickle.saveStudentP(i)
            # Leemos el nuevo dato del archivo students.db
            print(f'\tNuevo dato\n{Spickle.readStudentP(nombre,apellido)}')

    # Leer todos los objetos
    def loadall(filename):
        with open(filename, "rb") as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break

# Clase Shelve
class Sshelve:
    _key = 0
    # Guardar en Shelve
    def saveStudentS(student):
        # Creacion archivo para shelve
        # archivoS = open('students', 'ab')
        with shelve.open('stutents') as s:
            s[str(Sshelve._key)] = student
            s.close()
            Sshelve._key += 1

    # Leer en Shelve
    def readStudentS(nombre, apellido):
        error = False
        with shelve.open('stutents') as s:
            for i in s:
                if Estudiante.mostrarNombre(s[i]) == nombre \
                        and Estudiante.mostrarApellido(s[i]) == apellido:
                    error = False
                    return s[i]
                else:
                    error = True
            if error == True:
                return (f"Error, estudiante \"{nombre} {apellido}\" no encontrado")
            s.close()

    def updateStudentS(student):
        error = False
        nombre = Estudiante.mostrarNombre(student)
        apellido = Estudiante.mostrarApellido(student)
        # Buscar donde esta el objeto
        with shelve.open('stutents') as s:
            for i in s:
                if Estudiante.mostrarNombre(s[i]) == nombre\
                        and Estudiante.mostrarApellido(s[i]) == apellido:
                    error = False
                    print(f'\tDato anterior\n{s[i]}')
                    del s[i]
                    s.close()
                    Sshelve.saveStudentS(student)
                    break
                else:
                    error = True
            Sshelve.saveStudentS(student)
            if error == True:
                print(f'Error, estudiante no encontrado')
            else:
                print(f'\tNuevo dato\n{Sshelve.readStudentS(nombre, apellido)}')