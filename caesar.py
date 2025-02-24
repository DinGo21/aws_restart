def getDoubleAlphabet(alphabet):
    return alphabet + alphabet

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = message.upper()

    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

def decryptMessage(message, cipherKey, alphabet):
    return encryptMessage(message, -1 * int(cipherKey), alphabet)

def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    myMessage = input("Please enter a message to encrypt: ")
    myCipherKey = input( "Please enter a key (whole number from 1-25): ")
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)

    print(f'Alphabet: {myAlphabet2}')
    print(myMessage)
    print(myCipherKey)
    print(f'Encrypted Message: {myEncryptedMessage}')
    print(f'Decypted Message: {myDecryptedMessage}')

runCaesarCipherProgram()
