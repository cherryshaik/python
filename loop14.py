Num=int(input("Enter the integer Value: "))
EvenSum=0
OddSum=0
for i in range(1,Num+1):
    if(i%2==0):
      EvenSum=EvenSum+i
    else:
       OddSum=OddSum+i
print("EvenSum :",EvenSum)
print("OddSum: ",OddSum)
