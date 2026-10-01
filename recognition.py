import cv2
import numpy as np
import os
import pickle
import face_recognition

kamera = cv2.VideoCapture(0)

encoded = []
personnamed = []

for namafile in os.listdir("encoded_data"):
    with open(f"./encoded_data/{namafile}", "rb") as file:
        encode = pickle.load(file)

    encoded.append(encode[0])
    personnamed.append(os.path.splitext(namafile)[0])

while True:
    erat, frame = kamera.read()
    resize = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    grey = cv2.cvtColor(resize, cv2.COLOR_BGR2RGB)
    track = face_recognition.face_locations(grey)

    if track == []:
        pass
    else:
        realtime = face_recognition.face_encodings(grey, track)
        
        for (atas, kanan, bawah, kiri), posisi in zip(track, realtime):
            compare = face_recognition.compare_faces(encoded, posisi)
            if True in compare:
                wajah_true = compare.index(True)
                nama = personnamed[wajah_true]
            else:
                nama = "Unknown"

            named = nama
            atas *= 4
            kanan *= 4
            bawah *= 4
            kiri *= 4
            cv2.rectangle(frame, (kiri, atas), (kanan, bawah), (255,0,0), 2)
            cv2.putText(frame, named, (kiri, atas - 10), (cv2.FONT_HERSHEY_COMPLEX), 0.5, (0,255,0), 1)

    cv2.imshow("Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break