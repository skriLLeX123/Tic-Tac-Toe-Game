from IPython.display import clear_output

def board_display(board):
    print(" ",end="\n")
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])



def player_input():
    marker=' '
    while marker!='X'and marker!='O':
        marker=input("Player 1: Please enter your marker 'X' or 'O': ").upper()
        
    if marker=='X':
        return ('X','O')
    else:
        return('O','X')


def place_marker(board,marker,position):
    board[position]=marker


def win_check(board,mark):
    return board[7]==board[8]==board[9]==mark or board[4]==board[5]==board[6]==mark or board[1]==board[2]==board[3]==mark or board[7]==board[4]==board[1]==mark or board[8]==board[5]==board[2]==mark or board[9]==board[6]==board[3]==mark or board[7]==board[5]==board[3]==mark or board[9]==board[5]==board[1]==mark


           

import random
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return 'Player1'
    else:
        return 'Player2'



def space_check(board,position):
    return board[position]==' '


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
    

def player_choice(board):
    
    position=0;
    while position not in range(1,10) or not space_check(board,position):
        position=int(input('Choose a postion: (1-9)'))
    print(position)
    return position
def replay():
    choice=input("Play again? Enter Yes or No")
    return choice=='Yes'
print('welcome to tic tac toe game')

#while loop to keep the game running
while True:
    
    #setup the board
    the_board=[' ']*10
    
    #selecting marker for player
    player1_marker,player2_marker=player_input()
    
    #selecting player turn
    turn=choose_first()
    print(turn+' will play first')
    
    #checking if player is ready to play game
    playgame=input("Ready to play? y or n")
    if playgame=='y':
        gameon=True
    else:
        gameon=False
    
    #if players are ready to play game
    while gameon:
        if turn=="Player1":
            print("player1 turn")
            #display the board
            board_display(the_board)
            
            #take position from player to be marked
            position=player_choice(the_board)
            
            #fill the position retrieved from above step with the marker
            place_marker(the_board,player1_marker,position)
            
            #check if player1 has won the game
            if win_check(the_board,player1_marker):
                board_display(the_board)
                print('Congratulations Player1 has won the game')
                gameon=False
            else:
                if full_board_check(the_board):
                    board_display(the_board)
                    print('Ooops game has tied')
                    gameon=False
                else:
                    turn="Player2"
        else:
            print("player1 turn")

            #display the board
            board_display(the_board)
            
            #take position from player to be marked
            position=player_choice(the_board)
            
            #fill the position retrieved from above step with the marker
            place_marker(the_board,player2_marker,position)
            
            #check if player1 has won the game
            if win_check(the_board,player2_marker):
                board_display(the_board)
                print('Congratulations Player2 has won the game')
                gameon=False
            else:
                if full_board_check(the_board):
                    board_display(the_board)
                    print('Ooops game has tied')
                    gameon=False
                else:
                    turn="Player1"
        
    
    
    
    #checking if player wants to play again if not break the while loop
    if not replay():
        break
