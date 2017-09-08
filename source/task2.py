a=input("please input a string:")
list_a=list(a)
j=0
for x in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
    i=0
    for y in list_a:
        if x==y:
            i=1
    if i==1:
        j=j+1
if j==26:
    print(a,"This string contains all letters of the alphabet")
else:
    print(a,"This string doesn't contain all letters of the alphabet")