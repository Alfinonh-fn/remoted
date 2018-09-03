import cv2
from client import *

face_cascade = cv2.CascadeClassifier('/usr/local/lib/python2.7/dist-packages/cv2/data/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('/usr/local/lib/python2.7/dist-packages/cv2/data/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
client = Client('081228924701','[pesawat]')
while True:
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		print "danger !!!"
		cv2.imwrite('/root/AL/adaorang.jpg',frame)
		client.sendLocalImage("/root/AL/adaorang.jpg", thread_id=100022394016980, thread_type=ThreadType.USER)
		cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color= frame[y:y+h, x:x+w]

		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,0,255), 2)

	cv2.imshow("mata fbssh", frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
