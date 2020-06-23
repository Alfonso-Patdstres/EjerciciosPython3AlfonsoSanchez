# Importar StudentIO
import StudentIO

# Creacion de estudiantes
e1 = StudentIO.Estudiante('alfonso', 'sanchez', 'alfsan@gmail', '1234')
e2 = StudentIO.Estudiante('alonso', 'ponce', 'alpon@hotmail.com', 'abcd')
e3 = StudentIO.Estudiante('juan', 'perez', 'juanper@outlook.com', '1q2w')
e4 = StudentIO.Estudiante('pedro', 'hernandez', 'pedher@yahoo.com', 'q2w3')
e5 = StudentIO.Estudiante('maria', 'lopez', 'marlo@gmail.com', '0987')

if __name__ == '__main__':
# Ingresar estudiantes al archivo de pickle
#     StudentIO.Spickle.saveStudentP(e1)
#     StudentIO.Spickle.saveStudentP(e2)
#     StudentIO.Spickle.saveStudentP(e3)
#     StudentIO.Spickle.saveStudentP(e4)
#     StudentIO.Spickle.saveStudentP(e5)

# Ingresar estudiantes al archivo de shelve
#     StudentIO.Sshelve.saveStudentS(e1)
#     StudentIO.Sshelve.saveStudentS(e2)
#     StudentIO.Sshelve.saveStudentS(e3)
#     StudentIO.Sshelve.saveStudentS(e4)
#     StudentIO.Sshelve.saveStudentS(e5)

# Leer estudiantes del arichivo pickle
#     print(StudentIO.Spickle.readStudentP('pedro', 'hernandez'))
#     print(StudentIO.Spickle.readStudentP('a', 'b'))

# Leer estudiantes del arichivo shelve
#     print(StudentIO.Sshelve.readStudentS('pedro', 'hernandez'))
#     print(StudentIO.Sshelve.readStudentS('a', 'b'))

# Modificar estudiante en pickel
    # e5 = StudentIO.Estudiante('maria', 'lopez', 'marlo@hotmail.mx', '0987')
    # print(StudentIO.Spickle.updateStudentP(e5))

# Modificar estudiante en shelve
    e5 = StudentIO.Estudiante('maria', 'lopez', 'marlo@hotmail.com', '0987')
    print(StudentIO.Sshelve.updateStudentS(e5))
