import numpy as np
import json
import re
import flatdict

def ustvariSkripto():
    ulmSlv = {}
    ulmSlv.update(izpisiLanguageStrings())
    ulmSlv.update(izpisiHideControls())
    ulmSlv.update(izpisiRandomBulshit1())
    ulmSlv.update(izpisiIncludeBlocks())
    ulmSlv.update(izpisiStartingExample())
    ulmSlv.update({"checkEndEveryTurn":True})
    ulmSlv.update(izpisiCheckEndCondition())
    ulmSlv.update({"ignoreInvalidMoves":False})
    ulmSlv.update(izpisiRandomBulsit2())
    ulmSlv.update(izpisiItemTypes())
    jsonStr = json.dumps(ulmSlv, indent = 5, ensure_ascii=False)
    jsString1 = re.sub("\"([^\"]+)\":", r"\1:", jsonStr).replace(r'\"', "")
    jsString1 = jsString1.replace("\"&#&", "").replace("&#&\"", "").replace("\\\\", "\"").replace("\\n", "\n").replace("\\t", "\t")
    str1 = "subTask.gridInfos = {};".format(jsString1)

    subTaskData = izpisiSubTaskData()
    jsonStr = json.dumps(subTaskData, indent = 5, ensure_ascii=False)
    jsString2 = re.sub("\"([^\"]+)\":", r"\1:", jsonStr).replace(r'\"', "").replace("\"&#&", "").replace("&#&\"", "")
    jsString2 = jsString2.replace("\\n", "\n")
    str2 = "subTask.data = {};".format(jsString2)

    theString = "function initTask(subTask) {{\n {0}\n{1}\ninitBlocklySubTask(subTask); \n}}".format(str1, str2)
    fajl = open("static/javascript/theTest.js", "w", encoding = "utf-8")
    fajl.write(theString)
    fajl.close()

def saveItemTypes():
    global itemsIT, matrixExamples
    currentState = {"itemsIT":itemsIT, "matrixExamples":"&&&".join(map(str,matrixExamples))}
    jsonStr = json.dumps(currentState, indent = 5, ensure_ascii=False)
    jsonFile = open("savedItemTypes.txt", "w")
    jsonFile.write(jsonStr)
    jsonFile.close()

def getItemTypes():
    global itemsIT, matrixExamples

    jsonFile = open("savedItemTypes.txt", "r")
    jsonStr = jsonFile.read()
    pyVar = json.loads(jsonStr)

    itemsIT = pyVar["itemsIT"]
    matrixExamples = pyVar["matrixExamples"].split("&&&")


def saveVariables():
    global languageStrings, randomBull1, strSE, groupByCategory, includeAllIB, wholeCategories, robotIB, singleBlocksIB, excludedBlocksIB, possibleCategories, typeOptions, checkEndEveryTurn, ignoreInvalidMoves, endCondition, randomBull2, itemsIT, matrixExamples, initialisationExamples
    currentState = {"languageStrings":languageStrings, "randomBull1":randomBull1, "strSE":strSE,
                    "groupByCategory":groupByCategory, "includeAllIB":includeAllIB, "wholeCategories":wholeCategories,
                    "robotIB":robotIB, "singleBlocksIB":singleBlocksIB, "excludedBlocksIB":excludedBlocksIB,
                    "possibleCategories":list(possibleCategories), "typeOptions":list(typeOptions), "checkEndEveryTurn":checkEndEveryTurn,
                    "ignoreInvalidMoves":ignoreInvalidMoves, "endCondition":endCondition, "randomBull2":randomBull2,
                    "itemsIT":itemsIT, "matrixExamples":"&&&".join(map(str,matrixExamples)), "initialisationExamples":initialisationExamples}
    jsonStr = json.dumps(currentState, indent = 5, ensure_ascii=False)
    jsonFile = open("savedDat.txt", "w")
    jsonFile.write(jsonStr)
    jsonFile.close()

def loadVariables():
    global languageStrings, randomBull1, strSE, groupByCategory, includeAllIB, wholeCategories, robotIB, singleBlocksIB, excludedBlocksIB, possibleCategories, typeOptions, checkEndEveryTurn, ignoreInvalidMoves, endCondition, randomBull2, itemsIT, matrixExamples, initialisationExamples

    jsonFile = open("savedDat.txt", "r")
    jsonStr = jsonFile.read()
    pyVar = json.loads(jsonStr)
    languageStrings = pyVar["languageStrings"]
    randomBull1 = pyVar["randomBull1"]
    strSE = pyVar["strSE"]
    groupByCategory = pyVar["groupByCategory"]
    includeAllIB = pyVar["includeAllIB"]
    wholeCategories = pyVar["wholeCategories"]
    robotIB = pyVar["robotIB"]
    singleBlocksIB = pyVar["singleBlocksIB"]
    excludedBlocksIB = pyVar["excludedBlocksIB"]
    possibleCategories = set(pyVar["possibleCategories"])
    typeOptions = set(pyVar["typeOptions"])
    checkEndEveryTurn = pyVar["checkEndEveryTurn"]
    ignoreInvalidMoves = pyVar["ignoreInvalidMoves"]
    endCondition = pyVar["endCondition"]
    randomBull2 = pyVar["randomBull2"]
    itemsIT = pyVar["itemsIT"]
    matrixExamples = pyVar["matrixExamples"].split("&&&")
    initialisationExamples = pyVar["initialisationExamples"]

def izpisiLanguageStrings():
    global languageStringsLS
    pySlv = {"languageStrings":{"sl":{}}}
    pySlv["languageStrings"]["sl"] = languageStringsLS
    
    # jsonStr = json.dumps(pySlv, indent = 5, ensure_ascii=False)
    # jsString = re.sub("\"([^\"]+)\":", r"\1:", jsonStr).replace(r'\"', "")
    # return jsString[1:-1]
    return pySlv

def dodajSlovar(id, text):
    global languageStringsValues, languageStringsKeys, languageStringsLS
    languageStringsValues[id] = text
    slv1  =languageStringsLS.copy()
    f1 = flatdict.FlatDict(slv1, delimiter=".")
    pot = languageStringsKeys[id]
    f2 = flatdict.FlatDict({pot:text})

    f1[f2.keys()[0]] = f2.values()[0]
    languageStringsLS = f1.as_dict()
    print(languageStringsLS)

def izpisiHideControls(restart = False, saveOrLoad = False, loadBestAnswer = False, speedSlider = False, backToFirst = False, nextStep = False, goToEnd = False):
    pySlv = {"hideControls":{}}
    slv = {"restart": restart, "saveOrLoad": saveOrLoad, "loadBestAnswer": loadBestAnswer, "speedSlider": speedSlider, "backToFirst": backToFirst, "nextStep": nextStep, "goToEnd": goToEnd,}
    pySlv["hideControls"] = slv

    # jsonStr = json.dumps(pySlv, indent = 5)
    # jsString = re.sub("\"([^\"]+)\":", r"\1:", jsonStr).replace(r'\"', "")
    # return jsString[1:-1]
    return pySlv

def izpisiRandomBulshit1():
    global randomBull1
    return randomBull1

def izpisiStartingExample():
    global strSE
    pySlv = {"startingExample":{}}
    
    #python slovar
    pySlv["startingExample"]["blockly"] = strSE
    # jsonStr = json.dumps(pySlv, indent = 5)
    # jsString = re.sub("\"([^\"]+)\":", r"\1:", jsonStr).replace(r'\"', "")
    # return jsString[1:-1]
    return pySlv

def izpisiIncludeBlocks():
    global groupByCategory, includeAllIB, wholeCategories, robotIB, singleBlocksIB, excludedBlocksIB
    
    robotList = []
    wholeCategoriesList = []
    for key in robotIB.keys():
        if robotIB[key]:
            robotList.append(key)
    for key in wholeCategories.keys():
        if wholeCategories[key]:
            wholeCategoriesList.append(key)

    slv = {"groupByCategory": groupByCategory, "generatedBlocks": {"robot": robotList}, "standardBlocks": {"includeAll": includeAllIB, "wholeCategories": wholeCategoriesList, "singleBlocks": singleBlocksIB, "excludedBlocks": excludedBlocksIB,},}
    pySlv = {"includeBlocks":{}}
    
    pySlv["includeBlocks"] = slv
    
    return pySlv

def izpisiCheckEndCondition():
    global endCondition

    indikator1 = endCondition["Exist"]["indikator1"]
    ime1 = endCondition["Exist"]["ime1"]
    negIndikator1 = endCondition["Exist"]["negIndikator1"]
    negIme1 = endCondition["Exist"]["negIme1"]
    indikatorA = endCondition["Coincide"]["indikatorA"]
    imeA = endCondition["Coincide"]["imeA"]
    indikatorB = endCondition["Coincide"]["indikatorB"]
    imeB = endCondition["Coincide"]["imeB"]
    keys = endCondition["Coincide"]["keys"]
    negIndikatorA = endCondition["Coincide"]["negIndikatorA"]
    negImeA = endCondition["Coincide"]["negImeA"]
    negIndikatorB = endCondition["Coincide"]["negIndikatorB"]
    negImeB = endCondition["Coincide"]["negImeB"]

    lst = [indikator1, ime1, negIndikator1, negIme1, indikatorA, imeA, indikatorB, imeB, keys, negIndikatorA, negImeA, negIndikatorB, negImeB]
    for i in range(len(lst)):
        if lst[i] == None:
            lst[i] = ""
    
    filters1 = r"{}"
    negFilters1 = r"{}"
    filtersA = r"{}"
    filtersB = r"{}"
    keys = r"[]"
    
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
        if lst[9] and lst[10]:
            negFiltersA = "{%s: \\%s\\}"%(lst[9], lst[10])
        if lst[11] and lst[12]:
            negFiltersB = "{%s: \\%s\\}"%(lst[11], lst[12])
        
        endCond2 = "robotEndConditions.checkItemCoincidence(context, lastTurn, filtersA, filtersB, keys, negFiltersA, negFiltersB)".replace("filtersA", filtersA).replace("filtersB", filtersB).replace("keys", keys).replace("negFiltersA", negFiltersA).replace("negFiltersB", negFiltersB)
        funkcija2 = "(context, lastTurn) => { %s }"%(endCond2)

    openFile = open("./generatorSkripte/endConditionTemplate.txt", "r")
    template = openFile.read()
    template = "&#&" + template.replace("funkcija1", funkcija1).replace("funkcija2", funkcija2) + "&#&"
    pySlv = {"checkEndCondition": template}
    openFile.close()
    
    return pySlv

def izpisiRandomBulsit2(): 
    global randomBull2
    return randomBull2

def izpisiItemTypes():
    global itemsIT
    kopija = {}
    for nameKey in itemsIT.keys():
        kopija[nameKey] = {}
        for k in itemsIT[nameKey].keys():
            if (k == "row" or k == "col") or (k == "num" and nameKey == "robot0"):
                continue
            else:
                kopija[nameKey][k] = itemsIT[nameKey][k]
    pySlv = {"itemTypes":kopija}
    
    return pySlv

def dodajItemType():
    global itemsIT, itemID, typeOptions, possibleCategories, itemSpecifications, matrixExamples, aktivenPrimer, catIT
    ime = itemSpecifications.pop("name")
    if ime == "":
        return
    if ime not in list(itemsIT.keys()):
        itemID += 1
    catsTrue = []
    for cat in catIT.keys():
        if catIT[cat]:
            catsTrue.append({"\"%s\""%cat:True})
            possibleCategories.add(cat)
    itemSpecifications["category"] = catsTrue[0]
    
    rows = itemSpecifications["row"]
    cols = itemSpecifications["col"]

    itemSpecifications["num"] = len(list(itemsIT.keys()))+2

    itemsIT[ime] = itemSpecifications
    itemsIT[ime]
    itemsIT[ime]
    updateMatrix()
    catIT = {'robot': False, 'obstacle': False, 'transportable': False, 'button': False, 'coin': False, 'number': False}
    
    #saveItemTypes()


    typeOptions.add(ime)
    itemSpecifications = {"name":"", "num": itemID, "img":"", "zOrder":itemID, "category":catIT, "value":0, "row":[0], "col":[0]} #nazaj na default

def updateMatrix():
    global itemsIT, matrixExamples, aktivenPrimer
    for key in itemsIT.keys():
        item = itemsIT[key]
        rows = item["row"]
        cols = item["col"]
        sizey = len(matrixExamples[aktivenPrimer])
        sizex = len(matrixExamples[aktivenPrimer][0])
        for i in range(len(rows)):
            if rows[i] < sizex and cols[i] < sizey:
                matrixExamples[aktivenPrimer][cols[i]][rows[i]] = item["num"]

def addRobot():
    global itemsIT, itemID, typeOptions, possibleCategories, itemSpecifications, matrixExamples, aktivenPrimer, catIT
    ime = itemSpecifications.pop("name")
    if ime == "":
        return
    itemID += 1
    itemSpecifications["category"] = {"\"robot\"":True}
    itemSpecifications["zOrder"] = 10
    row = itemSpecifications["row"][0]
    col = itemSpecifications["col"][0]

    itemsIT[ime] = itemSpecifications
    
    # inicializacija
    removeInicialisation(ime)
    addInicialisation({"row":row, "col":col, "type":ime, "dir": 0, "value": 0})
    alreadyInitialized.add(ime)

    catIT = {'robot': False, 'obstacle': False, 'transportable': False, 'button': False, 'coin': False, 'number': False}
    
    #saveItemTypes()
    typeOptions.add(ime)
    itemSpecifications = {"name":"", "num": itemID, "img":"", "zOrder":itemID, "category":catIT, "value":0, "nbStates":1,"row":[0], "col":[0]} #nazaj na default

def deleteItemType(ime):
    global itemsIT, itemID, typeOptions, possibleCategories
    
    itemID -= 1
    if ime in list(itemsIT.keys()):
        typeOptions.remove(ime)
        itemsIT.pop(ime)
    removeInicialisation(ime)

def izpisiSubTaskData():
    global matrixExamples, initialisationExamples, mmm, nnn
    changeMatrixSize()
    pySlv = {}
    pyLst = []
    for i in range(len(initialisationExamples)):
        pyLst.append({"tiles":izpisiMatriko(matrixExamples[i]), "initItems":initialisationExamples[i]})

    
    pySlv["easy"] = pyLst
    return pySlv
    
def izpisiMatriko(matrix):
    #matrix = np.array(matrix)
    return "&#&" + str(matrix).replace("],", "], \n") + "&#&"


def addMatrix(mmm, nnn):
    global matrixExamples, aktivenPrimer
    matrixExamples[aktivenPrimer] = [[1 for i in range(mmm)] for j in range(nnn)]

def addInicialisation(initSlv):
    global initialisationExamples, aktivenPrimer
    initialisationExamples[aktivenPrimer].append(initSlv)

def removeInicialisation(name):
    for i in range(len(initialisationExamples[aktivenPrimer])):
        if initialisationExamples[aktivenPrimer][i]["type"] == name:
            initialisationExamples[aktivenPrimer] = initialisationExamples[aktivenPrimer][:i] + initialisationExamples[aktivenPrimer][i+1:]


def addExample():
    global initialisationExamples, aktivenPrimer, mmm, nnn
    aktivenPrimer += 1
    initialisationExamples.append([])
    matrixExamples.append([])
    addMatrix(mmm, nnn)

def changeMatrixValues(row, col, value):
    global matrixExamples, aktivenPrimer
    matrixExamples[aktivenPrimer][row][col] = value

def changeMatrixSize():
    global matrixExamples, aktivenPrimer, nnn, mmm
    mat = matrixExamples[aktivenPrimer]
    rr = len(mat)
    cc = len(mat[0])
    # upam da se mat obnaša klokr referenca ne kokr solo matrika
    mat = np.array(mat)
    mat2 = np.ones((nnn, mmm), dtype=np.int8)
    if (rr > nnn and cc > mmm):
        mat = mat[:nnn, :mmm]
    elif (rr < nnn and cc < mmm):
        mat2[:rr, :cc] = mat
        mat = mat2
    elif (rr > nnn and cc < mmm):
        mat2[::, :cc] = mat[:nnn, ::]
        mat = mat2
    elif (rr < nnn and cc > mmm):
        mat2[:rr, ::] = mat[::, :mmm]
        mat = mat2
    matrixExamples[aktivenPrimer] = [[mat[j][i] for i in range(mmm)] for j in range(nnn)]
    updateMatrix()

def ustvariSkripto():
    print("USTVARJAM SKRIPTO")
    ulmSlv = {}
    ulmSlv.update(izpisiLanguageStrings())
    ulmSlv.update(izpisiHideControls())
    ulmSlv.update(izpisiRandomBulshit1())
    ulmSlv.update(izpisiIncludeBlocks())
    ulmSlv.update(izpisiStartingExample())
    ulmSlv.update({"checkEndEveryTurn":False})
    ulmSlv.update(izpisiCheckEndCondition())
    ulmSlv.update({"ignoreInvalidMoves":False})
    ulmSlv.update(izpisiRandomBulsit2())
    ulmSlv.update(izpisiItemTypes())
    jsonStr = json.dumps(ulmSlv, indent = 5, ensure_ascii=False)
    jsString1 = re.sub("\"([^\"]+)\":", r"\1:", jsonStr).replace(r'\"', "")
    jsString1 = jsString1.replace("\"&#&", "").replace("&#&\"", "").replace("\\\\", "\"").replace("\\n", "\n").replace("\\t", "\t")
    str1 = "subTask.gridInfos = {};".format(jsString1)

    subTaskData = izpisiSubTaskData()
    jsonStr = json.dumps(subTaskData, indent = 5, ensure_ascii=False)
    jsString2 = re.sub("\"([^\"]+)\":", r"\1:", jsonStr).replace(r'\"', "").replace("\"&#&", "").replace("&#&\"", "")
    jsString2 = jsString2.replace("\\n", "\n")
    str2 = "subTask.data = {};".format(jsString2)

    theString = "function initTask(subTask) {{\n {0}\n{1}\ninitBlocklySubTask(subTask); \n}}".format(str1, str2)
    fajl = open("static/javascript/theTest.js", "w", encoding = "utf-8")
    fajl.write(theString)
    fajl.close()

def saveItemTypes():
    global itemsIT, matrixExamples
    currentState = {"itemsIT":itemsIT, "matrixExamples":"&&&".join(map(str,matrixExamples))}
    jsonStr = json.dumps(currentState, indent = 5, ensure_ascii=False)
    jsonFile = open("savedItemTypes.txt", "w")
    jsonFile.write(jsonStr)
    jsonFile.close()

def getItemTypes():
    global itemsIT, matrixExamples

    jsonFile = open("savedItemTypes.txt", "r")
    jsonStr = jsonFile.read()
    pyVar = json.loads(jsonStr)

    itemsIT = pyVar["itemsIT"]
    matrixExamples = pyVar["matrixExamples"].split("&&&")


def saveVariables():
    global languageStrings, randomBull1, strSE, groupByCategory, includeAllIB, wholeCategories, robotIB, singleBlocksIB, excludedBlocksIB, possibleCategories, typeOptions, checkEndEveryTurn, ignoreInvalidMoves, endCondition, randomBull2, itemsIT, matrixExamples, initialisationExamples
    currentState = {"languageStrings":languageStrings, "randomBull1":randomBull1, "strSE":strSE,
                    "groupByCategory":groupByCategory, "includeAllIB":includeAllIB, "wholeCategories":wholeCategories,
                    "robotIB":robotIB, "singleBlocksIB":singleBlocksIB, "excludedBlocksIB":excludedBlocksIB,
                    "possibleCategories":list(possibleCategories), "typeOptions":list(typeOptions), "checkEndEveryTurn":checkEndEveryTurn,
                    "ignoreInvalidMoves":ignoreInvalidMoves, "endCondition":endCondition, "randomBull2":randomBull2,
                    "itemsIT":itemsIT, "matrixExamples":"&&&".join(map(str,matrixExamples)), "initialisationExamples":initialisationExamples}
    jsonStr = json.dumps(currentState, indent = 5, ensure_ascii=False)
    jsonFile = open("savedDat.txt", "w")
    jsonFile.write(jsonStr)
    jsonFile.close()

def loadVariables():
    global languageStrings, randomBull1, strSE, groupByCategory, includeAllIB, wholeCategories, robotIB, singleBlocksIB, excludedBlocksIB, possibleCategories, typeOptions, checkEndEveryTurn, ignoreInvalidMoves, endCondition, randomBull2, itemsIT, matrixExamples, initialisationExamples

    jsonFile = open("savedDat.txt", "r")
    jsonStr = jsonFile.read()
    pyVar = json.loads(jsonStr)
    languageStrings = pyVar["languageStrings"]
    randomBull1 = pyVar["randomBull1"]
    strSE = pyVar["strSE"]
    groupByCategory = pyVar["groupByCategory"]
    includeAllIB = pyVar["includeAllIB"]
    wholeCategories = pyVar["wholeCategories"]
    robotIB = pyVar["robotIB"]
    singleBlocksIB = pyVar["singleBlocksIB"]
    excludedBlocksIB = pyVar["excludedBlocksIB"]
    possibleCategories = set(pyVar["possibleCategories"])
    typeOptions = set(pyVar["typeOptions"])
    checkEndEveryTurn = pyVar["checkEndEveryTurn"]
    ignoreInvalidMoves = pyVar["ignoreInvalidMoves"]
    endCondition = pyVar["endCondition"]
    randomBull2 = pyVar["randomBull2"]
    itemsIT = pyVar["itemsIT"]
    matrixExamples = pyVar["matrixExamples"].split("&&&")
    initialisationExamples = pyVar["initialisationExamples"]

def resetVariables():
    global languageStrings, languageStringsKeys, languageStringsKeyWord, languageStringsValues, languageStringsLS, randomBull1, strSE, groupByCategory, includeAllIB, wholeCategories, robotIB, singleBlocksIB, excludedBlocksIB, possibleCategories, typeOptions, checkEndEveryTurn, ignoreInvalidMoves, endCondition, randomBull2, itemsIT, matrixExamples, initialisationExamples

    fajlLS = open('imenaDelckov.txt', "r", encoding = ("utf-8"))
    # returns JSON object as 
    # a dictionary
    languageStringsSlv = json.load(fajlLS)["sl"]
    # # Closing file
    fajlLS.close()
    languageStringsSlvFlat  = flatdict.FlatDict(languageStringsSlv, delimiter=".")
    languageStringsKeys = [key for key in languageStringsSlvFlat.keys()]

    languageStringsKeyWord = [key.split(".")[-1] for key in languageStringsSlvFlat.keys()]
    languageStringsValues = languageStringsSlvFlat.values()

    #TE SPREMENLJIVKE SE SPREMINJAJO DIREKTNO S SPLETNE STRANI   KUL?
    #Globalna spremenljivka LANGUAGE STRINGS - shranjuje vse language stringe
    languageStringsLS = {}

    # languageStrings = dodajSlovar(idLS, txtLS) # za posodobitev kliči to funkcijo in za drugi paramter uporabi kar pride iz spletne strani

    # RANDOM BULŠIT 1
    randomBull1 = {"introMaxHeight": "33%",
        "maxListSize": 100, 
        "scrollbars": True,
        "zoom": {
            "controls": True,
            "scale": 1,
            },
        "actionDelay": 400,				
        "blocklyColourTheme": "bwinf",
        "maxInstructions": 0
        }
    # Spreminjava samo maxInstructions!
    # ZAČETNA POSTAVITEV - na spletni strani naj bo gumb - posodobi začetno postavitev. Samo zamenjaj string
    strSE = ''

    # INCLUDE BLOCKS
    groupByCategory = True # neki za obklukat
    includeAllIB = False # neki za obklukat
    wholeCategories = {"tools":False, "logic":False, "loops":False, "math":False, "texts":False, "lists":False, "colour":False, "variables":False, "functions":False} # neki za obklukat
    # bloki za robota, na začetku so vsi false, na spletni strani naj bo dropdown za klukat, ko obkljuka spremeni v True
    robotIB = {"move": False, "moveSimple": False, "forward": False, "forwardSimple": False, "turn": False, "turnAround": False, "jump": False, "changeRobot": False, "transport": False, "sensorBool": False, "sensorValue": False, "alterValue": False, "destroy": False, "create": False, "wait": False, "nitems": False, "sensorRowCol": False}
    singleBlocksIB = []
    excludedBlocksIB = []
    # možnosti "move", "moveSimple", "forward", "forwardSimple", "turn", "turnAround", "jump", "changeRobot", "transport", "sensorBool", "sensorValue", "alterValue", "destroy", "create", "wait", "nitems", "sensorRowCol"

    # END CONDITIONS
    possibleIdicateors = {'category', 'value', 'type'} # možnosti

    possibleCategories = set() # updejta se samodejno pri ustvarjenju objektov
    typeOptions = set() #imena predmetov, ki so na izbiro za inicializacijo objekta, dodajajo se avtomatsko s klicanjem funkcije dodajItemType.
    # opcije za indikator = possibleIdicateors
    # odvisno od izbranega indikatorja so odvisna tudi imena
    # če je indikator category = opcije za ime = possibleCategories
    # če je indikator value = opcije za ime = kerakol številka. Mejbi bo treba dtr omejitev
    # če je indikator type = opcije za ime = typeOptions
    # jebeš keys, nerabš

    checkEndEveryTurn = True
    ignoreInvalidMoves = False
    # to je default, vpisuj notr kar najdeš v zgornjih opcijah
    endCondition = {"Exist": {"indikator1": "category", "ime1": "coin", "negIndikator1": None, "negIme1": None},
                    "Coincide": {"indikatorA": None, "imeA": None, "indikatorB": None, "imeB": None, "keys": None, "negIndikatorA": None, "negImeA": None, "negIndikatorB": None, "negImeB": None}}

    #RANDOM BULŠIT 2
    randomBull2 = {"border": 0.02,
        "backgroundColour": "white",
        "backgroundTile": "",
        "borderColour": "black",
        "showLabels": True,
        "cellSide": 60,	
        "numberOfRobots": 1
        }
    #numberOfRobots naj bo 1 default

    #OBJEKTI
    itemsIT = {} # samodejno shranjuje vse iteme
    itemID = 2 #se poveča samodejno, odvisen od števila itemov
    # ko uporabnik želi ustvariti nov objekt naj ima možnosti ime, slika, kategorija, vrednost - izbira naj se vpiše v itemSpecifications
    # poleg možnosti naj bosta zraven še gumba ustvari in izbriši ki kličeta funkciji dodajItemType

    catIT = {'robot': False, 'obstacle': False, 'transportable': False, 'button': False, 'coin': False, 'number': False} #za obklukat - možnosti kategorij

    # imgIT = ["pisek.png"]
    # zOrderIT #naj bo odvisen od vrstnega reda stvaritve objektov, seprav isti kokritemID
    # nbStatesIT = 8 odvisen le od robota

    #globalna spremenljivka trenutnih nastavitev za nov item, po ustvarjenju itema se resetira na default vrednosti
    itemSpecifications = {"name":"", "num": 2, "img":"", "zOrder":2, "category":{}, "value":0, "nbStates":8,"row":[0], "col":[0]}

    #MREŽA
    #GLOBAL
    aktivenPrimer = 0 # če imaš več primerov, Id katerega trenutno editiraš
    mmm = 5
    nnn = 5
    matrixExamples = [[]] #seznam matrik - lahko da je več testov
    initialisationExamples = [[]]
    addMatrix(mmm, nnn)
    globalka = 0

    alreadyInitialized = set()

fajlLS = open('imenaDelckov.txt', "r", encoding = ("utf-8"))
# returns JSON object as 
# a dictionary
languageStringsSlv = json.load(fajlLS)["sl"]
# # Closing file
fajlLS.close()
languageStringsSlvFlat  = flatdict.FlatDict(languageStringsSlv, delimiter=".")
languageStringsKeys = [key for key in languageStringsSlvFlat.keys()]

languageStringsKeyWord = [key.split(".")[-1] for key in languageStringsSlvFlat.keys()]
languageStringsValues = languageStringsSlvFlat.values()

#TE SPREMENLJIVKE SE SPREMINJAJO DIREKTNO S SPLETNE STRANI   KUL?
#Globalna spremenljivka LANGUAGE STRINGS - shranjuje vse language stringe
languageStringsLS = {}

# languageStrings = dodajSlovar(idLS, txtLS) # za posodobitev kliči to funkcijo in za drugi paramter uporabi kar pride iz spletne strani

# RANDOM BULŠIT 1
randomBull1 = {"introMaxHeight": "33%",
    "maxListSize": 100, 
    "scrollbars": True,
    "zoom": {
        "controls": True,
        "scale": 1,
        },
    "actionDelay": 400,				
    "blocklyColourTheme": "bwinf",
    "maxInstructions": 0
    }
# Spreminjava samo maxInstructions!
# ZAČETNA POSTAVITEV - na spletni strani naj bo gumb - posodobi začetno postavitev. Samo zamenjaj string
strSE = ''

# INCLUDE BLOCKS
groupByCategory = True # neki za obklukat
includeAllIB = False # neki za obklukat
wholeCategories = {"tools":False, "logic":False, "loops":False, "math":False, "texts":False, "lists":False, "colour":False, "variables":False, "functions":False} # neki za obklukat
# bloki za robota, na začetku so vsi false, na spletni strani naj bo dropdown za klukat, ko obkljuka spremeni v True
robotIB = {"move": False, "moveSimple": False, "forward": False, "forwardSimple": False, "turn": False, "turnAround": False, "jump": False, "changeRobot": False, "transport": False, "sensorBool": False, "sensorValue": False, "alterValue": False, "destroy": False, "create": False, "wait": False, "nitems": False, "sensorRowCol": False}
singleBlocksIB = []
excludedBlocksIB = []
# možnosti "move", "moveSimple", "forward", "forwardSimple", "turn", "turnAround", "jump", "changeRobot", "transport", "sensorBool", "sensorValue", "alterValue", "destroy", "create", "wait", "nitems", "sensorRowCol"

# END CONDITIONS
possibleIdicateors = {'category', 'value', 'type'} # možnosti

possibleCategories = set() # updejta se samodejno pri ustvarjenju objektov
typeOptions = set() #imena predmetov, ki so na izbiro za inicializacijo objekta, dodajajo se avtomatsko s klicanjem funkcije dodajItemType.
# opcije za indikator = possibleIdicateors
# odvisno od izbranega indikatorja so odvisna tudi imena
# če je indikator category = opcije za ime = possibleCategories
# če je indikator value = opcije za ime = kerakol številka. Mejbi bo treba dtr omejitev
# če je indikator type = opcije za ime = typeOptions
# jebeš keys, nerabš

checkEndEveryTurn = True
ignoreInvalidMoves = False
# to je default, vpisuj notr kar najdeš v zgornjih opcijah
endCondition = {"Exist": {"indikator1": "category", "ime1": "coin", "negIndikator1": None, "negIme1": None},
                "Coincide": {"indikatorA": None, "imeA": None, "indikatorB": None, "imeB": None, "keys": None, "negIndikatorA": None, "negImeA": None, "negIndikatorB": None, "negImeB": None}}

#RANDOM BULŠIT 2
randomBull2 = {"border": 0.02,
    "backgroundColour": "white",
    "backgroundTile": "",
    "borderColour": "black",
    "showLabels": True,
    "cellSide": 60,	
    "numberOfRobots": 1
    }
#numberOfRobots naj bo 1 default

#OBJEKTI
itemsIT = {} # samodejno shranjuje vse iteme
itemID = 2 #se poveča samodejno, odvisen od števila itemov
# ko uporabnik želi ustvariti nov objekt naj ima možnosti ime, slika, kategorija, vrednost - izbira naj se vpiše v itemSpecifications
# poleg možnosti naj bosta zraven še gumba ustvari in izbriši ki kličeta funkciji dodajItemType

catIT = {'robot': False, 'obstacle': False, 'transportable': False, 'button': False, 'coin': False, 'number': False} #za obklukat - možnosti kategorij

# imgIT = ["pisek.png"]
# zOrderIT #naj bo odvisen od vrstnega reda stvaritve objektov, seprav isti kokritemID
# nbStatesIT = 8 odvisen le od robota

#globalna spremenljivka trenutnih nastavitev za nov item, po ustvarjenju itema se resetira na default vrednosti
itemSpecifications = {"name":"", "num": 2, "img":"", "zOrder":2, "category":{}, "value":0, "nbStates":8,"row":[0], "col":[0]}

#MREŽA
#GLOBAL
aktivenPrimer = 0 # če imaš več primerov, Id katerega trenutno editiraš
mmm = 5
nnn = 5
matrixExamples = [[]] #seznam matrik - lahko da je več testov
initialisationExamples = [[]]
addMatrix(mmm, nnn)
globalka = 0

alreadyInitialized = set()
# type nujno!!! izberi it typeOptions
#inicialisationOptions = {"row":0, "col":0, "type":list(typeOptions)[0], "dir": 0, "value": 0}

if __name__ == "__main__":
    #ustvariSkripto()
    #saveVariables()
    #loadVariables()
    ustvariSkripto()
