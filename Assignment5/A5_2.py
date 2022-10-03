#6
#6
from pickle import OBJ


w=int(input("enter a 3 digit number"))
w=w//10     #removes last value
answer=w%10  #returns last value

print(answer)
print()
#7
a=int(input("enter a 3 digit number"))
print(a%10)
print()
#8
b=[1,2,3,4]
print(1 in b)
#always returns  boolean value
#9
print(10 not in b)
print()
#10
c=[1,2,3,4]
print(b is c) #share different id
print(b==c) #share same id
print()
#in bis c case both b and c have different memory adress
#but not happen in case of b and c
