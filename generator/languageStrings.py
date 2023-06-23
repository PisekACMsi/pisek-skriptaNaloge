import flatdict
import json

class LanguageStrings:
    def __init__(self):
        self.changedLanguageStrings = flatdict.FlatDict({})
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

    def represent(self):
        return {"sl":self.changedLanguageStrings.as_dict()}

