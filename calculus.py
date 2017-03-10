def derivative_axton(function):
    elementList = function.split("^") #Split at power symbol
    exPower = int(elementList[1]) #Save old power
    new = []
    for i in elementList[0]: #Make a list out of the first term
        new += i
    indX = new.index("x") #Find index of x
    oldCoeff = ""
    for i in range(len(new)-1):
        oldCoeff += new[i] #Identify the old coefficient: everything before x
    oldCoeff = int(oldCoeff)
    newCoeff = oldCoeff * exPower #Identify the new coefficient: the old coefficient times the old power
    newPower = exPower - 1 #Reduce the power by one
    newFunction = (str(newCoeff) + "x^" + str(newPower))  #Make the function into string form
    checkPower = False
    for i in newFunction: #Simplify x^0 to nothing and x^1 to x
        if checkPower:
            if i == "0": #Find and remove the x^0
                return(str(newCoeff))
            elif i == "1": #Find and remove the 1 in x^1
                return str(newCoeff) + "x"
            else:
                return newFunction
        if i == "^": #Find the ^ symbol
            checkPower = True
print(derivative_axton(input("Enter a function: ")))