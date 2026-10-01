import face_recognition
import pickle

name = "musk2"
img = face_recognition.load_image_file(f"./training/{name}.jpg")
encode = face_recognition.face_encodings(img)

with open(f"./test_encoding/{name}.plk", "wb") as file:
    sv = pickle.dump(encode, file)