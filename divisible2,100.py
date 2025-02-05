list=[]
num=int(input("enter how many number to add in list"))
for i in range(num):
        num1=int(input("enter the number"))
        if(num1%2==0 and num1%100!=0):
            list.append(num1)
            print("this ",num1,"divisible by 2 and not divisible 100")
        else:
            print("the given number is not divisible")

print(list)
              
