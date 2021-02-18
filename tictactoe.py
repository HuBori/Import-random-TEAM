import os
import sys
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
    clear_board()
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
    time.sleep(3)

def graphic_gameover(player, mode):
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


    if player == -1 and mode != "AI-AI":
        who = ""
        if mode == "HUMAN-AI":
            who = "We"
        elif mode == "HUMAN-HUMAN":
            who = "You"
        print("\n" + who + " both are a\n" + looser)
    elif mode == "HUMAN-AI" and player == 0:
        print("\nI won!")
        print(looser)
    elif mode == "HUMAN-AI" and player == 1:
        print("\nCongratularions! You are the")
        for i in range(3):
            time.sleep(1)
            print(".")
        time.sleep(1)
        print(winner)
    elif mode == "AI-AI":
        time.sleep(2)
        clear_board()
        print("I discussed it with myself,\nand we both agree that the result should be tie,\nso that we both are a\n")
        for i in range(3):
            time.sleep(1)
            print(".")
        time.sleep(2)
        print(winner)
        print("\n(I am so proud of myself! I should go and celebrate!)\n")
    elif winner != -1:
        print("\nCongratulations! Player" + str(player-1) + " is the")
        for i in range(3):
            time.sleep(1)
            print(".")
        time.sleep(1)
        print(winner)
    else:
        print("There is no winner, no looser, and no tie, which is weird.")
        

def init_board(): #Davies
    """Returns an empty 3-by-3 board (with .)."""
    board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
    return board

def get_move(board, player):
    valid = False
    while not valid:
        position = input('\nChoose field: ')

        if position[0].isalpha() and position[1].isnumeric():
            if int(position[1]) <= 3 and int(position[1]) >= 1:
                abc = ['a', 'b', 'c']
                column = -1
                for letter in range(len(abc)):
                    if position[0].lower() == abc[letter]:
                        column = letter
                row = int(position[1])- 1
                if column >= 0 and column < 3:
                    valid = True
                    return (row, column)
        elif position == 'quit':
            quit()


def get_ai_move(board, player): #Bori
    """Returns the coordinates of a valid move for player on board."""
    sign = {1: "X", 2: "O"}
    letters = {0: 'A', 1: 'B', 2: 'C'}

    # STEP 1
    # Check rows
    best_option = []
    for r in range(len(board)):
        if board[r][0] != "." and board[r][0] == board[r][1] and board[r][2] == ".":
            if board[r][2] == sign[player]:
                print("I chose: C" + str(r+1))
                return r, 2
            else:
                best_option = [r, 2]
        elif board[r][1]  != "." and board[1][1] == board[r][2] and board[r][0] == ".":
            if board[r][0] == sign[player]:
                print("I chose: A" + str(r+1))
                return r, 0
            else:
                best_option = [r, 0]
        elif board[r][0]  != "." and board[r][0] == board[r][2] and board[r][1] == ".":
            if board[r][1] == sign[player]:
                print("I chose: B" + str(r+1))
                return r, 1
            else:
                best_option = [r, 1]

    # Check columns    
        if board[0][r] != "." and board[0][r] == board[1][r] and board[2][r] == ".":
            if board[2][r] == sign[player]:
                print("I chose: " + letters[r] + "3")
                return 2, r
            else:
                best_option = [2, r]
        elif board[1][r] != "." and board[1][r] == board[2][r] and board[0][r] == ".":
            if board[0][r] == sign[player]:
                print("I chose: " + letters[r] + "1")
                return 0, r
            else:
                best_option = [0, r]
        elif board[0][r] != "." and board[0][r] == board[2][r] and board[1][r] == ".":
            if board[1][r] == ".":
                print("I chose: " + letters[r] + "2")
                return 1, r
            else:
                best_option = [1, r]

    # Check diagonals    
    if board[0][0]  != "." and board[0][0] == board[1][1] and board[2][2] == ".":
        if board[2][2] == sign[player]:
            print("I chose: C3")
            return 2, 2
        else:
            best_option = [2, 2]
    elif board[1][1]  != "." and board[1][1] == board[2][2] and board[0][0] == ".":
        if board[0][0] == sign[player]:
            print("I chose: A1")
            return 0, 0
        else:
            best_option = [0, 0]
    elif (board[0][0]  != "." and board[0][2]  != ".") and (board[0][0] == board[2][2] or board[0][2] == board[2][0]) and board[1][1] == ".":
        if board[1][1] == sign[player]:
            print("I chose: B2")
            return 1, 1
        else:
            best_option = [1, 1]
    elif board[0][2]  != "." and board[0][2] == board[1][1] and board[2][0] == ".":
        if board[2][0] == sign[player]:
            print("I chose: C1")
            return 2, 0
        else:
            best_option = [2, 0]
    elif board[1][1]  != "." and board[1][1] == board[2][0] and board[0][2] == ".":
        if board[0][2] == sign[player]:
            print("I chose: A3")
            return 0, 2
        else:
            best_option = [0, 2]

    if len(best_option) == 2: # If can't win, prevents loosing
        return best_option[0], best_option[1]

    # STEP 2: Get middle if empty
    if board[1][1] == ".":
        print("I chose: B2")
        return 1, 1

    #STEP 3: Get corner if empty
    corners = [[0,0], [2,2], [0,2], [2,0]]
    random.shuffle(corners)
    for i in corners:
        if board[i[0]][i[1]] == ".":
            print("I chose: " + letters[i[0]] + str(i[1]+1))
            return i[0], i[1]

    # STEP 4: Get one of the leftover fields
    for i in corners:
        i[0] = (i[0]+1) % 3
        i[1] = (i[1]+1) % 3
        if board[i[0]][i[1]] == ".":
            print("I chose: " + letters[i[0]] + str(i[1]+1))
            return i[0], i[1]

    # In the very unlikely case it doesn't do any of the above, checks if there is any empty field.
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == ".":
                print("I chose: " + letters[c] + str(r+1))
                return r, c

    # In the even more unlikely case it still hasn't chosen, lets the user know that there is a mistake.
    print("I didn't choose anything, becouse I'm stupid.")
    return None


def mark(board, player, row, col): #Davies
    sign = {1: "X", 2: "O"}
    valid = False
    while not valid:
        if board[row][col] == ".":
            board[row][col] = sign[player]
            valid = True
        else:
            print("Please give me a valid answer!")
            (row, col) = get_move(board, player)

def has_won(board, player): #Bori
    for i in range(3):
        if board[i][1] != ".":
            if board[i][0] == board[i][1] and board[i][2] == board[i][1]:
                return True
        if board[0][i] != ".":
            if board[0][i] == board[1][i] and board[2][i] == board[0][i]:
                return True
    if board[1][1] != ".":
        if board[0][0] == board[1][1] and board[2][2] == board[1][1]:
            return True
        elif board[0][2] == board[1][1] and board[2][0] == board[1][1]:
            return True
    return False


def is_full(board): #Bori
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
    if winner == -1:
        print("\nGame Over! It's a tie.")
        graphic_gameover(winner, mode)
    elif winner == 1 or winner == 2:
        graphic_gameover(winner + 1, mode)
    else:
        graphic_gameover(0, mode)

    time.sleep(2)
    clear_board()
    if input("\nDo you want to save the results?\n1: Yes\n2: No\nYour answer: ") == "1":
        if mode == "HUMAN-HUMAN":
            name1 = input("Player1, please give me your name: ")
            name2 = input("Player2, please give me your name: ")
            save(name1, name2, winner)
        elif mode == "HUMAN-AI":
            name1 = input("Please give me your name: ")
            save("Artificial Intelligence", name1, winner-1)
        else:
            save("Artificial Intelligence", "Artificial Intelligence", 0)
        play_again()
    else:
        play_again()

def save(name1, name2, winner):
    with open("results.txt", "r") as save:
        is_1 = False
        is_2 = False
        content = []
        for line in save.readlines():
            content.append(line)
            this_player = False
            if line[:len(name1)] == name1:
                is_1 = True
                sc_str = line.split('(')[1]
                sc_str = sc_str.split(")")[0]
                if "-" in sc_str:
                    score = -abs(int(sc_str[1:]))
                else:
                    score = int(sc_str)
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
                    matches = int(line[len(n)+3:-len(" matches")])
                    matches += 1
                    line= "\t" + n + ": " + str(matches) + " matches\n"
                    changed = True
            elif line == "" and not changed:
                this_player = False
                line = "\t" + name2 + ": " + str(1) + " matches\n"

            elif line[:len(name2)] == name2:
                is_2 = True
                sc_str = line.split('(')[1]
                sc_str = sc_str.split(")")[0]
                if "-" in sc_str:
                    score = -abs(int(sc_str[1:]))
                else:
                    score = int(sc_str)
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
            content.append(name1 + " (" + str(score) + ")\n\t" + name2 + ": 1 matches\n")
        if not is_2:
            if winner == 2:
                score = 1
            else:
                score = -1
            content.append(name2 + " (" + str(score) + ")\n\t" + name1 + ": 1 matches\n")

    with open('results.txt', "w") as save:
        new = ""
        for line in content:
            new += line
        save.write(new)

def check_scores(*args):
    if len(args) == 0:
        with open("results.txt", "r") as load:
            print(load.read())
            trash = input("If you read all, press ENTER!")
    else:
        name = args[0]
        this_player = False
        with open("results.txt", "r") as load:
            for line in load.readlines():
                if line[:len(name)] == name or this_player:
                    print(line)
                    this_player = True
                elif line == "":
                    this_player = False
        trash = input("If you read all, press ENTER!")

def tictactoe_game(mode): #Bori
    board = init_board()

    current_player = 1
    winner = 0
    if mode == 'HUMAN-AI':
        clear_board()
        time.sleep(1)
        ai_turn = random.randint(1, 2)
        print("I am Player" + str(ai_turn))
    else:
        ai_turn = 0

    sign = {1: "X", 2: "O"}
    while not has_won(board, current_player) and not is_full(board):
        clear_board()

        if mode == 'HUMAN-HUMAN' or (mode != 'AI-AI' and current_player != ai_turn):
            print("Player" + str(current_player) + ", it's your turn!\n")
            print_board(board)
            position = get_move(board, current_player)
        else:
            if mode == 'AI-AI':
                print("It's " + sign[current_player] + "'s turn.\n")
            else:
                print("It's my turn.\n")
            print_board(board)
            position = get_ai_move(board, current_player)
            time.sleep(1)
        mark(board, current_player, position[0], position[1])

        if is_full(board) and not has_won(board, current_player):
            clear_board()
            print_board(board)
            print_result(-1, mode)
            break
        elif has_won(board, current_player):
            clear_board()
            print_board(board)
            if mode == "HUMAN-AI" or mode == "AI-AI":
                print_result(0, mode)
            elif mode == "HUMAN-HUMAN":
                print_result(current_player, mode)
            break
        current_player = (current_player % 2) + 1
    
def graphic_menu():
    menu = ""
    menu += " ___  ___   _______   ___     _   _     _\n"
    menu += "|   \/   | |  _____| |   \   | | | |   | |\n"
    menu += "| |\__/| | | |__     | |\ \  | | | |   | |\n"
    menu += "| |    | | |  __|    | | \ \ | | | |   | |\n"
    menu += "| |    | | | |_____  | |  \ \| | | |___| |\n"
    menu += "|_|    |_| |_______| |_|   \___|  \_____/\n"
    print(menu)

def main_menu(): #Davies
    clear_board()
    graphic_menu()
    print('[1] HUMAN vs. HUMAN')
    print('[2] HUMAN vs. AI')
    print('[3] AI vs AI')
    print('[4] HIGH SCORES')
    print('[0] exit')

    option = input('Enter Your option! ')
    while option != '0':
        if option == '1':
            tictactoe_game('HUMAN-HUMAN')
            break
        elif option == '2':
            tictactoe_game('HUMAN-AI')
            break
        elif option == '3':
            tictactoe_game('AI-AI')
            break
        elif option == '4':
            check_scores(input('Who\'s Score are you courious of? '))
            break
        elif option == '0':
            print("Goodbye!")
            quit()
        else:
            clear_board()
            print('\nINVALID\n')
            main_menu()
    
def play_again():        
    clear_board()
    if input("Do you want to play again?\n1: Yes\n2: No\nYour answer: ") == "1":
        main_menu()
    else:
        print("Goodbye!")
        quit()
            
if __name__ == '__main__':
    graphic_welcome()
    main_menu()
