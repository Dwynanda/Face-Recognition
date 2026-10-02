import cv2
import face_recognition
from pathlib import Path
import pickle
import mysql.connector

kamera = cv2.VideoCapture(0)

nama_file = input("Masukkan nama : ")
path_image = f"./img/{nama_file}.jpg"

folder = Path("test_encoding")
file_loc = folder / f"{nama_file}.txt"

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "face_recog"
)

cursors = database.cursor()
command = "INSERT INTO encoding_image(encoding) VALUES (%s)"


while True:
    ret, frame = kamera.read()
    coloring = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    key = cv2.waitKey(1) & 0xFF

    cv2.imshow("Kamera", frame)

    if key == ord('c'):
        cv2.imwrite(path_image, frame)
        
    if key == ord('q'):
        source_img = face_recognition.load_image_file(path_image)
        encode_wajah = face_recognition.face_encodings(source_img)[0]
        # with open(f"./test_encoding/{nama_file}.pkl", "wb") as file:
        #     pickle.dump(encode_wajah, file)

        # with open(f"./person_name/{nama_file}.txt", "w", encoding="utf-8") as file:
        #     file.write(nama_file)
        data_bytes = pickle.dumps(encode_wajah)
        value = (data_bytes,)
        cursors.execute(command, value)
        database.commit()

        print("Success!")
        break