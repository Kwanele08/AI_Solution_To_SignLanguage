import cv2 #webcam
from cvzone.HandTrackingModule import HandDetector #to crop wherever hand ends
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
from TextToSpeech import TextToSpeech

cap=cv2.VideoCapture(0) #id of webcam
detector= HandDetector(maxHands=1) #only detects one hand
classifier = Classifier("Model/keras_model.h5","Model/labels.txt")

offset = 20
imgSize = 300

#to save image whenever we press s key
folder= "Data/C"
counter = 0

labels=["A", "B", "C", "D","E", "F", "H", "I","V","X", "Y", "PLEASE"]
while True:
    success, img= cap.read() #reads what the webcam is returning
    imgOutput =img.copy()
    hands, img= detector.findHands(img) #locates hands from the webcam
    if hands:  #if hands are visible
        hand=hands[0] #get the hand
        x, y, w, h=hand['bbox']   #get the hand width and height

        #create a matrix of fixed size so that the dimensions don't move around when we change hand signs
        imgWhite = np.ones((imgSize, imgSize,3), np.uint8)*255 #square size with colour 3 ,unsigned int from0 to 255
        imgCrop = img[y-offset:y+h+offset, x-offset:x+w+offset] #specify starting height,width and ending height and width, start:end

        imgCropShape = imgCrop.shape

        #if height is bigger, make width the same value and vice versa

        aspectRatio= h/w #value will be zero if width is bigger else 1

        if aspectRatio >1: #meaning height s bigger
            k = imgSize/h
            wCal = math.ceil(k*w) #new width rounded off
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))  #resize the cropped image
            imgResizeShape = imgResize.shape

            #to center the image
            wGap = math.ceil((imgSize-wCal)/2)
            imgWhite[:, wGap:wCal+wGap] = imgResize
            prediction ,index =classifier.getPrediction(imgWhite, draw=False)
            print(prediction,index)
            TextToSpeech(labels[index])



        else: #if width is greater than height
            k = imgSize / w
            hCal = math.ceil(k * h)  # new width rounded off
            imgResize = cv2.resize(imgCrop, (imgSize,hCal)) # resize the cropped image
            imgResizeShape = imgResize.shape

            # to center the image
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw=False)
            TextToSpeech(labels[index])

        cv2.rectangle(imgOutput, (x - offset, y - offset-50), (x - offset+ 90 ,y - offset-50+50), (255, 0, 255), cv2.FILLED)
        cv2.putText(imgOutput,labels[index],(x,y-26),cv2.FONT_HERSHEY_COMPLEX, 1.7,(255,255,255), 2)
        cv2.rectangle(imgOutput, (x-offset ,y -offset ), (x + w+offset , y + h+ offset), (255, 0, 255), 4)
        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image", imgOutput)
    cv2.waitKey(1) #delay
