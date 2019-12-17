#For Testing Purpose only

import pytesseract as tesser
from PIL import Image

image_1 = Image.open('IMG_NEWS_1.png')

text_1 = tesser.image_to_string(image_1)

print(text_1)
