#install package/module
#pip install googletrans==3.1.0a0

#import package/module
from googletrans import Translator

#store some text for translation in french language.
text = 'What is your final goal?'


#create an instance of Translator to use
translator = Translator()


#detact the language
lang = translator.detect(text)
print(lang)

#call the translate()
res = translator.translate(text, dest='hi')

#print the result
print(res)
