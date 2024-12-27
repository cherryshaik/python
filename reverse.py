Num=int(input("Enter the Integer: "))
Rem=0
Reversed_Num=0
while(Num!=0):
    Rem=Num%10
    Reversed_Num=Reversed_Num*10+Rem
    Num=Num//10
print("Reversed Number : ",Reversed_Num)