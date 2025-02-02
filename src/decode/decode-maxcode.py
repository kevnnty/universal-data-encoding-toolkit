import zxing
import cv2
import numpy as np

reader = zxing.BarCodeReader()
image_path = "../../assets/given-image-06.png"
image = cv2.imread(image_path)

decoded = reader.decode(image_path)

if decoded:
    print(f"Decoded Data: {decoded.parsed}")
    print(f"Barcode Format: {decoded.format}")
    # Draw the bounding box around the MaxiCode (if points are available)
    if decoded.points:
        points = [(int(p.x), int(p.y)) for p in decoded.points]
        cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)
        # Annotate the decoded data beside the bounding box
        x, y = points[0]  # Take the first point of the bounding box
        cv2.putText(image, decoded.parsed, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    cv2.imshow("MaxiCode with Annotation", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Save the annotated image
    output_file = "../../assets/decoded/decoded_maxicode.png"
    cv2.imwrite(output_file, image)
    print(f"Annotated image saved as {output_file}")
else:
    print("Failed to decode the MaxiCode.")