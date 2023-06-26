from item import *
class Itemtypes:
    def __init__(self):
        self.items = {}
        self.addedCategories = set()

    def createDefaultItem(self, cats, parameters):
        cat = cats[0]
        numOfItems, missingNumber = self.numberOfItemsCategory(cat)
        itemName = cat +"_"+ str(missingNumber)
        num = self.findMissingNumber(2, len(list(self.items.keys()))+3, [self.items[itemName].num for itemName in self.items])
        
        if cat == "robot":
            if numOfItems < 3:
                item = Robot(name = itemName, num = num, category = cats, images = parameters, zOrder = None, nbStates=8)
                self.addItem(item)
            elif numOfItems==3:
                item = Robot(name = "robot_2", num = num, category = cats, images = parameters, zOrder = None, nbStates=8)
                self.addItem(item)
        elif cat == "number":
            itemName = "number_" + parameters
            item = Number(name = itemName, num = num, category = cats, zOrder = None, images=[""], value=parameters)
            self.addItem(item)
        elif cat == "colour":
            item = Color(name = itemName, num = num, category = cats, images = [""], zOrder = None, colour=parameters)
            self.addItem(item)
        elif cat == "button":
            item = Button(name = itemName, num = num, category = cats, images = parameters, zOrder = None, id = missingNumber)
            self.addItem(item)
        elif cat in ["image", "transportable","obstacle", "coin"]:
            item = ItemType(name = itemName, num = num, category = cats, images = parameters, zOrder=None)
            self.addItem(item)

    def createCustomItem(self, name, num, category, images, zOrder):
        item = ItemType(name, num, category, images, zOrder)

    def numberOfItemsCategory(self, category): #Prešteje vse default iteme in spremeni indeks
        numOfItems = 0
        itemsIds = []
        for addedType in list(self.items.keys()):
            if category in addedType:
                numOfItems += 1
                itemsIds.append(int(addedType[addedType.find("_")+1:]))

        missingNumber = self.findMissingNumber(1, len(itemsIds)+2, itemsIds)
        return numOfItems, missingNumber
    
    def findMissingNumber(self, minNum, maxNum, numbers):
        num_set = set(numbers)

        for missingNumber in range(minNum, maxNum):
            if missingNumber not in num_set:
                return missingNumber
        return None
        
    
    def addItem(self, item):
        self.items[item.name] = item
        self.updateItemList()

    def updateItemList(self):
        self.addedCategories = set()
        for type in self.items.keys():
            for cat in self.items[type].categorys:
                self.addedCategories.add(cat)
    
    def removeItem(self, itemName):
        self.items.pop(itemName)
        self.updateItemList()

    def represent(self):
        repr = {}
        for type in self.items.keys():
            repr[type] = self.items[type].represent()
        return {"itemTypes":repr}