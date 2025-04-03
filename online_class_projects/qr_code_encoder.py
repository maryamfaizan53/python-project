import qrcode

# Data to encode
data = "https://www.example.com"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # Version of the QR code (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in pixels
    border=4  # Border size in boxes
)

# Add data to QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill="black", back_color="white")

# Save the QR code as an image file
img.save("qr_code.png")

# Show the generated QR code
img.show()
