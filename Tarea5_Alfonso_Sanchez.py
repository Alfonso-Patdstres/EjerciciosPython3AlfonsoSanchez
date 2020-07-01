from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Slot

from ventana import Ui_MainWindow
import Tarea4

import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Tarea5')

        self.ui.guardarB.clicked.connect(self.guardar)
        self.ui.buscarB.clicked.connect(self.buscar)
        self.ui.leertodosB.clicked.connect(self.mostarTodos)
        self.ui.actualizarB.clicked.connect(self.actualizar)
        self.ui.limpiarB.clicked.connect(self.ui.log.clear)
        self.ui.eliminarB.clicked.connect(self.eliminar)

    @Slot()
    def guardar(self):
        Tarea4.escribirMe(self.ui.guardarnombre.text(), self.ui.guardarcorreo.text(), self.ui.guardarcontra.text())
        self.ui.guardarnombre.clear()
        self.ui.guardarcorreo.clear()
        self.ui.guardarcontra.clear()

    @Slot()
    def buscar(self):
        bn = self.ui.buscarnombre.text()
        self.ui.log.append('Estudiantes encontrados:')
        self.ui.log.append(Tarea4.leerMe(bn))

    @Slot()
    def mostarTodos(self):
        text = 'MOSTRANDO TODOS LOS ESTUDIANTES\n' \
               f'------------------------------' \
               f'------------------------------'

        self.ui.log.append(text)

        for o in Tarea4.estudiantes.objects:
            self.ui.log.append(Tarea4.leerMe(o.nombre))

        text = f'------------------------------' \
               f'------------------------------'

        self.ui.log.append(text)

    @Slot()
    def actualizar(self):
        buscar = self.ui.buscarnombre.text()
        nombre = self.ui.actualizarnombre.text()
        correo = self.ui.actualizarcorreo.text()
        contra = self.ui.actualizarcontrasena.text()
        self.ui.log.append(f'Estudiante actualizado \n{Tarea4.actualizarMe(buscar, nombre, correo, contra)}')
        self.ui.actualizarnombre.clear()
        self.ui.actualizarcorreo.clear()
        self.ui.actualizarcontrasena.clear()

    @Slot()
    def eliminar(self):
        eid = self.ui.estudianteid.text()
        self.ui.log.append(f'ELIMINADO estudiante  {Tarea4.borrarMe(eid)}')


        text = f'------------------------------' \
               f'------------------------------'

        self.ui.log.append(text)


if __name__ == '__main__':
    app = QApplication()

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

