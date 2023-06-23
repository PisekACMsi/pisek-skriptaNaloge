class EndCondition():
    def __init__(self, ):
        self.cond = {
            "indikator1":"category",
            "ime1":"",
            "negIndikator1":"",
            "negIme1":"",
            
            "indikatorA":"",
            "imeA":"",
            "indikatorB":"",
            "imeB":"",
            "keys":"",
            "negIndikatorA":"",
            "negImeA":"",
            "negIndikatorB":"",
            "negImeB":"",
        }
        self.funkcija1 = r"//"
        self.funkcija2 = r"//"

    def addCondition(self, key, val):
        self.cond[key] = val
        self.createConditions()
    
    def createConditions(self):
        filters1 = r"{}"
        negFilters1 = r"{}"
        filtersA = r"{}"
        filtersB = r"{}"
        keys = r"[]"
        
        negFiltersA = r"{}"
        negFiltersB = r"{}"
        if (self.cond["indikator1"] == "" or self.cond["ime1"] == "") and (self.cond["negIndikator1"] == "" or self.cond["negIme1"] == ""):
            self.funkcija1 = r"//"
        else:
            if self.cond["indikator1"] != "" and self.cond["ime1"] != "":
                filters1 = "{%s: \\%s\\}"%(self.cond["indikator1"], self.cond["ime1"])
            if self.cond["negIndikator1"] != "" and self.cond["negIme1"] != "":
                negFilters1 = "{%s: \\%s\\}"%(self.cond["negIndikator1"], self.cond["negIme1"])
            endCond1 = "robotEndConditions.checkItemExistence(context, lastTurn, filters1, negFilters1, exist=false)".replace("filters1", filters1).replace("negFilters1", negFilters1)
            self.funkcija1 = "(context, lastTurn) => { %s }"%(endCond1)


        if ((self.cond["indikatorA"] == "" or self.cond["imeA"] == "") and (self.cond["indikatorB"] == "" or self.cond["imeB"] == "")) and ((self.cond["negIndikatorA"] == "" or self.cond["negImeA"] == "") and (self.cond["negIndikatorB"] == "" or self.cond["negImeB"] == "")):
            funkcija2 = r"//"
        else:
            if self.cond["indikatorA"] and self.cond["imeA"]:
                filtersA = "{%s: \\%s\\}"%(self.cond["indikatorA"], self.cond["imeA"])
            if self.cond["indikatorB"] and self.cond["imeB"]:
                filtersB = "{%s: \\%s\\}"%(self.cond["indikatorB"], self.cond["imeB"])
            if self.cond["negIndikatorA"] and self.cond["negImeA"]:
                negFiltersA = "{%s: \\%s\\}"%(self.cond["negIndikatorA"], self.cond["negImeA"])
            if self.cond["negIndikatorB"] and self.cond["negImeB"]:
                negFiltersB = "{%s: \\%s\\}"%(self.cond["negIndikatorB"], self.cond["negImeB"])
            
            endCond2 = "robotEndConditions.checkItemCoincidence(context, lastTurn, filtersA, filtersB, keys, negFiltersA, negFiltersB)".replace("filtersA", filtersA).replace("filtersB", filtersB).replace("keys", keys).replace("negFiltersA", negFiltersA).replace("negFiltersB", negFiltersB)
            self.funkcija2 = "(context, lastTurn) => { %s }"%(endCond2)

    def represent(self):
        openFile = open("generator/endConditionTemplate.txt", "r")
        template = openFile.read()
        template = "&#&" + template.replace("funkcija1", self.funkcija1).replace("funkcija2", self.funkcija2) + "&#&"
        pySlv = {"checkEndCondition": template}
        openFile.close()  
        return pySlv
        

