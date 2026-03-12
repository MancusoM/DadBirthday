import streamlit as st

st.set_page_config(page_icon="❤️", layout="centered", page_title="We Love You, Dad!")

from pathlib import Path
import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

current_script_path = Path(__file__).resolve()
parent_directory = current_script_path.parent

st.title("John James Mancuso")

container = st.container()

#def display_image(file_path:str,caption:str,width:int):
 #   return st.image(file_path,caption,width)

import streamlit as st
from PIL import Image
import streamlit as st
from PIL import Image
import os

Pics, nice_things= st.tabs(["Dad Memories",'Happy Birthday'])
with Pics:
    # Folder containing images
    IMAGE_FOLDER = f"{parent_directory}/pics"

    def convert_to_jpeg(image_path):
        """
        Opens an image and converts it to JPEG format in memory.
        """
        img = Image.open(image_path)

        # Convert to RGB (required for JPEG)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        return img

    images = []

    for file in os.listdir(IMAGE_FOLDER):
        file_path = os.path.join(IMAGE_FOLDER, file)

        if os.path.isfile(file_path):
            try:
                img = convert_to_jpeg(file_path)
                images.append(img)
            except Exception as e:
                st.write(f"Skipping {file}: {e}")

    # Display images
    if images:
        st.image(images, caption=[f"Image {i+1}" for i in range(len(images))],width=400)
    else:
        st.write("No valid images found.")
with nice_things:

    list_of_sayings =['Happy Birthday Dad! Youre such a great influence! Heres to another 75 years-Matt',
                      "Happy 75th Birthday to my wonderful husband! Celebrating you today and all the love, strength, and joy you bring to my life and to our family. I love you always.-Mom",
                    "Happy birthday Dad! My quarter life twin birthday! Thanks for all the laughs and happiness over the years! Cant wait to celebrate you today and everyday love you-Julia",
                    "Dear John,Happy Birthday to my favorite Sicilian brother-in-law and Birthday twin. Here’s to many more Italian meals and espressos together! Much love, Eileen"]

    for saying in list_of_sayings:
        st.markdown(saying)
