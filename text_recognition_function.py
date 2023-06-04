import cv2
import tesserocr
from PIL import Image

def Text_recognition_handling(im_path):
# Path to the tessdata directory
    tessdata_dir = 
    image_path = im_path
# Initialize the tesserocr PyTessBaseAPI
    api = tesserocr.PyTessBaseAPI(path=tessdata_dir, lang='eng')

    image = cv2.imread(image_path)
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    pil_image = Image.fromarray(gray_img)

    api.SetImage(pil_image)
    text = api.GetUTF8Text()
    api.End()
    return text