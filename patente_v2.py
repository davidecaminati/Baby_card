# how to use
# hit [1] to fix the image
# if ok press [q] otherwise press again [1] to repeat

# import the necessary packages
from pyimagesearch.facedetector import FaceDetector
from pyimagesearch import imutils
import argparse
import cv2
import numpy as np

#variables
cx = 0
cy = 0
larghezza_foto = 85
blank_image_raw = np.zeros((larghezza_foto,larghezza_foto), np.uint8)
blank_image = cv2.cvtColor(blank_image_raw, cv2.COLOR_GRAY2BGR)
proportional_w = 10
proportional_h = 8
offset_constant = 2.5

# construct the face detector
fd = FaceDetector("cascades/haarcascade_frontalface_default.xml")

# open video capture
camera = cv2.VideoCapture(0)

#load demo_image
image_patente = cv2.imread("patente-fronte.png")

#think on use tag for place text and picture in demo_image

# merge image with text
font = cv2.FONT_HERSHEY_SIMPLEX # abbastanza buono
cv2.putText(image_patente,'PIPPO',(130,40), font, 0.4,(0,0,0),1,16)
cv2.putText(image_patente,'PAPERINO',(130,55), font, 0.4,(0,0,0),1,16)
cv2.putText(image_patente,'08/07/97  Forli  (FC)',(130,72), font, 0.3,(0,0,0),1,16)
cv2.putText(image_patente,'03/02/1995       MIT-UCO',(130,89), font, 0.3,(0,0,0),1,16)
cv2.putText(image_patente,'03/02/2025',(130,105), font, 0.4,(0,0,0),1,16)
cv2.putText(image_patente,'X000000000X',(130,120), font, 0.4,(0,0,0),1,16)

# keep looping
while True:
	while True:
		# grab the current frame
		(grabbed, frame) = camera.read()

		# if we are viewing a video and we did not grab a
		# frame, then we have reached the end of the video
		if not grabbed:
			break

		# resize the frame and convert it to grayscale
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# detect faces in the image and then clone the frame
		# so that we can draw on it
		faceRects = fd.detect(gray, scaleFactor = 1.3, minNeighbors = 5,minSize = (100, 100))
		frameClone = frame.copy()
		face = []
		# loop over the face bounding boxes and draw them
		for (fX, fY, fW, fH) in faceRects:
			try:
				#find centroid of the rectangle
				cx = fX + int(fW/2)
				cy = fY + int(fH/2)
				fX -= int(fX/10*offset_constant)
				fY -= int(fY/10*offset_constant)
				fW += int(int(fX/10)*offset_constant) * 2

				face = frameClone[fY:fY+int((fW*proportional_w)/proportional_h),fX:fX+fW]
				#resize
				face_resized = imutils.resize(face, width = larghezza_foto)
				blank_image = face_resized
			except:
				pass
		#merge
		(h, w) = blank_image.shape[:2]
		image_patente[65:int(65+h), 19:int(19+w)] = blank_image
		#show
		cv2.imshow("LIVE", image_patente)

		# if the '1' key is pressed, stop the loop
		c = cv2.waitKey(1)
		if '1' == chr(c & 255):
			cv2.destroyWindow("LIVE")
			break

	cv2.imshow("SELECTED", image_patente)
	c = cv2.waitKey(0)
	cv2.destroyWindow("SELECTED")
	if 'q' == chr(c & 255):
		break

#----NOTE----
# texting
#font = cv2.FONT_HERSHEY_PLAIN  # molto sottile
#font = cv2.FONT_HERSHEY_SIMPLEX # abbastanza buono
#font = cv2.FONT_HERSHEY_SIMPLEX   # sottile
#font = cv2.FONT_HERSHEY_PLAIN   # sottile
#font = cv2.FONT_HERSHEY_DUPLEX   # doppio segno
#font = cv2.FONT_HERSHEY_COMPLEX   # sottile
#font = cv2.FONT_HERSHEY_TRIPLEX   # sottile
#font = cv2.FONT_HERSHEY_COMPLEX_SMALL   # sottile
#font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX    # 

#cv2.LINE_AA = 16
#cv2.putText(image_patente,'OpenCV',(10,50), font, 4,(255,255,255),2,cv2.LINE_AA)

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
