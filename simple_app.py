#  a simple Flask app with a single view and route.
from flask import Flask
#from flask import request   # get the request object
from flask import render_template

app = Flask(__name__)

@app.route('/')     # Decorator, Use this function as the route '/'
@app.route('/<name>')
def index(name="Bob"):
    return render_template("index.html", name=name)
    #name = request.args.get('name', name)
    #return "Hello {}!".format(name)

# Routes take strings, integers and floats
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')

def add(num1, num2):
    context = { 'num1': num1, 'num2': num2 }
    return render_template("add.html", **context)
    #return render_template("add.html", num1=num1, num2=num2)
    #return '{} + {} = {}'.format(num1, num2, num1+num2)

    
    
app.run(debug=True, port=3000, host='0.0.0.0')  #debug=True restarts sever on changes

