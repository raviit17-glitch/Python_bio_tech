n=int(input("Enter number="));
if(n==0):
    print("{} is odd number".format(n))
else:
    print("{} is even number".format(n))
    
# three variable is bigger, small

a=int(input("enter value of a="));
b=int(input("enter value of b="));
c=int(input("enter value of c"));
if(c<a>b):
    print("big({} {} {}={})".format(a,b,c,a))
    if(c<a<b):
    print("big({} {} {}={})".format(a,b,c,b))
    if(c>a>b):
    print("big({} {} {}={})".format(a,b,c,c))
    if(c==a==b):
    print("all value is equal{} {} {}={}".format(a,b,c,a))