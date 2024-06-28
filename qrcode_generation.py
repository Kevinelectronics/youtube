import qrcode
# Create a QR code object with custom settings
qr = qrcode.QRCode(
 version=1,
 error_correction=qrcode.constants.ERROR_CORRECT_L,
 box_size=10,
 border=4,
)
# Add data to the QR code
data = "https://finviz.com/"
qr.add_data(data)
qr.make(fit=True)
# Create an image from the QR code instance
img = qr.make_image(fill='black', back_color='white')
# Save the image
img.save("custom_qr.png")