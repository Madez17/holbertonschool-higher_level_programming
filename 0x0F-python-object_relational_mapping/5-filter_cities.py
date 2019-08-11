#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         port=3306,
                         host="localhost",
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM cities JOIN states ON
                   states.id=cities.state_id
                   WHERE states.name=%s;""", (argv[4],))
    resc = cursor.fetchall()
    for iter in resc:
        if iter is not resc[len(resc) - 1]:
            print("{}".format(iter[0]), end=", ")
        else:
            print("{}".format(iter[0]), end="\n")
    cursor.close()
    db.close()
