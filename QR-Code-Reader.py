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


""" Generate a QR Code that contains the personal data stored in a text file. """

import qrcode

qr = qrcode.QRCode(
    version = 1, 
    error_correction = qrcode.constants.ERROR_CORRECT_L, 
    box_size = 10, 
    border = 4
    )
qr.add_data("Personal-Data.txt")
qr.make(fit = True)
img = qr.make_image(fill_color = "black", back_color = "maroon")
img.save("QRCode.png")


""" Reads the QR Code through web camera then displays the data stored in it. """

import cv2