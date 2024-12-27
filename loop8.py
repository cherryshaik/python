Num=int(input("Enter the value of Num : "))
print("Multiplication table of ",Num,":")
for i in range(1,Num+1):
  for j in range(1,11):
    print(i,"X",j,"=",j*i)
  