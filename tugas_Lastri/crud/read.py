
import mysql.connector

def read():
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="keuangan"
    )

    mycursor = mysb.cursor(buffered=True)

    sql = "SELECT * FROM transaksi"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    mycursor.close()
    mysb.close()

    # print(myresult)
    
    for value in myresult:
        print(value)
