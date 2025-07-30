def countWords(srcTxt):
    allWords = srcTxt.split()
    return len(allWords)

def countChars(bookTxt):
    charLog = {}
    letters = bookTxt.lower()

    for letter in letters:
        if letter in charLog:
            charLog[letter] += 1
        else:
            charLog[letter] = 1
    return charLog
    
def displayCharLog(chars):
    ########## non nested display
    for char in chars:
        print(f"'{char}': {chars[char]}")
        #print(chars)

def sort_on(items):
    return items["num"]

#{"char": "b", "num": 4868}
def createNest(charList):
    nestList = []
    for c in charList:
        a = {"char": c, "num": charList[c]}
        nestList.append(a)
    nestList.sort(reverse=True, key=sort_on)
    
    #e: 44538
    for i in range(len(nestList)):
        print(f"{nestList[i]['char']}: {nestList[i]['num']}")


    return charList

