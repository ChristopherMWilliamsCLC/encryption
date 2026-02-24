# Moves the ordinal value of a charachter up using the specified distance.
def CaesarEncryption(message, distance):
    encryptedCharString = ""
    for ch in message:
        ordValue = ord(ch)
        encryptedValue = ordValue + distance
        encryptedCharString += chr(encryptedValue)
    return encryptedCharString

# Moves the ordinal value of a charachter down using the specified distance.
def CaesarDecryption(message, distance):
    decryptedCharString = ""
    for ch in message:
        ordValue = ord(ch)
        decryptedValue = ordValue - distance
        decryptedCharString += chr(decryptedValue)
    return decryptedCharString

# Converts a message string into binary.
def MessageToBitstring(message):
    invertedBinary = ""
    for ch in message:
        decimal = ord(ch)
        invertedBinary += str(decimal % 2)
        while decimal > 0:
            decimal //= 2
            remainder = decimal % 2
            invertedBinary += str(remainder)
        invertedBinary += " "
    bitString = ""
    for word in invertedBinary.split():
        for i in range(len(word), 0, -1):
            bitString += word[i-1]
        bitString += " "
    return bitString

# Converts binary back to a message string.
def BitstringToMessage(bitString):
    decimal = 0
    message = ""
    for word in bitString.split():
        exponent = len(word)-1
        for ch in word:
            decimal += int(ch) * 2 ** exponent
            exponent -= 1
        message += str(chr(decimal))
        decimal = 0
    return message

# Shuffles the bitstring using a special pattern.  
def StringSpliceEncryption(bitString):
    i = 0
    encryptedString = ""
    for word in bitString.split():
        # Split the word in half.
        leftHalf = word[0:len(word)//2]
        rightHalf = word[len(word)//2: len(word)]

        # For every other iteration of words in the string.
        if i % 2 == 0:
            #if True:
            # Shift the bit of the left half to the left.
            leftHalf = leftHalf[len(leftHalf)-1:len(leftHalf)] + leftHalf[0:len(leftHalf)-1]
            # Shift the bit of the right half to the right.
            rightHalf = rightHalf[1:len(rightHalf)] + rightHalf[0:1]
        else:
            #if False:
            # Shift the bit of the left half to the right.
            leftHalf = leftHalf[1:len(leftHalf)] + leftHalf[0:1]
            # Shift the bit of the right half to the left.
            rightHalf = rightHalf[len(rightHalf)-1:len(rightHalf)] + rightHalf[0:len(rightHalf)-1]
        # Increment i
        i += 1
        # Create the new splice encrypted string by concatenating the left and right halves.
        encryptedString += leftHalf + rightHalf + " "
    #return the encrypted string.
    return encryptedString

# Unshuffles the bitstring.
def StringSpliceDecryption(bitString):
    i = 0
    decryptedString = ""
    for word in bitString.split():
        leftHalf = word[0:len(word)//2]
        rightHalf = word[len(word)//2: len(word)]

        if i % 2 == 0:
            leftHalf = leftHalf[1:len(leftHalf)] + leftHalf[0:1]
            rightHalf = rightHalf[len(rightHalf)-1:len(rightHalf)] + rightHalf[0:len(rightHalf)-1]
        else:
            leftHalf = leftHalf[len(leftHalf)-1:len(leftHalf)] + leftHalf[0:len(leftHalf)-1]
            rightHalf = rightHalf[1:len(rightHalf)] + rightHalf[0:1]
        i += 1
        decryptedString += leftHalf + rightHalf + " "
    return decryptedString

# Encrypts a message.
def Encrypt(message, distance):      
    caesarCipherEncrypt = CaesarEncryption(message, distance)
    messageToBitstring = MessageToBitstring(caesarCipherEncrypt)
    encryptedMessage = StringSpliceEncryption(messageToBitstring)
    return encryptedMessage

# Decrypts a message.
def Decrypt(message, distance):
    unshuffledBitstring = StringSpliceDecryption(message)    
    bitstringToMessage = BitstringToMessage(unshuffledBitstring)
    decryptedMessage = CaesarDecryption(bitstringToMessage, distance)
    return decryptedMessage
    
def main():
    print("Encryption = " + Encrypt("Encryption", 10))
        
if __name__ == "__main__":
    main()
