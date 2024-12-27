Num=int(input("Enter the Number: "))
Rem=0
Reversed_Num=0
Temp=Num
while(Num!=0):
    Rem=Num%10
    Reversed_Num=Reversed_Num*10+Rem
    Num=Num//10
if(Temp==Reversed_Num):
    print(Temp,"is a palindrome number")
else:
    print(Temp,"is not a palindrome Number")