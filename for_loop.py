n=list(range(1,11))
for i in n:
    if i%2==0:
        print(i,'is even')
    else:
        print(i,'is odd')

        # prime number

for n in range(2,20):
    for i in range(1,11):
        if n%i==0:
            print(n,"is not prime")
            break
    else:
        print(n,"is prime")

a=5
b=6
c=8
x=lambda a,b,c : a+b+c+10
print(x)
