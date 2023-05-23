import bottle 
import skripta

"""Bottle poskrbi, da stran laufa in da so vse stvari povezane med sabo."""

#css 
@bottle.route('static/css/<filename:re:.*\.css>')
def send_css(filename):
    return bottle.static_file(filename, root='static/css')

#img
@bottle.route('static/img/<filename:re:.*\.png>')
def send_img(filename):
    return bottle.static_file(filename, root='static/img')

#javascript
@bottle.route('static/javascript/<filename:re:.*\.js>')
def send_javascript(filename):
    return bottle.static_file(filename, root='static/javascript')

#html - naloga
@bottle.route('naloga/<filename:re:.*\.html>')
def send_html(filename):
    return bottle.static_file(filename, root='naloga')

#javascript robotlib
@bottle.route('naloga/<filename:re:.*\.js>')
def send_file_js(filename):
    return bottle.static_file(filename, root='naloga')

#knjižnica v modules
#raphaelFactory-1.0
#delayFactory-1.0
#simulationFactory-1.0
#beav-1.0
@bottle.route('../static/javascript/_common/<filename:re:.*>')
def send_lib_js(filename):
    return bottle.static_file(filename, root='../../Pisek/pisek-git/_common/modules/pemFioi')

#jquery-1.7.1
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

#beaver-task-2.0 

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
def senminiPlatform(filename):
    return bottle.static_file(filename, root='../../Pisek/pisek-git/_common/modules/integrationAPI.01/official')

#taskStyles-mobileFirst
@bottle.route('../static/javascript/_common/modules/pemFioi/<filename:re:.*\.css>')
def send_taskStyles(filename):
    return bottle.static_file(filename, root='../../Pisek/pisek-git/_common/modules/pemFioi')

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

#numeric_keypad_css
@bottle.route('../static/javascript/_common/modules/pemFioi/shared/numeric_keypad/<filename:re:.*\.css>')
def send_numeric_keypadd_css(filename):
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
@bottle.route('../static/javascript/_common/modules/pemFioi/quickAlgo/<filename:re:.*\.css>')
def send_quickAlgo_css(filename):
    return bottle.static_file(filename, root='../../Pisek/pisek-git/_common/modules/pemFioi/quickAlgo')

@bottle.get("/")    
def home():              
    return bottle.template("index.html")

@bottle.post("/") 
def get_data():
    m = bottle.request.forms.get('m')
    n = bottle.request.forms.get('n')
    bottle.redirect("/login")






def start_bottle():
    #Zaženemo bottle

    bottle.run(debug=True, reloader=True)