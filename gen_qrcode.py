import qrcode

# Create a QRCode object
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box
    border=4,  # Width of the border
)

# Add data to the QR code
qr.add_data("www.linkedin.com/in/yash-singhal-9a5068285")  # Replace with your URL or data
qr.make(fit=True)

# Create an image from the QRCode object
img = qr.make_image(fill_color="blue", back_color="white")

# Show the generated QR code image
img.show()
