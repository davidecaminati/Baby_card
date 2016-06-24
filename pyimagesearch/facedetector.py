# original source code from
# http://www.pyimagesearch.com


# import the necessary packages
import cv2

class FaceDetector:
	def __init__(self, faceCascadePath):
		# load the face detector
		self.faceCascade = cv2.CascadeClassifier(faceCascadePath)

	def detect(self, image, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30)):
		# detect faces in the image
		rects = self.faceCascade.detectMultiScale(image,
			scaleFactor = scaleFactor, minNeighbors = minNeighbors,
			minSize = minSize, flags = cv2.CASCADE_SCALE_IMAGE)

		# return the rectangles representing boundinb
		# boxes around the faces
		return rects


# note
# the cv2.cv submodule got removed in opencv3.0, also some constants were changed.
# please use cv2.CASCADE_SCALE_IMAGE instead
# (do a help(cv2) to see the updated constants)
