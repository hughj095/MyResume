# This file makes a QR Code

import qrcode    

# text comment when hovering over qr code
data = 'Subscribe Here!'

# make QR Code
img = qrcode.make(data)
img.save('C:/Users/johnm/OneDrive/Desktop/MyResume/Python/Other Projects/qr_code.png')

# Add size, border, color, etc
qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
qr.add_data(data)
qr.make(fit=True)





