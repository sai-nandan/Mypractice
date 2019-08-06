prime = []
i = 0
while(i<=40):
    x = 1
    count = 0 
    while (x<=i and i % x!=0):
        count+=1
        x+=1
    else:
        x+=1
    if(count == 2):
        prime.append(i)
    i+=1
print(prime)
