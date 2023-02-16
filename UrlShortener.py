#install the module/package
#pip install pyshorteners

#import the module/package
import pyshorteners as sh

link = 'https://www.linkedin.com/pulse/create-dynamic-ansible-playbook-deploying-webpage-redhat-8-singh'

s = sh.Shortener()

print(s.tinyurl.short(link))

