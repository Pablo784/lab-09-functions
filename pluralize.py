def pluralize(word):  # 1. Word is passed as input PARAMETER into the function.
    return word + "s" # 2. Word is returned in place at the function call with processed data.

userword = input("Word please: ")
print(pluralize(userword)) # 3. userword is a variable that's passed as an ARGUEMENT to the function call.
