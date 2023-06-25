class IncludeBlocks:
    def __init__(self):  
        self.categoryBlocks = {"logic":False, "loops":False, "math":False, "texts":False, "lists":False, "colour":False, "variables":False, "functions":False} # neki za obklukat
        self.robotBlocks = {"move": False, "moveSimple": False, "forward": False, "forwardSimple": False, "turn": False, "turnAround": False, "jump": False, "changeRobot": False, "transport": False, "sensorBool": False, "sensorValue": False, "alterValue": False, "destroy": False, "create": False, "wait": False, "nitems": False, "sensorRowCol": False}
        self.individualBlocks = {"robot_start": False, "math_arithmetic": False, "math_number": False, "math_number": False, "controls_repeat_ext": False, "math_number": False, "math_number": False, "variables_get": False, "controls_whileUntil": False, "math_single": False, "math_number": False, "variables_set": False, "math_number_property": False, "math_number": False, "controls_for": False, "math_number": False, "math_number": False, "math_number": False, "math_round": False, "math_number": False, "math_modulo": False, "math_number": False, "math_number": False, "controls_flow_statements": False, "procedures_defreturn": False, "procedures_defnoreturn": False, "math_change": False, "math_number": False, "procedures_ifreturn": False, "procedures_callnoreturn": False, "procedures_callreturn": False}
        self.groupByCategory = True
        self.includeAll = False

    def addCategoryBlock(self, block):
        self.categoryBlocks[block] = True    
    
    def addRobotBlock(self, block):
        self.robotBlocks[block] = True
    
    def addRobotBlock(self, block):
        self.robotBlocks[block] = True
    
    def represent(self):
        categoryBlocksAdd = []
        for block in self.categoryBlocks.keys():
            if self.categoryBlocks[block]:
                categoryBlocksAdd.append(block)
        robotBlocksAdd = []
        for block in self.robotBlocks.keys():
            if self.robotBlocks[block]:
                robotBlocksAdd.append(block)
        individualBlocksAdd = []
        for block in self.individualBlocks.keys():
            if self.individualBlocks[block]:
                individualBlocksAdd.append(block)


        return {"includeBlocks":{"groupByCategory": self.groupByCategory, "generatedBlocks":{"robot": robotBlocksAdd}, 
                                 "standardBlocks":{"includeAll":self.includeAll, "wholeCategories":categoryBlocksAdd, 
                                 "singleBlocks": individualBlocksAdd, "excludedBlocks":[]}}}