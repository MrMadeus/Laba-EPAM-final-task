#!flask/bin/python
from flask import Flask
import requests
import json

reaper = Flask (__name__)

@reaper.route('/getdata', methods=['GET'])
def get_data():
	appid = 'bfea39101f8dd2703f8c68be119914f6'
	city_id = [625144, 630428, 629634, 628035]
	for city in city_id:
		res = requests.get("http://api.openweathermap.org/data/2.5/weather", 
			params={'id': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
		in_data = res.json()
		headers = {'Content-Type':'application/json', 'Accept':'*/*'}
		put_request = requests.post('http://0.0.0.0:2010/putdata', json=in_data, headers=headers)
	if put_request.status_code == 200:
		return 'Done'
	else:
		return 'Can not download data'

@reaper.route('/gotdata', methods=['GET'])
def got_data():
	got_data = {"id": "123", "name": "andrew", "status": "fuck"}
	send = requests.post('http://0.0.0.0:2010/putdata', json=got_data, headers={"Content-Type":"aplication/json"})
	if send.status_code == 200:
		return 'Done'
	else:
		return "Data don't send"

#@reaper.route('http://0.0.0.0:2010/putdata', methods='POST')
#def send_data(data):
#	pass

if __name__ == '__main__':
	reaper.run(host='0.0.0.0', port=2008, debug=True)