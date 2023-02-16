#install the module/package
#pip install instaloader

#import the module/package
import instaloader

test = instaloader.Instaloader()

acc = input("Enter the Account username :")

test.download_profile(acc, profile_pic_only=False)

