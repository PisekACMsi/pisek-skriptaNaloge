class Matrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.createMatrix()
    
    def createMatrix(self):
        self.matrix = [[1 for i in range(self.width)] for j in range(self.height)]
    
    def addItem(self, row, col, num):
        if row < self.height and col < self.width:
            if self.matrix[row][col] == 1:
                self.matrix[row][col] = num
                return True
            else:
                return False
        
    def removeItem(self, row, col):
        self.matrix[row][col] = 1
    
    def removeAllItem(self, num):
        for i in range(self.width):
            for j in range(self.height):
                if self.matrix[i][j] == num:
                    self.matrix[i][j] == 1

    def represent(self):
        return "&#&" + str(self.matrix).replace("],", "], \n") + "&#&"
    
    def resizeMatrix(self, wd, he):
        oldMatrix = self.matrix.copy()
        self.width = wd
        self.height = he
        self.createMatrix()
        for i in range(len(oldMatrix)):
            for j in range(len(oldMatrix[0])):
                self.addItem(i, j, oldMatrix[i][j])
    
