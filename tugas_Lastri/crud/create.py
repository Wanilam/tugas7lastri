import mysql.connector

def create_record(id, tanggal, deskripsi):
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="keuangan"
    )

    mycursor = mysb.cursor()

    sql = "INSERT INTO transaksi (id, tanggal, deskripsi) VALUES ( %s, %s, %s)"
    val = (id, tanggal, deskripsi)
    mycursor.execute(sql, val)

    mysb.commit()
    
    print(mycursor.rowcount, "record inserted.")

    mycursor.close()
    mysb.close()