from pylibdmtx.pylibdmtx import decode
import cv2
import numpy as np

# Load the image in grayscale
image_path = "../../assets/given-image-02.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Decode the DataMatrix code from the image with a timeout of 500ms
decoded_objects = decode(image, timeout=500)

# Check if any objects were decoded
if decoded_objects:
    for obj in decoded_objects:
        # Decode and print the data from the DataMatrix
        data = obj.data.decode("utf-8")
        print("Decoded Data:", data)

        # Extract the points of the bounding box
        points = obj.rect
        if points:
            points = np.array(points, dtype=np.int32).reshape((-1, 1, 2))  # Reshape to correct format for polylines

            # Draw a bounding box around the decoded DataMatrix code
            cv2.polylines(image, [points], isClosed=True, color=(0, 255, 0), thickness=2)

            # Annotate the decoded data beside the bounding box
            x, y = points[0][0]  # Take the first point of the bounding box
            cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Define the output path for saving the annotated image
    output_file = "../../assets/decoded/decoded_data-matrix.png"
    cv2.imwrite(output_file, image)  # Save the image with annotation
    print(f"Annotated image saved as {output_file}")

    # Show the annotated image in a window
    cv2.imshow("Barcode with Annotation", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No DataMatrix codes detected.")
