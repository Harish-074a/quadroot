import math
def quad():
    print("ax²+bx+c")
    a=float(input("enter the value of a : "))
    b=float(input("enter the value of b  : "))
    c=float(input("enter the value of c : "))
    print("The Equation is : (",a,")x²+(",b,")x+(",c,")")
    p=b**2
    o=4*a*c
    i=p-o
    u=2*a
    q=math.sqrt(i)
    e=abs((-b+q)/(u))
    r=abs((-b-q)/(u))
    #print(p,o,i,u,q)
    #print(e,r)
    print("the factors of the following equation is (x +",round(e,2),")")
    print("the factors of the following equation is (x -",round(r,2),")")
quad()
    
          
