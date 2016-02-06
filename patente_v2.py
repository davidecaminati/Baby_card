# USAGE
# python cam.py --face cascades/haarcascade_frontalface_default.xml
# python cam.py --face cascades/haarcascade_frontalface_default.xml --video video/adrian_face.mov

# import the necessary packages
from pyimagesearch.facedetector import FaceDetector
from pyimagesearch import imutils
import argparse
import cv2
import numpy as np


cx = 0
cy = 0
larghezza_foto = 85
blank_image_raw = np.zeros((larghezza_foto,larghezza_foto), np.uint8)
blank_image = cv2.cvtColor(blank_image_raw, cv2.COLOR_GRAY2BGR)
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help = "path to the (optional) video file")
args = vars(ap.parse_args())

# construct the face detector
fd = FaceDetector("cascades/haarcascade_frontalface_default.xml")

# if a video path was not supplied, grab the reference
# to the gray
if not args.get("video", False):
	camera = cv2.VideoCapture(0)

# otherwise, load the video
else:
	camera = cv2.VideoCapture(args["video"])

# keep looping
while True:
	# grab the current frame
	(grabbed, frame) = camera.read()

	# if we are viewing a video and we did not grab a
	# frame, then we have reached the end of the video
	if args.get("video") and not grabbed:
		break

	# resize the frame and convert it to grayscale
	#frame = imutils.resize(frame, width = 300)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# detect faces in the image and then clone the frame
	# so that we can draw on it
	faceRects = fd.detect(gray, scaleFactor = 1.3, minNeighbors = 5,
		minSize = (100, 100))
	frameClone = frame.copy()
	volto = []
	# loop over the face bounding boxes and draw them
	for (fX, fY, fW, fH) in faceRects:
		try:
			#find centroid of the rectangle

			constant = 2.5
			cx = fX + int(fW/2)
			cy = fY + int(fH/2)
			fX -= int(fX/10*constant)
			fY -= int(fY/10*constant)
			fW += int(int(fX/10)*constant) * 2
			#fH += int(int(fY/10)*constant) * 2

			#cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + int((fW*10)/8)), (0, 255, 0), 2)		
			#cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH), (0, 255, 0), 2)
			
			volto = frameClone[fY:fY+int((fW*10)/8),fX:fX+fW]
			#volto = frameClone[fY:fY+fH,fX:fX+fW]
			#resize
			volto_resize = imutils.resize(volto, width = larghezza_foto)
			blank_image = volto_resize
			cv2.imshow("Volto", blank_image)
		except:
			pass
	# show our detected faces
	cv2.imshow("Face", frameClone)

	# if the 'q' key is pressed, stop the loop
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break
# apertura foto
#image_patente = cv2.imread("patente-fronte.png")
#cv2.imshow("Original", image_patente)
#cv2.waitKey(0)

#merge
image_patente = cv2.imread("patente-fronte.png")
#faccia = image_patente[10:100, 100:180]
(h, w) = blank_image.shape[:2]
#debug
print h
print w
image_patente[65:int(65+h), 19:int(19+w)] = blank_image
# texting
#font = cv2.FONT_HERSHEY_PLAIN  # molto sottile
font = cv2.FONT_HERSHEY_SIMPLEX # abbastanza buono
#font = cv2.FONT_HERSHEY_SIMPLEX   # sottile
#font = cv2.FONT_HERSHEY_PLAIN   # sottile
#font = cv2.FONT_HERSHEY_DUPLEX   # doppio segno
#font = cv2.FONT_HERSHEY_COMPLEX   # sottile
#font = cv2.FONT_HERSHEY_TRIPLEX   # sottile
#font = cv2.FONT_HERSHEY_COMPLEX_SMALL   # sottile
#font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX    # 

cv2.putText(image_patente,'CAMINATI',(190,40), font, 0.4,(0,0,0),1)
cv2.putText(image_patente,'DAVIDE',(190,55), font, 0.4,(0,0,0),1)
#cv2.putText(image_patente,'OpenCV',(10,50), font, 4,(255,255,255),2,cv2.LINE_AA)

#show

cv2.imshow("Merged", image_patente)
cv2.waitKey(0)

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
