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


""" Generate QR Code that contains the personal data stored in a text file. """

# import qrcode library
import qrcode

# open and read the text file
with open('Personal-Data.txt') as personalData:
    data = personalData.read()

# generate QR code
QRCode = qrcode.make(data)
QRCode.save('QRCode.jpg')