import numpy as np
import json
import re
import flatdict

#ne dela nč...
def saveItemTypes():
    global itemsIT, matrixExamples
    currentState = {"itemsIT":itemsIT, "matrixExamples":"&&&".join(map(str,matrixExamples))}
    jsonStr = json.dumps(currentState, indent = 5, ensure_ascii=False)
    jsonFile = open("savedItemTypes.txt", "w")
    jsonFile.write(jsonStr)
    jsonFile.close()

#še nč ne dela
def getItemTypes():
    global itemsIT, matrixExamples

    jsonFile = open("savedItemTypes.txt", "r")
    jsonStr = jsonFile.read()
    pyVar = json.loads(jsonStr)

    itemsIT = pyVar["itemsIT"]
    matrixExamples = pyVar["matrixExamples"].split("&&&")

#še nč ne dela
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

#še nč ne dela
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

#Language strigs zapakira v pythonov slovar.
def izpisiLanguageStrings():
    global languageStringsLS
    pySlv = {"languageStrings":{"sl":{}}}
    pySlv["languageStrings"]["sl"] = languageStringsLS
    
    # jsonStr = json.dumps(pySlv, indent = 5, ensure_ascii=False)
    # jsString = re.sub("\"([^\"]+)\":", r"\1:", jsonStr).replace(r'\"', "")
    # return jsString[1:-1]
    return pySlv

#V language strings doda spremenjen slovar
def dodajSlovar(id, text):
    global languageStringsValues, languageStringsKeys, languageStringsLS
    languageStringsValues[id] = text
    slv1  =languageStringsLS.copy()
    f1 = flatdict.FlatDict(slv1, delimiter=".")
    pot = languageStringsKeys[id]
    f2 = flatdict.FlatDict({pot:text})

    f1[f2.keys()[0]] = f2.values()[0]
    languageStringsLS = f1.as_dict()

#v slovarju vrne podatke za hideControl. Je na default
def izpisiHideControls(restart = False, saveOrLoad = False, loadBestAnswer = False, speedSlider = False, backToFirst = False, nextStep = False, goToEnd = False):
    pySlv = {"hideControls":{}}
    slv = {"restart": restart, "saveOrLoad": saveOrLoad, "loadBestAnswer": loadBestAnswer, "speedSlider": speedSlider, "backToFirst": backToFirst, "nextStep": nextStep, "goToEnd": goToEnd,}
    pySlv["hideControls"] = slv

    # jsonStr = json.dumps(pySlv, indent = 5)
    # jsString = re.sub("\"([^\"]+)\":", r"\1:", jsonStr).replace(r'\"', "")
    # return jsString[1:-1]
    return pySlv

#vrne slovar randomBull1
def izpisiRandomBulshit1():
    global randomBull1
    return randomBull1

#vrne slovar v katerem je začetzni primer
def izpisiStartingExample():
    global strSE
    pySlv = {"startingExample":{}}
    strSE = strSE.replace("\"", "'")
    #python slovar
    pySlv["startingExample"]["blockly"] = strSE
    # jsonStr = json.dumps(pySlv, indent = 5)
    # jsString = re.sub("\"([^\"]+)\":", r"\1:", jsonStr).replace(r'\"', "")
    # return jsString[1:-1]
    return pySlv

#rne slovar z blocky
def izpisiIncludeBlocks():
    global groupByCategory, includeAllIB, wholeCategoriesIB, robotIB, singleBlocksIB, excludedBlocksIB
    
    robotList = []
    wholeCategoriesList = []
    singleBlocksList = []
    for key in robotIB.keys():
        if robotIB[key]:
            robotList.append(key)
    for key in wholeCategoriesIB.keys():
        if wholeCategoriesIB[key]:
            wholeCategoriesList.append(key)
    for key in singleBlocksIB.keys():
        if singleBlocksIB[key]:
            singleBlocksList.append(key)

    slv = {"groupByCategory": groupByCategory, "generatedBlocks": {"robot": robotList}, "standardBlocks": {"includeAll": includeAllIB, "wholeCategories": wholeCategoriesList, "singleBlocks": singleBlocksList, "excludedBlocks": excludedBlocksIB,},}
    pySlv = {"includeBlocks":{}}
    
    pySlv["includeBlocks"] = slv
    
    return pySlv

#vrne slovar s končnimi pogoji v stringu
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
    if (lst[0] == "" or lst[1] == "") and (lst[2] == "" or lst[3] == ""):
        funkcija1 = r"//"
    else:
        if lst[0] != "" and lst[1] != "":
            filters1 = "{%s: \\%s\\}"%(lst[0], lst[1])
        if lst[2] != "" and lst[3] != "":
            negFilters1 = "{%s: \\%s\\}"%(lst[2], lst[3])
        endCond1 = "robotEndConditions.checkItemExistence(context, lastTurn, filters1, negFilters1, exist=false)".replace("filters1", filters1).replace("negFilters1", negFilters1)
        funkcija1 = "(context, lastTurn) => { %s }"%(endCond1)

    if ((lst[4] == "" or lst[5] == "") and (lst[6] == "" or lst[7] == "")) and ((lst[9] == "" or lst[10] == "") and (lst[11] == "" or lst[12] == "")):
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

#isto kokr randombull1
def izpisiRandomBulsit2(): 
    global randomBull2
    return randomBull2

#izpiše slovar itemTypov
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

#v slovar iteTypov doda item type
def dodajItemType():
    global itemsIT, itemID, typeOptions, possibleCategories, itemSpecifications, matrixExamples, activeExample, catIT
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
    typeOptions.add(ime)
    itemSpecifications["category"] = catsTrue
    print(itemSpecifications)
    itemSpecifications["num"] = len(list(typeOptions))+2

    itemsIT[ime] = itemSpecifications

    setCategoryDeafult()
    
    #saveItemTypes()
    itemSpecifications = {"name":"", "num": itemID, "img":"", "zOrder":itemID, "category":catIT, "value":0, "row":[], "col":[]} #nazaj na default

#vse trenutne kategorije da na false
def setCategoryDeafult():
    global catIT
    for key in list(catIT.keys()):
        catIT[key] = False

#v slovar iteTypov doda item 
def createDefaultItem(itemCategory, itemImage):
    global itemsIT, itemID, typeOptions, possibleCategories, itemSpecifications, matrixExamples, activeExample, catIT
    itemNameId = 0
    for itemName in itemsIT.keys():
        if itemCategory in itemName:
            if itemImage != itemsIT[itemName]["img"][:-4]:
                itemNameId += 1
    ime = itemCategory + str(itemNameId)
    typeOptions.add(ime)
    itemSpec = {"num": 2, "img":"", "zOrder":5, "category":{}, "value":0, "row":[[]for i in range(len(matrixExamples))], "col":[[]for i in range(len(matrixExamples))]}
    
    itemSpec["category"] = [{"\"%s\""%itemCategory:True}]
    itemSpec["num"] = len(list(typeOptions))+2
    itemSpec["img"] = [itemImage]
    itemSpec["zOrder"] = len(typeOptions)

    itemsIT[ime] = itemSpec

#v slovar iteTypov doda number
def createDefaultNumber(itemValue):
    global itemsIT, itemID, typeOptions, possibleCategories, itemSpecifications, matrixExamples, activeExample, catIT
    itemCategory = "number"
    ime = itemCategory + itemValue
    typeOptions.add(ime)
    itemSpec = {"num":2, "zOrder":4, "row":[[]for i in range(len(matrixExamples))], "col":[[]for i in range(len(matrixExamples))]}
    
    itemSpec["category"] = [{"\"%s\""%itemCategory:True}]
    itemSpec["value"] = itemValue
    itemSpec["num"] = len(list(typeOptions))+2
    itemsIT[ime] = itemSpec
    
#v slovar iteTypov doda barvo
def createDefaultColor(itemCol):
    global itemsIT, itemID, typeOptions, possibleCategories, itemSpecifications, matrixExamples, activeExample, catIT
    itemCategory = "color"
    itemNameId = 0
    for itemName in itemsIT.keys():
        if itemCategory in itemName:
            if itemCol != itemsIT[itemName]["colour"]:
                itemNameId += 1
    ime = itemCategory + str(itemNameId)
    typeOptions.add(ime)
    itemSpec = {"num":2, "zOrder":2, "value":0, "row":[[]for i in range(len(matrixExamples))], "col":[[]for i in range(len(matrixExamples))]}
    
    itemSpec["colour"] = itemCol
    itemSpec["num"] = len(list(typeOptions))+2
    itemsIT[ime] = itemSpec

#v slovar iteTypov doda gumb
def createDefaultButton(buttonOn, buttonOff):
    global itemsIT, itemID, typeOptions, possibleCategories, itemSpecifications, matrixExamples, activeExample, catIT
    itemCategory = "button"
    itemNameId = 0
    for itemName in itemsIT.keys():
        if itemCategory in itemName:
            itemNameId += 1
    ime = itemCategory +"_"+ str(itemNameId)
    typeOptions.add(ime)
    itemSpec = {"img":[buttonOn, buttonOff], "num":2, "zOrder":3, "value":0, "id":itemNameId, "row":[[]for i in range(len(matrixExamples))], "col":[[]for i in range(len(matrixExamples))]}
    itemSpec["num"] = len(list(typeOptions))+2
    itemSpec["category"] = [{"\"%s\""%itemCategory:True}]
    itemsIT[ime] = itemSpec

# item type doda na matriko, če na matriki že obstaja ga inicializira
def addItemTypeToMatrix(itemName, itemRow, itemCol):
    global itemsIT, activeExample
    if "robot" in itemName:
        itemsIT[itemName]["row"][activeExample] = [itemRow]
        itemsIT[itemName]["col"][activeExample] = [itemCol]
        removeInicialisation(itemName, -1, -1)
        addInicialisation({"row":itemRow, "col":itemCol, "type":itemName, "dir": 0, "value": 0})

    obstaja = False
    for i in range(len(itemsIT[itemName]["row"][activeExample])):
        if itemRow == itemsIT[itemName]["row"][activeExample][i] and itemCol == itemsIT[itemName]["col"][activeExample][i]:
            obstaja = True
    if not obstaja:
        itemsIT[itemName]["row"][activeExample].append(itemRow)
        itemsIT[itemName]["col"][activeExample].append(itemCol)
        updateMatrix()

#odstrani iz matrike in iz inicializacije
def removeItemTypeFromMatrix(itemName, itemRow, itemCol):
    global itemsIT, activeExample
    if itemRow in itemsIT[itemName]["row"][activeExample] and itemCol in itemsIT[itemName]["col"][activeExample]:
        itemsIT[itemName]["row"][activeExample].remove(itemRow)
        itemsIT[itemName]["col"][activeExample].remove(itemCol)
        updateMatrix()
        removeInicialisation(itemName, itemRow, itemCol)

#posodobi matriko. Iz vsakega itema prebere kje je.
def updateMatrix():
    global itemsIT, matrixExamples, activeExample
    numRows = len(matrixExamples[activeExample])
    numCols = len(matrixExamples[activeExample][0])
    for i in range(numRows):
        for j in range(numCols):
            matrixExamples[activeExample][i][j] = 1
    for key in itemsIT.keys():
        item = itemsIT[key]
        rows = item["row"][activeExample]
        cols = item["col"][activeExample]
        
        for i in range(len(cols)):
            if cols[i] < numCols and rows[i] < numRows and "robot" not in key:
                if matrixExamples[activeExample][rows[i]][cols[i]] == 1:
                    matrixExamples[activeExample][rows[i]][cols[i]] = item["num"]
                else:
                    removeInicialisation(key, rows[i], cols[i])
                    addInicialisation({"row":rows[i], "col":cols[i], "type":key, "dir": 0, "value": 0})

#v inicializacijo doda robota
def addRobot(itemImage):
    global itemsIT, itemID, typeOptions, possibleCategories, itemSpecifications, matrixExamples, activeExample, catIT
    
    itemNameId = 0
    for itemName in itemsIT.keys():
        if "robot" in itemName:
            if itemImage != itemsIT[itemName]["img"]:
                itemNameId += 1
    randomBull2["numberOfRobots"] = itemNameId+1
    itemSpec = {"img":"", "zOrder":20, "value":0, "nbStates":9, "row":[[0]for i in range(len(matrixExamples))], "col":[[0]for i in range(len(matrixExamples))]}
    ime = "robot" + str(itemNameId)
    typeOptions.add(ime)
    itemSpec["category"] = [{"\"robot\"":True}]
    itemSpec["img"] = [itemImage]
    itemsIT[ime] = itemSpec
    setCategoryDeafult()
    addItemTypeToMatrix(ime, 0, 0)

#izbriše itemtype
def deleteItemType(ime):
    global itemsIT, itemID, typeOptions, possibleCategories, matrixExamples
    removeInicialisation(ime, -1, -1)
    
    if ime in list(itemsIT.keys()):
        typeOptions.remove(ime)
        itemsIT.pop(ime)
    
    updateMatrix()

#v python slovar vrne subtaskdata
def izpisiSubTaskData():
    global matrixExamples, initialisationExamples
    pySlv = {}
    pyLst = []
    for i in range(len(initialisationExamples)):
        pyLst.append({"tiles":izpisiMatriko(matrixExamples[i]), "initItems":initialisationExamples[i]})

    
    pySlv["easy"] = pyLst
    return pySlv
    
#vrne matriko v obliki stringa
def izpisiMatriko(matrix):
    #matrix = np.array(matrix)
    return "&#&" + str(matrix).replace("],", "], \n") + "&#&"

#doda novo matriko v testne primere
def addMatrix(mmm, nnn):
    global matrixExamples, activeExample
    matrixExamples[activeExample] = [[1 for i in range(mmm)] for j in range(nnn)]

#doda inicializacijo
def addInicialisation(initSlv):
    global initialisationExamples, activeExample
    initialisationExamples[activeExample].append(initSlv)

#odstrani inicializacijo, če sta row in col negativni odstrani vse inicializacije s tem imenom
def removeInicialisation(itemName, itemRow, itemCol):
    global activeExample, initialisationExamples
    zaIzbris = []
    for init in initialisationExamples[activeExample]:
        if init["type"] == itemName and init["row"] == itemRow and init["col"] == itemCol:
            zaIzbris.append(init)
        if init["type"] == itemName and itemRow==-1 and itemCol==-1:
            zaIzbris.append(init)
    for init in zaIzbris:
        initialisationExamples[activeExample].remove(init)

#Doda nov testni primer ali posodobi trenutni izbrain primer
def updateExample(newActiveExample, le, he):
    global initialisationExamples, activeExample, mmm, nnn, itemsIT
    if newActiveExample > len(matrixExamples):
        matrixExamples.append([])
        initialisationExamples.append([])
        for ime in itemsIT.keys():
            itemsIT[ime]["row"].append([])
            itemsIT[ime]["col"].append([])

        activeExample = len(matrixExamples)-1
        itemSpecifications["row"].append([])
        itemSpecifications["col"].append([])
        addMatrix(le, he)
    else:
        activeExample = newActiveExample - 1
        changeMatrixSize(le, he)

#izbriše example
def deleteExample(deleteExampleId):
    global itemsIT, matrixExamples
    if deleteExampleId == 0 and len(matrixExamples)==1:
        return
    for ime in itemsIT.keys():
        itemsIT[ime]["row"].pop(deleteExampleId)
        itemsIT[ime]["col"].pop(deleteExampleId)
    matrixExamples.pop(deleteExampleId)
    initialisationExamples.pop(deleteExampleId)

#Spremeni vrednost matrike-mislm da ne rabm
def changeMatrixValues(row, col, value):
    global matrixExamples, activeExample
    matrixExamples[activeExample][row][col] = value

#spremeni velikost matrike
def changeMatrixSize(le, he):
    global matrixExamples, activeExample
    mat = matrixExamples[activeExample]
    rr = len(mat)
    cc = len(mat[0])
    # upam da se mat obnaša klokr referenca ne kokr solo matrika
    mat = np.array(mat)
    mat2 = np.ones((he, le), dtype=np.int8)
    if (rr > he and cc > le):
        mat = mat[:he, :le]
    elif (rr < he and cc < le):
        mat2[:rr, :cc] = mat
        mat = mat2
    elif (rr > he and cc < le):
        mat2[::, :cc] = mat[:he, ::]
        mat = mat2
    elif (rr < he and cc > le):
        mat2[:rr, ::] = mat[::, :le]
        mat = mat2
    matrixExamples[activeExample] = [[mat[j][i] for i in range(le)] for j in range(he)]
    updateMatrix()

#ustvari skripto, spremeni poslane stringe
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

#ne dela
def saveItemTypes():
    global itemsIT, matrixExamples
    currentState = {"itemsIT":itemsIT, "matrixExamples":"&&&".join(map(str,matrixExamples))}
    jsonStr = json.dumps(currentState, indent = 5, ensure_ascii=False)
    jsonFile = open("savedItemTypes.txt", "w")
    jsonFile.write(jsonStr)
    jsonFile.close()

#ne dela
def getItemTypes():
    global itemsIT, matrixExamples

    jsonFile = open("savedItemTypes.txt", "r")
    jsonStr = jsonFile.read()
    pyVar = json.loads(jsonStr)

    itemsIT = pyVar["itemsIT"]
    matrixExamples = pyVar["matrixExamples"].split("&&&")

#ne dela
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

#ne dela
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

def createItemTypesHtmlString():
    if len(itemsIT.keys()) == 0:
        return "Ni dodanih predmetov"
    else:
        returnHtml = ""
        for ime in itemsIT.keys():
            returnHtml += "<span style='font-size: larger; font-weight: bold;'>" + ime +"</span>" + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
            if "img" in itemsIT[ime].keys():
                img = itemsIT[ime]["img"][0]
                returnHtml += "<b>img" + ": </b>" + img + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
            if "category" in itemsIT[ime].keys():
                returnHtml += "<b>category" + ": </b>" + str(itemsIT[ime]["category"]) + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
            
            returnHtml += "<b>points" + ": </b>["
            print(itemsIT[ime]["row"][activeExample])
            for ind in range(len(itemsIT[ime]["row"][activeExample])):
                returnHtml += "(" + str(itemsIT[ime]["col"][activeExample][ind]) + "," + str(itemsIT[ime]["row"][activeExample][ind]) + "),"+ "&nbsp;"
            returnHtml += "]"
            returnHtml += "<br>"
        return returnHtml

def updateLanguageStringHtml(id):
    html = ""
    for i in range(len(languageStringsKeyWord)):
        if i == id:
            html += "<option selected='selected'>" + languageStringsKeyWord[i] + ": " + languageStringsValues[i] + "</option>"
        else:
            html += "<option>" + languageStringsKeyWord[i] + ": " + languageStringsValues[i] + "</option>"
    return html

def updateItemTypesHtmlString():
    itemTypesNames = list(typeOptions)
    html=""
    for name in itemTypesNames:
        html += "<option>" + str(name) + "</option> <br>"
    return html

def updateCategoryOptionsHtmlString():
    html = ""
    for cat in catIT.keys():
        if cat != "button" and cat != "number":
            html += "<option>" + cat + "</option> <br>"
    return html

def updateButtonHtmlString():
    html = ""
    for item in itemsIT.keys():
        if "button" in item:
            html += "<option>" + item + "</option> <br>"
    return html

def updateExamplesHtmlString():
    html = ""
    for i in range(len(matrixExamples)):
        html += "<option>" + str(i+1) + "</option> <br>"
    return html

def blocksCategoryHtml():
    html = ""
    for block in wholeCategoriesIB.keys():
        if wholeCategoriesIB[block]:
            html += "<option selected='selected'>" + block + "</option> <br>"
        else:
            html += "<option>" + block + "</option> <br>"
    return html

def blocksRobotHtml():
    html = ""
    for block in robotIB.keys():
        if robotIB[block]:
            html += "<option selected='selected'>" + block + "</option> <br>"
        else:
            html += "<option>" + block + "</option> <br>"
    return html

def blocksSingleHtml():
    html = ""
    for block in singleBlocksIB.keys():
        if singleBlocksIB[block]:
            html += "<option selected='selected'>" + block + "</option> <br>"
        else:
            html += "<option>" + block + "</option> <br>"
    return html

#resetira vse globalne variable
def resetVariables():
    global languageStrings, languageStringsKeys, languageStringsKeyWord, languageStringsValues, languageStringsLS, possibleIdicateors, randomBull1, strSE, groupByCategory, includeAllIB, wholeCategoriesIB, robotIB, singleBlocksIB, excludedBlocksIB, possibleCategories, typeOptions, checkEndEveryTurn, ignoreInvalidMoves, endCondition, randomBull2, itemsIT, matrixExamples, initialisationExamples, itemID, catIT, activeExample, itemSpecifications, alreadyInitialized, mmm, nnn, globalka

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
    randomBull1 = {
        "hasGravity": False,
        "introMaxHeight": "33%",
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
    wholeCategoriesIB = {"logic":False, "loops":False, "math":False, "texts":False, "lists":False, "colour":False, "variables":False, "functions":False} # neki za obklukat
    # bloki za robota, na začetku so vsi false, na spletni strani naj bo dropdown za klukat, ko obkljuka spremeni v True
    robotIB = {"move": False, "moveSimple": False, "forward": False, "forwardSimple": False, "turn": False, "turnAround": False, "jump": False, "changeRobot": False, "transport": False, "sensorBool": False, "sensorValue": False, "alterValue": False, "destroy": False, "create": False, "wait": False, "nitems": False, "sensorRowCol": False}
    singleBlocksIB = {"robot_start": False, "math_arithmetic": False, "math_number": False, "math_number": False, "controls_repeat_ext": False, "math_number": False, "math_number": False, "variables_get": False, "controls_whileUntil": False, "math_single": False, "math_number": False, "variables_set": False, "math_number_property": False, "math_number": False, "controls_for": False, "math_number": False, "math_number": False, "math_number": False, "math_round": False, "math_number": False, "math_modulo": False, "math_number": False, "math_number": False, "controls_flow_statements": False, "procedures_defreturn": False, "procedures_defnoreturn": False, "math_change": False, "math_number": False, "procedures_ifreturn": False, "procedures_callnoreturn": False, "procedures_callreturn": False}
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
    endCondition = {"Exist": {"indikator1": None, "ime1": None, "negIndikator1": None, "negIme1": None},
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
    itemSpecifications = {"name":"", "num": 2, "img":"", "zOrder":2, "category":{}, "value":0, "nbStates":8, "row":[[]], "col":[[]]}

    #MREŽA
    #GLOBAL
    activeExample = 0 # če imaš več primerov, Id katerega trenutno editiraš
    mmm = 5
    nnn = 5
    matrixExamples = [[]] #seznam matrik - lahko da je več testov
    initialisationExamples = [[]]
    addMatrix(mmm, nnn)
    globalka = 0

    alreadyInitialized = set()

if __name__ == "__main__":
    resetVariables()
    ustvariSkripto()