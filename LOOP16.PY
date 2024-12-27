Num=int(input("Enter the Integer: "))
OddCount=0
for i in range(1,Num+1):
    if(i%2!=0):
        OddCount+=1
print(OddCount,"is the count of odd numbers")