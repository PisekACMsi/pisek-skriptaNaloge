import flatdict
import json

class LanguageStrings:
    def __init__(self):
        self.changedLanguageStrings = flatdict.FlatDict({},delimiter=".")
        self.initializeLanguageStrings()

    def initializeLanguageStrings(self):
        fajlLS = open('generator/imenaDelckov.txt', "r", encoding = ("utf-8"))
        languageStringsSlv = json.load(fajlLS)["sl"]
        fajlLS.close()
        self.languageStringsSlvFlat  = flatdict.FlatDict(languageStringsSlv, delimiter=".")
        self.languageStringsKeys = [key for key in self.languageStringsSlvFlat.keys()]
        self.keyWords = [key.split(".")[-1] for key in self.languageStringsKeys]

    def addFlatDictCategories(self, id, value):
        key = self.languageStringsKeys[id]
        self.changedLanguageStrings[key] = value
        self.languageStringsSlvFlat[key] = value

    def represent(self):
        return {"languageStrings":{"sl":self.changedLanguageStrings.as_dict()}}