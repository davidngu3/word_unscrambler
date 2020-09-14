def unscramble(fileObj):
    rawtext = input("Please enter text to unscramble: ")

    for line in fileObj:    
        line = line.rstrip().lower()
        if checkEquiv(rawtext, line):
            print("Unscrambled is: " + line)
            return True

    print("This is not a real word!")
    return True
    

def checkEquiv(string1, string2):
    str1Sorted = sorted(string1)
    str2Sorted = sorted(string2)

    if str1Sorted == str2Sorted:
        return True
    else:
        return False

if __name__ == "__main__":
    fileObj = open("300kwords.txt", "r")
    unscramble(fileObj)
    fileObj.close()
    




