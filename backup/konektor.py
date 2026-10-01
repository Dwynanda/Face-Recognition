import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "face_recog"
)

cursors = database.cursor()
cursors.execute("SELECT idimage, encoding FROM encoding_image")
data = cursors.fetchall

test = []

for baris in data():
    id_image = baris[0],
    encoding = baris[1],
    test.append((id_image, encoding))

print(test)

cursors.close()
database.close()
