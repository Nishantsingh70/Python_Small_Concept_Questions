#install module/package
#pip install pyjokes => one liner joke generator module/package

#import the module/package
import pyjokes

#fetch the joke
joke1 = pyjokes.get_joke(language='en', category='all')

#display the joke
print("joke1 :", joke1)

#a different category.
joke2 = pyjokes.get_joke(language='en', category='neutral')

#display the joke
print("joke2 : " , joke2)

#fetch a bunch of jokes.

jokes = pyjokes.get_jokes(language='en', category='neutral')

for i in range(5):
   print("Joke Number" , str(i+1), ":" , str(jokes[i]))
   #print(i+1,".",jokes[i])