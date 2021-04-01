#!flask/bin/python
from flask import Flask, request
import requests
import sqlite3

keeper = Flask (__name__)

@keeper.route('/putdata', methods=['POST'])
def put_data():
	input_data = request.json
	db = sqlite3.connect('weather.sqlite')
	c = db.cursor()
	c.execute('''CREATE TABLE IF NOT EXISTS curent_weather 
		(id text, 
		temp text, 
		country text)''')
	columns = ['id', 'temp', 'country']
	c.execute('INSERT INTO curent_weather VALUES (?,?,?)', input_data)
	c.close()
	return '', 200

@keeper.route('/returndata', methods=['GET'])
def return_data():
	pass

if __name__ == '__main__':
	keeper.run(host='0.0.0.0', port=2010, debug=True)