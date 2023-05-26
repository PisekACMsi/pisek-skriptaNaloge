import numpy as np
import json
import re
import flatdict

def izpisiLanguageStrings(lst:list):
    slv = {}
    for par in lst:
        slv.update(par)
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
    '''Spreminja hide controls - neuporbno pomoje'''
    pySlv = {"hideControls":{}}
    slv = {"restart": restart, "saveOrLoad": saveOrLoad, "loadBestAnswer": loadBestAnswer, "speedSlider": speedSlider, "backToFirst": backToFirst, "nextStep": nextStep, "goToEnd": goToEnd,}
    pySlv["hideControls"] = slv

    # jsonStr = json.dumps(pySlv, indent = 5)
    # jsString = re.sub("\"([^\"]+)\":", r"\1:", jsonStr).replace(r'\"', "")
    # return jsString[1:-1]
    return pySlv

def izpisiRandomBulshit1(introMaxHeight = "33%", maxListSize = 100, scrollbars = True, controls = True, scale = 1, actionDelay = 400, blocklyColourTheme = "bwinf", maxInstructions = 0):
    '''Pazi max instructions!'''
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
    pySlv["startingExample"]["blockly"] = strSE
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

def izpisiItemTypes():
    global itemsIT
    pySlv = {"itemTypes":{}}
    pySlv["itemTypes"] = itemsIT
    return pySlv

def ustvariItemType(num, img = "", zOrder = 0, nbStates = 1, category = "", value = 0):
    slv = {}
    
    itemSpecifications["category"] = catsTrue
    ime = itemSpecifications.pop("name")
    itemsIT[ime] = itemSpecifications
    typeOptions.append(ime)
    

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



#Globalna spremenljivka LANGUAGE STRINGS - shranjuje vse language stringe
slvLS = {}
#posodobitev slvLS
parLS = {"categories": {"actions": "Gibanje"}} #dobljeni parameter s spletne strani, možne parametre najdeš v templateText.txt
slvLS = dodajSlovar(slvLS, parLS) # za posodobitev kliči to funkcijo in za drugi paramter uporabi kar pride iz spletne strani

# ZAČETNA POSTAVITEV - na spletni strani naj bo gumb - posodobi začetno postavitev. Samo zamenjaj string
strSE = ''


# INCLUDE BLOCKS
groupByCategory = True # neki za obklukat
includeAllIB = False # neki za obklukat
wholeCategories = {"tools":False, "logic":False, "loops":False, "math":False, "texts":False, "lists":False, "colour":False, "variables":False, "functions":False}
# bloki za robota, na začetku so vsi false, na spletni strani naj bo dropdown za klukat, ko obkljuka spremeni v True
robotIB = {"move": False, "moveSimple": False, "forward": False, "forwardSimple": False, "turn": False, "turnAround": False, "jump": False, "changeRobot": False, "transport": False, "sensorBool": False, "sensorValue": False, "alterValue": False, "destroy": False, "create": False, "wait": False, "nitems": False, "sensorRowCol": False}
singleBlocksIB = {}
excludedBlocksIB = {}
# moćžnosti "move", "moveSimple", "forward", "forwardSimple", "turn", "turnAround", "jump", "changeRobot", "transport", "sensorBool", "sensorValue", "alterValue", "destroy", "create", "wait", "nitems", "sensorRowCol"

# END CONDITIONS
possibleIdicateors = {'category', 'value', 'type'}
possibleCategories = {} # updejta se pri ustvarjenju objektov
typeOptions = [] #imena predmetov, ki so na izbiro za inicializacijo objekta, dodajajo se avtomatsko s klicanjem funkcije dodajItemType.
# opcije za indikator = possibleIdicateors
# odvisno od izbranega indikatorja so odvisna tudi imena
# če je indikator category = opcije za ime = possibleCategories
# če je indikator value = opcije za ime = kerakol številka. Mejbi bo treba dtr omejitev
# če je indikator type = opcije za ime = typeOptions
# jebeš keys, nerabš
# ubistvu lahko karkol napišeš notr, prazne opcije bo pohendlala funkcija
endCondition = {"Exist": {"indikator1": "category", "ime1": "coin", "negIndikator1": "", "negIme1": ""},
                "Coincide": {"indikatorA": "", "imeA": "", "indikatorB": "", "imeB": "", "keys": "", "negIndikatorA": "", "negImeA": "", "negIndikatorB": "", "negImeB": ""}}


#OBJEKTI
itemsIT = {} #shranjuje vse iteme
itemID = 2 #se poveča samodejno, odvisen od števila itemov
catIT = {'junak': False, 'ovira': False, 'paket': False, 'gumb': False, 'kovanec': False, 'številka': False} #za obklukat

# imgIT = ["pisek.png"]
# zOrderIT #naj bo odvisen od vrstnega reda stvaritve objektov, seprav isti kokritemID
# nbStatesIT = 8 odvisen le od robota

itemSpecifications = {"name":"objekt_{}".format(itemID-2), "num": itemID, "img":"", "zOrder":itemID, "category":catIT, "value":0}
dodajItemType(itemSpecifications) #kliče naj se z gumbom ustvari

#MREŽA
#GLOBAL
aktivenPrimer = 0
mmm = 5
nnn = 5
matrixExamples = [[]] #seznam matrik - lahko da je več testov
initialisationExamples = [[]]
ityp = 0 # izberi iz typeOptions
inicialisationOptions = {"row":0, "col":0, "type":typeOptions[ityp], "dir": 0, "value": 0}
addMatrix(mmm, nnn) #dodaj test, naj se izvede ob zagonu
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
    fajl = open("theTest.txt", "w", encoding = "utf-8")
    fajl.write(theString)
    fajl.close()

ustvariSkripto()
