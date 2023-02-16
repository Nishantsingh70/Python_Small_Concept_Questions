#! python

#Install the library
#pip install captcha

#import the necessary module
from captcha.audio import AudioCaptcha

#Define properties
audio = AudioCaptcha()

#Define data
data = audio.generate('789')

#Write to the file
audio.write('789', "AudioCaptcha.wav")