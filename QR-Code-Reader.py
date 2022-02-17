# Contact Tracing App
# 	- Create a python program that will read QRCode using your webcam
# 	- You may use any online QRCode generator to create QRCode
# 	- All personal data are in QRCode 
# 	- You may decide which personal data to include
# 	- All data read from QRCode should be stored in a text file including the date and time it was read

# Note: 
# 	- Search how to generate QRCode
# 	- Search how to read QRCode using webcam
# 	- Search how to create and write to text file
# 	- Your source code should be in github before Feb 19
# 	- Create a demo of your program (1-2 min) and send it directly to my messenger.

""" Reads the QR Code through web camera then displays the data stored in it. """

import cv2; from pyzbar import pyzbar; from datetime import *

def readQR ():
    capture = cv2.VideoCapture(0)
    while True:
        _, image = capture.read()
        image = decodeQR(cv2.resize(image, None, fx = 1.0, fy = 1.0, interpolation = cv2.INTER_AREA))
        cv2.imshow("QR Code Scanner", image)
        if cv2.waitKey(1) == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()

def decodeQR (image):
    qrCode = pyzbar.decode(image)
    for details in qrCode:
        qrData = details.data.decode('utf-8')
        with open ("QR-Code-Result.txt", "w") as textfile:
            textfile.write(qrData)
    return image

readQR()