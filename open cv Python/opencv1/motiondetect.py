import cv2

import pandas
import time

from datetime import datetime

firstframe = None
status_list = [None, None]
times = []
df = pandas.DataFrame(columns=["start", "end"])

video = cv2.VideoCapture(0)
while True:
    check, frame = video.read()
    statuc = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    cv2.imshow("Captured", gray)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    if firstframe is None:
        firstframe = gray
        continue
    delta = cv2.absdiff(firstframe, gray)
    thresh = cv2.threshold(delta, 30, 255, cv2.THRESH_BINARY)[1]

    thresh = cv2.dilate(thresh, None, iterations=0)
    
    (_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
    cv2.imshow('frame', frame)
    cv2.imshow('capturing', gray)
    cv2.imshow('delta', delta)
    cv2.imshow('threshold', thresh)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
