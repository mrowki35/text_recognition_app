import cv2
import tesserocr
from PIL import Image

# Path to the tessdata directory
tessdata_dir = "path"
image_path = "path"


# Initialize the tesserocr PyTessBaseAPI
api = tesserocr.PyTessBaseAPI(path=tessdata_dir, lang='eng')

image = cv2.imread(image_path)

# Preprocess the image
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply image preprocessing (e.g., thresholding, blurring) if necessary
# processed_image = ...

# Convert the NumPy array to a PIL Image object
pil_image = Image.fromarray(gray_img)

# Set the image for OCR
api.SetImage(pil_image)

# Perform OCR
text = api.GetUTF8Text()

# Print the extracted text
print(text)

# Release the tesserocr PyTessBaseAPI
api.End()