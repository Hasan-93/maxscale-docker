import pymysql

conn = pymysql.connect(host="192.168.0.180",port=4000,user="maxuser",passwd="maxpwd")

cur = conn.cursor()

cur.execute("SELECT * FROM zipcodes_two.zipcodes_two ORDER BY Zipcode LIMIT 1")
databaseList0 = cur.fetchall()
cur.execute("SELECT * FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 1")
databaseList1 = cur.fetchall()
cur.execute("SELECT * FROM zipcodes_two.zipcodes_two LIMIT 10")
databaseList2 = cur.fetchall()
cur.execute("SELECT * FROM zipcodes_one.zipcodes_one LIMIT 9990,10")
databaseList3 = cur.fetchall()

for database in databaseList0:
    print(database)

for database in databaseList1:
    print(database)

for database in databaseList2:
    print(database)

for database in databaseList3:
    print(database)


conn.close()

#The smallest zipcode number in zipcodes_two
#cursor.execute("SELECT * FROM zipcodes_two.zipcodes_two ORDER BY Zipcode LIMIT 1;")


#The largest zipcode number in zipcodes_one
#cursor.execute("SELECT * FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 1;")


#The first 10 rows of zipcodes_tow
#cursor.execute("SELECT * FROM zipcodes_two.zipcodes_two LIMIT 10")


#The last 10 rows of zipconde_one
#cursor.execute("SELECT * FROM zipcodes_one.zipcodes_one LIMIT 9990,10")
