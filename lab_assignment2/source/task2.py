string= input("Please input a number:")
k=int(string)
dict={}
if k>0:
  for i in range(1,k+1):
      dict[i]=i*i
  print(dict)
else:
    print("This number is invalid.")

