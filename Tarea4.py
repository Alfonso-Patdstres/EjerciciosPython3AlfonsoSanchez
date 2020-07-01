# Importar Mongoengine
from mongoengine import *

# Definimos base de datos
connect('padts', host='localhost', port=27017)


# Esquema / Modelo
# class estudiantes(Document):
#     nombre = StringField(required=True)
#     apellido = StringField(required=True)
#     correo = StringField(required=True)
#     password = StringField(required=True)

class estudiantes(Document):
    nombre = StringField(required=True)
    correo = StringField(required=True)
    password = StringField(required=True)


# Escribir con mongoengine
# def escribirMe(nnombre, aapellido, ccorreo, ppassword):
#     estudiante = estudiantes(
#         nombre=str(nnombre),
#         apellido=str(aapellido),
#         correo=str(ccorreo),
#         password=str(ppassword)
#     )
#     estudiante.save()
def escribirMe(nnombre, ccorreo, ppassword):
    estudiante = estudiantes(
        nombre=str(nnombre),
        correo=str(ccorreo),
        password=str(ppassword)
    )
    estudiante.save()


# def leerMe(nnombre, aapellido):
#     error = True
#     for p in estudiantes.objects:
#         if p.nombre == nnombre and p.apellido == aapellido:
#             error = False
#             print(f'Estudiante:\n'
#                   f'Nombre: {p.nombre}\n'
#                   f'Apellido: {p.apellido}\n'
#                   f'Correo: {p.correo}\n'
#                   f'Contraseña: {p.password}')
#             n = p.nombre
#             return n
def leerMe(nnombre):
    error = True
    for p in estudiantes.objects:
        if p.nombre == nnombre:
            error = False
            print(f'Estudiante:\n'
                  f'Nombre: {p.nombre}\n'
                  f'Correo: {p.correo}\n'
                  f'Contraseña: {p.password}')
            return f'Nombre: {p.nombre}\n'\
                   f'Correo: {p.correo}\n'\
                   f'Contraseña: {p.password}'
    if error is True:
        print(f'Error, estudiente: \'{nnombre} \' no encontrado')
        return f'Error, estudiente: \'{nnombre}\' no encontrado'


# def actualizarMe(nnombre, aapellido, newn, newa, newc, newp):
#     error = True
#     for p in estudiantes.objects:
#         if p.nombre == nnombre and p.apellido == aapellido:
#             error = False
#             print(f'\t\nDatos viejos:\n')
#             leerMe(nnombre, aapellido)
#             p.nombre = newn
#             p.apellido = newa
#             p.correo = newc
#             p.password = newp
#             p.save()
#             print(f'\t\nDatos nuevos:\n')
#             leerMe(newn, newa)
#     if error is True:
#         print(f'Error, estudiente: \'{nnombre} {aapellido}\' no encontrado')
def actualizarMe(nnombre, newn, newc, newp):
    error = True
    for p in estudiantes.objects:
        if p.nombre == nnombre:
            error = False
            print(f'\t\nDatos viejos:\n')
            leerMe(nnombre)
            p.nombre = newn
            p.correo = newc
            p.password = newp
            p.save()
            print(f'\t\nDatos nuevos:\n')
            leerMe(newn)
            return leerMe(newn)
    if error is True:
        print(f'Error, estudiente: \'{nnombre}\' no encontrado')
        return f'Error, estudiente: \'{nnombre}\' no encontrado'

# def borrarMe(nnombre, aapellido):
#     error = True
#     for p in estudiantes.objects:
#         if p.nombre == nnombre and p.apellido == aapellido:
#             error = False
#             p.delete()
#         if error is False:
#             print(f'Estudiantes restantes: \n')
#             for o in estudiantes.objects:
#                 leerMe(o.nombre, o.apellido)
#                 print('')
#                 # print(f'Nombre: {o.nombre}\n'
#                 #       f'Apellido: {o.apellido}\n\n')
#             break
#     if error is True:
#         print(f'Error, estudiente: \'{nnombre} {aapellido}\' no encontrado')

def borrarMe(nnombre):
    error = True
    for p in estudiantes.objects:
        if p.nombre == nnombre:
            error = False
            p.delete()
            return f' {nnombre}'
        else:
            error = True
    if error is True:
        return f'Error, estudiente: \'{nnombre} \' no encontrado'


# # introducir / escribir  estudiantes
#escribirMe('alfonso', 'alfsan@gmail', '1234')
# escribirMe('alonso', 'ponce', 'alpon@hotmail.com', 'abcd')
# escribirMe('juan', 'perez', 'juanper@outlook.com', '1q2w')
# escribirMe('pedro', 'hernandez', 'pedher@yahoo.com', 'q2w3')
# escribirMe('maria', 'lopez', 'marlo@gmail.com', '0987')

# # Leer estudiantes
# print(leerMe('alfonso'))

# # Actualizar estudiantes
# actualizarMe('alfonso','sanchez','1', '2', '3', '4')

# # Borrar estudiantes
# borrarMe('1', '2')
