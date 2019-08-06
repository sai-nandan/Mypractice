mylist=[]
def numprime():
    n=int(input("enter number:"))
    for i in range(1,n):
        if i%2==0:
            pass
        else:
            mylist.append(i)
numprime()
print(mylist)
prime = []
n = int(input('enter upto number: '))
for i in range(n):
    x = 1
    count = 0 
    while (x<=i):
        if ((i%x)==0):
            count+=1
        x+=1
    if(count == 2):
        prime.append(i)
print(prime)