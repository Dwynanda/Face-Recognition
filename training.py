from fastapi import FastAPI, UploadFile, File
import face_recognition
import numpy as np
import mysql.connector

app = FastAPI()

database = mysql.connector.connect(
	host = "localhost",
	user = "yuda"
	password = "dwinandayuda"
	database = "face_recognition"
)

command1 = "INSERT INTO faces_name(name) VALUES(%s)"
command2 = "INSER INTO encoding_faces(encoding) VALUES(%s)"
cursors.execute(command1, (file_name,))
name_id = cursors.lastrowid
cursors.execute(command2, (name_id, ))

cursors = database.cursor()

