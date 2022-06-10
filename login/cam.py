from imutils.video import VideoStream
from imutils.video import FPS
from os import listdir
from os.path import isfile, join
import imutils
import cv2, os, urllib.request, pickle
import numpy as np
from django.conf import settings


class FaceDetect(object):
    def __init__(self):
        # extract_embeddings.embeddings()
        # train_model.model_train()
        # initialize the video stream, then allow the camera sensor to warm up
        self.vs = VideoStream(src=0).start()
        # start the FPS throughput estimator
        self.fps = FPS().start()

    def __del__(self):
        self.vs.stop()

    def get_frame(self):
        # grab the frame from the threaded video stream
        frame = self.vs.read()
        frame = cv2.flip(frame, 1)

        # resize the frame to have a width of 600 pixels (while
        # maintaining the aspect ratio), and then grab the image
        # dimensions
        frame = imutils.resize(frame, width=600)



        # update the FPS counter
        self.fps.update()
        ret, jpeg = cv2.imencode('.jpg', frame)
        return frame,jpeg.tobytes()
