class Initialization:
    def __init__(self):
        self.init = []
    
    def addInitialization(self, objectName, row, col):
        self.init.append({"type":objectName,"row":row,"col":col})

    def dellInitialization(self, objectName, row, col):
        initForDelete = []
        for init in self.init:
            if init["type"] == objectName and init["row"] == row and init["col"] == col:
                initForDelete.append(init)
        for init in initForDelete:
            self.init.remove(init)

    def dellAllInitialization(self, objectName):
        initForDelete = []
        for init in self.init:
            if init["type"] == objectName:
                initForDelete.append(init)
        for init in initForDelete:
            self.init.remove(init)

    def represent(self):
        return self.init
