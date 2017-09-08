f = open("file.txt")
f1 = open("filenew.txt",'w')
line=f.read()
list= line.split(" ")
listn=[]
for x in list:
    i = 0
    for y in list:
         if(x==y):
             i=i+1
    f1.write(x+str(i)+"\n")
f.close()
f1.close()