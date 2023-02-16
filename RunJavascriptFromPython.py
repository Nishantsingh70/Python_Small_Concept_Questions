#import module/package
#pip install js2py

#import the module/package
import js2py

#example1
#a js command
js1 = 'console.log("Hello World!!")'
res1 = js2py.eval_js(js1)

#print the result
res1

#example1
#a js function
js2 = '''function add(a,b){
     return a+b;
	 }'''

a = int(input("Enter the first numnber :"))
b = int(input("Enter the second numnber :"))

res2 = js2py.eval_js(js2)

#print the result
print(res2(a,b))