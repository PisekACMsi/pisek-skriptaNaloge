from item import *
class Itemtypes:
    def __init__(self):
        self.items = {}
        self.addedCategories = set()
        self.addedTypes = set()

    def addItem(self, item):
        self.items[item.name] = item
        self.updateItemList()

    def createDefaultItem(self, cats, parameters):
        cat = cats[0]
        id = 0
        for addedType in list(self.addedTypes):
            if cat in addedType:
                id += 1
        itemName = cat + str(id)
        num = len(list(self.addedTypes))
        if cat == "robot":
            item = Robot(name = itemName, num = num, category = cats, images = parameters, zOrder = 10, nbStates=8)
            self.addItem(item)
        elif cat == "number" and type(parameters) == "int":
            item = Number(name = itemName, num = num, category = cats, zOrder = 5, images=[""], value=parameters)
            self.addItem(item)
        elif cat == "colour":
            item = Color(name = itemName, num = num, category = cats, images = [""], zOrder = 2, colour=parameters)
            self.addItem(item)
        elif cat in ["image", "transportable","button","obstacle"]:
            item = ItemType(name = itemName, num = num, category = cats, images = parameters, zOrder = 3)
            self.addItem(item)

    def updateItemList(self):
        self.addedCategories = set()
        self.addedTypes = set()
        for type in self.items.keys():
            self.addedTypes.add(type)
            for cat in self.items[type].categorys:
                self.addedCategories.add(cat)
    
    def removeItem(self, itemName):
        self.items.remove(itemName)

    def represent(self):
        repr = {}
        for type in self.items.keys():
            repr[type] = self.items[type].represent()
        return {"itemTypes":repr}