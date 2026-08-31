print("Solving function: x = ax^2 + bx + c")

def inputValueThatIsNotZero(val):
    foo = 0
    while foo==0:
        foo = float(input("Input is not allowed to be zero. Give input" + val))
    return foo

a = inputValueThatIsNotZero("a")
b = inputValueThatIsNotZero("b")
c = inputValueThatIsNotZero("c")

D = b**2 - 4*a*c

if D<0:
    print("Problem! D is less that 0. There are no x solutions.")
elif D==0:
    print("D is 0. There is one x solution")
    x = (-b/(2*a))
    print("The root is" + x)
elif D>0:
    print("D is bigger than 0. There are two x solutions")
    x1= ( ( -b + D**(1/2) ) / 2*a)
    x2= ( (-b - D**(1/2) )/ 2*a)
    print("Roots are "+x1+" and "+x2)

