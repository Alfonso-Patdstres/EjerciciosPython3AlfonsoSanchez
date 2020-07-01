# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(553, 655)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.guardarnombre = QLineEdit(self.groupBox)
        self.guardarnombre.setObjectName(u"guardarnombre")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.guardarnombre)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.guardarcorreo = QLineEdit(self.groupBox)
        self.guardarcorreo.setObjectName(u"guardarcorreo")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.guardarcorreo)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.guardarcontra = QLineEdit(self.groupBox)
        self.guardarcontra.setObjectName(u"guardarcontra")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.guardarcontra)


        self.verticalLayout.addLayout(self.formLayout)

        self.guardarB = QPushButton(self.groupBox)
        self.guardarB.setObjectName(u"guardarB")

        self.verticalLayout.addWidget(self.guardarB)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buscarnombre = QLineEdit(self.groupBox_2)
        self.buscarnombre.setObjectName(u"buscarnombre")

        self.horizontalLayout.addWidget(self.buscarnombre)

        self.buscarB = QPushButton(self.groupBox_2)
        self.buscarB.setObjectName(u"buscarB")

        self.horizontalLayout.addWidget(self.buscarB)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.leertodosB = QPushButton(self.groupBox_2)
        self.leertodosB.setObjectName(u"leertodosB")

        self.verticalLayout_2.addWidget(self.leertodosB)


        self.verticalLayout_6.addWidget(self.groupBox_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.actualizarnombre = QLineEdit(self.groupBox_3)
        self.actualizarnombre.setObjectName(u"actualizarnombre")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.actualizarnombre)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.actualizarcorreo = QLineEdit(self.groupBox_3)
        self.actualizarcorreo.setObjectName(u"actualizarcorreo")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.actualizarcorreo)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.actualizarcontrasena = QLineEdit(self.groupBox_3)
        self.actualizarcontrasena.setObjectName(u"actualizarcontrasena")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.actualizarcontrasena)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.busqueda_actualizar = QLineEdit(self.groupBox_3)
        self.busqueda_actualizar.setObjectName(u"busqueda_actualizar")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.busqueda_actualizar)


        self.verticalLayout_3.addLayout(self.formLayout_2)

        self.actualizarB = QPushButton(self.groupBox_3)
        self.actualizarB.setObjectName(u"actualizarB")

        self.verticalLayout_3.addWidget(self.actualizarB)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.estudianteid = QLineEdit(self.groupBox_5)
        self.estudianteid.setObjectName(u"estudianteid")

        self.horizontalLayout_3.addWidget(self.estudianteid)

        self.eliminarB = QPushButton(self.groupBox_5)
        self.eliminarB.setObjectName(u"eliminarB")

        self.horizontalLayout_3.addWidget(self.eliminarB)


        self.verticalLayout_5.addWidget(self.groupBox_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.log = QTextEdit(self.groupBox_4)
        self.log.setObjectName(u"log")

        self.verticalLayout_4.addWidget(self.log)

        self.limpiarB = QPushButton(self.groupBox_4)
        self.limpiarB.setObjectName(u"limpiarB")

        self.verticalLayout_4.addWidget(self.limpiarB)


        self.verticalLayout_7.addWidget(self.groupBox_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 553, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tarea5 Pedro Valenzuela", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.guardarnombre.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.guardarB.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.buscarB.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.leertodosB.setText(QCoreApplication.translate("MainWindow", u"Leer Todos", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.busqueda_actualizar.setText("")
        self.actualizarB.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.eliminarB.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Log", None))
        self.limpiarB.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
    # retranslateUi

