import math
# Python program to find the roots by Itrative / Bisection method

print("BISECTION METHOD\n")

# Making equtaion

def maineqx(x):
    return 2*x**3 - 2*x - 5

# Asking user to assing the range

a = int(input("Enter The -ve Number: ")) # taking -ve number

# Checking wethere the user entered right value of a

if (maineqx(a)<0):
    print("f(a) = " + str(maineqx(a)))
    print("The value of a is set to " + str(a))
else:
    print("f(a) = " + str(maineqx(a)))
    print("Your value is wrong as f(a) output is +ve")
    exit()
    
b = int(input("Enter The +ve Number: ")) # taking +ve number

# Checking wethere the user entered right value of b

if (maineqx(b)>0):
    print("f(b) = " + str(maineqx(b)))
    print("The value of b is set to " + str(b))
else:
    print("f(b) = " + str(maineqx(b)))
    print("Your value is worng as f(b) output is -ve")
    exit()

# Checking a main condition

if (maineqx(a)*maineqx(b)>0):
    print("Your data is Wrong")
    exit()
else:
    print("\n")

n = int(input("Enter the Iteration you have to find : ")) # Asking user how many time iteration is to be done

def bisection(a,b):
    # Step 1st
    c = (a+b)/2
    print("\na+b/2 = " + str(a) + "+" + str(b) + "/2 = " + str(c))
    
    # Step 2nd
    c_value = maineqx(c)
    print("So the value of f(" + str(c) + ") is " + str(c_value))
    
    # Step 3rd
    if (c_value < 0):
        print("Which is -ve")
        a = c
        b = b
        print("now new value of a is " + str(a))
        print("And the value of b was " + str(b))
        
    else:
        print("Which is +ve")
        b = c
        a = a
        print("now new value of b is " + str(b))
        print("And the value of a was " + str(a))
    return (a,b)

for i in range(1, n+1):
    print("\nIteration Number:" + str(i) + "\n")
    print("-------------------------------------")
    a,b = bisection(a,b)
    myexit = int(input("Enter 1 for exit and 0 for next Iteration: "))
    if (myexit == 1):
        print("\nSo the final root for this function is " + str(a) + " or " + str(b) + " at Iteration no. " + str(i))
        exit()
    print("-------------------------------------")
    
print("\nSo the final root for this function is " + str(a) + " or " + str(b) + " at Iteration no. " + str(i))