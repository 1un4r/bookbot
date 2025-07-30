import sys
from stats import countWords
from stats import countChars
from stats import createNest

def argCheck():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return

def getBookTxt(fPath):
    with open(fPath) as f:
        bookTxt = f.read()
    return bookTxt

def displayCharLogA(chars):
    for char in chars:
        print(f"'{char}': {chars[char]}")

def header(w):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {w} total words")
    print("--------- Character Count -------")

def footer():
    print(f"============= END ===============")

def main():
    argCheck()
    fullTxt = getBookTxt(sys.argv[1])
    ##### comment me for full list #####
    #fullTxt = " djjjjjjjjjjjjjjkkkkkd  jkdddddd jkd"
    wordTotal = countWords(fullTxt)
    charLog = countChars(fullTxt)
    
    header(wordTotal)
    createNest(charLog)
    footer()


    
main()

