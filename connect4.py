Board = [["0", "0", "0", "0", "0", "A"],
         ["0", "0", "0", "0", "0", "B"],
         ["0", "0", "0", "0", "0", "C"],
         ["0", "0", "0", "0", "0", "D"],
         ["0", "0", "0", "0", "0", "E"],
         ["A", "B", "C", "D", "E", "/"]]

pointers = [4, 4, 4, 4, 4]  # initialise the pointers to first available position

# ----------- show board -------------------
def Show_Board():
    global Board
    for row in range(0, 6):
        for column in range(0, 5):
            print(Board[row][column], "   ", end='')  # prints Horizontally
        print()  # adds New Line


# ----------update Board -----
def Update_Board(colour, column):
    global Board, pointers
    # convert the column to column number
    colNumber = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}  # dictionary to convert letters to numbers
    cnumber = colNumber[column]
    if pointers[cnumber] != -1:
        row = pointers[cnumber]
        Board[row][cnumber] = colour
        pointers[cnumber] -= 1
    else:
        print("The column you have chosen is full.")

# --------- Check for  Winner -------
def IsWinner():
    global Board, colour
    count = 0
    r = 0
    # horizontal
    for i in range(0, 5):
        for c in range(0, 5):
            if Board[i + 1][r] == colour:
                count += 1
            else:
                count = 0
        if count == 4:
            break
        else:
            r += 1

    if count != 4:
        col = 0
        # vertical
        for i in range(0, 5):
            for c in range(0, 5):
                if Board[c + 1][col] == colour:
                    count += 1
                else:
                    count = 0
            if count == 4:
                break
            else:
                col += 1

    if count == 4:
        return True
    else:
        return False

# --------play -----------------------
def play():
    global colour
    Show_Board()
    # ask players for their names, store them in two variables.
    player_1 = input("Enter first player name: ")
    player_2 = input("Enter second player name: ")
    # inform players letter allocation: player 1 will have Y and player 2 R
    print(player_1 + " will use Yellow colour (Y), while " + player_2 + " will use red (R)")
    # set winner to False
    winner = False
    attempt = 0
    while not winner: # while there is no winner
        #   if attempt is odd, use Player Symbol Y, otherwise use R
        if attempt % 2 == 0:
            current_player = player_1
            colour = "Y"
        else:
            current_player = player_2
            colour = "R"
        #   Ask player the column they want to use from (A, B, C, D, E)
        print()  # just to improve the screen presentation
        print(current_player + " turn : ")
        column = input("Which column you want (type A, B, C, D, or E)  ")
        Update_Board(colour, column) # call update board
        Show_Board()  # show the board to players
        winner = IsWinner() # check if there is a winner
        attempt += 1
    print("The winner is " + current_player)

# ----------  main program--------------
play()
