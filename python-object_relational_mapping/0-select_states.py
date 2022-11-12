#!/usr/bin/python3
"""This module lists all states from the database hbtn_0e_0_usa
   Created on Saturday, November 12, 2022
   @author: Daisy Chipana Lapa
"""


import MySQLdb
from sys import argv
conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
