#!flask/bin/python
from flask import Flask
import requests

master = Flask (__name__)

@master.route('/')
def index():
	return 'To get data from openweathermap.org go to: /loaddata\nTo get info about weather in city go to: /getinfo/{city name} (avalible: Minsk, Baranovichi, Brest)'

@master.route('/loaddata')
def loaddata():
	load = requests.get('http://0.0.0.0:2008/getdata')
	if load.status_code == 200:
		return 'Done'
	else:
		return 'Can not download data'

#@master.route('/getinfo/Minsk')
#def get_info(city = 'Minsk'):


if __name__ == '__main__':
	master.run(host='0.0.0.0', port=2006, debug=True)