Num=int(input("Enter the Integer Value: "))
DigitCount=0
while(Num!=0):
    Num=Num//10
    DigitCount=DigitCount+1
print(DigitCount,"Digits")
