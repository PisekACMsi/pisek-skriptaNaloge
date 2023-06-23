import flatdict
import json

class LanguageStrings:
    def __init__(self):
        self.changedLanguageStrings = flatdict.FlatDict({},delimiter=".")
        self.initializeLanguageStrings()

    def initializeLanguageStrings(self):
        fajlLS = open('imenaDelckov.txt', "r", encoding = ("utf-8"))
        languageStringsSlv = json.load(fajlLS)["sl"]
        fajlLS.close()
        self.languageStringsSlvFlat  = flatdict.FlatDict(languageStringsSlv, delimiter=".")
        self.languageStringsKeys = [key for key in self.languageStringsSlvFlat.keys()]

    def addFlatDictCategories(self, id, value):
        key = self.languageStringsKeys[id]
        self.changedLanguageStrings[key] = value
        self.languageStringsSlvFlat[key] = value

    def represent(self):
        return {"languageStrings":{"sl":self.changedLanguageStrings.as_dict()}}

    def languageStringsHtml(self, selectedId):
        html = ""
        for id, key in enumerate(self.languageStringsKeys):
            if id == selectedId:
                html += "<option selected='selected'>" + key + ": " + self.languageStringsSlvFlat[key] + "</option>"
            else:
                html += "<option>" + key + ": " + self.languageStringsSlvFlat[key] + "</option>"
        return html