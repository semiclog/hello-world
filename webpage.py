# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 20:59:24 2019

@author: emdan
"""

from flask import Flask, render_template
app = Flask(__name__)

stats = { }

@app.route("/")
#@app.route("/home")
def home():
    #return "<h1>Home Page</h1>"
    return render_template('home.html')
     
#@app.route("/about")
#def about():
#    return "<h1>About Page</h1>"

if __name__ == '__main__':
#Or disable the reloader if you want to call app.run from Jupyter.
    app.run(debug=True, use_reloader=False)
    