#!flask/bin/python
from flask import Flask, request, jsonify
import requests
import sqlite3
import json

keeper = Flask (__name__)

@keeper.route('/putdata', methods=['POST', 'GET'])
def put_data():
	data_out = request.json
	data_for_db = [data_out["name"], data_out["main"]["temp"], str(data_out["wind"])]
	db = sqlite3.connect('weather.sqlite')
	c = db.cursor()
	c.execute('''CREATE TABLE IF NOT EXISTS curent_weather 
		(city text PRIMARY KEY, 
		temp real, 
		wind text)''')
	c.execute('''SELECT city FROM curent_weather WHERE city=?''', (data_for_db[0],))
	exist = c.fetchall()
	if not exist:
		c.execute('INSERT INTO curent_weather VALUES (?,?,?)', data_for_db)
		db.commit()
	else:
		c.execute('UPDATE curent_weather SET temp=? wind=? WHERE city=?', (data_for_db[1], data_for_db[2], data_for_db[0]))
	c.close()
	return '', 200

"""@keeper.route('/test', methods=['POST'])
def test():
	data_out = request.json
	return data_out"""

@keeper.route('/returndata', methods=['GET'])
def return_data():
	db = sqlite3.connect('weather.sqlite')
	c = db.cursor()
	c.execute('''SELECT * FROM curent_weather''')
	get_data = json.dumps(c.fetchall(), ensure_ascii=False)
	c.close()
	return get_data

if __name__ == '__main__':
	keeper.run(host='0.0.0.0', port=2010, debug=True)