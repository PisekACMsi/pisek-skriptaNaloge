import bottle 
import skripta

"""Bottle poskrbi, da stran laufa in da so vse stvari povezane med sabo."""

@bottle.route('/static/css/<filename:re:.*\.css>')
def send_css(filename):
    return bottle.static_file(filename, root='static/css')

@bottle.route('/static/img/<filename:re:.*\.png>')
def send_img(filename):
    return bottle.static_file(filename, root='static/img')

@bottle.route('/static/javascript/<filename:re:.*\.js>')
def send_javascript(filename):
    return bottle.static_file(filename, root='static/javascript')

@bottle.route('/naloga/<filename:re:.*\.html>')
def send_html(filename):
    return bottle.static_file(filename, root='naloga')

@bottle.route('/naloga/<filename:re:.*\.js>')
def send_file_js(filename):
    return bottle.static_file(filename, root='naloga')

@bottle.route('/../../Pisek/pisek-git/_common/modules/pemFioi/<filename:re:.*\.js>')
def send_lib_js(filename):
    return bottle.static_file(filename, root='../../Pisek/pisek-git/_common/modules/pemFioi')


@bottle.get("/")    
def home():              
    return bottle.template("bla.html")

@bottle.post("/") 
def get_data():
    m = bottle.request.forms.get('m')
    n = bottle.request.forms.get('n')
    bottle.redirect("/login")






def start_bottle():
    #Zaženemo bottle

    bottle.run(debug=True, reloader=True)