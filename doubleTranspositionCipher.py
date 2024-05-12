# making Double Transposition cipher encryption and decryption using python

import sys
import math
 
# this function is for encryption steps 
def encryptionLoop(key, userInput):
    userInput = userInput.replace(" ","")    # excluding space from the sentence
    sizeOfKey = len(str(key))   # column size
    sizeOfInput = len(userInput)
    
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

    return cipher


# main encryption function
def encryption(key, userInput):
    
    cipher = encryptionLoop(key, userInput)  # single encryption cipher
    userInput = cipher
    cipher = encryptionLoop(key, userInput)  # double encryption cipher

    print(f"The encrypted message is: {cipher}")


# this function is for decryption steps 
def decryptionLoop(key, userInput):

    sizeOfKey = len(str(key))   # column size
    sizeOfInput = len(userInput)
    numberOfRow = math.ceil(sizeOfInput / sizeOfKey) # row size

    matrix = [["" for space in range(sizeOfKey)] for space in range(numberOfRow)] # making matrix
    
    # column by column write-------------------###[step 1]
    for i in range(sizeOfKey):
        for j in range(numberOfRow):
            index = i * numberOfRow + j   # when i = 0,1 and j = 0,1 then index =[[0][0],[0][1]],[[1][0],[1][1]] 
            if index < len(userInput):
                matrix[j][i] = userInput[index]   # when i = 0,1 and j = 0,1 then value of matrix= [[0][0],[1][0]], [[0][1],[1][1]]

    # shuffle by key-------------------###[step 2]
    strKey = str(key) # making integer key to string for store every individual index
    shuffledMatrix = [["" for space in range(sizeOfKey)] for space in range(numberOfRow)] # making  new matrix for store the shuffled value

    for i in range(numberOfRow):
        for j in range(sizeOfKey):
            shuffledMatrix[i][int(strKey[j])-1] = matrix[i][j]
    
    # write the plaintext-------------------###[step 3]
    plaintext = ""
    for i in range(numberOfRow):     # have to reapet as row size
        for j in range(sizeOfKey):    # have to reapet as column size
            value = shuffledMatrix[i][j]   # when i = 0,1 and j = 0,1 then value = [[0][0],[0][1]], [[1][0],[1][1]]
            plaintext = plaintext + value

    return plaintext


# main decryption function
def decryption(key, userInput):

    plaintext = decryptionLoop(key, userInput)   # single decryption plaintext
    userInput = plaintext
    plaintext = decryptionLoop(key, userInput)   # double decryption plaintext
    
    finalText = ""
    for i in range(len(plaintext)): 
        if i < inputSize:    # input size is a global variable
            finalText = finalText + plaintext[i]

    print(f"The decrypted message is: {finalText}")


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

            userInput = userInput.replace(" ","")    # excluding space from the sentence
            sizeOfInput = len(userInput)
            global inputSize   # this is the global variable
            inputSize = sizeOfInput
        elif number == 2:
            userInput = input("Enter your text to decrypt: ")
            key = int(input("Enter the key: "))
            userInput = userInput.lower()
            decryption(key, userInput)
        elif number == 3:
            sys.exit()
        else:
            print("Input should be a number from 1 to 3")

    choice(number) 