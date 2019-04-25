# Flask Basics Notes


- View: In flask and Django "a view is a function that returns an HTTP response." 
  - "This response has to be a string but can be any string you want."
  - Views manage the request response cycle
  - In other frameworks, Views are called Controllers
- Route: "A route is the URL path to a view. They always start with a forward slash / and can end with one if you want."
- dunder: "A quick way of saying "double underscore".

- Set up the name space so the app refers to itself, ` app = Flask(__name__)`
  - When run directly through python the namespace refers to itself (__main__)
  - When imported into another file, the namespace is "simple_app"
- Decorator: a function which wraps around another function to allow you to do things with it
  - Use this function as the route '/'
```python
# Decorator, Use this function as the route '/'
@app.route('/')		# Decorator function
def index():
	return "Hello World!"
```

### Create a View
- Add a view function named index. Give this view a route of "/". Make the view return your name. 

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')   
def index():
    return "Bob"
```

### Request Variables

- What object do we need to import from Flask to have access to the query string?
- Import request from Flask. Then update the index view to return "Hello {name}", replacing {name} with a name argument in the query string.

- global: "A global is a variable that exists outside of the normal Python scopes." 
  - "It is available everywhere."
- query string: "The part of a URL that comes after the ?."
- The arguements in the request are held by `args`. Similiar to get/post keywords and values.


```python
#Import request from Flask. 
#Then update the index view to return "Hello {name}", replacing {name} with a name argument in the query string.

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index(name="Bob"):
    name = request.args.get('name', name)
    return "Hello {}".format(name)
```

- To access the query string, import the request object from Flask.

### Routes that take Numbers
- Change the string values in a route to integers, `@app.route('/add/<int:num1>/<int:num2>')`
	-  ``` https://flask-basics-edward.codeanyapp.com/add/2/5 ```


- Add a new route to hello() that expects a name argument. The view will need to accept a name argument, too.

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def hello(name):
     return 'Hello {}'.format(name)
```

- Now give hello() a default name argument of "Treehouse".
```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def hello(name="Treehouse"):
     return 'Hello {}'.format(name)
```

- Add a view named multiply. Give multiply a route named /multiply. Make multiply() return the product of 5 * 5. Remember, views have to return strings.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/multiply')
@app.route('/multiply/<int:num1>/<int:num2>')

def multiply():
    num1 = 5
    num2 = 5
    result = num1 * num2
    result = str(result)
    return result
```

- Add a new route to multiply() that has two arguments. Add the same two arguments to the multiply() view. They should have defaults of 5.
- Mark both route arguments as ints.
- Add routes to allow floats or a combination of floats and ints.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/multiply')
@app.route('/multiply/<int:num1>/<int:num2>')
@app.route('/multiply/<float:num1>/<float:num2>')
@app.route('/multiply/<float:num1>/<int:num2>')
@app.route('/multiply/<int:num1>/<float:num2>')


def multiply(num1 = 5, num2 = 5):       
    result = num1 * num2
    result = str(result)
    return result
```
- Change the response to multiply the two arguments and return their product.
```    return str(num1 * num2) ```

## 2. Templates and Static Files

### Objectives

- How to render templates, 
- Take advantage of template inheritance, 
- Use static files to make our templates look nicer.

### Render Templates

- "Use {{ and }} to print items in templates."
- "Flask looks for templates in a directory named templates by default." 
    - "This directory should be in the same directory as your app script."
- Flask automatically uses the templates inside the "templates" folder.
- To import template rendering from flask, ` from flask import render_template `

```python
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/hello/<name>')
def hello(name="Treehouse"):
    context = { 'name': name }
	return render_template("hello.html", **context)
	
	#return render_template("hello.html")
```


### Template Inheritance

- Templates can inherit html from each other and overide the inheritance in specific blocks.
- Blocks are created with urly brackets and percent sign, {% %}, designates a command area
- Start/End tags designate a block, ` {% block title %}{% endblock %} `



- `{% block %}`, defines a block in a template. 
  - In extended templates, these areas are overridable.
  - "In templates that extend other templates, this areas will override the parent template's block."
    ``` {% block title %} Howdy!  | {{ super() }} {% endblock %} ```
	
- `{% extends %}`, specifies what template is the parent of the current template, like extended classes in Python. 
  - You can have a change of extensions if you need them.
  ``` {% extends "layout.html" %} ```
  
- `{{ super() }}`, This function brings in whatever content was in the same block in the parent template. 
  - Include the existing content and insert new content before or after the old.
	``` {% block title %} Welcome!  | {{ super() }} {% endblock %} ```
	

### Example App

```python
# flask_app.py

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
	
```

```python

# templates/layout.html

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
	
```

```python

# templates/index.html
{%extends 'layout.html'%}

{%block title%} {{ super() }} Homepage {%endblock%}

{%block content%} 
<h1>Smells Like Bakin'!</h1>
<p>Welcome to my bakery web site!</p>
{%endblock%}

```


### Review Template & Static Files

- Add an import for render_template. It comes directly from the flask library.
- Use render_template() to render the "hello.html" template in hello().
- Pass the name argument to the template. Print the name variable in the <h1> in the template.

#### Create Templates

`templates/layout.html`
- Create an html file and html doctype, html, head, and body elements
- Add two blocks to the "layout.html" template. 
  - Add a block named title around the content of the <title> tag. 
  - Add a block named content inside the <body> tag.

`templates/index.html`
- Change "index.html" so it extends "layout.html".
- Add an h1 and p element and content in the <body> tag in "index.html" in the {% block content %} block.
- Put the contents of the <title> tag in "index.html" into the title block.
- Remove everything from "index.html" except for the extends and block tags and their contents.
- Finally, change the "index.html" <title> tag to be: {{ super() }} Homepage. 
  - Make sure there's a space before "Homepage".
  
  
## Sources

- [Flask Basics](https://teamtreehouse.com/library/flask-basics)
- [Flask](http://flask.pocoo.org/)
- [Windows: Install Flask](https://teamtreehouse.com/library/setting-up-a-local-python-environment-windows)
- [Websites Developed with Python](https://www.quora.com/What-are-some-websites-developed-using-Python)
- [Jinja Template Engine](http://jinja.pocoo.org/)





