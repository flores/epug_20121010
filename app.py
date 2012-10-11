#!/usr/bin/env python

import markdown
from flask import Flask
from flask import render_template
from flask import Markup
from flask import send_from_directory

app = Flask(__name__)
@app.route('/ecpug/pypal')

def index():
  content = """
# Pythoning With A Pal! 
 
## What's the project?

```curl -s -X POST -d 'name=Foo' localhost:5000/hello```

```Hello, Foo!```

```curl -s -X POST -d 'name=Bar' localhost:5000/hello```

```Hello, Bar!```

  - Build a web app that replies "Hello, Foo!" to a post request to /hello, with the data "name=Foo"
  - Hint: Use [Flask](http://flask.pocoo.org/) for a really easy framework.  But you can pick whatever you want.
  - *Extra Credit* - Write an http client in python that performs Step 1
## FAQ:
  - What if I don't know how to install Python, or even what a Python is? Find a handsome, competent Steering Committee Member who will help you out with [this](http://www.diveintopython.net/installing_python/index.html)
  - Is this an individual project?  No, this project requires a buddy.  The person sitting next to you is now your buddy.
  - How long will people have to complete the project?  You will have 30 minutes to complete the project.
  - Who Wins? Everyone who completes Step 1 will write their name on a piece of paper and drop it into the bag for a prize drawing.  An additional entry can be submitted for anyone who completes the Extra Credit.
"""
  content = Markup(markdown.markdown(content))
  return render_template('index', **locals())

@app.route('/ecpug/lpthw/<path:filename>')
def send_foo(filename):
     return send_from_directory('/usr/local/ec_pyug/static/', filename)

app.run(debug=True)
