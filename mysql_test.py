import mysql.connector
import pickle

mysql = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "face_recog")

cursors = mysql.cursor()

command = "SELECT encoding FROM encoding_image"
cursors.execute(command)
data = cursors.fetchone()

# nilai = ("welowelo",)

blobb = data[0]
dencode = pickle.loads(blobb)


print(dencode)
mysql.commit()
