#import the module/package.
import random
import string

print("Hello, Welcome to password generator!!")

length = int(input("\nEnter the password: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#print(lower)
#print(upper)
#print(num)
#print(symbols)

all = lower + upper + num + symbols

temp = random.sample(all, length)
print(temp)

password = "".join(temp)

print(password)