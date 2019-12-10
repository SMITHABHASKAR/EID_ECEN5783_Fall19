from qrcode import *
import qrcode.image.pil
from PIL import Image
import PIL

qr = QRCode(version = 4, box_size=5, border=0, error_correction=ERROR_CORRECT_L)
qr.add_data("test")
qr.make()

qr.make(fit=True)
im = qr.make_image(qrcode.image.pil.PilImage)

width = 128
height = 128
im = im.resize((width, height), Image.ANTIALIAS)

ext = ".bmp"
im.save("output" + ext)