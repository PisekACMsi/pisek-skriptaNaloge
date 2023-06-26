class ItemType():
    def __init__(self, name, num, category, images, zOrder = None, id=0):
        self.name = name
        self.num = num
        self.categorys = category #seznham kategorij
        self.image = images #seznam slik
        self.zOrderOrder = {"obstacle":5, "coin":6, "transportable":6, "button":3, "number":4, "image":2, "robot":10, "colour":1}
        self.id = id
        self.setZOrder(zOrder)
        self.createCategoryDict()

    def setZOrder(self, zOrder):
        if zOrder == None:
            self.zOrder = self.zOrderOrder[self.categorys[0]]
        else:
            self.zOrder = zOrder

    def createCategoryDict(self):
        returnCat = []
        for cat in self.categorys:
            returnCat.append({"'" + cat + "'":True})
        self.returnCat = returnCat
    
    def represent(self):
        return {"num":self.num, "category":self.returnCat, "img":self.image, "zOrder":self.zOrderOrder[self.categorys[0]], "id":self.id}

class Robot(ItemType):
    def __init__(self, name, num, category, images, nbStates, zOrder = None, id=0):
        super().__init__(name, num, category, images, zOrder)
        self.nbStates = nbStates
    
    def represent(self):
        return {"category":self.returnCat, "img":self.image, "zOrder":self.zOrderOrder[self.categorys[0]], "nbStates":self.nbStates, "id":self.id}

class Number(ItemType):
    def __init__(self, name, num, category, images, value, zOrder = None, id=0):
        super().__init__(name, num, category, images, zOrder)
        self.value = value
    def represent(self):
        return {"num":self.num, "category":self.returnCat, "zOrder":self.zOrderOrder[self.categorys[0]], "value":self.value, "id":self.id}

class Color(ItemType):
    def __init__(self, name, num, category, images, colour, zOrder = None, id=0):
        super().__init__(name, num, category, images, zOrder)
        self.color = colour
    def represent(self):
        return {"num":self.num, "zOrder":self.zOrderOrder[self.categorys[0]], "colour":self.color, "id":self.id}
    
class Button(ItemType):
    def __init__(self, name, num, category, images, id, zOrder = None):
        super().__init__(name, num, category, images, zOrder)
        self.id = id
    def represent(self):
        return {"num":self.num, "zOrder":self.zOrderOrder[self.categorys[0]], "category":self.returnCat, "img":self.image, "id":self.id}
    
