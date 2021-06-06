# TicTacToe

the_board = {7: ' ', 8: ' ', 9: ' ',
            4: ' ', 5: ' ', 6: ' ',
            1: ' ', 2: ' ', 3: ' '}
theBoard = the_board.copy()


def draw_board(board):
    print(f'''
    {board[7]}|{board[8]}|{board[9]}
    -+-+-
    {board[4]}|{board[5]}|{board[6]}
    -+-+-
    {board[1]}|{board[2]}|{board[3]}''')

def restart():
    if game_over:
        res = input('Restart?(y/n): ')
        if res.lower() == 'y':
            global theBoard
            theBoard = the_board.copy()
            game()
        elif res.lower() == "n":
            print("thanks for playing!!!".title())
        else:
            print("please enter a valid input!")
            restart()

    
    
def game():
    turn = 'O'
    count = 9
    global game_over
    game_over = False
    
    
    def tw(): # short for "{turn} wins"
        print(f""" _________ 
|{turn} wins!! |
|Game Over|
-----------""")

        global game_over
        game_over = True


    def check_winner():
        
        if theBoard[7] == theBoard[8] == theBoard[9] != ' ':
            tw()
        elif theBoard[4] == theBoard[5] == theBoard[6] != ' ':
            tw()
        elif theBoard[1] == theBoard[2] == theBoard[3] != ' ':
            tw()
            
        elif theBoard[7] == theBoard[4] == theBoard[1] != ' ':
            tw()
        elif theBoard[8] == theBoard[5] == theBoard[2] != ' ':
            tw()
        elif theBoard[9] == theBoard[6] == theBoard[3] != ' ':
            tw()
            
        elif theBoard[7] == theBoard[5] == theBoard[3] != ' ':
            tw()
        elif theBoard[1] == theBoard[5] == theBoard[9] != ' ':
            tw()

# Game Loop

    while count > 0 and not game_over:
            
        draw_board(theBoard)
        inp = int(input(f"{turn}'s turn. Where to move?: "))
        
        if inp in theBoard and theBoard[inp] == ' ':
            theBoard[inp] = turn
            count -= 1

            check_winner()
            
            if turn == 'O':
                turn = 'X'
            else:
                turn = 'O'
        else:
            print("Invalid Move.".upper())
            
    else:
        draw_board(theBoard)
        if count <= 0 and not game_over:        
            print("It's a tie.")
    restart()
    

if __name__ == "__main__":
    game()
    
