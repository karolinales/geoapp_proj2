from __future__ import unicode_literals # obsluga polskich znaków diaktrtycznych
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demo_App import * # import kodu pythona ze schematem GUI
import numpy as np
import PyQt5.QtGui

class MyForm(QDialog): # QDialog jako klasa nadrzedna
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog() # Nazwa klasy z pliku przekonwertowanego z UI
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.deg2grad)
        self.ui.pushButton.clicked.connect(self.model)
        self.ui.pushButton.clicked.connect(self.deg2rad)
        self.ui.pushButton.clicked.connect(self.sigma)
        self.ui.pushButton.clicked.connect(self.filam2gk)
        self.ui.pushButton.clicked.connect(self.gk2pl2000)
        self.ui.pushButton.clicked.connect(self.fila2pl1992)
        self.setWindowIcon(QtGui.QIcon('ikona.png'))
        


    def deg2grad(self):
        if self.ui.radioButtonYes.isChecked():
            if len(self.ui.lineEditFiDeg.text()) != 0:
                df = int(self.ui.lineEditFiDeg.text())
            else:
                df = 0
            if len(self.ui.lineEditFiMin.text()) != 0:
                mf = int(self.ui.lineEditFiMin.text())
            else:
                mf = 0 
            if len(self.ui.lineEditFiSec.text()) != 0:
                sf = float(self.ui.lineEditFiSec.text())
            else:
                sf = 0
            degf = df+mf/60+sf/3600
            radf = np.deg2rad(degf)
            gradf = radf*200/np.pi
            
            if len(self.ui.lineEditLamDeg.text()) != 0:
                dl = int(self.ui.lineEditLamDeg.text())
            else:
                dl = 0
            if len(self.ui.lineEditLamMin.text()) != 0:
                ml = int(self.ui.lineEditLamMin.text())
            else:
                ml = 0 
            if len(self.ui.lineEditLamSec.text()) != 0:
                sl = float(self.ui.lineEditLamSec.text())
            else:
                sl = 0
            degl = dl+ml/60+sl/3600
            radl = np.deg2rad(degl)
            gradl = radl*200/np.pi
            
            self.ui.FiGrad.setText(f'Fi: {gradf:.4f}g')
            self.ui.LamGrad.setText(f'Lam: {gradl:.4f}g')
        else:
            self.ui.FiGrad.setText("Nie przeliczono")
            self.ui.LamGrad.setText("Nie przeliczono")
    
    
    def model(self):
        if self.ui.radioButtonGRS80.isChecked():
            a = 6378137.0
            b = 6356752.31414036
            flattening = (a - b) / a
            ecc2 = (a**2 - b**2)/a**2
            # self.ui.X1992.setText(f'{b}')
        elif self.ui.radioButtonWGS84.isChecked():
            a = 6378137.0
            b = 6356752.31424518 
            flattening = (a - b) / a
            ecc2 = (a**2 - b**2)/a**2
            # self.ui.X1992.setText(f'{b}')
        else: 
            self.ui.X2000.setText("Nie wybrano modelu elipsoidy")
            self.ui.Y2000.setText("Nie wybrano modelu elipsoidy")
            self.ui.X1992.setText("Nie wybrano modelu elipsoidy")
            self.ui.Y1992.setText("Nie wybrano modelu elipsoidy")
        return a, b, flattening, ecc2
        
     
                   
    def deg2rad(self):
        if len(self.ui.lineEditFiDeg.text()) != 0:
            df = int(self.ui.lineEditFiDeg.text())
        else:
            df = 0
        if len(self.ui.lineEditFiMin.text()) != 0:
            mf = int(self.ui.lineEditFiMin.text())
        else:
            mf = 0 
        if len(self.ui.lineEditFiSec.text()) != 0:
            sf = float(self.ui.lineEditFiSec.text())
        else:
            sf = 0
        degf = df+mf/60+sf/3600
        radf = np.deg2rad(degf)
            
        if len(self.ui.lineEditLamDeg.text()) != 0:
            dl = int(self.ui.lineEditLamDeg.text())
        else:
            dl = 0
        if len(self.ui.lineEditLamMin.text()) != 0:
            ml = int(self.ui.lineEditLamMin.text())
        else:
            ml = 0 
        if len(self.ui.lineEditLamSec.text()) != 0:
            sl = float(self.ui.lineEditLamSec.text())
        else:
            sl = 0
        degl = dl+ml/60+sl/3600
        radl = np.deg2rad(degl)
        return radf, radl
        

    def strefa(self):
        if self.ui.radioButtonZ5.isChecked():
            strefa = 5
        elif self.ui.radioButtonZ6.isChecked():
            strefa = 6
        elif self.ui.radioButtonZ7.isChecked():
            strefa = 7
        elif self.ui.radioButtonZ8.isChecked():
            strefa = 8
        return strefa
    
        
    def sigma(self):
        radf, radl = self.deg2rad()
        a, b, flattening, ecc2 = self.model()
        A0 = 1 - (ecc2/4)-(3*ecc2**2/64)-(5*ecc2**3/256)
        A2=(3/8)*(ecc2 + (ecc2**2/4)+((15*ecc2**3)/128))
        A4=15/256*(ecc2**2+(3*ecc2**3/4))
        A6=35*ecc2**3/3072
        sigma = a * (A0*radf - A2*np.sin(2*radf) + A4*np.sin(4*radf) - A6*np.sin(6*radf))
        return sigma
    
    def filam2gk(self):
        strefa = self.strefa()
        a, b, flattening, ecc2 = self.model()
        radf, radl = self.deg2rad()
        lam0 = (strefa*3) * np.pi/180
        b2 = b ** 2
        ep2 = ((a ** 2 ) - b2) / b2
        t = np.tan(radf)
        n2 = ep2 * ((np.cos(radf)) ** 2)
        N = a/np.sqrt(1 - (ecc2 * np.sin(radf)**2))
        si = self.sigma()
        d_lam = radl - lam0
        eta2 = ep2 * np.cos(radf)**2
        xgk = si + ((d_lam**2)/2) * N * np.sin(radf) * np.cos(radf) * (1 + ((d_lam**2)/12) * np.cos(radf)**2 * (5 - t**2 + 9 * eta2 + 4 * eta2**2) + ((d_lam**4)/360) * np.cos(radf)**4 * (61 - 18 * t**2 + t**4 + 270 * eta2 - 330 * eta2 * t**2))
        ygk = d_lam * N * np.cos(radf) * (1 + d_lam**2/6 * np.cos(radf)**2 * (1 - t**2 + eta2) + d_lam**4/120 * np.cos(radf)**4 * (5 - 18 * t**2 + t**4 + 14 * eta2 - 58 * eta2 * t**2))
        return xgk, ygk
    
    def gk2pl2000(self):
        strefa = self.strefa()
        xgk, ygk = self.filam2gk()
        x2000 = xgk * 0.999923
        y2000 = ygk * 0.999923 + strefa * 1000000 + 500000
        self.ui.X2000.setText(f'X: {x2000:.3f}')
        self.ui.Y2000.setText((f'Y: {y2000:.3f}'))
    
    def fila2pl1992(self):
        a, b, flattening, ecc2 = self.model()
        radf, radl = self.deg2rad()
        lam0 = (19*np.pi/180) * np.pi/180
        b2 = b ** 2
        ep2 = ((a ** 2 ) - b2) / b2
        t = np.tan(radf)
        n2 = ep2 * ((np.cos(radf)) ** 2)
        N = a/np.sqrt(1 - (ecc2 * np.sin(radf)**2))
        si = self.sigma()
        d_lam = radl - lam0
        eta2 = ep2 * np.cos(radf)**2
        xgk = si + ((d_lam**2)/2) * N * np.sin(radf) * np.cos(radf) * (1 + ((d_lam**2)/12) * np.cos(radf)**2 * (5 - t**2 + 9 * eta2 + 4 * eta2**2) + ((d_lam**4)/360) * np.cos(radf)**4 * (61 - 18 * t**2 + t**4 + 270 * eta2 - 330 * eta2 * t**2))
        ygk = d_lam * N * np.cos(radf) * (1 + d_lam**2/6 * np.cos(radf)**2 * (1 - t**2 + eta2) + d_lam**4/120 * np.cos(radf)**4 * (5 - 18 * t**2 + t**4 + 14 * eta2 - 58 * eta2 * t**2))
        x92 = xgk * 0.9993 - 5300000
        y92 = ygk * 0.9993 + 500000
        self.ui.X1992.setText(f'X: {x92:.3f}')
        self.ui.Y1992.setText((f'Y: {y92:.3f}'))


    
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())        
