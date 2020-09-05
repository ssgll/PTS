# -*- coding: UTF-8 -*-
from flask import render_template

def indexView():
	return render_template("index.html")
