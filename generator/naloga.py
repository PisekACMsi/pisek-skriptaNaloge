import re
from subTaskData import *
from languageStrings import *
from includeBlocks import *
from board import *
from itemTypes import *
from endCondition import *
from item import *

class Naloga:
    def __init__(self):
        self.languageStrings = LanguageStrings()
        self.board = Board()
        self.includeBlocks = IncludeBlocks()
        self.endCondition = EndCondition()
        self.itemTypes = Itemtypes()
        self.subTaskData = SubtaskData()

    def createFile(self):
        print("USTVARJAM FAJL")
        ulmSlv = {}
        ulmSlv.update(self.languageStrings.represent())
        ulmSlv.update(self.board.representHideControls())
        ulmSlv.update(self.board.representZoom())
        ulmSlv.update(self.board.representSolo())
        ulmSlv.update(self.board.representStartingExample())
        ulmSlv.update(self.includeBlocks.represent())
        ulmSlv.update(self.endCondition.represent())
        ulmSlv.update(self.itemTypes.represent())
        jsonStr = json.dumps(ulmSlv, indent = 5, ensure_ascii=False)
        jsString1 = re.sub("\"([^\"]+)\":", r"\1:", jsonStr).replace(r'\"', "")
        jsString1 = jsString1.replace("\"&#&", "").replace("&#&\"", "").replace("\\\\", "\"").replace("\\n", "\n").replace("\\t", "\t")
        str1 = "subTask.gridInfos = {};".format(jsString1)

        subTaskData = self.subTaskData.represent()
        jsonStr = json.dumps(subTaskData, indent = 5, ensure_ascii=False)
        jsString2 = re.sub("\"([^\"]+)\":", r"\1:", jsonStr).replace(r'\"', "").replace("\"&#&", "").replace("&#&\"", "")
        jsString2 = jsString2.replace("\\n", "\n")
        str2 = "subTask.data = {};".format(jsString2)

        theString = "function initTask(subTask) {{\n {0}\n{1}\ninitBlocklySubTask(subTask); \n}}".format(str1, str2)
        fajl = open("static/javascript/theTest.js", "w", encoding = "utf-8")
        fajl.write(theString)
        fajl.close()

