from zxing import BarCodeReader

# Initialize the barcode reader
reader = BarCodeReader()

# Path to the barcode image
image_path = "../../assets/given-image-01.jpg"

# Decode the barcode from the image
barcode = reader.decode(image_path)

# Print the barcode data
if barcode:
    print("Decoded Barcode Data:")
    print(barcode)
else:
    print("No barcode detected or failed to decode.")
