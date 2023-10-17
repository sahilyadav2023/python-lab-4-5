N=int(input("Enter any number: "))
temp=N
a=0
while N>0:
    r=N%10
    a=(10*a)+r
    N=N//10
if a==temp:
        print("It is Palindrome ")
else:
    print("It is not palindrome ")
