import cv2
import face_recognition
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    nama = input("Insert your'e name : ")
    if nama == "Yuda":
        sourcy = face_recognition.load_image_file("./training/yoeda.jpg")
        break
    elif nama == "Musk":
        sourcy = face_recognition.load_image_file("./training/musk.jpg")
        break
    else:
        print("Try Again!")

lokasi_img = cv2.cvtColor(sourcy, cv2.COLOR_BGR2RGB)
source = face_recognition.face_encodings(lokasi_img)[0]

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
        hasil_encode = face_recognition.compare_faces([realtime], source)
        if hasil_encode == np.True_:
            print("Berhasil!")
            
        else:
            print("Tidak Cocok")

    cv2.imshow("Ngaca!", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break