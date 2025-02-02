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
        # Convert the points to numpy array and reshape it for polylines
        points = np.array(points, dtype=np.int32).reshape((-1, 1, 2))

        # Draw the bounding polygon (Aztec code area)
        cv2.polylines(image, [points], isClosed=True, color=(0, 255, 0), thickness=2)

        # Put the decoded text above the bounding box
        x, y = points[0][0]
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    except Exception as e:
        print(f"Error drawing bounding box: {e}")


def decode_aztec(image_path, output_path):
    """Decodes Aztec code using ZXing and annotates the image."""
    # Check if the image file exists
    if not os.path.exists(image_path):
        print(f"Error: File not found - {image_path}")
        return

    # Read the image
    image = cv2.imread(image_path)

    # Initialize ZXing barcode reader
    reader = zxing.BarCodeReader()

    # Decode the image to get the Aztec code information
    decoded = reader.decode(image_path)

    if decoded:
        print(f"Decoded Data: {decoded.parsed}")
        print(f"Format: {decoded.format}")

        # If bounding points are found, annotate the image
        if decoded.points:
            draw_bounding_box(image, decoded.points, decoded.parsed)

        # Ensure directory exists for output file
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Save the annotated image
        cv2.imwrite(output_path, image)
        print(f"Annotated image saved as {output_path}")

        # Display the annotated image
        cv2.imshow("Aztec Code", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print("Could not decode the Aztec code.")


# Run the function
decode_aztec(image_path, output_path)
