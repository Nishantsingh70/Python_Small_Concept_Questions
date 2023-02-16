#install package/module
#pip install googletrans==3.1.0a0

from googletrans import Translator

text = ''' आयरन मैन मार्वल कॉमिक्स का सुपर हीरो है। चरित्र लेखक और संपादक स्टैन ली द्वारा बनाया गया था,
                      और इसकी स्क्रिप्ट लारी लिबियर द्वारा विकसित की गई थी,
		और डिजाइन कलाकार डॉन हैक और जैक किर्बी द्वारा बनाया गया था।
		चरित्र ने अपनी पहली उपस्थिति टेल्स ऑफ सस्पेंस #३९ (कवर मार्च १९६३) में दर्ज की। '''

translator = Translator()

lang = translator.detect(text)
print(lang)

translated = translator.translate(text, dest = 'en')

print(translated.text)