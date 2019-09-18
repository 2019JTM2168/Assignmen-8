def inp():
    x=int(input("Enter position : "))  #taking position from user
    if(x>9 or x<1):
        print("Invalid position")
        exit()
    y=int(input("Enter number : ")) #taking number from user
    if(y>9 or y<1):
        print("Invalid number")
        exit()
    return x,y

def assgn():
    global a, b, c, g, f, e, d, i, h
    if (x == 1):
        a = y
    if (x == 2):
        b = y
    if (x == 3):
        c = y
    if (x == 4):
        d = y
    if (x == 5):
        e = y
    if (x == 6):
        f = y
    if (x == 7):
        g = y
    if (x == 8):
        h = y
    if (x == 9):
        i = y
    return a, b, c, d, e, f, g, h, i

print("Welcome to the game")
print("Player 1")
x,y=inp()

print("Player 2")
x,y=inp()
a, b, c, d, e, f, g, h, i = assgn()

