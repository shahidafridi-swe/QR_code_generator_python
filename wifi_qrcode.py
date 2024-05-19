import qrcode
from PIL import Image, ImageDraw

# Create QR Code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=8,  # Larger box size for better visibility
    border=4
)

# Add data to the QR Code
qr.add_data("WIFI:T:WPA;S:MARUF_SUPER_HOSTEL;P:maruf404;;")
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")  # Custom colors

# Open the logo image
logo = Image.open("afridi.png")
logo = logo.convert("RGBA")

# Calculate the size of the QR code and the logo
qr_width, qr_height = img.size
logo_size = qr_width // 3  # Adjust size of the logo relative to the QR code

# Resize the logo
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

# Create a circular mask for the logo
mask = Image.new("L", (logo_size, logo_size), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, logo_size, logo_size), fill=255)

# Apply the circular mask to the logo
circular_logo = Image.new("RGBA", (logo_size, logo_size))
circular_logo.paste(logo, (0, 0), mask)

# Calculate the position to place the logo
logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

# Paste the circular logo onto the QR code
img.paste(circular_logo, logo_pos, mask=circular_logo)

# Save the image to a file
img.save("custom_shahid_fb10.jpg")

print("QR code with circular logo saved as custom_shahid_fb1.jpg")
