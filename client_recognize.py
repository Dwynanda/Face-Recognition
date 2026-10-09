import requests
import cv2
import face_recognition

url = "http://192.168.50.10:8000/recognize"
# img = "./img/Musk.jpg"

# with open(img, "rb") as file:
#     response = requests.post(url, files={"file":file})

# print(response.status_code)
# print(response.json())

kamera = cv2.VideoCapture(0)
koordinat = []


while True:
    ret, frame = kamera.read()
    ret, numerik = cv2.imencode(".jpg", frame)
    response =  requests.post(url, files={"file": ("frame.jpg", numerik.tobytes(), "image/jpg")})
    resize = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    grey = cv2.cvtColor(resize, cv2.COLOR_BGR2RGB)
    posisi_wajah = face_recognition.face_locations(grey)
    koordinat.append(posisi_wajah)

    hasil_response = response.json()
    faces = hasil_response["output"]
    for face in faces:
        pesan = face["pesan"]
        person_name = face["person"]
        atas, kanan, bawah, kiri = face["box"]
        if not person_name:
            person_name = ""
        else:
            if pesan == "Correct!":
                text_color = 0,255,0
            else:
                text_color = 0,0,255

        if koordinat == []:
            pass
        else:
            cv2.rectangle(frame, (kiri, atas), (kanan, bawah), (255,0,0), 2)
            cv2.putText(frame, person_name, (kiri, atas - 10), (cv2.FONT_HERSHEY_PLAIN), 1, (text_color), 2)

    cv2.imshow("Detect!", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break