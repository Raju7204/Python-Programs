n=int(input("Enter the number"))
flag=0
m=n//2
for i in range(2,m,1):
    if n%i==0:
        print("It is not a prime number")
        flag=1
        break
if flag==0:
    print("it is prime number")
