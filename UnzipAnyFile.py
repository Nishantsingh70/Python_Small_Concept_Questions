import zipfile as zf

#source of zip file
target = 'jdk.zip'

print('Starting to unzip the file..')

root = zf.ZipFile(target)

#destination location
root.extractall(r'C:\Users\Nishant Singh\Desktop\Python\Python_Video_Code\Zip\Destination')

root.close()

print("File is successfully unzipped..")