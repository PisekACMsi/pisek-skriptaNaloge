class IncludeBlocks:
    def __init__(self):
        self.categoryBlocks = []
        self.robotBlocks = []
        self.individualBlocks = []
        self.groupByCategory = True
        self.includeAll = False

    def addCategoryBlock(self, block):
        self.categoryBlocks.append(block)
    
    def addRobotBlock(self, block):
        self.robotBlocks.append(block)
    
    def addRobotBlock(self, block):
        self.robotBlocks.append(block)
    

    def represent(self):
        return {"includeBlocks":{"groupByCategory":self.groupByCategory, "generatedBlocks":{"robot":self.robotBlocks}, "standardBlocks":{"includeAll":self.includeAll}, "wholeCategories":self.categoryBlocks, "singleBlocks":self.individualBlocks, "excludedBlocks":[]}}