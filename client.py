import cv2,socket,pickle,os
import numpy as np
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,1000000)
server_ip = "192.168.1.5"
server_port = 6666

cap = cv2.VideoCapture(-1)
while True:
	ret,photo = cap.read()
	cv2.imshow('streaming',photo)
	ret,buffer = cv2.imencode(".jpg",photo,[int(cv2.IMWRITE_JPEG_QUALITY),30])
	x_as_bytes = pickle.dumps(buffer)
	s.sendto((x_as_bytes),(server_ip,server_port))
	if cv2.waitKey(10)==13:
		break
cv2.destroyAllWindows()
cap.release()
