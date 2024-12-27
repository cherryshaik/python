Num=int(input("Enter the Year: "))
Count=20
Leap_Count=0
while(Leap_Count!=Count):
    if(Num%4==0 and Num%100!=0)or(Num%400==0):
        Leap_Count+=1
        print(Num)
    Num=Num+1