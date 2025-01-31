listt=[]
a=int(input("enter the number to add in list"))
for i in range(a):
    num=int(input("enter the number:"))
    listt.append(num)
print(listt)
rot=int(input("enter the rotation index"))
f=listt[rot:a+1]
g=listt[0:rot]
v=f+g
print(v)
