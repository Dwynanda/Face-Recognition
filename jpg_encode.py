import face_recognition
import pickle

name = "Musk" # <-- Insert file name

img = face_recognition.load_image_file(f"./img/{name}.jpg")
encode = face_recognition.face_encodings(img)

with open(f"./encoded_data/{name}.pkl", "wb") as file:
    sv = pickle.dump(encode, file)

with open(f"./person_name/{name}.txt", "w", encoding="utf-8") as file:
    file.write(name)

print("Success!")