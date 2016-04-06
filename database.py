import sqlite3 as lite

con = lite.connect('getting_started.db')

# Inserting rows by passing values directly to `execute()`
with con:
    cur = con.cursor()
    weather = (('New York City',   2013,    'July',        'January',     62),
               ('Boston',          2013,    'July',        'January',     59),
               ('Chicago',         2013,    'July',        'January',     59),
               ('Miami',           2013,    'August',      'January',     84),
               ('Dallas',          2013,    'July',        'January',     77),
               ('Seattle',         2013,    'July',        'January',     61),
               ('Portland',        2013,    'July',        'December',    63),
               ('San Francisco',   2013,    'September',   'December',    64),
               ('Los Angeles',     2013,    'September',   'December',    75))
    cur.executemany('INSERT INTO WEATHER VALUES (?, ?, ?, ?, ?)', weather)
