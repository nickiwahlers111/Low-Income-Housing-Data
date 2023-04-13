import mysql.connector as conn

try:
    cnx = conn.connect(
        host="localhost",
        user="root",
        password=""
    )

    mycursor = cnx.cursor()

    mycursor.execute("SHOW DATABASES")
    results = mycursor.fetchall()
    print(results)

    # move to the next result set
    mycursor.nextset()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS Housing")

    # fetch all the results
    results = mycursor.fetchall()
    print(results)

    for x in mycursor:
        print(x)

except Exception as e:
    print("Error while connecting to MySQL", e)

finally:
    cnx.close()
