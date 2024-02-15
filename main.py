userInput = ''

def InitialInput():
    global userInput
    print("Please select which method of input you would like to use")
    userInput = input("String or file? ")
    userInput = userInput.strip().lower()

    if (userInput == "string"):
        StringInput()
    elif (userInput == "file"):
        FileInput()
    else:
        InitialInput()
    # print(userInput)

def StringInput():
    print("Please enter a string: ")
    strInput = input()
    ASCIIReport(strInput)

def FileInput():
    print("Please enter a file path: ")
    fileName = input()
    try:
        # Good code here
        file = open(fileName, "r")
        ASCIIReport(file.read())
        file.close()

    except PermissionError:
        # Bad code here
        print("This file does not have read privileges")
        FileInput()

def ASCIIReport(text):
    # Create a dictionary of some sort
    diction = {}
    high = ['', 0]
    mid = ['', 0]
    low = ['', 0]

    for letter in text:
        # If the letter is not there, add it.
        if letter not in diction.keys():
            diction[letter] = 1
        else:
            diction[letter] += 1

        # Pulls last 3 that occur the highest amounts
        # In other words, if there were 4 matches, then only the first 3 matches would be stored.
        if diction[letter] > high[1]:
            high[0] = letter
            high[1] = diction[letter]
        elif diction[letter] > mid[1]:
            mid[0] = letter
            mid[1] = diction[letter]
        elif diction[letter] > low[1]:
            low[0] = letter
            low[1] = diction[letter]

    # parse the dictionary for three most occurring values
    # print(diction)
    print(f"{256 - len(diction.keys())} Characters Not Used")
    print(f"{len(diction.keys())} Characters Used")
    print(diction)
    print(low, mid, high)

    # Reverses string
    print(text[::-1])
    pass


if __name__ == '__main__':
    tmpIn = ""
    while(tmpIn.lower() != "yes"):
        InitialInput()
        tmpIn = input("Exit? ")


