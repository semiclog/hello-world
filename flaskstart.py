# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 20:27:20 2019

@author: semiclog
"""

from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Welcome to TutsPlus!"

if __name__ == '__main__':
    app.run()