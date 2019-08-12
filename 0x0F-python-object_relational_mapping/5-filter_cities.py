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
    cursor.execute("""SELECT cities.name FROM cities INNER JOIN states ON
                   cities.state_id=states.id
                   WHERE states.name=%s""", (argv[4],))
    resc = cursor.fetchall()

    if resc:
        for iter in resc:
            if iter is not resc[len(resc) - 1]:
                print("{}".format(iter[0]), end=", ")
            else:
                print("{}".format(iter[0]), end="\n")
    cursor.close()
    db.close()
