# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(597, 379)
        self.groupBoxEnter = QtWidgets.QGroupBox(Dialog)
        self.groupBoxEnter.setGeometry(QtCore.QRect(20, 20, 171, 125))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBoxEnter.setFont(font)
        self.groupBoxEnter.setObjectName("groupBoxEnter")
        self.labelFi = QtWidgets.QLabel(self.groupBoxEnter)
        self.labelFi.setGeometry(QtCore.QRect(10, 50, 15, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelFi.setFont(font)
        self.labelFi.setObjectName("labelFi")
        self.labelLam = QtWidgets.QLabel(self.groupBoxEnter)
        self.labelLam.setGeometry(QtCore.QRect(10, 80, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelLam.setFont(font)
        self.labelLam.setObjectName("labelLam")
        self.lineEditFiDeg = QtWidgets.QLineEdit(self.groupBoxEnter)
        self.lineEditFiDeg.setGeometry(QtCore.QRect(32, 50, 30, 20))
        self.lineEditFiDeg.setObjectName("lineEditFiDeg")
        self.labelDeg = QtWidgets.QLabel(self.groupBoxEnter)
        self.labelDeg.setGeometry(QtCore.QRect(30, 30, 40, 15))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelDeg.setFont(font)
        self.labelDeg.setObjectName("labelDeg")
        self.labelMin = QtWidgets.QLabel(self.groupBoxEnter)
        self.labelMin.setGeometry(QtCore.QRect(70, 30, 40, 15))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelMin.setFont(font)
        self.labelMin.setObjectName("labelMin")
        self.labelSec = QtWidgets.QLabel(self.groupBoxEnter)
        self.labelSec.setGeometry(QtCore.QRect(110, 30, 40, 15))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelSec.setFont(font)
        self.labelSec.setObjectName("labelSec")
        self.lineEditFiMin = QtWidgets.QLineEdit(self.groupBoxEnter)
        self.lineEditFiMin.setGeometry(QtCore.QRect(72, 50, 30, 20))
        self.lineEditFiMin.setObjectName("lineEditFiMin")
        self.lineEditFiSec = QtWidgets.QLineEdit(self.groupBoxEnter)
        self.lineEditFiSec.setGeometry(QtCore.QRect(113, 50, 30, 20))
        self.lineEditFiSec.setObjectName("lineEditFiSec")
        self.lineEditLamDeg = QtWidgets.QLineEdit(self.groupBoxEnter)
        self.lineEditLamDeg.setGeometry(QtCore.QRect(32, 80, 30, 20))
        self.lineEditLamDeg.setObjectName("lineEditLamDeg")
        self.lineEditLamMin = QtWidgets.QLineEdit(self.groupBoxEnter)
        self.lineEditLamMin.setGeometry(QtCore.QRect(72, 80, 30, 20))
        self.lineEditLamMin.setObjectName("lineEditLamMin")
        self.lineEditLamSec = QtWidgets.QLineEdit(self.groupBoxEnter)
        self.lineEditLamSec.setGeometry(QtCore.QRect(113, 80, 30, 20))
        self.lineEditLamSec.setObjectName("lineEditLamSec")
        self.WyborElipsy = QtWidgets.QGroupBox(Dialog)
        self.WyborElipsy.setGeometry(QtCore.QRect(215, 20, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.WyborElipsy.setFont(font)
        self.WyborElipsy.setObjectName("WyborElipsy")
        self.radioButtonGRS80 = QtWidgets.QRadioButton(self.WyborElipsy)
        self.radioButtonGRS80.setGeometry(QtCore.QRect(20, 20, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.radioButtonGRS80.setFont(font)
        self.radioButtonGRS80.setObjectName("radioButtonGRS80")
        self.radioButtonWGS84 = QtWidgets.QRadioButton(self.WyborElipsy)
        self.radioButtonWGS84.setGeometry(QtCore.QRect(20, 40, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.radioButtonWGS84.setFont(font)
        self.radioButtonWGS84.setObjectName("radioButtonWGS84")
        self.groupBoxZone = QtWidgets.QGroupBox(Dialog)
        self.groupBoxZone.setGeometry(QtCore.QRect(410, 20, 171, 125))
        self.groupBoxZone.setObjectName("groupBoxZone")
        self.radioButtonZ5 = QtWidgets.QRadioButton(self.groupBoxZone)
        self.radioButtonZ5.setGeometry(QtCore.QRect(20, 20, 82, 20))
        self.radioButtonZ5.setObjectName("radioButtonZ5")
        self.radioButtonZ6 = QtWidgets.QRadioButton(self.groupBoxZone)
        self.radioButtonZ6.setGeometry(QtCore.QRect(20, 45, 82, 20))
        self.radioButtonZ6.setObjectName("radioButtonZ6")
        self.radioButtonZ7 = QtWidgets.QRadioButton(self.groupBoxZone)
        self.radioButtonZ7.setGeometry(QtCore.QRect(20, 70, 82, 20))
        self.radioButtonZ7.setObjectName("radioButtonZ7")
        self.radioButtonZ8 = QtWidgets.QRadioButton(self.groupBoxZone)
        self.radioButtonZ8.setGeometry(QtCore.QRect(20, 95, 82, 20))
        self.radioButtonZ8.setObjectName("radioButtonZ8")
        self.groupBoxResults2000 = QtWidgets.QGroupBox(Dialog)
        self.groupBoxResults2000.setGeometry(QtCore.QRect(20, 210, 261, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBoxResults2000.setFont(font)
        self.groupBoxResults2000.setObjectName("groupBoxResults2000")
        self.X2000 = QtWidgets.QLabel(self.groupBoxResults2000)
        self.X2000.setGeometry(QtCore.QRect(10, 25, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.X2000.setFont(font)
        self.X2000.setText("")
        self.X2000.setObjectName("X2000")
        self.Y2000 = QtWidgets.QLabel(self.groupBoxResults2000)
        self.Y2000.setGeometry(QtCore.QRect(10, 50, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Y2000.setFont(font)
        self.Y2000.setText("")
        self.Y2000.setObjectName("Y2000")
        self.wyniki = QtWidgets.QLabel(Dialog)
        self.wyniki.setGeometry(QtCore.QRect(250, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.wyniki.setFont(font)
        self.wyniki.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.wyniki.setObjectName("wyniki")
        self.groupBoxResults1992 = QtWidgets.QGroupBox(Dialog)
        self.groupBoxResults1992.setGeometry(QtCore.QRect(305, 210, 271, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBoxResults1992.setFont(font)
        self.groupBoxResults1992.setObjectName("groupBoxResults1992")
        self.X1992 = QtWidgets.QLabel(self.groupBoxResults1992)
        self.X1992.setGeometry(QtCore.QRect(10, 25, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.X1992.setFont(font)
        self.X1992.setText("")
        self.X1992.setObjectName("X1992")
        self.Y1992 = QtWidgets.QLabel(self.groupBoxResults1992)
        self.Y1992.setGeometry(QtCore.QRect(10, 50, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Y1992.setFont(font)
        self.Y1992.setText("")
        self.Y1992.setObjectName("Y1992")
        self.groupBoxGrad = QtWidgets.QGroupBox(Dialog)
        self.groupBoxGrad.setGeometry(QtCore.QRect(215, 85, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.groupBoxGrad.setFont(font)
        self.groupBoxGrad.setObjectName("groupBoxGrad")
        self.radioButtonYes = QtWidgets.QRadioButton(self.groupBoxGrad)
        self.radioButtonYes.setGeometry(QtCore.QRect(20, 20, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.radioButtonYes.setFont(font)
        self.radioButtonYes.setChecked(True)
        self.radioButtonYes.setObjectName("radioButtonYes")
        self.radioButtonNo = QtWidgets.QRadioButton(self.groupBoxGrad)
        self.radioButtonNo.setGeometry(QtCore.QRect(20, 40, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.radioButtonNo.setFont(font)
        self.radioButtonNo.setObjectName("radioButtonNo")
        self.groupBoxdeg2grad = QtWidgets.QGroupBox(Dialog)
        self.groupBoxdeg2grad.setGeometry(QtCore.QRect(195, 299, 200, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBoxdeg2grad.setFont(font)
        self.groupBoxdeg2grad.setObjectName("groupBoxdeg2grad")
        self.FiGrad = QtWidgets.QLabel(self.groupBoxdeg2grad)
        self.FiGrad.setGeometry(QtCore.QRect(10, 20, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FiGrad.setFont(font)
        self.FiGrad.setText("")
        self.FiGrad.setObjectName("FiGrad")
        self.LamGrad = QtWidgets.QLabel(self.groupBoxdeg2grad)
        self.LamGrad.setGeometry(QtCore.QRect(10, 45, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LamGrad.setFont(font)
        self.LamGrad.setText("")
        self.LamGrad.setObjectName("LamGrad")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(215, 150, 171, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kalkulatora Geodezyjny"))
        self.groupBoxEnter.setTitle(_translate("Dialog", "Wsp????rz??dne wej??ciowe"))
        self.labelFi.setText(_translate("Dialog", "fi"))
        self.labelLam.setText(_translate("Dialog", "lam"))
        self.labelDeg.setText(_translate("Dialog", "Stopnie"))
        self.labelMin.setText(_translate("Dialog", "Minuty"))
        self.labelSec.setText(_translate("Dialog", "Sekundy"))
        self.WyborElipsy.setTitle(_translate("Dialog", "Wyb??r elipsoidy"))
        self.radioButtonGRS80.setText(_translate("Dialog", "GRS80"))
        self.radioButtonWGS84.setText(_translate("Dialog", "WGS84"))
        self.groupBoxZone.setTitle(_translate("Dialog", "Wyb??r strefy dla uk????du PL-2000"))
        self.radioButtonZ5.setText(_translate("Dialog", "5"))
        self.radioButtonZ6.setText(_translate("Dialog", "6"))
        self.radioButtonZ7.setText(_translate("Dialog", "7"))
        self.radioButtonZ8.setText(_translate("Dialog", "8"))
        self.groupBoxResults2000.setTitle(_translate("Dialog", "Wsp????rz??dne w uk????dnie PL-2000"))
        self.wyniki.setText(_translate("Dialog", "Wyniki"))
        self.groupBoxResults1992.setTitle(_translate("Dialog", "Wsp????rz??dne w uk????dnie PL-1992"))
        self.groupBoxGrad.setTitle(_translate("Dialog", "Czy przeliczy?? stopnie na grady?"))
        self.radioButtonYes.setText(_translate("Dialog", "Tak"))
        self.radioButtonNo.setText(_translate("Dialog", "Nie"))
        self.groupBoxdeg2grad.setTitle(_translate("Dialog", "Fi i lam w gradach"))
        self.pushButton.setText(_translate("Dialog", "Oblicz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

