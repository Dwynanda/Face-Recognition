import mysql.connector
import pickle
import numpy as np

mysql = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "face_recog")

cursors = mysql.cursor()

named = input("Masukkan nama : ")

name_faces = []
encoding_faces = []

command = """
    SELECT name_faces.name, encoding_faces.encoding
    FROM name_faces
    JOIN encoding_faces
    ON name_faces.id = encoding_faces.facesname_id
    WHERE name_faces.name = %s
"""

cursors.execute(command, (named,))
data = cursors.fetchone()

# nilai = ("welowelo",)

# blobb = data[0]
# dencode = pickle.loads(blobb)

# for name, ncode in data:
#     encoding = pickle.loads(ncode)

#     name_faces.append(name)
#     encoding_faces.append(encoding)

if data:
    nama  = data[0]
    ncode = data[1]

    ubah = pickle.loads(ncode)

    print(nama)
    print(ubah)
else:
    print("gagal")



# print(name_faces, encoding_faces)
mysql.commit()
