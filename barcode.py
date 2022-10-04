import qrcode

img = qrcode.make('1')
img.save('bar.jpg')
