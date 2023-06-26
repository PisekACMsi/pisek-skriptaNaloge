class HtmlCreator:
    def __init__(self, naloga):
        self.naloga = naloga
        self.categories = ["obstacle", "coin", "transportable", "image"]

    def addCustomCategory(self, categoy):
        self.categories.append(categoy)

    def getAllImages(self):
        backgTile = self.naloga.board.backgImage
        otherImages = [backgTile] if backgTile != "" else []
        for item in self.naloga.itemTypes.items.values():
            for image in item.image:
                otherImages.append(image)
        return otherImages

    def languageStringsHtml(self, selectedId):
        languageStringsKeys = self.naloga.languageStrings.languageStringsKeys
        keyWords = self.naloga.languageStrings.keyWords
        languageStringsSlvFlat = self.naloga.languageStrings.languageStringsSlvFlat
        html = ""
        for id, key in enumerate(languageStringsKeys):
            if id == selectedId:
                html += "<option selected='selected'>" + keyWords[id] + ": " + languageStringsSlvFlat[key] + "</option>"
            else:
                html += "<option>" + keyWords[id] + ": " + languageStringsSlvFlat[key] + "</option>"
        return html

    def createItemTypesHtmlString(self):
        items = self.naloga.itemTypes.items
        if len(items.keys()) == 0:
            return "Ni dodanih predmetov"
        else:
            returnHtml = ""
            for ime in items.keys():
                returnHtml += "<b>" + ime + ": </b>"
                for thingi in items[ime].represent().keys():
                    returnHtml += "<b>" + thingi + ": </b>  " + str(items[ime].represent()[thingi]) + "      "
                returnHtml += "<br>"

            return returnHtml
        
    def updateItemTypesHtmlString(self):
        itemTypesNames = list(self.naloga.itemTypes.items.keys())
        html=""
        for name in itemTypesNames:
            html += "<option>" + str(name) + "</option> <br>"
        return html
    
    def updateItemTypesNoButtonsHtmlString(self):
        itemTypesNames = list(self.naloga.itemTypes.items.keys())
        html=""
        for name in itemTypesNames:
            if "button" not in name:
                html += "<option>" + str(name) + "</option> <br>"
        return html
    
    def updateCategoryOptionsHtmlString(self):
        addedCategories = self.naloga.itemTypes.addedCategories
        html = ""
        for cat in list(addedCategories):
            if cat != "button" and cat != "number":
                html += "<option>" + cat + "</option> <br>"
        return html
    
    def updateButtonHtmlString(self):
        items = self.naloga.itemTypes.items
        html = "<option value=''> Ni povezave </option> <br>"
        for item in items.keys():
            if "button" in item:
                html += "<option>" + item + "</option> <br>"
        return html
    
    def blocksCategoryHtml(self):
        categoryBlocks = self.naloga.includeBlocks.categoryBlocks
        html = ""
        for block in categoryBlocks.keys():
            if categoryBlocks[block]:
                html += "<option selected='selected'>" + block + "</option> <br>"
            else:
                html += "<option>" + block + "</option> <br>"
        return html
    
    def blocksRobotHtml(self):
        robotBlocks = self.naloga.includeBlocks.robotBlocks
        html = ""
        for block in robotBlocks.keys():
            if robotBlocks[block]:
                html += "<option selected='selected'>" + block + "</option> <br>"
            else:
                html += "<option>" + block + "</option> <br>"
        return html
    
    def blocksSingleHtml(self):
        individualBlocks = self.naloga.includeBlocks.individualBlocks
        html = ""
        for block in individualBlocks.keys():
            if individualBlocks[block]:
                html += "<option selected='selected'>" + block + "</option> <br>"
            else:
                html += "<option>" + block + "</option> <br>"
        return html
    
    def categoriesHtml(self):
        html = ""
        for categroy in self.categories:
            html += "<option>" + categroy + "</option>"
        return html
    

    

