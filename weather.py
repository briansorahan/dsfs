import requests
import sqlite3       as lite
import time

from pandas.io.json  import json_normalize

con     = lite.connect('weather.db')
apikey  = '8f30f6b1ab2d7700660fd87ac5421415'
baseURL = 'https://api.forecast.io/forecast'

cities = [
    ('Atlanta, GA', 33.762909, -84.422675),
    ('Austin, TX', 30.303936, -97.754355),
    ('Boston, MA', 42.331960, -71.020173),
    ('Chicago, IL', 41.837551, -87.681844),
    ('Cleveland, OH', 41.478462, -81.679435),
    ('Denver, CO', 39.761850, -104.881105),
    ('Las Vegas, NV', 36.229214, -115.26008),
    ('Los Angeles, CA', 34.019394, -118.410825),
    ('Miami, FL', 25.775163, -80.208615),
    ('Minneapolis, MN', 44.963324, -93.268320),
    ('Nashville, TN', 36.171800, -86.785002),
    ('New Orleans, LA', 30.053420, -89.934502),
    ('New York, NY', 40.663619, -73.938589),
    ('Philadelphia, PA', 40.009376, -75.133346),
    ('Phoenix, AZ', 33.572154, -112.090132),
    ('Salt Lake City, UT', 40.778996, -111.932630),
    ('San Francisco, CA', 37.727239, -123.032229),
    ('Seattle, WA', 47.620499, -122.350876),
    ('Washington, DC', 38.904103, -77.017229)
]

createTables = """
CREATE TABLE max_temperatures (
    city            TEXT,
    time            INT,
    max_temperature NUMERIC
);
"""

insertMaxTemp = """
INSERT INTO max_temperatures (city, time, max_temperature)
VALUES                       (?,    ?,    ?)
"""

def getMaxTempsFor(city):
    with con:
        cur    = con.cursor()
        now    = int(time.time())
        oneday = 60 * 60 * 24     # secs
        
        for t in range(now - oneday, now - (oneday * 31), -1 * oneday):
            lat, lng      = city[1], city[2]
            u             = '{}/{}/{},{},{}'.format(baseURL, apikey, lat, lng, t)
            r             = requests.get(u)
            max_temp      = r.json()['daily']['data'][0]['temperatureMax']
            max_temp_time = r.json()['daily']['data'][0]['temperatureMaxTime']
            cur.execute(insertMaxTemp, (city[0], max_temp_time, max_temp))

def main():
    with con:
        con.cursor().execute(createTables)
    for city in cities:
        getMaxTempsFor(city)

if __name__ == "__main__":
    main()
