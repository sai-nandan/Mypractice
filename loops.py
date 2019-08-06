# a = 1
# while a<=10:
#     b=1
#     while b<=5:
#         print(b, end=" ")
#         b+=1
#     a+=1
#     print() 
# rows = int(input("enter size:"))
# a=1
# while a<=rows:
#     b= rows
#     c=1
#     while b>=a: 
#         print(" ", end=" ")
#         b-=1
#     while c<=a:
#         print(c,end="  ")
#         print("",end="  ")
#         c+=1
#     a+=1
#     print("")        

# a=4
# while a>=1:
#     b=1
#     c=4
#     while b<=a:
#         print('',end="")
#         b+=1
#     while c<=a:
#         print(c,end=" ")
#         c+=1
#     a-=1
#     print()    

# a=0
# b=1
# n=0
# print (a,b)
# while(n<=100):
#     n=a+b
#     a,b=b,n
#     print (n)

    # fibonacci

# a=0
# b=1
# n=0
# nums=int(input('enter num:'))
# print(a)
# print(b)
# while (n<=nums):
#     n=a+b
#     a=b
#     b=n
#     if (n<=nums):
#         print (n)

 
#revesing a number

a=1234
rem=0
rev=0
while a>=0:
  rem=a%10
  print(rem)
  rev=rev*10+rem
  a=a/10
print(rev)

