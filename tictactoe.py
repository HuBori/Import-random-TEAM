import os
import time
clear = lambda: os.system('clear')

board = [ [ '.','.','.' ],[ '.','.','.' ],[ '.','.','.' ] ]

def ask_field():
    position = input('Enter position: ')
    if position.lower() == 'a1':
        board[0][0] = 'x' or '0'
        clear()
    elif position.lower() == 'a2':
        board[1][0] = 'x' or '0'
        clear()
    elif position.lower() == 'a3':
        board[2][0] = 'x' or '0'
        clear()
    elif position.lower() == 'b1':
        board[0][1] = 'x' or '0'
        clear()
    elif position.lower() == 'b2':
        board[1][1] = 'x' or '0'
        clear()
    elif position.lower() == 'b3':
        board[2][1] = 'x'
        clear()
    elif position.lower() == 'c1':
        board[0][2] = 'x'
        clear()
    elif position.lower() == 'c2':
        board[1][2] = 'x'
        clear()
    elif position.lower() == 'c3':
        board[2][2] = 'x'
        clear()
    else:
        print('Please enter valid position! ')
        time.sleep(1)
        clear()
    print_table()



def print_table():
    print("   A " + "  B " + "  C")
    print( "1  " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print('  ---+---+---')
    print( "2  " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("  ---+---+---")
    print( "3  " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    ask_field()
    clear()


print_table()



