import qrcode as qr

img = qr.make("https://www.facebook.com/photo/?fbid=3713399105561367&set=a.1396172790617355")
img.save('shahid.png')
