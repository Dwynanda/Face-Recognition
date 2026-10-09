from  fastapi import FastAPI, UploadFile, File
import numpy as np
import cv2
import pickle
import face_recognition
import mysql.connector

app = FastAPI()
encoded_list = []
name_list = []

database = mysql.connector.connect(
	host = "localhost",
	user = "python",
	password = "dwinandayuda",
	database = "face_recognition"
)

command = """
	SELECT faces_name.person_name, encoding_faces.encoding
	FROM faces_name
	JOIN encoding_faces
	ON faces_name.id = encoding_faces.facesname_id
"""

cursors = database.cursor()
cursors.execute(command)
data = cursors.fetchall()

for person_name, ncode in data:
	convert = pickle.loads(ncode)
	encoded_list.append(convert)
	name_list.append(person_name)


@app.get("/")
def home():
	return{"pesan": "Server aktif!"}

@app.post("/recognize")
async def recognize(file: UploadFile = File(...)):
	image = await file.read()
	array = np.frombuffer(image, dtype=np.uint8)
	image_fix = cv2.imdecode(array, cv2.IMREAD_COLOR)

	frame = image_fix

	resize = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
	grey = cv2.cvtColor(resize, cv2.COLOR_BGR2RGB)
	track = face_recognition.face_locations(grey)

	hasil = []
	if track == []:
		return{"output": ""}
	else:
		img_encode = face_recognition.face_encodings(grey, track)

		for (atas, kanan, bawah, kiri), posisi in zip(track, img_encode):
			compare = face_recognition.compare_faces(encoded_list, posisi)
			if True in compare:
				true_face = compare.index(True)
				name = name_list[true_face]
				pesan = "Correct!"

			else:
				name = "Unknown"
				pesan = "Tidak Cocok"

			hasil.append({"pesan": pesan, "person": name, "box": [atas*4, kanan*4, bawah*4, kiri*4]})

		return{"output": hasil}
