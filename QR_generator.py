import qrcode

data = ""

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)

qr.add_data(data)
qr.make()

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr.png")

print("QR generado: qr.png")