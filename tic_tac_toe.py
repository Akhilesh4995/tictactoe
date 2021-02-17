#Implementation of Two Player Tic-Tac-Toe game in Python.
#Importing regular expression library to validate the input.
import re
''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

gameBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in gameBoard:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Now we'll write the main function which has all the gameplay functionality.
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(gameBoard)
        print(turn + " Choose your move")

        move = input()
        validateInput = re.search("[1-9]",move)
        if validateInput and int(move) < 10:
            if gameBoard[move] == ' ':
                gameBoard[move] = turn
                count += 1
            else:
           	    print("That place is already filled.\nMove to which place?")
           	    continue
        	# Now we will check if player X or O has won,for every move after 5 moves. 
            if count >= 5:
                if gameBoard['7'] == gameBoard['8'] == gameBoard['9'] != ' ': # across the top
                    printBoard(gameBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")                
                    break
                elif gameBoard['4'] == gameBoard['5'] == gameBoard['6'] != ' ': # across the middle
                    printBoard(gameBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break
                elif gameBoard['1'] == gameBoard['2'] == gameBoard['3'] != ' ': # across the bottom
                    printBoard(gameBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break
                elif gameBoard['1'] == gameBoard['4'] == gameBoard['7'] != ' ': # down the left side
                    printBoard(gameBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break
                elif gameBoard['2'] == gameBoard['5'] == gameBoard['8'] != ' ': # down the middle
                    printBoard(gameBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break
                elif gameBoard['3'] == gameBoard['6'] == gameBoard['9'] != ' ': # down the right side
                    printBoard(gameBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break 
                elif gameBoard['7'] == gameBoard['5'] == gameBoard['3'] != ' ': # diagonal
                    printBoard(gameBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break
                elif gameBoard['1'] == gameBoard['5'] == gameBoard['9'] != ' ': # diagonal
                    printBoard(gameBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break 

        	# If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
            if count == 9:
                print("\nGame Over.\n")                
                print("It's a Tie!!")
                break
        else:
            print("Invalid input")
            break

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            gameBoard[key] = " "

        game()

if __name__ == "__main__":
    game()