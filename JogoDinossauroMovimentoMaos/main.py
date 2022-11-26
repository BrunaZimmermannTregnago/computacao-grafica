import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

video = cv2.VideoCapture(0)

video.set(3, 1280)
video.set(4, 720)

kb = Controller()

detector = HandDetector(detectionCon=0.8)

while True:
    _, img = video.read()
    hands, img = detector.findHands(img)

    if hands:
        estado = detector.fingersUp(hands[0])
        print(estado)
        print(hands[0]['type'])
        if hands[0]['type'] == 'Right' and estado == [0, 0, 0, 0, 0]:
            print('pular')
            kb.press(Key.up)
            kb.release(Key.up)

        if hands[0]['type'] == 'Left' and estado == [0, 0, 0, 0, 0]:
            print('abaixar')
            kb.press(Key.down)
            kb.release(Key.down)

    cv2.imshow('img', cv2.resize(img, (300, 250)))
    cv2.waitKey(1)