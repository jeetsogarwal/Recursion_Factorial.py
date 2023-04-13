#finding factorial by recursion

n=int(input("enter the number: "))
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return (n*fact(n-1))
print("factorial of",n,"is",fact(n))

