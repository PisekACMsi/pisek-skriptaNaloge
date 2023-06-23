class ItemType():
    def __init__(self, name, num, category, images, zOrder):
        self.name = name
        self.num = num
        self.categorys = category #seznham kategorij
        self.image = images #seznam slik
        self.zOrder = zOrder
        self.createCategoryDict()

    def createCategoryDict(self):
        returnCat = []
        for cat in self.categorys:
            returnCat.append({"'" + cat + "'":True})
        self.returnCat = returnCat
    
    def represent(self):
        return {"num":self.num, "category":self.returnCat, "img":self.image, "zOrder":self.zOrder}

class Robot(ItemType):
    def __init__(self, name, num, category, images, zOrder, nbStates):
        super().__init__(name, num, category, images, zOrder)
        self.nbStates = nbStates
    
    def represent(self):
        return {"num":self.num, "category":self.returnCat, "img":self.image, "zOrder":self.zOrder, "nbStates":self.nbStates}

class Number(ItemType):
    def __init__(self, name, num, category, images, zOrder, value):
        super().__init__(name, num, category, images, zOrder)
        self.value = value
    def represent(self):
        return {"num":self.num, "category":self.returnCat, "zOrder":self.zOrder, "value":self.value}

class Color(ItemType):
    def __init__(self, name, num, category, images, zOrder, colour):
        super().__init__(name, num, category, images, zOrder)
        self.color = colour
    def represent(self):
        return {"num":self.num, "zOrder":self.zOrder, "colour":self.color}
    
class Button(ItemType):
    def __init__(self, name, num, category, images, zOrder, id):
        super().__init__(name, num, category, images, zOrder)
        self.id = id
    def represent(self):
        return {"num":self.num, "zOrder":self.zOrder, "category":self.returnCat, "img":self.image, "id":self.id}
    
