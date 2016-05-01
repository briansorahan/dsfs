import collections
import requests
import sqlite3       as lite
import time
        
from dateutil.parser import parse
from pandas.io.json  import json_normalize

con = lite.connect('citi_bike.db')

createCitibikeTable = """
CREATE TABLE citibike_reference (
    id INT PRIMARY KEY,
    totalDocks INT,
    city TEXT,
    altitude INT, 
    stAddress2 TEXT,
    longitude NUMERIC,
    postalCode TEXT,
    testStation TEXT,
    stAddress1 TEXT,
    stationName TEXT,
    landMark TEXT,
    latitude NUMERIC,
    location TEXT
)
"""

insertCitibike = """
INSERT INTO citibike_reference (
    id,
    totalDocks,
    city,
    altitude,
    stAddress2,
    longitude,
    postalCode,
    testStation,
    stAddress1,
    stationName,
    landMark,
    latitude,
    location
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

def createTables(station_ids):
    """
    Create SQL tables for citibike data and per-station availability.
    """
    with con:
        cur = con.cursor()
        cur.execute(createCitibikeTable)
        # add the '_' to the station name and also add the data type for SQLite
        station_ids = ['_' + str(x) + ' INT' for x in station_ids]
        # we concatenate the string and joining all the station ids (now with '_' and 'INT' added)
        cur.execute("CREATE TABLE available_bikes ( execution_time INT, " +  ", ".join(station_ids) + ");")

def insertStationList(station_list):
    """
    Insert citibike data.
    """
    with con:
        cur = con.cursor()
        for station in station_list:
            cur.execute(insertCitibike, (
                station['id'],
                station['totalDocks'],
                station['city'],
                station['altitude'],
                station['stAddress2'],
                station['longitude'],
                station['postalCode'],
                station['testStation'],
                station['stAddress1'],
                station['stationName'],
                station['landMark'],
                station['latitude'],
                station['location']
            ))

def insertAvailableBikes(exec_time, stations):
    """
    Insert per-station availability data.
    """
    with con:
        cur      = con.cursor()
        id_bikes = collections.defaultdict(int) # defaultdict to store available bikes by station
        
        cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s'),))
        
        # loop through the stations in the station list
        for station in stations:
                id_bikes[station['id']] = station['availableBikes']

        for k, v in id_bikes.iteritems():
            cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%s') + ";")

def main():
    r         = requests.get('http://www.citibikenyc.com/stations/json')
    stations  = r.json()['stationBeanList']
    df        = json_normalize(stations)
    exec_time = parse(r.json()['executionTime'])
    
    # create the tables
    createTables(df['id'].tolist())
    
    # insert the station list
    insertStationList(stations)

    for x in range(0, 60):
        insertAvailableBikes(exec_time, stations)
        time.sleep(60)

if __name__ == "__main__":
    main()
