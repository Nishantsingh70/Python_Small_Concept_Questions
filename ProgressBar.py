#import module/package
#pip install tqdm

#import the module/package
from tqdm import tqdm,trange
import time

for i in tqdm(range(10)):
   time.sleep(0.4)

print("\n")
print ("Second way to do it")  

for i in trange(5):
   time.sleep(0.4)