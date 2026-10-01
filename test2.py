import cv2
import numpy as np
import os
import pickle
import face_recognition

# kamera = cv2.VideoCapture(0)

encoded = []
personnamed = []

# for namafile in os.listdir("test_encoding"):
source = face_recognition.load_image_file(f"./training/bajigurs.jpg")
coloring = cv2.cvtColor(source, cv2.COLOR_BGR2RGB)
encode = face_recognition.face_encodings(coloring)[0]
    # ubah_data = np.array(map(float, namafile))
    # with open(f"./test_encoding/{namafile}", "r") as file:
    #     isi = file.read()
    #     encode = np.fromstring(isi, sep=",")
    #     encoded.append(f"./test/{namafile}")

    # with open(f"./test_encoding/{namafile}", "rb") as file:
    #     encode = pickle.load(file)
encoded.append(encode)
# personnamed.append(os.path.splitext(namafile)[0])

print(encoded)