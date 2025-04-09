#baseConverter.py

# menu for user's selection
def menu():
    print("""
    WELCOME TO BASE CONVERTER

    WHAT BASE IS YOUR NUMBER IN?
    0) QUIT
    1) BINARY      (Base 2)
    2) OCTAL       (Base 8)
    3) DECIMAL     (Base 10)
    4) HEXADECIMAL (Base 16)
    """)
    output = input("Answer: ")
    return output

#handles binary to decimal conversions
def bToDecimal(bNum):
    length = len(bNum) - 1
    dNum = 0
    for i in range(len(bNum)):
        inte = int(bNum[i])
        dNum += inte * (2** (length - i))
    return dNum

#handles binary to octal conversions
def bToOctal(bNum):
    oNum = ""
    #change binary to decimal first
    num = bToDecimal(bNum)
    power = 1
    root = 0
    while power < num:
        power = power * 8
        root += 1
    root = root - 1

    while root > -1:
        digit = int(num / (8 ** root))
        oNum = oNum + str(digit)
        num = num - (digit * (8**root))
        root = root - 1

    return oNum

#handles binary to hexadecimal conversions
def bToHexadecimal(bNum):
    #an array to hold hexadecimal letters
    alpha = ["A","B","C","D","E","F"]
    hNum = ""
    #change binary to decimal first
    num = bToDecimal(bNum)
    power = 1
    root = 0
    while power < num:
        power = power * 16
        root += 1
    root = root - 1

    while root > -1:
        digit = int(num / (16 ** root))
        if digit > 9:
            dig = alpha[(digit - 10)]
            hNum = hNum + str(dig)
        else:
            hNum = hNum + str(digit)
        num = num - (digit * (16**root))
        root = root - 1

    return hNum

#binary checkpoint
def binary():
    #collect user's number
    bNum = input("Binary Number: ")

    #boolean variable to ensure the user's number is in binary
    isBinary = True

    #loop to make sure every digit is a 0 or 1
    i = 0
    while isBinary and (i < len(bNum)) :
        if (bNum[i] == "0" or bNum[i] == "1"):
            isBinary = True
        else:
            isBinary = False
            print("The number you provided is not a binary number")
        i += 1

    #print conversions if the entered number is in Binary
    if isBinary == True:
        print("""
        Octal = {}
        Decimal = {}
        Hexadecimal = {}
        """.format(bToOctal(bNum), bToDecimal(bNum), bToHexadecimal(bNum)))

#handles decimal to binary conversions
def dToBinary(dNum):
    bNum = ""
    power = 1
    root = 0
    while power < dNum:
        power = power * 2
        root += 1
    root = root - 1

    while root > -1:
        digit = int(dNum / (2 ** root))
        bNum = bNum + str(digit)
        dNum = dNum - (digit * (2**root))
        root = root - 1

    return bNum

#handles decimal to octal conversions
def dToOctal(dNum):
    #convert to Binary
    num = dToBinary(dNum)

    #convert to Octal
    oNum = bToOctal(num)
    return oNum

#handles decimal to hexadecimal conversions
def dToHexadecimal(dNum):
    #convert to Binary
    num = dToBinary(dNum)

    #convert to Hexadecimal
    hNum = bToHexadecimal(num)
    return hNum

#decimal number checkpoint
def decimal():
    #collect user's number
    dNum = input("Decimal number: ")

    #check that it is a decimal number
    if dNum.isnumeric() == True:
        dNum = int(dNum)
        print("""
        Binary = {}
        Octal = {}
        Hexadecimal = {}
        """.format(dToBinary(dNum), dToOctal(dNum), dToHexadecimal(dNum)))
    else:
        print("The number you provided is not a decimal number")

#handles octal to decimal conversions
def oToDecimal(oNum):
    length = len(oNum) - 1
    dNum = 0
    for i in range(len(oNum)):
        num = int(oNum[i]) * (8 ** (length-i))
        dNum = dNum + num
    return dNum

#handles octal to binary conversions
def oToBinary(oNum):
    #convert to decimal first
    num = oToDecimal(oNum)

    #convert decimal to binary
    bNum = dToBinary(num)
    return bNum

#handles octal to hexadecimal conversions
def oToHexadecimal(oNum):
    #convert to decimal first
    num = oToDecimal(oNum)

    #convert decimal to hex
    hNum = dToHexadecimal(num)
    return hNum

#octal numbers checkpoint
def octal():
    #collect user's number:
    oNum = input("Octal Number: ")

    #check that it is an octal number:
    isOctal = True
    if oNum.isnumeric() == True:
        i = 0
        while isOctal and (i < len(oNum)) :
            if (int(oNum[i]) < 8):
                isOctal = True
            else:
                isOctal = False
                print("The number you provided is not an Octal number")
            i += 1

        if isOctal == True:
            print("""
            Binary = {}
            Decimal = {}
            Hexadecimal = {}
            """.format(oToBinary(oNum), oToDecimal(oNum), oToHexadecimal(oNum)))
    else:
        print("The number you provided is not an Octal number")

#handles hexadecimal to decimal conversions
def hToDecimal(hNum):
    dNum = 0
    alpha = ["A","B","C","D","E","F"]
    length = len(hNum) - 1
    for i in range(len(hNum)):
        if hNum[i].isalpha():
            letter = hNum[i].upper()
            num = alpha.index(letter) + 10
            dNum = dNum + (num * (16 ** (length - i)))
        else:
            num = int(hNum[i]) * (16 ** (length - i))
            dNum = dNum +  num
    return dNum

#handles hexadecimal to binary conversions
def hToBinary(hNum):
    #convert to decimal
    num = hToDecimal(hNum)

    #convert decimal to binary
    bNum = dToBinary(num)
    return bNum

#handles hexadecimal to octal conversions
def hToOctal(hNum):
    #convert to decimal
    num = hToDecimal(hNum)

    #convert deciaml to Octal
    oNum = dToOctal(num)
    return oNum

#hexadecimal numbers checkpoint
def hexadecimal():
    #collect user's number
    hNum = input("Hexadecimal Numer: ")

    #check if it is a hexadecimal
    if hNum.isalnum():
        print("""
        Binary = {}
        Octal = {}
        Decimal = {}
        """.format(hToBinary(hNum), hToOctal(hNum), hToDecimal(hNum)))
    else:
        print("The number you provided is not a Hexadecimal number")

def main():
    keepGoing = True
    while keepGoing:
        response = menu()
        if response == "1":
            binary()
        elif response == "2":
            octal()
        elif response == "3":
            decimal()
        elif response == "4":
            hexadecimal()
        elif response == "0":
            print("Thank you for using Base Converter!")
            keepGoing = False
        else:
            print("Your response was not an option. Please select an option.")
main()