from google.colab import drive
drive.mount('/content/drive')

import easyocr
import cv2
import matplotlib.pyplot as plt
import numpy as np

image_path = "/content/drive/MyDrive/images.jpeg"
reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(image_path)
print(result)  

# Extracting bounding box coordinates and text
top_left = tuple(result[0][0][0])
bottom_right = tuple(result[0][0][2])
text = result[0][1]
font = cv2.FONT_HERSHEY_SIMPLEX

# Loading image and drawing the bounding box
img = cv2.imread(image_path)  # Corrected function name
img = cv2.rectangle(img, top_left, bottom_right, (0,255,0), 5)
img = cv2.putText(img, text, top_left, font, 0.5, (255,255,255), 2, cv2.LINE_AA)  

# Displaying the image
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  
plt.axis('off')
plt.show()
