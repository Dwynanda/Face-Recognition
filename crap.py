import cv2
import face_recognition

kamera = cv2.VideoCapture(0)

## da file
gmbar = face_recognition.load_image_file("./training/yoeda.jpg")
gmbar2 = face_recognition.load_image_file("./training/musk2.jpg")
located = face_recognition.face_locations(gmbar)
koor = face_recognition.face_landmarks(gmbar)

## encoding
encod_left = face_recognition.face_encodings(gmbar)[0]
encod_right = face_recognition.face_encodings(gmbar2)[0]

hasil = face_recognition.compare_faces([encod_left], encod_right)

print(located)

# if not kamera.isOpened():
#     print("Eyoo kamera rusak")

# while True:
#     ret, frame = kamera.read()
#     greyshi = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     lokasi_muka = face_recognition.face_locations(greyshi)
#     for atas, kanan, bawah, kiri in lokasi_muka:
#         cv2.rectangle(frame, (kiri, atas), (kanan, bawah), (255,0,0), 2)

#     cv2.imshow("Ngaca!", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

