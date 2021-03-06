# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from ui_parallelline import Ui_ParallelLine
import os, sys

class ParallelLineGui(QDialog, Ui_ParallelLine):

    okClicked = pyqtSignal(str, float)
    unsetTool = pyqtSignal()
    btnSelectVertex_clicked = pyqtSignal()

    def __init__(self, parent, flags):
        QDialog.__init__(self, parent, flags)
        self.setupUi(self)

        self.method = "fixed"

        self.okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        self.okButton.clicked.connect(self.accept)

        self.cancelButton = self.buttonBox.button(QDialogButtonBox.Cancel)
        self.cancelButton.clicked.connect(self.close)


    def initGui(self):
        self.spinBoxDistance.setMinimum(-10000000)
        self.spinBoxDistance.setMaximum(10000000)
        self.spinBoxDistance.setDecimals(3)

        self.radioFixed.setChecked(True)
        self.radioVertex.setChecked(False)

        self.btnSelectVertex.setEnabled(False)

        self.buttonBox.setEnabled(True)
        pass


    @pyqtSignature("on_radioVertex_clicked()")    
    def on_radioVertex_clicked(self):     
        self.method = "vertex"
        self.spinBoxDistance.setEnabled(False)
        self.btnSelectVertex.setEnabled(True)
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)


    @pyqtSignature("on_radioFixed_clicked()")    
    def on_radioFixed_clicked(self):      
        self.method = "fixed"
        self.spinBoxDistance.setEnabled(True)
        self.btnSelectVertex.setEnabled(False)
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)


    @pyqtSignature("on_btnSelectVertex_clicked()") 
    def on_btnSelectVertex_clicked(self):
        self.method = "vertex"
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)   
        self.btnSelectVertex_clicked.emit()


    def accept(self):
        self.okClicked.emit(self.method,self.spinBoxDistance.value())
        pass


    def close(self):
        self.unsetTool.emit()
        pass
