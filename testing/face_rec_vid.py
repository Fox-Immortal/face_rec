import cv2
import sys
import face_recognition

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
face_locations = []
while True:
	ret, frame = cap.read()
	img = frame[:, :, ::-1]
	face_locations = face_recognition.face_locations(img)

	for (x, y, w, h) in face_locations:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

	cv2.imshow("Webcame", frame)
	cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
