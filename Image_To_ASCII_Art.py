#install the module/package
#pip install pywhatkit

#import the module/package
import pywhatkit as kt

print("Lets turn Images to ASCII Art!!")

source_path = "webpage.png"
target_path = "ASCII_art.text"

kt.image_to_ascii_art(source_path, target_path)

