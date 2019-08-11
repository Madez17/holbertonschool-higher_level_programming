#!/usr/bin/python3
""" Script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         port=3306,
                         host="localhost",
                         db=argv[3])
    cursor = db.cursor()
    recs = cursor.execute("""SELECT * FROM states WHERE name LIKE "{}" ORDER BY
                          id ASC""".format(argv[4]))
    for iter in range(recs):
        print(cursor.fetchone())
    cursor.close()
    db.close()
