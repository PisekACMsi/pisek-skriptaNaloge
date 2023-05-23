from bottle import Bottle, static_file, template, run
import os

app = Bottle()

@app.route('/')
def serve_html():
    return template('index.html')

def add_routes_from_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.js'):
                # Get the relative path of the file
                relative_path = os.path.relpath(os.path.join(root, file), folder_path)
                # Define the route pattern based on the relative path
                route_pattern = f'/modules/{relative_path}'
                
                @app.route(route_pattern)
                def serve_static_file():
                    return static_file(file, root=folder_path)

# Specify the path to the 'modules' folder
modules_folder = '../Pisek/pisek-git/_common/modules'
add_routes_from_folder(modules_folder)

# Specify the path to your index.html file
html_file_path = 'naloga/index.html'

# Define a route for serving the HTML file
@app.route('/')
def serve_html():
    return static_file('index.html', root=os.path.dirname(html_file_path))

run(app, host='localhost', port=8080)