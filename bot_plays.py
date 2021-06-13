from random import choice, randint
from sys import platform

groups = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 4, 1], [8, 5, 2], [9, 6, 3], [7, 5, 3], [9, 5, 1]]

# groups -> Possible marks to win
# Level_1 -> The bot will make totally random moves
# Level_2 -> The bot will randomly choose between making a smart move or not
# Level_3 -> The bot will always make a smart move

def bot_turn_1(board: dict):
    # Level 1 of difficulty
    possible_movements = []

    for movement in board.items():
        if movement[1] == ' ':
            possible_movements.append(movement[0])
    move = choice(possible_movements)

    board[move] = 'X'
    return board

def bot_turn_2(board: dict):
    # Level 2 of difficulty
    smart = randint(1, 2) # 1 means smart move, 2 means not smart move

    if smart == 1:
        # Check if someone is near to a win
        for possibility in groups:
            group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
            if group.count('X') == 2 and group.count(' ') == 1: # Means that the bot is near to a win
                where = group.index(' ') # Finding where to move to win
                board[possibility[where]] = 'X'
                return board
        
        # If arrived here, it means that the bot isn't near to a win, so the bot is going to check if the player is near to a win
        for possibility in groups:
            group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
            if group.count('O') == 2 and group.count(' ') == 1: # Means that the player is near to a win
                where = group.index(' ') # Finding where to block the player
                board[possibility[where]] = 'X'
                return board

        # If arrived here, it means that anyone is near to a win, so the bot does a random play
        board = bot_turn_1(board)
        return board
    else:
        return bot_turn_1(board)