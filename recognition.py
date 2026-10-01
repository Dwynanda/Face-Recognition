import cv2
import numpy as np
import os
import pickle
import face_recognition

kamera = cv2.VideoCapture(0)

encoded = []
personnamed = []

for namafile in os.listdir("test_encoding"):
    # source = face_recognition.load_image_file(f"./training/{namafile}")
    # coloring = cv2.cvtColor(source, cv2.COLOR_BGR2RGB)
    # encode = face_recognition.face_encodings(coloring)[0]
    # ubah_data = np.array(map(float, namafile))
    # with open(f"./test_encoding/{namafile}", "r") as file:
    #     isi = file.read()
    #     encode = np.fromstring(isi, sep=",")
    #     encoded.append(f"./test/{namafile}")

    with open(f"./test_encoding/{namafile}", "rb") as file:
        encode = pickle.load(file)
    encoded.append(encode[0])
    personnamed.append(os.path.splitext(namafile)[0])

# sourc1 = face_recognition.load_image_file("./Training/yoeda.jpg")
# sourc2 = face_recognition.load_image_file("./Training/musk.jpg")
# sourc3 = face_recognition.load_image_file("./Training/awikwok.jpg")

# sourc1 = cv2.cvtColor(sourc1, cv2.COLOR_BGR2RGB)

# test1 = face_recognition.face_encodings(sourc3)[0]
# yoeda = face_recognition.face_encodings(sourc1)[0]
# musk = face_recognition.face_encodings(sourc2)[0]

# raw_faces = [musk, yoeda]
# muka_anjy = ["musk", "yoeda"]

# lokasi_muka = face_recognition.face_locations(sourc1)

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
            

    # if face_recognition.face_locations(ubah) == []:
    #     pass
    # else:
    #     hasil_encode = face_recognition.compare_faces([realtime], source)
    #     if hasil_encode == np.True_:
    #         print("Berhasil!")
            
    #     else:
    #         print("Tidak Cocok")

    cv2.imshow("Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# test = face_recognition.face_distance([test1], musk)
# print(test)

##koor = face_recognition.