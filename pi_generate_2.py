# Importing libraries
import qrcode
import numpy as np
# Data which for you want to make QR code
# Here we are using URL of MakeUseOf website
data = "https://github.com/SyedUmaidAhmed"
# Name of the QR code Image file
QRCodefile = "CustomisedImgBoxQRCode.png"
# instantiate QRCode object
qrObject = qrcode.QRCode(version=1, box_size=12)
# add data to the QR code
qrObject.add_data(data)
# compile the data into a QR code array
qrObject.make()
image = qrObject.make_image()
image.save(QRCodefile)
# print the image size (version)
print("Size of the QR image(Version):")
print(np.array(qrObject.get_matrix()).shape)