# Python program to find the roots by False Position Method

print("FALSE POSITION METHOD\n")

# Making equtaion

def maineqx(x):
    return x**3 - 3*x + 1

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

n = int(input("Enter the Itration you have to find : ")) # Asking user how many time itration is to be done
    
    
def false_pos(a,b):
    
    # STEP 1 for sloving the formula and find the value of c
    
    half_1 = b-a 
    # print(half_1)
    
    half_2 = maineqx(b) - maineqx(a)
    # print(half_2)
    
    half_12 = half_1 / half_2
    # print(half_12)
    
    half_3 = maineqx(a) * half_12
    # print(half_3)
    
    c = a - half_3
    
    print("We calculated value of c form c = a - {f(b) * [b-a / f(b)-f(a)]}")
    print("And we got c as: " + str(c))    
    
    # STEP 2 now finding f(c)
    
    c_value = maineqx(c)
    print("So the value of f(" + str(c) + ") is " + str(c_value))
    
    # STEP 3 see and of c_value for -ve and +ve for changeing a or b
    
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
    print("\nItration Number:" + str(i) + "\n")
    print("-------------------------------------")
    a,b = false_pos(a,b)
    myexit = int(input("Enter 1 for exit and 0 for next Itration: "))
    if (myexit == 1):
        print("\nSo the final root for this funtion is " + str(a) + " or " + str(b) + " at Itration no. " + str(i))
        exit()
    print("-------------------------------------")
    
print("\nSo the final root for this funtion is " + str(a) + " or " + str(b) + " at Itration no. " + str(i))
    
    