import qrcode 
from PIL import Image
import qrcode.constants


qr = qrcode.QRCode(version=1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 5,
                   border = 5)
qr.add_data("https://www.facebook.com/shahidafridi.swe/")
qr.make(fit = True) 
img = qr.make_image(fill_color='black',back_color='green')
img.save("shahid_fb.jpg")

