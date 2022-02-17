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

# import qrcode library
import qrcode

# define a function that will generate QR Code
def generateQR ():
    # open the text file containing the personal data
    with open('Personal-Data.txt') as file:
        personal_data = file.read()
        # customizes the QR code
        qr = qrcode.QRCode(
            version = 1, # create a 21x21 matrix QR code
            error_correction = qrcode.constants.ERROR_CORRECT_L, # controls the error correction up to 7% used for the QR code
            box_size = 10, # controls the number of pixels in each box of the QR code
            border = 4) # controls the thickness of the border
        qr.add_data(personal_data) # stores data in the QR code
        qr.make(fit = True)
        QRCode = qr.make_image(fill_color = "black", back_color = "brown") # customizes the color of the QR code
        QRCode.save('QRCode.png') # generates the QR code

# call the function to generate QR Code
generateQR()