def double(n):  # 4. Pass the data into the function via its PARAMETERS
    return n * 2 # 5. return the doubled value of usernum

userstring = input("Please type a number:") # 1. Request user input
usernum = int(userstring) # 2. Convert to an integer

print(double(usernum))
