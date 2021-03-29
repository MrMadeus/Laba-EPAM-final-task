#!flask/bin/python
from flask import Flask

master = Flask (__name__)

@master.route('/')
def index():
	start_command = input ('Enter command: ')
	return start_command

if __name__ == '__main__':
	master.run(debug=True)