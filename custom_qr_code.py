import qrcode
from PIL import Image

# Create QR Code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,  # Larger box size for better visibility
    border=4
)

# Add data to the QR Code
qr.add_data("https://www.facebook.com/shahidafridi.swe/")
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")  # Custom colors

# Open the logo image
logo = Image.open("logo.png")
logo = logo.convert("RGBA")

# Calculate the size of the QR code and the logo
qr_width, qr_height = img.size
logo_size = qr_width // 3  # Adjust size of the logo relative to the QR code

# Resize the logo
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

# Calculate the position to place the logo
logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

# Paste the logo image onto the QR code
img.paste(logo, logo_pos, mask=logo)

# Save the image to a file
img.save("custom_shahid_fb1.jpg")
