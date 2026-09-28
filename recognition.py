import cv2
import numpy as np
import face_recognition

kamera = cv2.VideoCapture(0)
sourc1 = face_recognition.load_image_file("./Training/yoeda.jpg")
sourc2 = face_recognition.load_image_file("./Training/musk.jpg")
sourc3 = face_recognition.load_image_file("./Training/awikwok.jpg")

sourc1 = cv2.cvtColor(sourc1, cv2.COLOR_BGR2RGB)

test1 = face_recognition.face_encodings(sourc3)[0]
yoeda = face_recognition.face_encodings(sourc1)[0]
musk = face_recognition.face_encodings(sourc2)[0]

raw_faces = [musk, yoeda]
muka_anjy = ["musk", "yoeda"]

while True:
    erat, frame = kamera.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    track = face_recognition.face_locations(grey)

    if track == []:
        pass
    else:
        realtime = face_recognition.face_encodings(grey)[0]
        compare = face_recognition.compare_faces(raw_faces, realtime)

        if True in compare:
            wajah_true = compare.index(True)
            nama = muka_anjy[wajah_true]
            for atas, kanan, bawah, kiri in track:
                cv2.rectangle(frame, (kiri, atas), (kanan, bawah), (0,0,255), 2)
                cv2.putText(frame, nama, (atas, kiri), (cv2.FONT_HERSHEY_COMPLEX), 0.8, (0,255,0), 2)

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