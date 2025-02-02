# Data Encoding and Decoding

## Exploring the world of data encoding and decoding, from barcodes to Aztec, MaxiCode, and more.

This project focuses on encoding and decoding various types of data formats, including but not limited to:

- Barcodes (e.g., EAN-13, Code 128)
- QR Codes
- Aztec Codes
- DataMatrix Codes
- MaxiCode

### Features
- Decoding different types of barcodes.
- Visualizing decoded data with annotations on the image.
- Integration with libraries and tools like OpenCV, ZXing, and Pyzbar.
- Supporting various image formats for encoding and decoding.

### Requirements
- Python 3.x
- OpenCV
- Pyzbar or ZXing (depending on implementation)
- Docker (if utilizing Java-based libraries)
- Required Java `.jar` files for ZXing (if using ZXing in Docker)

### Setup
1. Clone this repository:
    ```bash
    git clone https://github.com/kevnnty/universal-data-encoding-toolkit.git
    cd data-encoding
    ```

2. Install the necessary Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure Docker is installed (for running Java-based libraries).

4. Place your barcode/QR code/other image files in the `assets/` directory.

### Usage
- Run the respective script for decoding with path to your image file in assets folder accordingly

Feel free to fork, open issues, or submit pull requests. Contributions are always welcome!

