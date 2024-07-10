
import mysql.connector

def update_record(id,  tanggal, deskripsi ):
    try:
        mysb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="keuangan"
        )

        mycursor = mysb.cursor()

        sql = "UPDATE transaksi SET id = %s, tanggal = %s, deskripsi = %s WHERE id = %s"
        val = (id, tanggal, deskripsi, id)
        print("Executing SQL:", sql % val)  
        mycursor.execute(sql, val)

        mysb.commit()
    
        print(mycursor.rowcount, "record(s) affected")

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        mycursor.close()
        mysb.close()


