import requests
from datetime import datetime

now = datetime.now()
timeString = now.strftime(("%Y/%m/%d %H:%M:%S"))

url = 'http://localhost:3010/reading'
readingObj = {
  'sensorId': 3,
  'readTime': timeString,
  'co': 0.0,
  'temp': 0.0,
  'humid': 0.0,
}

x = requests.post(url, json=readingObj)
