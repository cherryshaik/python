Num=int(input("Enter the Integer Value: "))
sum_Digits=0
Rem=0
while(Num!=0):
    Rem=Num%10
    Num=Num//10
    sum_Digits=sum_Digits+Rem
print("Sum Of Digits : ",sum_Digits)
