import sys
import os
from PIL import Image

origin, new = sys.argv[1:3]  # reading folder names from terminal

try:
    images = os.listdir(origin)  # storing image names
except FileNotFoundError as err:
    print(f"File {origin} is not found, please create file in working directory then try again")

is_not_accessible = not os.access(new, os.F_OK)  # checking if new exists
if is_not_accessible:
    os.mkdir(new)  # creating new directory of it doesn't exist

for image in images:
    # iterating through image names and converting each one to png then saving it to new folder
    pokemone = Image.open(fr"{origin}{image}")
    print(image)
    image = image.replace("jpg", "png")
    pokemone.save(f"{new}{image}", "png")
