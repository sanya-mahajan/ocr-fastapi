import pytesseract

from PIL import Image
import pathlib

BASE_DIR = pathlib.Path(__file__).parent
IMG_DIR=BASE_DIR/"images"
img_path=IMG_DIR/"test.png"

img=Image.open(img_path)

extracted_test=pytesseract.image_to_string(img,lang="eng")

print(extracted_test)
