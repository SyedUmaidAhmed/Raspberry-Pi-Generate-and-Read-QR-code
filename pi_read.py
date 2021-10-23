from PIL import Image
from pyzbar.pyzbar import decode
data = decode(Image.open('site.png'))
print(data[0])