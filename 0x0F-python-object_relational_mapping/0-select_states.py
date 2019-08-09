#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1],
		         passwd=argv[2],
                         port=3306,
                         host="localhost",
                         db=argv[3]);
cursor = db.cursor()
recs=cursor.execute("SELECT * FROM states ORDER BY id ASC");
for iter in range(recs):
    print(cursor.fetchone())
