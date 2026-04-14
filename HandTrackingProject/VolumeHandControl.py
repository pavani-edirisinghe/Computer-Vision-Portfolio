import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from pycaw.pycaw import AudioUtilities

#########################
wCam, hCam = 640, 480
##########################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)


device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume
print(f"Audio output: {device.FriendlyName}")
print(f"- Muted: {bool(volume.GetMute())}")
print(f"- Volume level: {volume.GetMasterVolumeLevel()} dB")
print(f"- Volume range: {volume.GetVolumeRange()[0]} dB - {volume.GetVolumeRange()[1]} dB")
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findHands(img)

    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # print(lmList[4],lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1,y1), 8, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2,y2), 8, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
        cv2.circle(img, (cx,cy), 8, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)
        print(length)

        # Hand range 20-170
        # Volume range -65 - 0

        vol = np.interp(length, [20,170], [minVol, maxVol])
        volBar = np.interp(length, [20, 170], [400, 150])
        volPer = np.interp(length, [20, 170], [0, 100])
        print(int(length),vol)
        volume.SetMasterVolumeLevel(vol, None)


        if length<50:
            cv2.circle(img, (cx, cy), 8, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img,(50,150), (85,400),(255,0,0),3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (30, 450), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS{int(fps)}', (30,40), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)

    cv2.imshow("Video", img)

    cv2.waitKey(1)