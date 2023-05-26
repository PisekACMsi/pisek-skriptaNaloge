import numpy as np
import json
import re
import flatdict

def izpisiLanguageStrings():
    global slvLS
    pySlv = {"languageStrings":{"sl":{}}}
    pySlv["languageStrings"]["sl"] = slvLS
    
    # jsonStr = json.dumps(pySlv, indent = 5, ensure_ascii=False)
    # jsString = re.sub("\"([^\"]+)\":", r"\1:", jsonStr).replace(r'\"', "")
    # return jsString[1:-1]
    return pySlv

def dodajSlovar(slv1, slv2):
    f1 = flatdict.FlatDict(slv1)
    f2 = flatdict.FlatDict(slv2)

    f1[f2.keys()[0]] = f2.values()[0]
    return f1.as_dict()

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

def izpisiItemTypes():
    global itemsIT
    pySlv = {"itemTypes":{}}
    pySlv["itemTypes"] = itemsIT
    return pySlv

def dodajItemType():
    global itemsIT, itemID, typeOptions, possibleCategories, itemSpecifications
    itemID += 1
    cats = itemSpecifications["category"]
    catsTrue = []
    for cat in cats.keys():
        if cats[cat]:
            catsTrue.append({"\"%s\""%cat:True})
            possibleCategories.add(cat)
    
    itemSpecifications["category"] = catsTrue
    ime = itemSpecifications.pop("name")
    itemsIT[ime] = itemSpecifications
    typeOptions.add(ime)
    itemSpecifications = {"name":"objekt_{}".format(itemID-2), "num": itemID, "img":"", "zOrder":itemID, "category":catIT, "value":0}

def izbrisiItemType(ime):
    global itemsIT, itemID, typeOptions, possibleCategories
    itemID -= 1
    typeOptions.pop(ime)
    itemsIT.pop(ime)

def izpisiSubTaskData():
    global matrixExamples, initialisationExamples
    pyLst = []

    for i in range(len(initialisationExamples)):
        pyLst.append({"tiles":izpisiMatriko(matrixExamples[i]), "initItems":initialisationExamples[i]})

    return pyLst
    
def izpisiMatriko(matrix):
    return "&#&" + np.array_repr(matrix).replace("array(", "").replace(", dtype=int8)", "") + "&#&"


def addMatrix(mmm, nnn):
    global matrixExamples, aktivenPrimer
    matrixExamples[aktivenPrimer] = np.ones((nnn,mmm), dtype = np.int8)

def addInicialisation():
    global initialisationExamples, aktivenPrimer, inicialisationOptions
    initialisationExamples[aktivenPrimer].append(inicialisationOptions)

def addExample():
    global initialisationExamples, aktivenPrimer, mmm, nnn
    aktivenPrimer += 1
    initialisationExamples.append([])
    matrixExamples.append([])
    addMatrix(mmm, nnn)

def changeMatrixValues(row, col, value):
    global matrixExamples, aktivenPrimer
    matrixExamples[aktivenPrimer][row][col] = value

def changeMatrixSize(nrows, ncols):
    global matrixExamples, aktivenPrimer
    mat = matrixExamples[aktivenPrimer]
    rr = len(mat)
    cc = len(mat[0])
    # upam da se mat obnaša klokr referenca ne kokr solo matrika
    mat2 = np.ones((nrows, ncols))
    if (rr > nrows and cc > ncols):
        mat = mat[:nrows, :ncols]
    elif (rr < nrows and cc < ncols):
        mat2[:rr, :cc] = mat
        mat = mat2
    elif (rr > nrows and cc < ncols):
        mat2[::, :cc] = mat[:nrows, ::]
    elif (rr < nrows and cc > ncols):
        mat2[:rr, ::] = mat[::, :ncols]


#TE SPREMENLJIVKE SE SPREMINJAJO DIREKTNO S SPLETNE STRANI   KUL?
#Globalna spremenljivka LANGUAGE STRINGS - shranjuje vse language stringe
slvLS = {}
#primer parametra
parLS = {"categories": {"actions": "Gibanje"}} #dobljeni parameter s spletne strani, možne parametre najdeš v templateText.txt - to naj bo dropdown z opcijami za obklukat

slvLS = dodajSlovar(slvLS, parLS) # za posodobitev kliči to funkcijo in za drugi paramter uporabi kar pride iz spletne strani

# ZAČETNA POSTAVITEV - na spletni strani naj bo gumb - posodobi začetno postavitev. Samo zamenjaj string
strSE = ''

# INCLUDE BLOCKS
groupByCategory = True # neki za obklukat
includeAllIB = False # neki za obklukat
wholeCategories = {"tools":False, "logic":False, "loops":False, "math":False, "texts":False, "lists":False, "colour":False, "variables":False, "functions":False} # neki za obklukat
# bloki za robota, na začetku so vsi false, na spletni strani naj bo dropdown za klukat, ko obkljuka spremeni v True
robotIB = {"move": False, "moveSimple": False, "forward": False, "forwardSimple": False, "turn": False, "turnAround": False, "jump": False, "changeRobot": False, "transport": False, "sensorBool": False, "sensorValue": False, "alterValue": False, "destroy": False, "create": False, "wait": False, "nitems": False, "sensorRowCol": False}
singleBlocksIB = {}
excludedBlocksIB = {}
# moćžnosti "move", "moveSimple", "forward", "forwardSimple", "turn", "turnAround", "jump", "changeRobot", "transport", "sensorBool", "sensorValue", "alterValue", "destroy", "create", "wait", "nitems", "sensorRowCol"

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
# to je default, vpisuj notr kar najdeš v zgornjih opcijah
endCondition = {"Exist": {"indikator1": "category", "ime1": "coin", "negIndikator1": "", "negIme1": ""},
                "Coincide": {"indikatorA": "", "imeA": "", "indikatorB": "", "imeB": "", "keys": "", "negIndikatorA": "", "negImeA": "", "negIndikatorB": "", "negImeB": ""}}


#OBJEKTI
itemsIT = {} # samodejno shranjuje vse iteme
itemID = 2 #se poveča samodejno, odvisen od števila itemov
# ko uporabnik želi ustvariti nov objekt naj ima možnosti ime, slika, kategorija, vrednost - izbira naj se vpiše v itemSpecifications
# poleg možnosti naj bosta zraven še gumba ustvari in izbriši ki kličeta funkciji dodajItemType

catIT = {'junak': False, 'ovira': False, 'paket': False, 'gumb': False, 'kovanec': False, 'številka': False} #za obklukat - možnosti kategorij

# imgIT = ["pisek.png"]
# zOrderIT #naj bo odvisen od vrstnega reda stvaritve objektov, seprav isti kokritemID
# nbStatesIT = 8 odvisen le od robota

#globalna spremenljivka trenutnih nastavitev za nov item, po ustvarjenju itema se resetira na default vrednosti
itemSpecifications = {"name":"objekt_{}".format(itemID-2), "num": itemID, "img":"", "zOrder":itemID, "category":catIT, "value":0}
dodajItemType() #kliče naj se z gumbom ustvari

#MREŽA
#GLOBAL
aktivenPrimer = 0 # če imaš več primerov, Id katerega trenutno editiraš
mmm = 5
nnn = 5
matrixExamples = [[]] #seznam matrik - lahko da je več testov
initialisationExamples = [[]]
# type nujno!!! izberi it typeOptions
inicialisationOptions = {"row":0, "col":0, "type":list(typeOptions)[0], "dir": 0, "value": 0}
addMatrix(mmm, nnn) #dodaj test. Naj se izvede ob zagonu

addInicialisation() # kliči da dodaš ityem v initialisationExamples
addExample() #kliči če želiš dodati dodaten primer

def ustvariSkripto():
    ulmSlv = {}
    ulmSlv.update(izpisiLanguageStrings())
    ulmSlv.update(izpisiHideControls())
    ulmSlv.update(izpisiRandomBulshit1())
    ulmSlv.update(izpisiIncludeBlocks())
    ulmSlv.update(izpisiStartingExample())
    ulmSlv.update(izpisiCheckEndCondition())
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

ustvariSkripto()
