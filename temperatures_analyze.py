import pandas  as pd
import sqlite3 as lite

con = lite.connect('temperatures.db')

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

columns = ['city', 'latitude', 'longitude', 'temperature_max', 'temperature_max_time', 'temperature_min', 'temperature_min_time',
           'apparent_temperature_max', 'apparent_temperature_max_time', 'apparent_temperature_min', 'apparent_temperature_min_time']

def profileData(city):
    with con:
        cur  = con.cursor()
        name = city[0]
        cur.execute("SELECT * FROM daily_temperatures WHERE city = ?", (name,))
        df = pd.DataFrame(cur.fetchall(), columns=columns)
        print('temperature range for {} was {} to {}'.format(name, df['temperature_min'].min(), df['temperature_max'].max()))
        print('mean temperature for {} was {}'.format(name, (df['temperature_min'].median() + df['temperature_max'].median()) / 2))
        print('variance in min temperature for {} was {}'.format(name, df['temperature_min'].var()))
        print('variance in max temperature for {} was {}'.format(name, df['temperature_max'].var()))

def main():
    # Analyze temperatures
    for city in cities:
        profileData(city)

if __name__ == "__main__":
    main()