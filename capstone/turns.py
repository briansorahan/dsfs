import math
import matplotlib.pyplot  as plt
import numpy              as np
import pandas             as pd
import psycopg2

# TODO: get headings for all devices for all companies
getHeadings = """
SELECT    h.device_id,
          h.heading,
          h.hb_time
FROM      heartbeats h
LEFT JOIN users u
       ON h.creator_id = u.user_id
WHERE     u.company_id = 2019
  AND     h.device_id = '3eb3a32b-0d0b-43a4-a8b4-0924489a1324'
  AND     h.hb_time > 1462826043
ORDER BY  h.hb_time DESC
"""

conn = psycopg2.connect("dbname=leaf user=leaf")

def main():
    with conn:
        # build a dataframe with device headings
        cur = conn.cursor()
        cur.execute(getHeadings)
        df = pd.DataFrame(cur.fetchall(), columns=['device_id','heading','hb_time'])
        # make slope and concavity indices
        df['concavity'] = df['heading'].shift(1) - df['heading']

        print('mean concavity is {}'.format(df['concavity'].mean()))
        
        # plot data
        df.plot(x='hb_time', y='concavity', grid=True)
        plt.show()

if __name__ == "__main__":
    main()
