def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."
    
def right_justify(s):
    length = len(s)
    print " " * (70 - length) + s
    
def do_twice(f):
    f()
    f()
    

def print_twice(string):
    print string
    print string
 
def do_four(f):
    do_twice(f)
    do_twice(f)
    
# do_four(print_twice, 'spam')


# Read "http://www.greenteapress.com/thinkpython/code/grid.py" and tried it on my own

def printPlus():
    print "+",
    
def printSpace():
    print " ",
    
def printDash():
    print "-",
    
def printSlash():
    print "/",
    
def printNothing():
    "does nothing"
    
def printHorizontalLine(f1, f2, f3):
    f1()
    do_four(f2)
    f3()
    
def printPlusMinusBeam(x):
    for i in range(0, x):
        printHorizontalLine(printPlus, printDash, printNothing)
    print "+"
    
def printSlashSpaceBeam(x):
    for i in range(0, 4):
        for i in range(0, x):
            printHorizontalLine(printSlash, printSpace, printNothing)
        print "/"

def printRowGrid(x, firstBeam):
    if firstBeam:
        printPlusMinusBeam(x)
    printSlashSpaceBeam(x)
    printPlusMinusBeam(x)
    
printRowGrid(4, True)
printRowGrid(4, False)
printRowGrid(4, False)
printRowGrid(4, False)