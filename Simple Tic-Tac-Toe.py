s = [" "] * 9
game = True
side = 'X'

def print_field():
    print("---------")
    print("|", s[0], s[1], s[2], "|")
    print("|", s[3], s[4], s[5], "|")
    print("|", s[6], s[7], s[8], "|")
    print("---------")

def mov():
    flag = True

    while flag:
        xy = input("Enter the coordinates:").split()
        if not xy[0].isdigit()  or not xy[1].isdigit():
            print("You should enter numbers!")
            continue
        if xy[0] not in "123" or xy[1] not in "123":
            print("Coordinates should be from 1 to 3!")
            continue
        
        n = int(xy[1]) - 1 + 3 * (int(xy[0]) - 1)
        if s[n] != " ":
            print("This cell is occupied! Choose another one!")
            continue
    
        s[n] = side
        flag = False

def check():
    global game
    wins = ["XXX", "OOO"]
    win = []
    count = 0
    for x in s:
        if x == 'X':
            count +=1
        if x == 'O':
            count -=1

    for i in range(3):
        if s[i*3] != ' ' and s[i * 3] + s[i * 3 + 1] + s[i * 3 + 2] in wins:
            win += s[i *3]
        if s[i] != ' ' and s[i] + s[i + 3] + s[i + 6] in wins:
            win += s[i]
    if s[0] != ' ' and s[0] + s[4] + s[8] in wins:
        win += s[0]
    if s[2] != ' ' and s[2] + s[4] + s[6] in wins:
        win += s[2]

    if abs(count) > 1 or len(win) > 1:
        print("Impossible")
        game = False
    elif len(win) == 1:
        print(win[0], "wins")
        game = False
    elif ' ' in s:
        pass
    else:
        print("Draw")
        game = False

print_field()
while game:
    mov()
    print_field()
    check()
    if side == "X":
        side = "O"
    else:
        side = "X"
