# Import Library
import cv2
# Name of the QR Code Image file
filename = "site.png"
# read the QRCODE image
image = cv2.imread(filename)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
# detect and decode
data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
# if there is a QR code
# print the data
if vertices_array is not None:
  print("QRCode data:")
  print(data)
else:
  print("There was some error")