import cv2
import face_recognition
import numpy as np
import os
import pickle
import mysql.connector

kamera = cv2.VideoCapture(0)
list_name = []

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "face_recog"
)

while True:
    nama = input("Masukkan nama : ")

    for person in os.listdir("person_name"):
        list_name.append(os.path.splitext(person)[0])

    if nama in list_name:
        # with open(f"./encoded_data/{nama}.pkl", "rb") as file:
        #     encoded = pickle.load(file)
        encoded = pickle.loads()
        break
    else:
        print("Try Again!")

source = encoded[0]

while True:
    detik, frame = kamera.read()
    ubah = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    lokasi_muka = face_recognition.face_locations(ubah)
    for atas, kanan, bawah, kiri in lokasi_muka:
        cv2.rectangle(frame, (kiri, atas), (kanan, bawah), (0,255,0), 2)

    ##encode
    if face_recognition.face_locations(ubah) == []:
        pass
    else:
        realtime = face_recognition.face_encodings(ubah)[0]
        hasil_encode = face_recognition.compare_faces([source], realtime)
        if hasil_encode == np.True_:
            print("Berhasil!")
            
        else:
            print("Tidak Cocok")

    cv2.imshow("Ngaca!", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break