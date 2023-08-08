import time
import requests
import datetime

URL = 'http://api.open-notify.org/iss-now.json'
filename = 'iss_positions.csv'

with open(filename, 'w') as file:
    file.write('           Date             Latitude  Longitude\n')


while True:
    response = requests.get(url=URL)
    data = response.json()

    date, latitude, longitude = (
        datetime.datetime.now(),
        data['iss_position']['latitude'], 
        data['iss_position']['longitude']
    )

    if date is not None and latitude is not None and longitude is not None:

        with open(filename, 'a') as file:
            file.write(f'{date}; {latitude}; {longitude}\n')

    time.sleep(5)
