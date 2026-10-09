import face_recognition
import pickle
import mysql.connector

name = "Musk" # <-- Insert file name

img = face_recognition.load_image_file(f"./img/{name}.jpg")
encode = face_recognition.face_encodings(img)[0]

# with open(f"./encoded_data/{name}.pkl", "wb") as file:
#     sv = pickle.dump(encode, file)

# with open(f"./person_name/{name}.txt", "w", encoding="utf-8") as file:
#     file.write(name)

database = mysql.connector.connect(
    host = "192.168.50.10",
    user = "yuda",
    password = "dwinandayuda",
    database = "face_recognition"
)

cursors = database.cursor()
command1 = "INSERT INTO faces_name(person_name) VALUES (%s)"
cursors.execute(command1, (name,))
name_id = cursors.lastrowid

command2 = "INSERT INTO encoding_faces(facesname_id, encoding) VALUES (%s, %s)"
data_bytes = pickle.dumps(encode)
cursors.execute(command2, (name_id, data_bytes))
database.commit()


print("Success!")