#!flask/bin/python
from flask import Flask, request
import requests
import json

master = Flask (__name__)

@master.route('/')
def index():
	return 'To get data from openweathermap.org go to: /loaddata\nTo get info about weather in city go to: /getinfo'

@master.route('/loaddata')
def loaddata():
	load = requests.get('http://reaper:2008/getdata')
	if load.status_code == 200:
		return 'Done'
	else:
		return 'Can not download data'

@master.route('/getinfo')
def get_info():
	returned_data = requests.get('http://keeper:2010/returndata')
	final_data = json.loads(returned_data.text)
	final_string = ''
	for i in final_data:
		final_string = final_string + '\n' + "In {} tempreture is {} and wind speed is {}".format(i[0], str(i[1]), str(i[2])[9:11])
	return final_string


if __name__ == '__main__':
	master.run(host='0.0.0.0', port=2006, debug=True)
