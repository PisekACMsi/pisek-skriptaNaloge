import bottle 
import generator
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
def home():              
    return bottle.template("index.html")

@bottle.post("/") 
def get_data():
    m = bottle.request.forms.get('m')
    n = bottle.request.forms.get('n')
    bottle.redirect("/login")

@bottle.post("/")
def add_background():
    #bd = bottle.request.forms.getall('backGroundTiles')
    print("aaaaaaaaaa", bd)

@bottle.post("/")
def add_food():
    #tukaj dobimo vrednosti iz Bottla
    bd = bottle.request.forms.getall('blocksDropdown')
    rbd = bottle.request.forms.getall('robotBlocksDropdown')
    gbc = bottle.request.forms.getall('groupByCategory')
    print("bbbbbbbbbbbbbbb", bd)


    #Preverimo ali želimo grupirat po kategorijah
    if "Izberi vse" in rbd:
        generator.groupByCategory = True
    else:
        generator.groupByCategory = False

    # nastavimo vse vrednosti, ki obstajajo v IB in Categories na true
    for el in rbd:
        if el != "Izberi vse":
            el= el[0].lower() + el[1:]
            generator.robotIB[el] = True

    for el in bd:
        if el != "Izberi vse":
            el= el[0].lower() + el[1:]
            generator.wholeCategories[el] = True

    generator.ustvariSkripto()
    bottle.redirect("/")




#----------------------------------------------------------------------------------------------------------

def start_bottle():
    #Zaženemo bottle

    bottle.run(debug=True, reloader=True, host='localhost', port=8081)