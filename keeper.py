#!flask/bin/python
from flask import Flask, request
import requests
import sqlite3

keeper = Flask (__name__)

@keeper.route('/putdata', methods=['POST'])
def put_data():
	input_data = request.json
	c.execute('''create table curent_weather 
		(id integer, 
		temp integer, 
		country text))''')
	db = sqlite3.connect('weather.sqlite')
	columns = ['id', 'temp', 'country']
	for data in input_data:
		keys = tuple(data[c] for c in columns)
		c = db.cursor()
		c.execute('insert into curent_weather values (?,?,?)', keys)
		c.close()

@keeper.route('/returndata', methods=['GET'])
def return_data():
	pass

if __name__ == '__main__':
	keeper.run(host='0.0.0.0', port=2010, debug=True)