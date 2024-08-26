import random, string

def generatorPassword(containsUppercase, containsNumber, containsSymbols, count):
    
    charsLength = int(count.cget("text"))
    charsForPassword = string.ascii_lowercase
    password = ""

    if containsNumber.get() == "on":
        charsForPassword += string.digits
    if containsUppercase.get() == "on":
        charsForPassword += string.ascii_uppercase
    if containsSymbols.get() == "on":
        charsForPassword += string.punctuation

    for _ in range(charsLength):
        password += random.choice(charsForPassword)

    return password