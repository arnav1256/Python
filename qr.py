import qrcode
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=50, border=1)
qr.add_data('https://www.youtube.com/watch/dQw4w9WgXcQ')
qr.make(fit=True)
img = qr.make_image(fill_colour='black', back_colour='white')
img.save('qr.png')