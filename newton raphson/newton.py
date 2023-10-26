# Python program to find the roots by False Position Method

print("NEWTON RAHPSON METHOD\n")

print("f(x) = x**3 - 5*x + 1\n")

# -----------------------------------------------------------------------

                        # finding Values of f(x) and f'(x)

# main f(x) finding

def maineqx(x):
    return x*x*x - 5*x + 1

# Slotion of f'(x)

def solv_defeqx(x):
    return 3*x*x - 5

# -----------------------------------------------------------------------

while True:
    try:
        a = int(input("\nEnter The -ve Number: "))
        if maineqx(a) < 0:
            print("f(a) = " + str(maineqx(a)))
            print("The value of a is set to " + str(a))
        else:
            print("f(a) = " + str(maineqx(a)))
            print("Your value is wrong as f(a) output is +ve")
            continue  # Restart the loop for incorrect input

        b = int(input("Enter The +ve Number: "))
        if maineqx(b) > 0:
            print("f(b) = " + str(maineqx(b)))
            print("The value of b is set to " + str(b))
        else:
            print("f(b) = " + str(maineqx(b)))
            print("Your value is wrong as f(b) output is -ve")
            continue  # Restart the loop for incorrect input
        
        break  # Break out of the loop if both 'a' and 'b' are valid

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Checking a main condition

if (maineqx(a)*maineqx(b)>0):
    print("Your data is Wrong")
    exit()
else:
    print("\n")

n = int(input("Enter the Itration you have to find : ")) # Asking user how many time itration is to be done
    
def step1(a,b):
    # Step 1st
    c = (a+b)/2
    print("\na+b/2 = " + str(a) + "+" + str(b) + "/2 = " + str(c))
    return c
c = step1(a,b)

def newton(c):
    # Step 2
    
    # finding f(c)
    c_value = maineqx(c)
    print("\nSo the f(c) = " + str(c_value))
    
    # finding f'(c)
    c_devalue = solv_defeqx(c)
    print("\nSo the value of f'(c) = " + str(c_devalue))
    
    # Step 3
    d = c-(c_value/c_devalue)
    print("\nd = c - {f(c)/f'(c)}")
    print("\nd = " + str(c) + " - { " + str(c_value) + "/" + str(c_devalue) + " }")
    print("\nSo d = " + str(d))
    
    # Step 4 finding f(d)
    
    d_value = maineqx(d)
    print("\nNow the value of f(d) is " + str(d_value))
    
    if(d_value==0):
        print("T    `he Roots of f(x) is " + str(d))
        exit()
    else:
        c = d
        return c

for i in range(1, n+1):
    print("\nItration Number:" + str(i) + "\n")
    print("-------------------------------------")
    c = newton(c)
    # myexit = int(input("Enter 1 for exit and 0 for next Itration: "))
    # if (myexit == 1):
    #     print("\nSo the final root for this funtion is " + str(c) + " at Itration no. " + str(i))
    #     exit()
    print("-------------------------------------")
    
print("\nSo the final root for this funtion is " + str(c) + " at Itration no. " + str(i))
        