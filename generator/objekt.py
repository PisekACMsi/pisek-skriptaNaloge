class ItemType():
    def __init__(self, name, num, category, images, zOrder):
        self.name = name
        self.num = num
        self.category = category
        self.image = images
        self.zOrder = zOrder
        self.createCategoryDict(self)

    def createCategoryDict(self):
        returnCat = []
        for cat in self.category:
            returnCat.append({cat:True})
        self.returnCat = returnCat
    
    def createItemDict(self):
        return {"num":self.num, "category":self.returnCat, "img":self.image, "zOrder":self.zOrder}

class Robot(ItemType):
    def __init__(self, nbStates):
        self.nbStates = nbStates
    
    def createItemDict(self):
        return {"num":self.num, "category":self.category, "img":self.image, "zOrder":self.zOrder, "nbStates":self.nbStates}

class Number(ItemType):
    def __init__(self, value):
        self.value = value
    def createItemDict(self):
        return {"num":self.num, "category":self.category, "img":self.image, "zOrder":self.zOrder, "value":self.value}

class Color(ItemType):
    def __init__(self, color):
        self.color = color
    def createItemDict(self):
        return {"num":self.num, "category":self.category, "img":self.image, "zOrder":self.zOrder, "colour":self.color}