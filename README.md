# OCR Text Detection using EasyOCR in Google Colab

This project demonstrates Optical Character Recognition (OCR) using **EasyOCR** in **Google Colab**. It processes images to extract text and visualize the detected text using OpenCV.

## Features
- Uses **EasyOCR** for text detection.
- Processes images uploaded via **Google Drive**.
- Visualizes detected text using **OpenCV**.
- Runs entirely in **Google Colab**, making it accessible without local installations.

## Setup and Dependencies
To run this project, install the required dependencies in your Colab notebook using pip:

```sh
!pip install easyocr
!pip install torch torchaudio torchvision
!pip install matplotlib
!pip install matplotlib.pyplot
```
See `code.ipynb` for the detailed setup and implementation.
To run this project, install the required dependencies in your Colab notebook.

## Uploading Files using Google Drive
Since Google Colab does not retain files after runtime termination, we use **Google Drive** to upload and access images.

### Steps to Attach Google Drive:
1. Mount Google Drive in your Colab session.
2. Upload the image to Google Drive and access it using the file path.

## Running OCR on Images
Once the image is uploaded, use **EasyOCR** to extract text. Refer to `code.ipynb` for the implementation details.

## How to Run the Project in Google Colab
1. Open Google Colab ([Google Colab](https://colab.research.google.com/)).
2. Mount Google Drive as shown above.
3. Upload your image to Google Drive.
4. Install dependencies using `pip install`.
5. Run the script in `code.ipynb` to extract text and visualize results.

## Output Example
The output image will display detected text with bounding boxes, making it easy to verify OCR results.

---

### Future Improvements
- Support for multiple languages.
- Web-based interface for user uploads.
- Enhanced text processing with NLP.

**Contributions & feedback are welcome!** 🚀

