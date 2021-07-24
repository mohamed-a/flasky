from flask import Flask
app = Flask(__name__)
 
def index():
   return '<h1>Hello World!</h1>'
 
# traditional way to register view function
app.add_url_rule('/', 'index', index)