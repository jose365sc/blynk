#!/usr/bin/env python

"""A simple python script template.
"""

from __future__ import print_function
import os
import sys
import subprocess
import sqlite3
import re
import datetime
import parse
from contextlib import closing
#import argparse

def main(arguments):

    dbname = '/home/pi/blynk/sensordata.sqlite'
    with closing(sqlite3.connect(dbname)) as conn:
        cur = conn.cursor()

	timestamp = datetime.datetime.now()

# sensor 2
#        result = subprocess.check_output(['/home/pi/blynk/read_bme280.py', '--dump', '1', '0x76'])
#        sys.stderr.write(result)
#	m = parse.parse('{:f} {:f} {:f}', result)
#        if m[0] is not None and m[1] is not None:
#            temperature = m[0]
#            humidity = m[1]
#            sys.stderr.write(str(temperature))
#            sys.stderr.write(str(humidity))
#	    cur.execute('insert into temperatures(id, datetime, temperature, humidity) values(?, ?, ?, ?)', [0, timestamp, temperature, humidity])
#            conn.commit()

# sensor 1
#        result = subprocess.check_output(['/home/pi/blynk/read_dht', '--dump', '22', '4'])
#        sys.stderr.write(result)
#	m = parse.parse('{:f} {:f}', result)
#        if m[0] is not None and m[1] is not None:
#            temperature = m[0]
#            humidity = m[1]
#            sys.stderr.write(str(temperature))
#            sys.stderr.write(str(humidity))
#	    cur.execute('insert into temperatures(id, datetime, temperature, humidity) values(?, ?, ?, ?)', [1, timestamp, temperature, humidity])
#            conn.commit()

# sensor 0
        result = subprocess.check_output(['/home/pi/blynk/read_dht', '--dump', '22', '17'])
        sys.stderr.write(result)
	m = parse.parse('{:f} {:f}', result)
        if m[0] is not None and m[1] is not None:
            temperature = m[0]
            humidity = m[1]
            sys.stderr.write(str(temperature))
            sys.stderr.write(str(humidity))
	    cur.execute('insert into temperatures(id, datetime, temperature, humidity) values(?, ?, ?, ?)', [0, timestamp, temperature, humidity])
            conn.commit()

# sensor 1
        result = subprocess.check_output(['/home/pi/blynk/read_dht', '--dump', '22', '18'])
        sys.stderr.write(result)
	m = parse.parse('{:f} {:f}', result)
        if m[0] is not None and m[1] is not None:
            temperature = m[0]
            humidity = m[1]
            sys.stderr.write(str(temperature))
            sys.stderr.write(str(humidity))
	    cur.execute('insert into temperatures(id, datetime, temperature, humidity) values(?, ?, ?, ?)', [1, timestamp, temperature, humidity])
            conn.commit()

# sensor 2
        result = subprocess.check_output(['/home/pi/blynk/read_dht', '--dump', '22', '22'])
        sys.stderr.write(result)
	m = parse.parse('{:f} {:f}', result)
        if m[0] is not None and m[1] is not None:
            temperature = m[0]
            humidity = m[1]
            sys.stderr.write(str(temperature))
            sys.stderr.write(str(humidity))
	    cur.execute('insert into temperatures(id, datetime, temperature, humidity) values(?, ?, ?, ?)', [2, timestamp, temperature, humidity])
            conn.commit()

# sensor 3
        result = subprocess.check_output(['/home/pi/blynk/read_dht', '--dump', '22', '23'])
        sys.stderr.write(result)
	m = parse.parse('{:f} {:f}', result)
        if m[0] is not None and m[1] is not None:
            temperature = m[0]
            humidity = m[1]
            sys.stderr.write(str(temperature))
            sys.stderr.write(str(humidity))
	    cur.execute('insert into temperatures(id, datetime, temperature, humidity) values(?, ?, ?, ?)', [3, timestamp, temperature, humidity])
            conn.commit()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
