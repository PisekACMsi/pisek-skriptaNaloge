from bottle import Bottle, run, template, static_file
import generator

# app je zdj Bottle
app = Bottle()

"""Bottle poskrbi, da stran laufa in da so vse stvari povezane med sabo."""

#css 
@app.route('/static/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='static/css')

#img
@app.route('/static/img/<filename:re:.*\.png>')
def send_img(filename):
    return static_file(filename, root='static/img')

#img 
@app.route('/static/javascript/modules/img/algorea<filename:re:.*\.png>')
def send_img2(filename):
    return static_file(filename, root='static/javascript/modules/img/algorea')

#html
@app.route('/views/<filename:re:.*\.html>')
def serve_html(filename):
    return static_file(filename, root='views')

#javascript
@app.route('/static/javascript/<filename:re:.*\.js>')
def send_javascript(filename):
    return static_file(filename, root='static/javascript')

#javascript robotlib
@app.route('/naloga/<filename:re:.*\.js>')
def send_file_js(filename):
    return static_file(filename, root='naloga')

#knjižnica v modules 
#raphaelFactory-1.0
#delayFactory-1.0
#simulationFactory-1.0
#beav-1.0
#beaver-task-2.0 
@app.route('../static/javascript/_common/<filename:re:.*\.js>')
def send_lib_js(filename):
    return static_file(filename, root='../../Pisek/pisek-git/_common/modules/pemFioi')

# jquery-1.7.1 
@app.route('../static/javascript/_common/modules/ext/jquery/<filename:re:.*\.js>')
def send_jquery(filename):
    return static_file(filename, root='../../Pisek/pisek-git/_common/modules/ext/jquery')

#JSON-js 
@app.route('../static/javascript/_common/modules/ext/json/<filename:re:.*\.js>')
def send_json(filename):
    return static_file(filename, root='../../Pisek/pisek-git/_common/modules/ext/json')

#raphael-2.2.1 
@app.route('../static/javascript/_common/modules/ext/raphael/2.2.1/<filename:re:.*\.js>')
def send_raphael(filename):
    return static_file(filename, root='../../Pisek/pisek-git/_common/modules/ext/raphael/2.2.1')

#jschannel 
@app.route('../static/javascript/_common/modules/ext/jschannel/<filename:re:.*\.js>')
def send_jschannel(filename):
    return static_file(filename, root='../../Pisek/pisek-git/_common/modules/ext/jschannel')

#platform-pr 
@app.route('../static/javascript/_common/modules/integrationAPI.01/official/<filename:re:.*\.js>')
def send_platformpr(filename):
    return static_file(filename, root='../../Pisek/pisek-git/_common/modules/integrationAPI.01/official')

#buttonsAndMessages 
@app.route('../static/javascript/_common/modules/integrationAPI.01/installationAPI.01/pemFioi/<filename:re:.*\.js>')
def send_buttonsAndMessages(filename):
    return static_file(filename, root='../../Pisek/pisek-git/_common/modules/integrationAPI.01/installationAPI.01/pemFioi')

#installationAPI.01
@app.route('../static/javascript/_common/modules/integrationAPI.01/installationAPI.01/pemFioi/<filename:re:.*\.js>')
def send_installationAPI(filename):
    return static_file(filename, root='../../Pisek/pisek-git/_common/modules/integrationAPI.01/installationAPI.01/pemFioi')

#miniPlatform
@app.route('../static/javascript/_common/modules/integrationAPI.01/official/<filename:re:.*\.js>')
def send_miniPlatform(filename):
    return static_file(filename, root='../../Pisek/pisek-git/_common/modules/integrationAPI.01/official')

#-----------------------------------------------------------------------------------------------
#Blockly knjižnica
#-----------------------------------------------------------------------------------------------

#acorn
@app.route('../static/javascript/_common/modules/ext/js-interpreter/<filename:re:.*\.js>')
def send_acorn(filename):
    return static_file(filename, root='../../Pisek/pisek-git/_common/modules/ext/js-interpreter')

#acorn-walk
@app.route('../static/javascript/_common/modules/ext/acorn/<filename:re:.*\.js>')
def send_acornWalk(filename):
    return static_file(filename, root='../../Pisek/pisek-git/_common/modules/ext/acorn')

#interpreter
@app.route('../static/javascript/_common/modules/ext/js-interpreter/<filename:re:.*\.js>')
def send_interpreter(filename):
    return static_file(filename, root='../../Pisek/pisek-git/_common/modules/ext/js-interpreter/')

#blockly
#blockly_blocks
#blockly_javascript
#blockly_python
#blockly_ + strLang (blockly_sl)
@app.route('../static/javascript/_common/modules/ext/blockly/<filename:re:.*\.js>')
def send_blockly(filename):
    return static_file(filename, root='../../Pisek/pisek-git/_common/modules/ext/blockly')

#blockly_fioi
@app.route('../static/javascript/_common/modules/ext/blockly-fioi/<filename:re:.*\.js>')
def send_blockly_fioi(filename):
    return static_file(filename, root='../../Pisek/pisek-git/_common/modules/ext/blockly-fioi')

#numeric_keypad
@app.route('../static/javascript/_common/modules/pemFioi/shared/numeric_keypad/<filename:re:.*\.js>')
def send_numeric_keypad(filename):
    return static_file(filename, root='../../Pisek/pisek-git/_common/modules/pemFioi/shared/numeric_keypad')

#quickAlgo_i18n
#quickAlgo_interface
#quickAlgo_utils
#quickAlgo_blockly_blocks
#quickAlgo_blockly_interface
#quickAlgo_blockly_runner
#quickAlgo_subtask
#quickAlgo_context
@app.route('../static/javascript/_common/modules/pemFioi/quickAlgo/<filename:re:.*\.js>')
def send_quickAlgo(filename):
    return static_file(filename, root='../../Pisek/pisek-git/_common/modules/pemFioi/quickAlgo')

#quickAlgo_css
@app.route('../static/css/modules/<filename:re:.*\.css>')
def send_quickAlgo_css(filename):
    return static_file(filename, root='../static/css/modules')

#---------------------------------------------------------------------------------------------------------
# Samo spodnjo kodo spreminjaj
#---------------------------------------------------------------------------------------------------------

@app.get("/")    
def home_get():              
    return template("index.html")

@app.post("/")
def home_add():

    # Za funkcijo includeBlocks()
    #-------------------------------------------------------------------

    bd = bottle.request.forms.getall('blocksDropdown')
    rbd = bottle.request.forms.getall('robotBlocksDropdown')
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

    for el in bd:
        if el != "Izberi vse":
            el= el[0].lower() + el[1:]
            generator.wholeCategories[el] = True

    #OZADJE
    backGroundColor = bottle.request.forms.get('backGroundSelector')
    borderColor = bottle.request.forms.get('borderSelector')
    borderWidth = bottle.request.forms.get('borderWidth')
    backgroundImage = bottle.request.forms.get('backgroundImage')
    showLabels = bottle.request.forms.get('showLabels')
    generator.randomBull2["backgroundColour"] = backGroundColor
    generator.randomBull2["borderColour"] = borderColor
    generator.randomBull2["border"] = float(borderWidth)
    generator.randomBull2["backgroundTile"] = backgroundImage + ".png"
    
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



    
    # Za funkcijo IzpisiHideControls(). Jo bom pustil kar prazno. 
    #--------------------------------------------------------------------

    # Za randomBull1 bom spremnil samo maxInstructions.
    # -------------------------------------------------------------------
    maxIns = int(app.request.forms.get('maxInstructions')) 
    generator.randomBull1['maxInstructions'] = maxIns


    # Ustvarimo skripto
    generator.ustvariSkripto()
    app.redirect("/")


#----------------------------------------------------------------------------------------------------------

def start_bottle():
    #Zaženemo bottle
    run(app, host='localhost', port=8080, debug=True)