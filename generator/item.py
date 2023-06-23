class ItemType():
    def __init__(self, name, num, category, images):
        self.name = name
        self.num = num
        self.categorys = category #seznham kategorij
        self.image = images #seznam slik
        self.zOrderOrder = {"obstacle":5, "coin":6, "transportable":6, "button":3, "number":4, "image":2, "robot":10, "colour":1}
        self.createCategoryDict()

    def createCategoryDict(self):
        returnCat = []
        for cat in self.categorys:
            returnCat.append({"'" + cat + "'":True})
        self.returnCat = returnCat
    
    def represent(self):
        return {"num":self.num, "category":self.returnCat, "img":self.image, "zOrder":self.zOrderOrder[self.categorys[0]]}

class Robot(ItemType):
    def __init__(self, name, num, category, images, zOrder, nbStates):
        super().__init__(name, num, category, images)
        self.nbStates = nbStates
    
    def represent(self):
        return {"category":self.returnCat, "img":self.image, "zOrder":self.zOrderOrder[self.categorys[0]], "nbStates":self.nbStates}

class Number(ItemType):
    def __init__(self, name, num, category, images, zOrder, value):
        super().__init__(name, num, category, images)
        self.value = value
    def represent(self):
        return {"num":self.num, "category":self.returnCat, "zOrder":self.zOrderOrder[self.categorys[0]], "value":self.value}

class Color(ItemType):
    def __init__(self, name, num, category, images, zOrder, colour):
        super().__init__(name, num, category, images)
        self.color = colour
    def represent(self):
        return {"num":self.num, "zOrder":self.zOrderOrder[self.categorys[0]], "colour":self.color}
    
class Button(ItemType):
    def __init__(self, name, num, category, images, zOrder, id):
        super().__init__(name, num, category, images)
        self.id = id
    def represent(self):
        return {"num":self.num, "zOrder":self.zOrderOrder[self.categorys[0]], "category":self.returnCat, "img":self.image, "id":self.id}
    
