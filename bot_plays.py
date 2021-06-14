from random import choice

groups = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 4, 1], [8, 5, 2], [9, 6, 3], [7, 5, 3], [9, 5, 1]]
corners = [1, 3, 7, 9]
r_corners = [9, 7, 3, 1]
middles = [2, 4, 6, 8]
opposites = {
    2: [7, 9],
    4: [3, 9],
    6: [1, 7],
    8: [1, 3]
}
plays = 1
bot_last_move = 0
strategy = 0

# groups -> Possible marks to win

# This variables above will be used just in the level 3 bot
# ↳ corners -> The board corners
# ↳ r_corners -> The corners, but reversed
# ↳ middles -> The middles of the board
# ↳ plays -> The number of times that the bot played
# ↳ bot_last_move -> The last move that the bot did
# ↳ strategy -> The strategy that the bot will use, actualy, this will only be usend on the level 3 bot

# This functions bellow will always return the board given, but with the modification of the bot's move

def bot_turn_1(board: dict):
    # Level 1 of difficulty
    # This level will make totally random moves everytime
    options = []
    
    # For every house in the board, if it's empty, append it on options
    for option in board.items():
        if option[1] == ' ':
            options.append(option[0])
    move = choice(options)

    board[move] = 'X'
    return board

def bot_turn_2(board: dict):
    # Level 2 of difficulty
    # This level will draw if make a random play or a kinda smart play
    smart = choice([1, 2]) # 1 -> smart move / 2 -> not smart move

    if smart == 1:
        # Check if someone is near to a win
        for possibility in groups:
            group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
            if group.count('X') == 2 and group.count(' ') == 1: # Means that the bot is near to a win
                move = group.index(' ') # Finding where to move to win
                board[possibility[move]] = 'X'
                return board
        
        # If arrived here, it means that the bot isn't near to a win, so the bot is going to check if the player is near to a win
        for possibility in groups:
            group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
            if group.count('O') == 2 and group.count(' ') == 1: # Means that the player is near to a win
                move = group.index(' ') # Finding where to block the player
                board[possibility[move]] = 'X'
                return board

    # If arrived here, it means that anyone is near to a win or that the draw resulted in 2 so the bot does a random play
    board = bot_turn_1(board)
    return board

def bot_turn_3(board: dict, last_move: int):
    global plays, groups, bot_last_move, corners, r_corners, strategy, opposites
    # Strategy 1 and 2 is when the bot is startin the game
    # ↳ Strategy 1 -> Start from the cernter of the board
    # ↳ Strategy 2 -> Start from the corner of the board

    if last_move == 0: # It means that the bot is starting the game
        strategy = choice([1, 2])
    
    elif last_move != 0 and plays == 1: # It means that the player has already started the game
        # So we have to check if the player moved to 5, if yes, we have a problem, so, strategy 3
        if last_move == 5:
            strategy = 3

        # If the player didn't moved to 5, we had luck, so, strategy 4
        else:
            strategy = 4

    if strategy == 1: # The bot is starting, and the strategy is start from center
        if plays == 1: # If it's the first move
            board[5] = 'X'
            plays += 1
            bot_last_move = 5
            return board
    
        elif plays == 2: # If this is the second bot's move
            if last_move in corners: # If the player's first move was in the corners
                move = r_corners[corners.index(last_move)] # The bot will find the oposite side of the player's move
                board[move] = 'X'
                plays += 1
                bot_last_move = move
                return board
                
            else: # If the player's first move was in the middles, the bot will win
                move = choice(opposites[last_move])
                board[move] = 'X'
                plays += 1
                bot_last_move = move
                return board

        elif plays == 3: # If this is the third bot's move
            # First, the bot will check if someone is near to a win
            for possibility in groups:
                group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
                if group.count('X') == 2 and group.count(' ') == 1: # Means that the bot is near to a win
                    move = group.index(' ') # Finding where to move to win
                    plays += 1
                    bot_last_move = move
                    board[possibility[move]] = 'X'
                    return board
                elif group.count('O') == 2 and group.count(' ') == 1: # Means that the player is near to a win
                    move = group.index(' ') # Finding where to block the player
                    board[possibility[move]] = 'X'
                    plays += 1
                    bot_last_move = move
                    return board
            
            # If arrived here, so nobody is near to a win
            # The bot will move to the opposite side of the player's play
            for b in choice([[0, 1], [1, 0]]):
                if board[opposites[last_move][b]] == ' ':
                    board[opposites[last_move][b]] = 'X'
                    plays += 1
                    bot_last_move = opposites[last_move][b]
                    return board
        
        else: # If arrived here, it means that the game will end in a draw
            # Check if someone is near to a win
            for possibility in groups:
                group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
                if group.count('X') == 2 and group.count(' ') == 1: # Means that the bot is near to a win
                    move = group.index(' ') # Finding where to move to win
                    plays += 1
                    bot_last_move = move
                    board[possibility[move]] = 'X'
                    return board
                elif group.count('O') == 2 and group.count(' ') == 1: # Means that the player is near to a win
                    move = group.index(' ') # Finding where to block the player
                    board[possibility[move]] = 'X'
                    plays += 1
                    bot_last_move = move
                    return board

        # If arrived here, the bot will meka a random play, because the game will end in a draw
        return bot_turn_1(board)

    elif strategy == 2: # The bot is starting, and the strategy is start from the corners
        if plays == 1:
            move = choice(corners)
            board[move] = 'X'
            plays += 1
            bot_last_move = move
            return board
        
        elif plays == 2:
            if bot_last_move == 1:
                if last_move in (2, 4, 6, 8):
                    if last_move == 4:
                        move = 3
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                    elif last_move == 8:
                        move = 7
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                    elif last_move == 6:
                        move = 3
                        print(move)
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                    elif last_move == 2:
                        move = 7
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                else:
                    if last_move == 3:
                        move = 7
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                    elif last_move == 7:
                        move = 3
                        print(move)
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                    elif last_move == 9:
                        move = choice([7, 3])
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board

            elif bot_last_move == 3:
                if last_move in (2, 4, 6, 8):
                    if last_move == 4:
                        move = choice([1, 9])
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                    elif last_move == 8:
                        move = choice([3, 7])
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                    elif last_move == 6:
                        move = 1
                        print(move)
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                    elif last_move == 2:
                        move = 9
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                else:
                    if last_move == 7:
                        move = choice([1, 9])
                        print(move)
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                    elif last_move == 9:
                        move = 1
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                    elif last_move == 1:
                        move = 9
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
            
            elif bot_last_move == 7:
                if last_move in (2, 4, 6, 8):
                    if last_move == 4:
                        move = 9
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                    elif last_move == 8:
                        move = 1
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                    elif last_move == 6:
                        move = choice[1, 9]
                        print(move)
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                    elif last_move == 2:
                        move = choice([1, 9])
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                else:
                    if last_move == 3:
                        move = choice([1, 9])
                        print(move)
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                    elif last_move == 9:
                        move = 1
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                    elif last_move == 1:
                        move = 9
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
            
            else:
                if last_move in (2, 4, 6, 8):
                    if last_move == 4:
                        move = choice([3, 7])
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                    elif last_move == 8:
                        move = 3
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                    elif last_move == 6:
                        move = 7
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                    elif last_move == 2:
                        move = choice([7, 3])
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                else:
                    if last_move == 3:
                        move = 7
                        print(move)
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                    elif last_move == 7:
                        move = 3
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
                    elif last_move == 1:
                        move = choice([3, 7])
                        board[move] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board

            if bot_last_move == 1:
                board[9] = 'X'
                plays += 1
                bot_last_move = 9
                return board
            
            elif bot_last_move == 3:
                board[7] = 'X'
                plays += 1
                bot_last_move = 7
                return board
            
            elif bot_last_move == 7:
                board[3] = 'X'
                plays += 1
                bot_last_move = 3
                return board
            
            elif bot_last_move == 9:
                board[1] = 'X'
                plays += 1
                bot_last_move = 1
                return board

        elif plays == 3:
            for possibility in groups:
                group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
                if group.count('X') == 2 and group.count(' ') == 1: # Means that the bot is near to a win
                    move = group.index(' ') # Finding where to move to win
                    board[possibility[move]] = 'X'
                    plays += 1
                    bot_last_move = move
                    return board
            
            for possibility in groups:
                group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
                if group.count('O') == 2 and group.count(' ') == 1: # Means that the player is near to a win
                    move = group.index(' ') # Finding where to block the player
                    board[possibility[move]] = 'X'
                    plays += 1
                    bot_last_move = move
                    return board
            
            board[5] = 'X'
            bot_last_move = 5
            plays += 1
            return board
        
        else:
            for possibility in groups:
                group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
                if group.count('X') == 2 and group.count(' ') == 1: # Means that the bot is near to a win
                    move = group.index(' ') # Finding where to move to win
                    board[possibility[move]] = 'X'
                    plays += 1
                    bot_last_move = move
                    return board
            
            for possibility in groups:
                group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
                if group.count('O') == 2 and group.count(' ') == 1: # Means that the player is near to a win
                    move = group.index(' ') # Finding where to block the player
                    board[possibility[move]] = 'X'
                    plays += 1
                    bot_last_move = move
                    return board

        return bot_turn_1(board)

    elif strategy == 3: # The player is starting, and the strategy is start from the center
        if plays == 1:
            if last_move == 5:
                move = choice(corners)
                board[move] = 'X'
                plays += 1
                bot_last_move = move
                return board
        
        elif plays == 2:
            for possibility in groups:
                group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
                if group.count('X') == 2 and group.count(' ') == 1: # Means that the bot is near to a win
                    move = group.index(' ') # Finding where to move to win
                    board[possibility[move]] = 'X'
                    plays += 1
                    bot_last_move = move
                    return board
            
            for possibility in groups:
                group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
                if group.count('O') == 2 and group.count(' ') == 1: # Means that the player is near to a win
                    move = group.index(' ') # Finding where to block the player
                    board[possibility[move]] = 'X'
                    plays += 1
                    bot_last_move = move
                    return board
            
            if last_move in corners and board[5] == 'O':
                if bot_last_move in (1, 9):
                    if board[3] == ' ':
                        board[3] = 'X'
                        plays += 1
                        bot_last_move = 7
                        return board
                    elif board[7] == ' ':
                        board[7] = 'X'
                        plays += 1
                        bot_last_move = 7
                        return board
                
                elif bot_last_move in (3, 7):
                    if board[1] == ' ':
                        print('a')
                        board[1] = 'X'
                        plays += 1
                        bot_last_move = 1
                        return board
                    elif board[9] == ' ':
                        print('b')
                        board[9] = 'X'
                        plays += 1
                        bot_last_move = 9
                        return board

            elif last_move in middles  and board[5] == 'O':
                for possibility in groups:
                    group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
                    if group.count('X') == 2 and group.count(' ') == 1: # Means that the bot is near to a win
                        move = group.index(' ') # Finding where to move to win
                        board[possibility[move]] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
            
                for possibility in groups:
                    group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
                    if group.count('O') == 2 and group.count(' ') == 1: # Means that the player is near to a win
                        move = group.index(' ') # Finding where to block the player
                        board[possibility[move]] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board

        else:
            for possibility in groups:
                group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
                if group.count('X') == 2 and group.count(' ') == 1: # Means that the bot is near to a win
                    move = group.index(' ') # Finding where to move to win
                    board[possibility[move]] = 'X'
                    plays += 1
                    bot_last_move = move
                    return board
            
            for possibility in groups:
                group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
                if group.count('O') == 2 and group.count(' ') == 1: # Means that the player is near to a win
                    move = group.index(' ') # Finding where to block the player
                    board[possibility[move]] = 'X'
                    plays += 1
                    bot_last_move = move
                    return board

        return bot_turn_1(board)

    elif strategy == 4: # The player is starting, and the strategy is start from the corners
        if plays == 1:
            board[5] = 'X'
            plays += 1
            bot_last_move = 5
            return board
        
        elif plays == 2:
            if last_move in corners: 
                for possibility in groups:
                    group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
                    if group.count('O') == 2 and group.count(' ') == 1: # Means that the player is near to a win
                        move = group.index(' ') # Finding where to block the player
                        board[possibility[move]] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
            
                move = choice(middles)
                board[move] = 'X'
                plays += 1
                bot_last_move = move
                return board
            
            else:
                for possibility in groups:
                    group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
                    if group.count('O') == 2 and group.count(' ') == 1: # Means that the player is near to a win
                        move = group.index(' ') # Finding where to block the player
                        board[possibility[move]] = 'X'
                        plays += 1
                        bot_last_move = move
                        return board
        
        else:
            for possibility in groups:
                group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
                if group.count('X') == 2 and group.count(' ') == 1: # Means that the bot is near to a win
                    move = group.index(' ') # Finding where to move to win
                    board[possibility[move]] = 'X'
                    plays += 1
                    bot_last_move = move
                    return board
            
            for possibility in groups:
                group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
                if group.count('O') == 2 and group.count(' ') == 1: # Means that the player is near to a win
                    move = group.index(' ') # Finding where to block the player
                    board[possibility[move]] = 'X'
                    plays += 1
                    bot_last_move = move
                    return board

        return bot_turn_1(board)

def reset():
    global plays, bot_last_move, strategy
    strategy = 0
    plays = 1
    bot_last_move = 0
