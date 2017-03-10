def derivative_axton(function):
    elementList = function.split("^")
    exPower = int(elementList[1])
    new = []
    for i in elementList[0]:
        new += i
    indX = new.index("x")
    oldCoeff = ""
    for i in range(len(new)-1):
        oldCoeff += new[i]
    oldCoeff = int(oldCoeff)
    newCoeff = oldCoeff * exPower
    newPower = exPower - 1
    newFunction = (str(newCoeff) + "x^" + str(newPower))
    checkPower = False
    for i in newFunction:
        if checkPower:
            if i == "0":
                return(str(newCoeff))
            elif i == "1":
                return str(newCoeff) + "x"
            else:
                return newFunction
        if i == "^":
            checkPower = True

print(derivative_axton(input("Enter a function: ")))