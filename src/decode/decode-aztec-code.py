import cv2
import numpy as np
import zxing
import os

# File paths
image_path = "../../assets/given-image-05.jpg"
output_path = "../../assets/decoded/decoded_aztec.png"

def draw_bounding_box(image, points, text):
    """Draws a bounding box and text on the image."""
    try:
        points = np.array(points, dtype=np.int32).reshape((-1, 1, 2))
        cv2.polylines(image, [points], isClosed=True, color=(0, 255, 0), thickness=2)

        # Put decoded text near the bounding box
        x, y = points[0][0]
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    except Exception as e:
        print(f"Error drawing bounding box: {e}")

def decode_aztec(image_path, output_path):
    """Decodes Aztec code using ZXing and annotates the image."""
    if not os.path.exists(image_path):
        print(f"Error: File not found - {image_path}")
        return

    image = cv2.imread(image_path)
    reader = zxing.BarCodeReader()
    decoded = reader.decode(image_path)

    if decoded:
        print(f"Decoded Data: {decoded.parsed}")
        print(f"Format: {decoded.format}")

        if decoded.points:
            draw_bounding_box(image, decoded.points, decoded.parsed)

        # Save and show image
        os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Ensure directory exists
        cv2.imwrite(output_path, image)
        cv2.imshow("Aztec Code", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(f"Saved as {output_path}")
    else:
        print("Could not decode the Aztec code.")

# Run the function
decode_aztec(image_path, output_path)
