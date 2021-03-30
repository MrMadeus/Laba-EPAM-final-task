#!flask/bin/python
from flask import Flask
import requests
import sqlite3

keeper = Flask (__name__)

@keeper.route('/putdata', methods=['POST'])
def put_data():
	pass

@keeper.route('/returndata', methods=['GET'])
def return_data():
	pass

if __name__ == '__main__':
	keeper.run(host='0.0.0.0', port=2010, debug=True)