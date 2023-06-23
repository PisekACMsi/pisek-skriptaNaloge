import sys
sys.path.insert(1, 'generator/')
from naloga import *
import bottle 
import generatorStari
import skripta
import json
import flatdict
import urllib.parse
import os


# caution: path[0] is reserved for script path (or '' in REPL)


test = 0
"""Bottle poskrbi, da stran laufa in da so vse stvari povezane med sabo."""

#css 
@bottle.route('/static/css/<filename:re:.*\.css>')
def send_css(filename):
    return bottle.static_file(filename, root='static/css')

@bottle.route('/static/javascript/pemFioi/<filename:re:.*\.css>')
def send_css2(filename):
    return bottle.static_file(filename, root='static/css')

#img
@bottle.route('/static/img/<filename:re:.*\.png>')
def send_img(filename):
    return bottle.static_file(filename, root='static/img')

#img 
@bottle.route('/static/javascript/modules/img/algorea<filename:re:.*\.png>')
def send_img2(filename):
    return bottle.static_file(filename, root='static/javascript/modules/img/algorea')

#html
@bottle.route('/views/<filename:re:.*\.html>')
def serve_html(filename):
    return bottle.static_file(filename, root='views')

#javascript
@bottle.route('/static/javascript/<filename:re:.*\.js>')
def send_javascript(filename):
    return bottle.static_file(filename, root='static/javascript')

#javascript robotlib
@bottle.route('/naloga/<filename:re:.*\.js>')
def send_file_js(filename):
    return bottle.static_file(filename, root='naloga')

#knjižnica v modules 
#raphaelFactory-1.0
#delayFactory-1.0
#simulationFactory-1.0
#beav-1.0
#beaver-task-2.0 
@bottle.route('../static/javascript/_common/<filename:re:.*\.js>')
def send_lib_js(filename):
    return bottle.static_file(filename, root='../../Pisek/pisek-git/_common/modules/pemFioi')

# jquery-1.7.1 
@bottle.route('../static/javascript/_common/modules/ext/jquery/<filename:re:.*\.js>')
def send_jquery(filename):
    return bottle.static_file(filename, root='../../Pisek/pisek-git/_common/modules/ext/jquery')

#JSON-js 
@bottle.route('../static/javascript/_common/modules/ext/json/<filename:re:.*\.js>')
def send_json(filename):
    return bottle.static_file(filename, root='../../Pisek/pisek-git/_common/modules/ext/json')

#raphael-2.2.1 
@bottle.route('../static/javascript/_common/modules/ext/raphael/2.2.1/<filename:re:.*\.js>')
def send_raphael(filename):
    return bottle.static_file(filename, root='../../Pisek/pisek-git/_common/modules/ext/raphael/2.2.1')

#jschannel 
@bottle.route('../static/javascript/_common/modules/ext/jschannel/<filename:re:.*\.js>')
def send_jschannel(filename):
    return bottle.static_file(filename, root='../../Pisek/pisek-git/_common/modules/ext/jschannel')

#platform-pr 
@bottle.route('../static/javascript/_common/modules/integrationAPI.01/official/<filename:re:.*\.js>')
def send_platformpr(filename):
    return bottle.static_file(filename, root='../../Pisek/pisek-git/_common/modules/integrationAPI.01/official')

#buttonsAndMessages 
@bottle.route('../static/javascript/_common/modules/integrationAPI.01/installationAPI.01/pemFioi/<filename:re:.*\.js>')
def send_buttonsAndMessages(filename):
    return bottle.static_file(filename, root='../../Pisek/pisek-git/_common/modules/integrationAPI.01/installationAPI.01/pemFioi')

#installationAPI.01
@bottle.route('../static/javascript/_common/modules/integrationAPI.01/installationAPI.01/pemFioi/<filename:re:.*\.js>')
def send_installationAPI(filename):
    return bottle.static_file(filename, root='../../Pisek/pisek-git/_common/modules/integrationAPI.01/installationAPI.01/pemFioi')

#miniPlatform
@bottle.route('../static/javascript/_common/modules/integrationAPI.01/official/<filename:re:.*\.js>')
def send_miniPlatform(filename):
    return bottle.static_file(filename, root='../../Pisek/pisek-git/_common/modules/integrationAPI.01/official')

#-----------------------------------------------------------------------------------------------
#Blockly knjižnica
#-----------------------------------------------------------------------------------------------

#acorn
@bottle.route('../static/javascript/_common/modules/ext/js-interpreter/<filename:re:.*\.js>')
def send_acorn(filename):
    return bottle.static_file(filename, root='../../Pisek/pisek-git/_common/modules/ext/js-interpreter')

#acorn-walk
@bottle.route('../static/javascript/_common/modules/ext/acorn/<filename:re:.*\.js>')
def send_acornWalk(filename):
    return bottle.static_file(filename, root='../../Pisek/pisek-git/_common/modules/ext/acorn')

#interpreter
@bottle.route('../static/javascript/_common/modules/ext/js-interpreter/<filename:re:.*\.js>')
def send_interpreter(filename):
    return bottle.static_file(filename, root='../../Pisek/pisek-git/_common/modules/ext/js-interpreter/')

#blockly
#blockly_blocks
#blockly_javascript
#blockly_python
#blockly_ + strLang (blockly_sl)
@bottle.route('../static/javascript/_common/modules/ext/blockly/<filename:re:.*\.js>')
def send_blockly(filename):
    return bottle.static_file(filename, root='../../Pisek/pisek-git/_common/modules/ext/blockly')

#blockly_fioi
@bottle.route('../static/javascript/_common/modules/ext/blockly-fioi/<filename:re:.*\.js>')
def send_blockly_fioi(filename):
    return bottle.static_file(filename, root='../../Pisek/pisek-git/_common/modules/ext/blockly-fioi')

#numeric_keypad
@bottle.route('../static/javascript/_common/modules/pemFioi/shared/numeric_keypad/<filename:re:.*\.js>')
def send_numeric_keypad(filename):
    return bottle.static_file(filename, root='../../Pisek/pisek-git/_common/modules/pemFioi/shared/numeric_keypad')

#quickAlgo_i18n
#quickAlgo_interface
#quickAlgo_utils
#quickAlgo_blockly_blocks
#quickAlgo_blockly_interface
#quickAlgo_blockly_runner
#quickAlgo_subtask
#quickAlgo_context
@bottle.route('../static/javascript/_common/modules/pemFioi/quickAlgo/<filename:re:.*\.js>')
def send_quickAlgo(filename):
    return bottle.static_file(filename, root='../../Pisek/pisek-git/_common/modules/pemFioi/quickAlgo')

#quickAlgo_css
@bottle.route('../static/css/modules/<filename:re:.*\.css>')
def send_quickAlgo_css(filename):
    return bottle.static_file(filename, root='../static/css/modules')

#---------------------------------------------------------------------------------------------------------
# Samo spodnjo kodo spreminjaj
#---------------------------------------------------------------------------------------------------------

@bottle.get("/") 
def home_get():
    global test

    tile_names = skripta.preberi_vsa_imena_slik("tiles") 
    character_names = skripta.preberi_vsa_imena_slik("characters")
    objects = skripta.preberi_vsa_imena_slik("objects")
    
    languageStrings = generator2.languageStrings.languageStringsHtml(0)

    scene = generator2.itemTypes.createItemTypesHtmlString()

    htmlListTypes = generator2.itemTypes.updateItemTypesHtmlString()

    customItemCategories = generator2.itemTypes.updateCategoryOptionsHtmlString()

    buttonNames = generator2.itemTypes.updateButtonHtmlString()

    numOfExamples = len(generator2.subTaskData.examples)

    blocksCategory = generator2.includeBlocks.blocksCategoryHtml()
    blocksRobot = generator2.includeBlocks.blocksRobotHtml()
    blocksSingle = generator2.includeBlocks.blocksSingleHtml()
    
    return bottle.template("index.html", tile_names=tile_names, character_names=character_names, objects=objects, languageStrings = languageStrings, scene=scene, htmlListTypes=htmlListTypes, customItemCategories=customItemCategories, buttonNames=buttonNames, numOfExamples=numOfExamples, blocksCategory=blocksCategory, blocksSingle=blocksSingle, blocksRobot=blocksRobot)

@bottle.post("/") 
def home_add():
    #generator.ustvariSkripto()
    bottle.redirect("/")

@bottle.post("/refreshText") 
def updateText():
    htmlFajl = open("./views/nalogaTemplate.txt", "r", encoding="utf-8")
    htmlString = htmlFajl.read()
    htmlFajl.close()

    titleHtml = bottle.request.forms.getunicode('title')
    text1Html = bottle.request.forms.getunicode('text1')
    text2Html = bottle.request.forms.getunicode('text2')

    htmlString = htmlString.replace("$#$Naslov$#$", titleHtml).replace("$#$Text1$#$", text1Html).replace("$#$Text2$#$", text2Html)
    htmlFajlOut = open("./views/naloga.html", "w", encoding = "utf-8")
    htmlFajlOut.write(htmlString)
    htmlFajlOut.close()


@bottle.post("/updateBlocks") 
def updateBlocks():
    categoryBlocks = json.loads(bottle.request.forms.get("categoryBlocks"))
    robotBlocks = json.loads(bottle.request.forms.get("robotBlocks"))
    singleBlocks = json.loads(bottle.request.forms.get("singleBlocks"))
    groupByCategory = bottle.request.forms.get("groupByCategory")
    maxInstructions = int(bottle.request.forms.get("maxInstructions"))

    categoryBlocks = [] if categoryBlocks == None else categoryBlocks
    robotBlocks = [] if robotBlocks == None else robotBlocks
    singleBlocks = [] if singleBlocks == None else singleBlocks
    # Preverimo ali želimo grupirat po kategorijah
    for block in categoryBlocks:
        if block != "Izberi vse":
            generator2.includeBlocks.categoryBlocks[block] = True
    for block in robotBlocks:
        if block != "Izberi vse":
            generator2.includeBlocks.robotBlocks[block] = True
    for block in singleBlocks:
        if block != "Izberi vse":
            generator2.includeBlocks.individualBlocks[block] = True

    
    if groupByCategory == "true":
        generator2.includeBlocks.groupByCategory = True
    else:
        generator2.includeBlocks.groupByCategory = False

    # Nastavimo vse vrednosti, ki obstajajo v IB in Categories na true
    generator2.board.maxInstructions = maxInstructions
    generator2.createFile()

@bottle.post("/deleteStartingExample")
def deleteStartingExample():
    generatorStari.strSE = ""
    generatorStari.ustvariSkripto()

@bottle.post("/updateEndConditions")
def updateEndConditions():
    indicate1 = bottle.request.forms.get("indicate1")
    name1 = bottle.request.forms.get("name1")
    indicateA = bottle.request.forms.get("indicateA")
    nameA = bottle.request.forms.get("nameA")
    indicateB = bottle.request.forms.get("indicateB")
    nameB = bottle.request.forms.get("nameB")

    generator2.endCondition.cond["indikator1"] = indicate1
    generator2.endCondition.cond["ime1"] = name1
    generator2.endCondition.cond["indikatorA"] = indicateA
    generator2.endCondition.cond["indikatorB"] = indicateB
    generator2.endCondition.cond["imeA"] = nameA
    generator2.endCondition.cond["imeB"] = nameB
    generator2.endCondition.createConditions()
    generator2.createFile()

@bottle.post("/customObject") 
def dodajItem():
    #ITEMTYPE
    itemName = bottle.request.forms.get("itemName")
    itemCategorys = json.loads(bottle.request.forms.get("itemCategory"))
    itemImages = json.loads(bottle.request.forms.get("itemImage"))
    itemValue = int(bottle.request.forms.get("itemValue"))
    zOrder = int(bottle.request.forms.get("itemZOrder"))
    buttonId = int(bottle.request.forms.get("buttonId"))
    itemColors = json.loads(bottle.request.forms.get("itemColor"))
    generatorStari.itemSpecifications["name"] = itemName
    generatorStari.itemSpecifications["img"] = itemImages
    generatorStari.itemSpecifications["value"] = itemValue
    generatorStari.itemSpecifications["zOrder"] = zOrder
    generatorStari.itemSpecifications["color"] = itemColors
    generatorStari.itemSpecifications["id"] = buttonId + 1
    
    for cat in itemCategorys:
        generatorStari.catIT[cat] = True
    
    generatorStari.dodajItemType() #kliče naj se z gumbom ustvari
    generatorStari.ustvariSkripto()
    bottle.redirect("/")

@bottle.post("/defaultItem")
def addDefaultItems():
    itemCategory = bottle.request.forms.get("defaultItemCategory")
    itemImage= bottle.request.forms.get("defaultItemImage")
    generator2.itemTypes.createDefaultItem([itemCategory], [itemImage])
    generator2.createFile()
    bottle.redirect("/")

@bottle.post("/defaultNumber")
def addDefaultNumber():
    print("BBBBBBBB")
    itemNum= bottle.request.forms.get("defaultItemNumber")
    generator2.itemTypes.createDefaultItem(["number"], itemNum)
    generator2.createFile()
    print(generator2.itemTypes.items.keys())
    bottle.redirect("/")

@bottle.post("/defaultColor")
def addDefaultColor():
    itemCol= bottle.request.forms.get("defaultItemColor")
    generator2.itemTypes.createDefaultItem(["colour"], [itemCol])
    generator2.createFile()
    bottle.redirect("/")

@bottle.post("/defaultButton")
def addDefaultButton():
    buttonOn = bottle.request.forms.get("defaultButtonImageOn")
    buttonOff = bottle.request.forms.get("defaultButtonImageOff")
    generator2.itemTypes.createDefaultItem(["button"], [buttonOn, buttonOff])
    generator2.createFile()
    bottle.redirect("/")

@bottle.post("/updateMatrixParameters")
def addMatrixExample():
    backgroundColor = bottle.request.forms.get("backgroundColor")
    borderColor = bottle.request.forms.get("borderColor")
    borderWidth = float(bottle.request.forms.get("borderWidth"))
    backgroundImage = bottle.request.forms.get("backgroundImage")
    showLabels = bottle.request.forms.get("showLabels")
    gravityOn = bottle.request.forms.get("gravityOn")
    exampleId = int(bottle.request.forms.get("activeExample"))
    matrixLength = int(bottle.request.forms.get("matrixLength"))
    matrixHeight = int(bottle.request.forms.get("matrixHeight"))
    generator2.board.backgColor = backgroundColor
    generator2.board.lineColor = borderColor
    generator2.board.lineWidth = float(borderWidth)
    generator2.board.backgImage = backgroundImage
    showLabels = True if showLabels == "true" else False
    gravityOn = True if gravityOn == "true" else False
    
    generator2.board.showLabels = showLabels
    generator2.board.gravity = gravityOn

    generator2.subTaskData.updateExample(exampleId, matrixLength, matrixHeight)
    generator2.createFile()
    return generator2.subTaskData.updateExamplesHtmlString()

@bottle.post("/deleteMatrixExamples")
def addMatrixExample():
    deleteExample = int(bottle.request.forms.get("deleteExample"))
    generator2.subTaskData.removeExample(deleteExample-1)
    generator2.createFile()
    return generator2.subTaskData.updateExamplesHtmlString()


@bottle.post("/addToMatrix")
def addToMatrix():
    itemName = bottle.request.forms.get("itemName")
    itemRow = int(bottle.request.forms.get("itemRow"))
    itemCol = int(bottle.request.forms.get("itemCol"))
    newActiveExample = 1 #int(bottle.request.forms.get("activeExample"))
    itemNumber = generator2.itemTypes.items[itemName].num
    generator2.subTaskData.examples[newActiveExample-1].addToMatrix(itemNumber, itemName, itemRow, itemCol)
    generator2.createFile()
    bottle.redirect("/")

@bottle.post("/removeFromMatrix")
def removeFromMatrix():
    itemName = bottle.request.forms.get("itemName")
    itemRow = int(bottle.request.forms.get("itemRow") )
    itemCol = int(bottle.request.forms.get("itemCol"))
    newActiveExample = int(bottle.request.forms.get("activeExample"))
    
    itemNumber = generator2.itemTypes.items[itemName].num
    generator2.subTaskData.examples[newActiveExample-1].removeFromMatrix(itemNumber, itemName, itemRow, itemCol)
    generator2.createFile()
    bottle.redirect("/")

@bottle.post("/addRobot") 
def addRobot():
    #ITEMTYPE
    itemImage = bottle.request.forms.get("itemImageR")
    
    generator2.itemTypes.createDefaultItem(["robot"], [itemImage])
    generator2.createFile()
    print("DODAJAM ROBOTA SERVER BRRRRRRR")
    bottle.redirect("/")

@bottle.post("/createNewCategory")
def createNewCategory():
    category = bottle.request.forms.get("category")
    generatorStari.catIT[category] = False
    return generatorStari.updateCategoryOptionsHtmlString()

@bottle.post("/removeItem") 
def deleteItem():
    deleteItem = bottle.request.forms.get("delName")

    itemNumber = generator2.itemTypes.items[deleteItem].num
    generator2.itemTypes.removeItem(deleteItem)
    generator2.subTaskData.removeItemType(deleteItem, itemNumber)
    print("IZBRISAL ITEM TYPE", deleteItem)
    generator2.createFile()
    bottle.redirect("/")

@bottle.post("/languageStrings")
def deleteLanguage():
    lsId = int(bottle.request.forms.get("idLS"))
    ls = bottle.request.forms.getunicode("textLS")
    generator2.languageStrings.addFlatDictCategories(lsId, ls)
    print("POSODOBIL LANGUAGE STRINGS")
    generator2.createFile()

    return generator2.languageStrings.languageStringsHtml(lsId)

@bottle.get("/updateItemTypes") 
def update_item_types():
    return generator2.itemTypes.createItemTypesHtmlString()

@bottle.post("/updateItemTypeOptions") 
def update_item_types():
    return generator2.itemTypes.updateItemTypesHtmlString()

@bottle.get("/updateButtons") 
def update_item_types():
    return generator2.itemTypes.updateButtonHtmlString()

@bottle.post("/resetFile")
def update_item_types():
    generator2 = Naloga()
    generator2.createFile()
    return home_get()

@bottle.post("/uploadImage")
def update_item_types():
    image = bottle.request.files.get('imageFile')
    path = bottle.request.forms.get('path')

    filePath = "static/img/" + path + "/" + image.filename
    if not os.path.exists(filePath):
        image.save(filePath)
        return 'Image uploaded successfully.'
    else:
        return 'Image upload failed.'
    
@bottle.post("/uploadStartingExample")
def update_item_types():
    uploaded_file = bottle.request.files.get('imageFile')
    if uploaded_file:
        file_content = uploaded_file.file.read()
        generator2.board.updateStartingExample(file_content.decode().replace("\"", "'"))
    generator2.createFile()

#----------------------------------------------------------------------------------------------------------

def start_bottle():
    global generator2
    generator2 = Naloga()
    generator2.createFile()
    bottle.run(host='localhost', port=8081, debug=True)