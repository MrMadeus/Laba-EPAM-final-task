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
		put_request = requests.post('http://keeper:2010/putdata', json=in_data, headers=headers)
	if put_request.status_code == 200:
		return 'Done'
	else:
		return 'Can not download data'

if __name__ == '__main__':
	reaper.run(host='0.0.0.0', port=2008, debug=True)
