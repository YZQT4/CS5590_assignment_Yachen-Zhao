string=input("please input a sentence:")
set= set(string.split(" "))
setorder=sorted(set)
for x in setorder:
  print (x,end=' ')