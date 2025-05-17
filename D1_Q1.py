#Check the data types of the following data:
# 10
# 9.8
# 3.14
# 4 - 4j
# ['Asabeneh', 'Python', 'Finland']
# Your name
          

#Press Cmd+K and Cmd+C to add "#" in front of all selected lines

#Lets call this data type checker:

def is_float(a):
    try:
        a = float(a)
        return not a.is_integer()  # not basicallt shortens the next few steps
        # if a.is_integer():
        #     return False
        # else:
        #     return True
    except ValueError:
        return False

def is_complex(s):
    try:
        b = complex(s)
        # Return True only if there is an imaginary part
        return b.imag != 0
    except ValueError:
        return False
    
X= input("Check the data type of any value: ")

# tried using print(type(X)), it only gives 'str' for all value

# solving it using if statement:

if X.isdigit(): 
    print("Data type: Integer")
elif is_float(X):
    print("Data type: Float")
elif X.startswith("[") and X.endswith("]"):
    print("Data type: List")
elif X.startswith("(") and X.endswith(")"):
    print("Data type: Tuple")
elif X.startswith("{") and X.endswith("}"):
    print("Data type: Set")
elif is_complex(X):
    print("Data type: Complex")
else:
    print("Data Type: String")

