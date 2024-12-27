Num=int(input("Enter the Integer Number: "))
for i in range(2,Num+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)