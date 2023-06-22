class Matrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def createMatrix(self):
        self.matrix = [[1 for i in range(self.width)] for j in range(self.height)]
    
    def addItem(self, row, col, num):
        if self.matrix[row][col] == 1:
            self.matrix[row][col] = num
            return True
        else:
            return False
    
    def removeItem(self, row, col):
        self.matrix[row][col] == 1

    def stringRepresentation():
        
    
