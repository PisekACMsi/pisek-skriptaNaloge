import numpy as np
import json
import re

def izpisiLanguageStrings(lst:list):
    slv = {}
    for par in lst:
        slv.update(par)
    pySlv = {"languageStrings":{"sl":{}}}

    pySlv["languageStrings"]["sl"] = slv
    
    # jsonStr = json.dumps(pySlv, indent = 5, ensure_ascii=False)
    # jsString = re.sub("\"([^\"]+)\":", r"\1:", jsonStr).replace(r'\"', "")
    # return jsString[1:-1]
    return pySlv

def izpisiHideControls(restart = False, saveOrLoad = False, loadBestAnswer = False, speedSlider = False, backToFirst = False, nextStep = False, goToEnd = False):
    pySlv = {"hideControls":{}}
    slv = {"restart": restart, "saveOrLoad": saveOrLoad, "loadBestAnswer": loadBestAnswer, "speedSlider": speedSlider, "backToFirst": backToFirst, "nextStep": nextStep, "goToEnd": goToEnd,}
    pySlv["hideControls"] = slv

    # jsonStr = json.dumps(pySlv, indent = 5)
    # jsString = re.sub("\"([^\"]+)\":", r"\1:", jsonStr).replace(r'\"', "")
    # return jsString[1:-1]
    return pySlv

def izpisiRandomBulshit1(introMaxHeight = "33%", maxListSize = 100, scrollbars = True, controls = True, scale = 1, actionDelay = 400, blocklyColourTheme = "bwinf", maxInstructions = 0):
    pySlv = {"introMaxHeight": introMaxHeight,
		"maxListSize": maxListSize, 
		"scrollbars": scrollbars,
		"zoom": {
			"controls": controls,
			"scale": scale,
			},
        "actionDelay": actionDelay,				
		"blocklyColourTheme": blocklyColourTheme,
		"maxInstructions": maxInstructions
        }
    return pySlv

def izpisiStartingExample(str):
    pySlv = {"startingExample":{}}
    
    #python slovar
    pySlv["startingExample"]["blockly"] = str
    # jsonStr = json.dumps(pySlv, indent = 5)
    # jsString = re.sub("\"([^\"]+)\":", r"\1:", jsonStr).replace(r'\"', "")
    # return jsString[1:-1]
    return pySlv

def izpisiIncludeBlocks(gbc = True, robot = ["move"], iclAll = True, whCat = [], sinBl = [], excBl = []):
    slv = {"groupByCategory": gbc, "generatedBlocks": {"robot": robot}, "standardBlocks": {"includeAll": iclAll, "wholeCategories": whCat, "singleBlocks": sinBl, "excludedBlocks": excBl,},}
    pySlv = {"includeBlocks":{}}
    
    pySlv["includeBlocks"] = slv
    
    return pySlv

def izpisiCheckEndCondition(indikator1 = "category", ime1 = "coin", negIndikator1 = "", negIme1 = "", indikatorA = "", imeA = "", indikatorB = "", imeB = "", keys = "", negIndikatorA = "", negImeA = "", negIndikatorB = "", negImeB = ""):
    lst = [indikator1, ime1, negIndikator1, negIme1, indikatorA, imeA, indikatorB, imeB, keys, negIndikatorA, negImeA, negIndikatorB, negImeB]
    
    filters1 = r"{}"
    negFilters1 = r"{}"
    filtersA = r"{}"
    filtersB = r"{}"
    keys = r"{}"
    negFiltersA = r"{}"
    negFiltersB = r"{}"

    if (lst[0] == "" and lst[1] == "") and (lst[2] == "" and lst[3] == ""):
        funkcija1 = r"//"
    else:
        if lst[0] != "" and lst[1] != "":
            filters1 = "{%s: \\%s\\}"%(lst[0], lst[1])
        if lst[2] != "" and lst[3] != "":
            negFilters1 = "{%s: \\%s\\}"%(lst[2], lst[3])
        endCond1 = "robotEndConditions.checkItemExistence(context, lastTurn, filters1, negFilters1, exist=false)".replace("filters1", filters1).replace("negFilters1", negFilters1)
        funkcija1 = "(context, lastTurn) => { %s }"%(endCond1)

    if ((lst[4] == "" and lst[5] == "") and (lst[6] == "" and lst[7] == "")) and ((lst[9] == "" and lst[10] == "") and (lst[11] == "" and lst[12] == "")):
        funkcija2 = r"//"
    else:
        if lst[4] and lst[5]:
            filtersA = "{%s: \\%s\\}"%(lst[4], lst[5])
        if lst[6] and lst[7]:
            filtersB = "{%s: \\%s\\}"%(lst[6], lst[7])
        keys = lst[8]
        if lst[9] and lst[10]:
            negFiltersA = "{%s: \\%s\\}"%(lst[9], lst[10])
        if lst[11] and lst[12]:
            negFiltersB = "{%s: \\%s\\}"%(lst[11], lst[12])
        endCond2 = "robotEndConditions.checkItemCoincidence(context, lastTurn, filtersA, filtersB, keys, negFiltersA, negFiltersB)".replace("filtersA", filtersA).replace("filtersB", filtersB).replace("keys", keys).replace("negFiltersA", negFiltersA).replace("negFiltersB", negFiltersB)
        funkcija2 = "(context, lastTurn) => { %s }"%(endCond2)

    template = open("./generatorSkripte/endConditionTemplate.txt", "r").read()
    template = "&#&" + template.replace("funkcija1", funkcija1).replace("funkcija2", funkcija2) + "&#&"
    pySlv = {"checkEndCondition": template}
    
    return pySlv

def izpisiRandomBulsit2(border = 0, backgroundColour = "white", backgroundTile = "", borderColour = "black", showLabels = True, cellSide = 60, numberOfRobots = 1): 
    slv = {"border": border,
    "backgroundColour": backgroundColour,
    "backgroundTile": backgroundTile,
    "borderColour": borderColour,
    "showLabels": showLabels,

    "cellSide": cellSide,	
    "numberOfRobots": numberOfRobots}
    return slv

def izpisiItemTypes(slv: dict):
    pySlv = {"itemTypes":{}}
    pySlv["itemTypes"] = slv

    return pySlv

def ustvariItemType(num, img = "", zOrder = 0, nbStates = 1, category = "", value = 0):
    slv = {}
    
    slv["num"] = num
    slv["img"] = img
    slv["zOrder"] = zOrder
    slv["nbStates"] = nbStates
    slv["category"] = category
    slv["value"] = value

    return slv

def izpisiSubTaskData(lst: list):
    pySlv = {"easy": lst}

    return pySlv
    

def sestaviMatriko(n,m):
    return "&#&" + np.array_repr(np.ones((n,m), dtype = np.int8)).replace("array(", "").replace(", dtype=int8)", "") + "&#&"

def sestaviIncializacijo(row, col, type, dir = 0, value = 0):
    slv = {}
    
    slv["row"] = row
    slv["col"] = col
    slv["dir"] = dir
    slv["type"] = type
    slv["value"] = value

    return slv


slvLS = {}
s1LS = "program 2"
par1LS = {"startingBlockName": s1LS,} #zadnji vnos je poljuben, ostali so fiksni
par2LS = {"categories": {"actions": "Gibanje"}}
par3LS = {"label": {"changeRobot": "zamenjaj vlogo %1 HAHA"}}
par4LS = {"label": {"colour": "LOL %1",}}
par5LS = {"options":{"pick": "poberi UPS",}}
par6LS = {"messages":{"itemsExist": "Kovanci so na mreži."}}
par7LS = {"messages":{"itemsDontExist": "Kovancev ni na mreži."}}
par8LS = {"options":{"tools": {"bool": {"category": "je"}}}}
parsLS = [par1LS, par2LS, par3LS, par4LS, par5LS, par6LS, par7LS, par8LS]

strSE = '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="robot_start" id="Yx#}`-PvOO]HA4c0m7]F" deletable="false" movable="false" editable="false" x="0" y="0"><next><block type="move" id="CoO|[q[@qpAx1_*bS`Or"><field name="PARAM_0">S</field><value name="PARAM_1"><shadow type="math_number" id="Hyc?21Pdl93/lRnSQ;yk"><field name="NUM">5</field></shadow></value><next><block type="move" id=".0,k.*t.-0!PhL2?iW=S"><field name="PARAM_0">W</field><value name="PARAM_1"><shadow type="math_number" id="Eoy,Bt|qklJL]F[A_HUS"><field name="NUM">5</field></shadow></value><next><block type="move" id="-0w[|/Bnh{6lzt*/qE/1"><field name="PARAM_0">N</field><value name="PARAM_1"><shadow type="math_number" id=")T;FmigiJI@U(YA2/T+["><field name="NUM">1</field></shadow></value></block></next></block></next></block></next></block><block type="controls_repeat_ext" id="2E]Uhs@W}KrbH3PJF36*" x="20" y="155"><value name="TIMES"><shadow type="math_number" id="z_GWSb[:HQjB|Qf]0C9N"><field name="NUM">3</field></shadow></value><statement name="DO"><block type="moveSimple" id="yar~u.Qkhzs]q=@VlZ9c"><field name="PARAM_0">S</field></block></statement><next><block type="controls_repeat_ext" id="z@Gfs[CGcB6T{G-72W|z"><value name="TIMES"><shadow type="math_number" id="73LZY(lJ1blr[EH[s;W*"><field name="NUM">4</field></shadow></value><statement name="DO"><block type="moveSimple" id="#-0m.#:qs#=w*PlCX[qW"><field name="PARAM_0">W</field></block></statement></block></next></block><additional>{}</additional></xml>'

robotIB = ["move", "moveSimple", "forward", "forwardSimple", "turn", "turnAround", "jump", "changeRobot", "transport", "sensorBool", "sensorValue", "alterValue", "destroy", "create", "wait", "nitems", "sensorRowCol",]


ime1IT = "robot0"
numIT = 2
imgIT = ["pisek.png"]
zOrderIT = 2
nbStatesIT = 8
catIT = "robot"
categoryIT = [{"\"%s\""%catIT:True}]
item1IT = ustvariItemType(numIT, imgIT, zOrderIT, nbStatesIT, categoryIT)
#default slvIT je prazen {}, nekam zapiši vse opcije in tipe inputa
slvIT = {}
slvIT[ime1IT] = item1IT

matrika1TD = sestaviMatriko(4,5)
items1TD = [sestaviIncializacijo(row = 2, col = 2, dir = 4, type = "robot", value = 1), sestaviIncializacijo(row = 3, col = 1, dir = 4, type = "krNekej", value = 5)]
easy1TD = {"tiles":matrika1TD, "initItems":items1TD}

matrika2TD = sestaviMatriko(5,8)
items2TD = [sestaviIncializacijo(row = 2, col = 2, dir = 4, type = "robot", value = 1), sestaviIncializacijo(row = 3, col = 1, dir = 4, type = "krNekej", value = 5)]
easy2TD = {"tiles":matrika2TD, "initItems":items2TD}

lstTD = [easy1TD, easy2TD]

languageStrings = izpisiLanguageStrings(slvLS)
hideControls = izpisiHideControls()
randomBulshit1 = izpisiRandomBulshit1()
startingExample = izpisiStartingExample(strSE)
includeBlocks = izpisiIncludeBlocks(robot = robotIB)
checkEndCondition = izpisiCheckEndCondition()
randomBulsit2 = izpisiRandomBulsit2()
itemTypes = izpisiItemTypes(slvIT)
subTaskData = izpisiSubTaskData(lstTD)

def zdruzi(languageStrings, hideControls, includeBlocks, startingExample, checkEndCondition, itemTypes, subTaskData):
    ulmSlv = {}
    ulmSlv.update(languageStrings)
    ulmSlv.update(hideControls)
    ulmSlv.update(randomBulshit1)
    ulmSlv.update(includeBlocks)
    ulmSlv.update(startingExample)
    ulmSlv.update(checkEndCondition)
    ulmSlv.update(randomBulsit2)
    ulmSlv.update(itemTypes)

    jsonStr = json.dumps(ulmSlv, indent = 5, ensure_ascii=False)
    jsString1 = re.sub("\"([^\"]+)\":", r"\1:", jsonStr).replace(r'\"', "")
    jsString1 = jsString1.replace("\"&#&", "").replace("&#&\"", "").replace("\\\\", "\"").replace("\\n", "\n").replace("\\t", "\t")
    str1 = "subTask.gridInfos = {};".format(jsString1)

    jsonStr = json.dumps(subTaskData, indent = 5, ensure_ascii=False)
    jsString2 = re.sub("\"([^\"]+)\":", r"\1:", jsonStr).replace(r'\"', "").replace("\"&#&", "").replace("&#&\"", "")
    jsString2 = jsString2.replace("\\n", "\n")
    str2 = "subTask.data = {};".format(jsString2)

    theString = "function initTask(subTask) {{\n {0}\n{1}\ninitBlocklySubTask(subTask); \n}}".format(str1, str2)
    fajl = open("theTest.txt", "w", encoding = "utf-8")
    fajl.write(theString)
    fajl.close()

zdruzi(languageStrings, hideControls, includeBlocks, startingExample, checkEndCondition, itemTypes, subTaskData)
