# making Double Transposition cipher encryption and decryption using python

import sys
import math

def encryptionLoop(key, userInput):
    userInput = userInput.replace(" ","")    # excluding space from the sentence
    sizeOfKey = len(str(key))   # column size
    sizeOfInput = len(userInput)
    global inputSize   # this is the global variable
    inputSize = sizeOfInput
    
    numberOfRow = math.ceil(sizeOfInput / sizeOfKey) # row size
    totalLengthOfInput = sizeOfKey * numberOfRow

    # for padding
    if totalLengthOfInput != sizeOfInput:
        padding = totalLengthOfInput - sizeOfInput
        for i in range(padding):
            userInput = userInput + "z"

    matrix = [["" for space in range(sizeOfKey)] for space in range(numberOfRow)] # making matrix

    # row by row write-------------------###[step 1]
    # inserting every single value of input into matrix with padding
    for i in range(numberOfRow):
        for j in range(sizeOfKey):
            index = i * sizeOfKey + j   # when i = 0,1 and j = 0,1 then index =[[0][0],[0][1]],[[1][0],[1][1]] 
            if index < len(userInput):
                matrix[i][j] = userInput[index]

    # shuffle the matrix with the key-------------------###[step 2]
    strKey = str(key) # making integer key to string for store every individual index
    shuffledMatrix = [["" for space in range(sizeOfKey)] for space in range(numberOfRow)] # making  new matrix for store the shuffled value

    for i in range(numberOfRow):
        for j in range(sizeOfKey):
            shuffledMatrix[i][j] = matrix[i][int(strKey[j])-1]

    # count by column-------------------###[step 3]
    cipher = ""
    for i in range(sizeOfKey):     # have to reapet as column size
        for j in range(numberOfRow):    # have to reapet as row size
            value = shuffledMatrix[j][i]   # when i = 0,1 and j = 0,1 then value = [[0][0],[1][0]], [[0][1],[1][1]]
            cipher = cipher + value
    # print(f"The encrypted message is: {cipher}")
    return cipher

def encryption(key, userInput):
    encryptionLoop(key, userInput)
    cipher = encryptionLoop(key, userInput)
    userInput = cipher
    encryptionLoop(key, userInput)
    cipher = encryptionLoop(key, userInput)
    print(f"The encrypted message is: {cipher}")




while(True):
    print("Enter your choice(Number): ")
    print("1. Encryption: ")
    print("2. Decryption: ")
    print("3. Exit: ")

    number = int(input("Enter the number: "))

    def choice(number):
        if number == 1:
            userInput = input("Enter your text to encrypt: ")
            key = int(input("Enter the key: "))
            userInput = userInput.lower()
            encryption(key, userInput)
        elif number == 2:
            userInput = input("Enter your text to decrypt: ")
            key = int(input("Enter the key: "))
            userInput = userInput.lower()
            # decryption(userInput, key)
        elif number == 3:
            sys.exit()
        else:
            print("Input should be a number from 1 to 3")

    choice(number) 