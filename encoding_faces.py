import cv2
import face_recognition
# import mysql.connector
from pathlib import Path
import pickle
# import json

kamera = cv2.VideoCapture(0)
# tb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="face_recog"
# )

# cursors = tb.cursor()
nama_file = input("Masukkan nama : ")
path_image = f"./training/{nama_file}.jpg"

folder = Path("test_encoding")
file_loc = folder / f"{nama_file}.txt"

while True:
    ret, frame = kamera.read()
    coloring = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    key = cv2.waitKey(1) & 0xFF

    cv2.imshow("Kamera", frame)

    if key == ord('c'):
        cv2.imwrite(path_image, frame)
        
    if key == ord('q'):
        source_img = face_recognition.load_image_file(path_image)
        encode_wajah = face_recognition.face_encodings(source_img)
        # ubah_data = ",".join(map(str, encode_wajah))
        # file_loc.write_text(ubah_data, encoding="utf-8")
        with open(f"./test_encoding/{nama_file}.plk", "wb") as file:
            pickle.dump(encode_wajah, file)


        # lokasi_wajah = face_recognition.face_locations(source_img)
        # jason = json.dumps(encode_wajah[0].tolist())
        # command = ("INSERT INTO encoding_image (encoding) VALUES (%s)")
        # data_sql = (jason,)
        # cursors.execute(command, data_sql)
        # tb.commit()
        # print(encode_wajah, lokasi_wajah)
        break

# cursors.close()
# tb.close()