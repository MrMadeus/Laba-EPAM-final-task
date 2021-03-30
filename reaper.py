#!flask/bin/python
from flask import Flask
import requests

reaper = Flask (__name__)

@reaper.route('/getdata', methods=['GET'])
def get_data():
	appid = 'bfea39101f8dd2703f8c68be119914f6'
	city_id = [625144, 630428, 629634, 628035]
	for city in city_id:
		try:
			res = requests.get("http://api.openweathermap.org/data/2.5/weather", 
				params={'id': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
			data = res.json()
			return ("conditions:", data['weather'][0]['description'])
		except Exception as e:
			return ("Exception (weather):", e)

if __name__ == '__main__':
	reaper.run(host='0.0.0.0', port=2008, debug=True)