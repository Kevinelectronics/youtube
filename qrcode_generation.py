import qrcode
# Create a QR code object with custom settings
from qrcode.image.svg import SvgImage

def generate_custom_qr(data, file_name="custom_qr.png"):
    # Configurar el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Agregar datos al código QR
    qr.add_data(data)
    qr.make(fit=True)
    
    # Crear una imagen del código QR
    img = qr.make_image(fill='black', back_color='white')
    
    # Guardar la imagen
    img.save(file_name)
    print(f"Código QR guardado como {file_name}")

# Usar la función con la URL de LinkedIn
generate_custom_qr("https://www.linkedin.com/in/kevin-meneses-897a28127/")



def generate_qr_svg(url, file_name="qrcode.svg"):
    # Configurar el generador de SVG
    factory = SvgImage

    # Crear el QR code
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url)
    qr.make(fit=True)

    # Guardar como archivo SVG
    img = qr.make_image(image_factory=factory)
    img.save(file_name)
    print(f"Código QR guardado como {file_name}")

# Usar la función con la URL del canal de YouTube
generate_qr_svg("https://www.youtube.com/channel/UC8B7LR70zfRE1zbESFkyyzQ?sub_confirmation=1")


