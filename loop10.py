Num=int(input("Enter the Integer Value: "))
EvenDigitCount=0
Rem=0
while(Num!=0):
    Rem=Num%10
    if(Rem%2==0):
        EvenDigitCount+=1
    Num=Num//10
print("Number of Even Digits are ",EvenDigitCount)