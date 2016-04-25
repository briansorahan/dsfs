import requests
import sqlite3       as lite
import time

from pandas.io.json  import json_normalize

con     = lite.connect('temperatures.db')
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

dropTables = "DROP TABLE IF EXISTS daily_temperatures;"

createTables = """
CREATE TABLE daily_temperatures (
    city                          TEXT,

    latitude                      NUMERIC,
    longitude                     NUMERIC,

    temperature_max               NUMERIC,
    temperature_max_time          INT,

    temperature_min               NUMERIC,
    temperature_min_time          INT,

    apparent_temperature_max      NUMERIC,
    apparent_temperature_max_time INT,

    apparent_temperature_min      NUMERIC,
    apparent_temperature_min_time INT
);
"""

insertDailyTemp = """
INSERT INTO daily_temperatures (
    city,
    latitude,
    longitude,
    temperature_max,
    temperature_max_time,
    temperature_min,
    temperature_min_time,
    apparent_temperature_max,
    apparent_temperature_max_time,
    apparent_temperature_min,
    apparent_temperature_min_time
) VALUES (?,?,?,?,?,?,?,?,?,?,?);
"""

def storeTempsFor(city):
    with con:
        cur    = con.cursor()
        now    = int(time.time())
        oneday = 60 * 60 * 24     # secs
        
        for t in range(now - oneday, now - (oneday * 31), -1 * oneday):
            name, lat, lng = city[0], city[1], city[2]
            u              = '{}/{}/{},{},{}'.format(baseURL, apikey, lat, lng, t)
            r              = requests.get(u)
            # daily data is an array with length 1
            # (just to be consistent with the structure of hourly data, I suppose)
            data   = r.json()['daily']['data'][0]
            values = (
                name,
                lat,
                lng,
                data['temperatureMax'],
                data['temperatureMaxTime'],
                data['temperatureMin'],
                data['temperatureMinTime'],
                data['apparentTemperatureMax'],
                data['apparentTemperatureMaxTime'],
                data['apparentTemperatureMin'],
                data['apparentTemperatureMinTime']
            )
            cur.execute(insertDailyTemp, values)

def main():
    # Fetch and store temperatures
    with con:
        con.cursor().execute(dropTables)
        con.cursor().execute(createTables)
    for city in cities:
        storeTempsFor(city)

if __name__ == "__main__":
    main()
