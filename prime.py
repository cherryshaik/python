Num=int(input("Enter the Integer Number: "))
Count=0
for i in range(1,Num+1):
    if(Num%i==0):
        Count+=1
if(Count==2):
    print("Prime Number")
else:
    print("Not a Prime Number")
