import os
import time
import random

def clear_board():
    try:
        os.system('cls')
    except NameError:
        os.system('clear')
    finally:
        pass
    

def graphic_welcome():
    print("Welcome to")
    for i in range(3):
        time.sleep(1)
        print(".")
    time.sleep(2)
    tictactoe = "  _________                         _                                       _\n"
    tictactoe += " /XXXXXXXXX|                      /|X|                                    /|X|\n"
    tictactoe += "|/_ |XX|___/_    ______           ||X|_                  ______           ||X|                    ______\n"
    tictactoe += "   ||XX|   /X|  / /XXXX\        /|XXXXX|     ________   / /XXXX\        /|XXXXX|      ______     / /XXXX\ \n"
    tictactoe += "   ||XX|  |/_  | |X|_/|X|  ___ |_  |X|/     / / XXXXX| | |X|_/|X|  ___ |_  |X|/      / /XXXX\   | |X|__/X| \n"
    tictactoe += "   ||XX|  /|X| | |X| / _  /XXX|  | |X|  _  | |X     X| | |X| / _  /XXX|  | |X|  _   | |X/\ \X|  | |XXXXXX| \n"
    tictactoe += "   ||XX|  ||X| | |X|_/|X| /__/   | |X|/|X| | |X     X| | |X|_/|X| /__/   | |X|/|X|  | |X\/_/X|  | |X|___/ \n"
    tictactoe += "   ||XX|  ||X|  \ \XXXX/         \ \XXXX/   \ \XXXXXX|  \ \XXXX/          \ \XXX/    \ \XXXX/    \ \XXXXX|\n"
    tictactoe += "   |/_/   |/_/   \____/           \____/     \______ |   \____/            \___/      \____/      \_____/"

    print(tictactoe)

def graphic_gameover(winner, mode):
    winner = " ___                      _____\n/\XX\        ____        / /XX/\n\ \XX\      / /XX\      / /XX/      _    ________     ________      ______      _______\n"
    winner += " \ \XX\    / /XXXX\    / /XX/      /X|  | |XXXXXX\   | |XXXXXX\    / /XXXX\    /|XXXXXX\ \n"
    winner += "  \ \XX\  / /XX/\XX\  / /XX/      |/_/  | |X|__/|X|  | |X|__/|X|  | |X|__/X|  | |X|__/|X|\n"
    winner += "   \ \XX\/ /XX/\ \XX\/ /XX/       /|X|  | |X|  ||X|  | |X|  ||X|  | |XXXXXX|  | |X|  |/_/\n"
    winner += "    \ \XX\/XX/  \ \XX\/XX/        ||X|  | |X|  ||X|  | |X|  ||X|  | |X|___/   | |X|\n"
    winner += "     \ \XXXX/    \ \XXXX/         ||X|  | |X|  ||X|  | |X|  ||X|   \ \XXXXX|  | |X|\n"
    winner += "      \/___/      \/___/          |/_/  |/__/  |/_/  |/__/  |/_/    \_____/   |/_/\n"

    looser = "  __\n/|XX|\n||XX|                                  _______     ______     _______\n"
    looser += "||XX|          ______      ______     / /XXXXX|   / /XXXX\   /|XXXXXX\ \n"
    looser += "||XX|         / /XXXX\    / /XXXX\   | |X|___/   | |X|__/X| | |X|__/|X|\n"
    looser += "||XX|        / /X/\ \X\  / /X/\ \X\   \ \XXXX\   | |XXXXXX| | |X|  |/_/\n"
    looser += "||XX|______  \ \X\/_/X/  \ \X\/_/X/    ____/|X|  | |X|___/  | |X|\n"
    looser += "||XXXXXXXXX|  \ \XXXX/    \ \XXXX/   /|XXXXXX/    \ \XXXXX| | |X|\n"
    looser += "|/________/    \____/      \____/    |______/      \_____/  |/_/\n"


    if mode == "HUMAN-AI" and winner == 0:
        print("I won!")
        looser = ""
        print(looser)
    elif mode == "HUMAN-AI":
        winner = ""
        print("Congratularions! You are the")
        for i in range(3):
            time.sleep(1)
            print(".")
        time.sleep(3)
        print(winner)
    elif winner != 3:
        which = random.radnint(1,2)
        print("Congratulations! Player" + str(which) + " is the")
        for i in range(3):
            time.sleep(1)
            print(".")
        time.sleep(3)
        if winner == which:
            print(winner)
        else:
            print(looser)

def init_board(): #Davies
    """Returns an empty 3-by-3 board (with .)."""
    board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
    return board

def get_move(board, player):
    valid = False
    while not valid:
        position = input('Choose field: ')

        if position[0].isalpha() and position[1].isnumeric():
            if position[1] <= 3 and position[1] >= 1:
                abc = ('a', 'b', 'c')
                column = -1
                for letter in range(len(abc)):
                    if position[0] == letter:
                        column == letter
                    row = int(position[1])- 1
                if column >= 0 and column < 3:
                    valid = True
                    return tuple(row, column)
        elif position == 'quit':
            quit()


def get_ai_move(board, player): #Bori
    """Returns the coordinates of a valid move for player on board."""
    sign = {1: "X", 2: "O"}
    
    for r in range(len(board)):
        if board[r][0] != "." and board[r][0] == board[r][1]:
            return r, 2
        elif board[r][1]  != "." and board[1][1] == board[r][2]:
            return r, 0
        elif board[r][0]  != "." and board[r][0] == board[r][2]:
            return r, 1
        
        if board[0][r] != "." and board[0][r] == board[1][r]:
            return 2, r
        elif board[1][r] != "." and board[1][r] == board[2][r]:
            return 0, r
        elif board[0][r] != "." and board[0][r] == board[2][r]:
            return 1, r
        
    if board[0][0]  != "." and board[0][0] == board[1][1]:
        return 2, 2
    elif board[1][1]  != "." and board[1][1] == board[2][2]:
        return 0, 0
    elif (board[0][0]  != "." and board[0][2]  != ".") and (board[0][0] == board[2][2] or board[0][2] == board[2][0]):
        return 1, 1
    elif board[0][2]  != "." and board[0][2] == board[1][1]:
        return 2, 0
    elif board[1][1]  != "." and board[1][1] == board[2][0]:
        return 0, 2
    # 1st step: Check if two in a row for me
    # 2nd step: Check if two in a row for player

    if board[1][1] == ".":
        return 1, 1
    # 3rd step: Get middle if empty

    corners = [[0,0], [2,2], [0,2], [2,0]]
    random.shuffle(corners)
    for i in corners:
        if board[i[0]][i[1]] == ".":
            return i[0], i[1]
    # 4th step: Get corner if empty

    for i in corners:
        i[0] = (i[0]+1) % 3
        i[1] = (i[1]+1) % 3
        if board[i[0]][i[1]] == ".":
            return i[0], i[1]
    # 5th What is left?

    return None


def mark(board, player, row, col): #Davies
    """Marks the element at row & col on the board for player."""
    sign = {1: "X", 2: "O"}
    board[row][col] = sign[player]


def has_won(board, player): #Bori
    """Returns True if player has won the game."""
    sign = {1: "X", 2: "O"}

    for r in range(len(board)):
        row = True
        for c in range(len(board)-1):
            if board[r][c] == sign[player]:
                if board[r][c] != board[r][c+1]:
                    row = False
        if row:
            return True

    for c in range(len(board)):
        column = True
        for r in range(len(board) - 1):
            if board[r][c] != sign[player] or board[r][c] != board[r][c+1]:
                column = False
        if column:
            return True

    diagonal_right = True
    diagonal_left = True
    for i in range(len(board)-1):        
        if board[i][i] != sign[player] or board[i][i] != board[i+1][i+1]:
            diagonal_right = False
        if board[i][-(i+1)] != sign[player] or board[i][-(i+1)] != board[i+1][-i]:
            diagonal_left = False

    return diagonal_left or diagonal_right


def is_full(board): #Bori
    """Returns True if board is full."""
    count = 0
    for r in board:
        for c in r:
            if c == ".":
                count += 1
    return count == 0

def print_board(board):
    print("   A " + "  B " + "  C")
    print( "1  " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print('  ---+---+---')
    print( "2  " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("  ---+---+---")
    print( "3  " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])

def print_result(winner, mode): #Bori
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == 0:
        print("Game Over! It's a tie.")
    else:
        #print("Congratulations, Player" + str(winner) + "! You won!")
        graphic_gameover(winner, mode)

    if input("\nDo you want to save the results?\n1: Yes\n2: No\nYour answer: ") == "1":
        if mode == "HUMAN-HUMAN":
            name1 = input("Player1, please give me your name: ")
            name2 = input("Player2, please give me your name: ")
            save(name1, name2, winner)
        elif mode == "HUMAN-AI":
            name1 = input("Please give me your name: ")
            save("Artificial Intelligence", name1, winner) #This is not good right like this. Waits for correction.
        else:
            save("Artificial Intelligence", "Artificial Intelligence", 1)
    clear_board()

    if input("Do you want to play again?\n1: Yes\n2: No\nYour answer: ") == "1":
        self.main_menu()
    else:
        print("Goodbye!")
        quit()

def save(name1, name2, winner):
    with open("results.txt", "r") as save:
        is_1 = False
        is_2 = False
        for line in save.readlines():
            content.append(line)
            if line[:len(name1)] == name1:
                is_1 = True
                score = int(line[len(name1)+1:-1])
                if winner == name1:
                    score += 1
                else:
                    score -= 1
                line = name1 + " (" + str(score) + ")"
                this_player = True
                changed = False
                n = name2
            elif this_player and line[0] == "\t":
                if line[1:len(n)+1] == n:
                    matches = int(line[len(n)+3:])
                    matches += 1
                    line= "\t" + n + ": " + str(matches) + " matches"
                    changed = True
            elif line == "" and not changed:
                this_player = False
                line = "\t" + name2 + ": " + str(1) + " matches\n"

            elif line[:len(name2)] == name2:
                is_2 = True
                score = int(line[len(name1)+1:-1])
                if winner == name2:
                    score += 1
                else:
                    score -= 1
                line = name1 + " (" + str(score) + ")"
                this_player = True
                changed = False
                n = name1
        if not is_1:
            if winner == 1:
                score = 1
            else:
                score = -1
            content.append(name1 + " (" + str(score) + ")\n\t" + name2 + ": 0")
        if not is_2:
            if winner == 2:
                score = 1
            else:
                score = -1
            content.append(name2 + " (" + str(score) + ")\n\t" + name1 + ": 0")

    with open(results.txt, "w") as save:
        new = ""
        for line in content:
            new += line + "\n"
        save.write(new)

def check_scores(*args):
    if len(args) == 0:
        with open("results.txt", "r") as load:
            print(load.read())
    else:
        name = args[0]
        this_player = False
        for line in load.readlines():
            if line[:len(name)] == name or this_player:
                print(line)
                this_player = True
            elif line == "":
                this_player = False

def tictactoe_game(mode): #Bori
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    current_player = 1
    winner = 0
    if mode == 'HUMAN-AI':
        ai_turn = random.randint(1, 2)
        print("I am Player" + ai_turn)
    else:
        ai_turn = 0

    sign = {1: "X", 2: "O"}
    while not has_won(board, current_player) and not is_full(board):
        clear_board()

        if mode == 'HUMAN-HUMAN' or current_player != ai_turn:
            print("Player" + current_player + ", it's your turn!")
            print_board(board)
            position = get_move(board, current_player)
        elif mode == 'HUMAN-AI' and current_player == ai_turn:
            print("It's my turn.")
            print_board(board)
            position = get_ai_move(board, player)
        else:
            time.sleep(1)
            print("It's " + sign[current_player] + "'s turn.")
            print_board(board)
            position = get_ai_move(board, player)
        mark(board, current_player, position[0], position[1])

        if has_won(board, current_player):
            winner = current_player
        elif is_full(board):
            winner = 3
            break
        current_player = (current_player % 2) + 1

    clear_board()
    print_board(board)
    print_result(winner, mode)


def main_menu(): #Davies
    print('[1] HUMAN vs. HUMAN')
    print('[2] HUMAN vs. AI')
    print('[3] HIGH SCORES')
    print('[0] exit')

    option = input('Enter Your option! ')
    while option != '0':
        if option == '1':
            tictactoe_game('HUMAN-HUMAN')
        elif option == '2':
            tictactoe_game('HUMAN-AI')
        elif option == '3':
            check_scores(input('Who\'s Score are you courious of? '))
            
            
if __name__ == '__main__':
    main_menu()
