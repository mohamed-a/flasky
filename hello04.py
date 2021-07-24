from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return f'<h1>__name__ is: {__name__}</h1>'

if __name__ == '__main__':    
    app.run()   
