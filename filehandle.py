
import os

if os.path.exists("file555.txt"):
  print("Yes file availabe..");
else:
  print("File not availabel ...");  


  print("this line added for github test ...");  




f =  open("file1.txt");

print(f.read(5));

print("*************");


print(f.readline());
print(f.readline());


l = open("file2.txt");


for x in l:
	print(x);
	
	
x = open("file2.txt","a");

x.write("add some more data in this file");	



  print("this line added for github test ...");  



