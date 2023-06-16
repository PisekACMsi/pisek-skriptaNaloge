import bottle 
import generator
import skripta
import json
import flatdict
import urllib.parse
test = 0
"""Bottle poskrbi, da stran laufa in da so vse stvari povezane med sabo."""

#css 
@bottle.route('/static/css/<filename:re:.*\.css>')
def send_css(filename):
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
    print("POSODOBIL HTML BI PU PIP")
    tile_names = skripta.preberi_vsa_imena_slik("tiles") 
    character_names = skripta.preberi_vsa_imena_slik("characters")
    objects = skripta.preberi_vsa_imena_slik("objects")
    itemTypes = generator.itemsIT
    
    languageStringsKeys = generator.languageStringsKeyWord
    languageStringsValues = generator.languageStringsValues
    
    scene = generator.createItemTypesHtmlString()

    htmlListTypes = generator.updateItemTypesHtmlString()

    customItemCategories = generator.updateCategoryOptionsHtmlString()

    buttonNames = generator.updateButtonHtmlString()
    return bottle.template("index.html", tile_names=tile_names, character_names=character_names, objects=objects, itemTypes=itemTypes, languageStrings = [languageStringsKeys, languageStringsValues], scene=scene, htmlListTypes=htmlListTypes, customItemCategories=customItemCategories, buttonNames=buttonNames)

@bottle.post("/") 
def home_add():
    print("USTVARJAM SKRIPTO")
    # Za funkcijo includeBlocks()
    #-------------------------------------------------------------------
    htmlFajl = open("./views/nalogaTemplate.txt", "r", encoding="utf-8")
    htmlString = htmlFajl.read()
    htmlFajl.close()

    titleHtml = bottle.request.forms.getunicode('exerciseTitle')
    text1Html = bottle.request.forms.getunicode('exerciseText')
    text2Html = bottle.request.forms.getunicode('exerciseText2')

    htmlString = htmlString.replace("$#$Naslov$#$", titleHtml).replace("$#$Text1$#$", text1Html).replace("$#$Text2$#$", text2Html)
    htmlFajlOut = open("./views/naloga.html", "w", encoding = "utf-8")
    htmlFajlOut.write(htmlString)
    htmlFajlOut.close()


    bd = bottle.request.forms.getall('blocksDropdown')
    rbd = bottle.request.forms.getall('robotBlocksDropdown')
    rsbd = bottle.request.forms.getall('robotSingleBlocksDropdown')
    gbc = bottle.request.forms.getall('groupByCategory')

    # Preverimo ali želimo grupirat po kategorijah
    if len(gbc) > 0:
        generator.groupByCategory = True
    else:
        generator.groupByCategory = False

    # Nastavimo vse vrednosti, ki obstajajo v IB in Categories na true
    for el in rbd:
        if el != "Izberi vse":
            el= el[0].lower() + el[1:]
            generator.robotIB[el] = True

    for el in rsbd:
        if el != "Izberi vse":
            el= el[0].lower() + el[1:]
            generator.singleBlocksIB[el] = True

    for el in bd:
        if el != "Izberi vse":
            el= el[0].lower() + el[1:]
            generator.wholeCategoriesIB[el] = True

    #OZADJE
    backGroundColor = bottle.request.forms.get('backGroundSelector')
    borderColor = bottle.request.forms.get('borderSelector')
    borderWidth = bottle.request.forms.get('borderWidth')
    backgroundImage = bottle.request.forms.get('backgroundImage')
    showLabels = bottle.request.forms.get('showLabels')
    sizeRows = bottle.request.forms.get('sizeRow')
    sizeCols = bottle.request.forms.get('sizeCol')
    generator.randomBull2["backgroundColour"] = backGroundColor
    generator.randomBull2["borderColour"] = borderColor
    generator.randomBull2["border"] = float(borderWidth)
    generator.randomBull2["backgroundTile"] = backgroundImage + ".png"
    generator.mmm = int(sizeRows)
    generator.nnn= int(sizeCols)
    
    if showLabels == "on":
        showLabels = True
    else:
        showLabels = False
    generator.randomBull2["showLabels"] = showLabels

    #END CONDITION
    indikator1 = bottle.request.forms.get("indikator1") 
    ime1 = bottle.request.forms.get("ime1") 
    indikatorA = bottle.request.forms.get("indikatorA") 
    indikatorB = bottle.request.forms.get("indikatorB") 
    imeA = bottle.request.forms.get("imeA")
    imeB = bottle.request.forms.get("imeB")
    generator.endCondition["Exist"]["indikator1"] = indikator1
    generator.endCondition["Exist"]["ime1"] = ime1
    generator.endCondition["Coincide"]["indikatorA"] = indikatorA
    generator.endCondition["Coincide"]["indikatorB"] = indikatorB
    generator.endCondition["Coincide"]["imeA"] = imeA
    generator.endCondition["Coincide"]["imeB"] = imeB

    generator.globalka += 1
    # Za funkcijo IzpisiHideControls(). Jo bom pustil kar prazno. 
    #--------------------------------------------------------------------

    # Za randomBull1 bom spremnil samo maxInstructions.
    # -------------------------------------------------------------------
    maxIns = int(bottle.request.forms.get('maxInstructions')) 
    generator.randomBull1['maxInstructions'] = maxIns


    # Ustvarimo skripto
    generator.ustvariSkripto()
    bottle.redirect("/")

@bottle.post("/customObject") 
def dodajItem():
    #ITEMTYPE
    print("DODAL ITEM TYPE, DELAM KOT ZAMORC")
    itemName = bottle.request.forms.get("itemName")
    itemCategorys = json.loads(bottle.request.forms.get("itemCategory"))
    itemImages = json.loads(bottle.request.forms.get("itemImage"))
    itemValue = bottle.request.forms.get("itemValue")
    zOrder = bottle.request.forms.get("itemZOrder")
    buttonId = int(bottle.request.forms.get("buttonId"))
    itemColors = json.loads(bottle.request.forms.get("itemColor"))
    generator.itemSpecifications["name"] = itemName
    generator.itemSpecifications["img"] = itemImages
    generator.itemSpecifications["value"] = itemValue
    generator.itemSpecifications["zOrder"] = zOrder
    generator.itemSpecifications["color"] = itemColors
    generator.itemSpecifications["id"] = buttonId
    
    for cat in itemCategorys:
        generator.catIT[cat] = True
    
    generator.dodajItemType() #kliče naj se z gumbom ustvari
    generator.ustvariSkripto()
    bottle.redirect("/")

@bottle.post("/defaultItem")
def addDefaultItems():
    itemCategory = bottle.request.forms.get("defaultItemCategory")
    itemImage= bottle.request.forms.get("defaultItemImage")
    generator.createDefaultItem(itemCategory, itemImage)
    generator.ustvariSkripto()
    print("Dodal default: ", itemCategory)
    bottle.redirect("/")

@bottle.post("/defaultNumber")
def addDefaultNumber():
    itemNum= bottle.request.forms.get("defaultItemNumber")
    generator.createDefaultNumber(itemNum)
    generator.ustvariSkripto()
    bottle.redirect("/")

@bottle.post("/defaultColor")
def addDefaultColor():
    itemCol= bottle.request.forms.get("defaultItemColor")
    generator.createDefaultColor(itemCol)
    generator.ustvariSkripto()
    bottle.redirect("/")

@bottle.post("/defaultButton")
def addDefaultButton():
    buttonOn = bottle.request.forms.get("defaultButtonImageOn")
    buttonOff = bottle.request.forms.get("defaultButtonImageOff")
    generator.createDefaultButton(buttonOn, buttonOff)
    generator.ustvariSkripto()
    bottle.redirect("/")

@bottle.post("/addToMatrix")
def addToMatrix():
    print("DODAJAM NA MATRIKO AAAAAAAAAAAAAAAA")
    itemName = bottle.request.forms.get("itemName")
    itemRow = int(bottle.request.forms.get("itemRow") )
    itemCol = int(bottle.request.forms.get("itemCol"))
    generator.addItemTypeToMatrix(itemName, itemRow, itemCol)
    generator.ustvariSkripto()
    bottle.redirect("/")

@bottle.post("/removeFromMatrix")
def addToMatrix():
    print("DODAJAM NA MATRIKO AAAAAAAAAAAAAAAA")
    itemName = bottle.request.forms.get("itemName")
    itemRow = int(bottle.request.forms.get("itemRow") )
    itemCol = int(bottle.request.forms.get("itemCol"))
    generator.removeItemTypeFromMatrix(itemName, itemRow, itemCol)
    generator.ustvariSkripto()
    bottle.redirect("/")

@bottle.post("/addRobot") 
def dodajItem():
    #ITEMTYPE
    itemRow = bottle.request.forms.get("coordRowR") 
    itemCol = bottle.request.forms.get("coordColR")
    itemCategory = "robot"
    itemImage = bottle.request.forms.get("itemImageR")
    generator.itemSpecifications["name"] = "robot0"
    generator.itemSpecifications["img"] = itemImage.replace(" ", "_") + ".png"
    generator.catIT[itemCategory] = True
    generator.itemSpecifications["row"] = [int(itemRow.split(",")[0])]
    generator.itemSpecifications["col"] = [int(itemCol.split(",")[0])]
    generator.itemSpecifications["nbStates"] = 9
    generator.addRobot()
    generator.ustvariSkripto()
    print("DODAJAM ROBOTA SERVER BRRRRRRR")
    bottle.redirect("/")

@bottle.post("/createNewCategory")
def createNewCategory():
    print("CREATE NEW CATEGORY")
    category = bottle.request.forms.get("category")
    generator.catIT[category] = False
    return generator.updateCategoryOptionsHtmlString()

@bottle.post("/removeItem") 
def deleteItem():
    print("BRIŠEM ITEM GRRRRRRR")
    deleteItem = bottle.request.forms.get("delName")
    generator.deleteItemType(deleteItem)
    print("IZBRISAL ITEM TYPE")
    generator.ustvariSkripto()
    bottle.redirect("/")

@bottle.post("/ls") 
def deleteLanguage():
    print("BRIŠEM LANGUAGE DONDE ESTA BLIBLIOTEKA")
    lsId = int(bottle.request.forms.get("idLS"))
    ls = bottle.request.forms.get("textLS")
    generator.dodajSlovar(lsId, ls)
    print("POSODOBIL LANGUAGE STRINGS")
    generator.ustvariSkripto()

    languageStringsKeys = generator.languageStringsKeyWord
    languageStringsValues = generator.languageStringsValues

    htmlStr = ""
    for i in range(len(languageStringsKeys)):
        htmlStr += "<option>{}. {} : {}</option> <br>".format(i, languageStringsKeys[i], languageStringsValues[i])
    return htmlStr

@bottle.get("/updateItemTypes") 
def update_item_types():
    return generator.createItemTypesHtmlString()

@bottle.post("/updateItemTypeOptions") 
def update_item_types():
    return generator.updateItemTypesHtmlString()

@bottle.get("/updateButtons") 
def update_item_types():
    print("GUMBI: ", generator.updateButtonHtmlString())
    return generator.updateButtonHtmlString()

@bottle.post("/resetFile")
def update_item_types():
    print("RESETIRAM WOOOOOOOOOOOOOOOOOOO")
    generator.resetVariables()
    generator.ustvariSkripto()
    return home_get()

#----------------------------------------------------------------------------------------------------------

def start_bottle():
    print("ZAGANJAM BOTTLE")
    generator.resetVariables()
    generator.ustvariSkripto()
    #Zaženemo bottle
    bottle.run(host='localhost', port=8081, debug=True)