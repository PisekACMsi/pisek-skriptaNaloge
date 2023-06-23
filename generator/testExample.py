from initialization import *
from matrix import *

class TestExample:
    def __init__(self, matrixWidth=5, matrixHeight=5):
        self.matrix = Matrix(matrixWidth, matrixHeight) #matrix object
        self.inicialisation = Initialization() #initialization object

    def addToMatrix(self, objectNum, objectName, row, col):
        objectNum = objectNum
        added = self.matrix.addItem(row, col, objectNum)
        if not added:
            self.inicialisation.addInitialization(objectName, row, col)

    def removeFromMatrix(self, objectNum, objectName, row, col):
        if self.matrix.matrix[row][col] == objectNum:
            self.matrix.removeItem(row, col)
        self.inicialisation.dellInitialization(objectName, row, col)

    def removeAllFromMatrix(self, objectNum, objectName):
        self.matrix.removeAllItem(objectNum)
        self.inicialisation.dellAllInitialization(objectName)

    def represent(self):
        return {"tiles":self.matrix.represent(), "initItems":self.inicialisation.represent()}