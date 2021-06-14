from random import choice, randint

groups = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 4, 1], [8, 5, 2], [9, 6, 3], [7, 5, 3], [9, 5, 1]]
corners = [1, 3, 7, 9]
middles = [2, 4, 6, 8]
r_corners = [9, 7, 3, 1]
plays = 1
bot_last_move = 0
strategy = 0
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

def bot_turn_3(board: dict, last_move: int):
    global plays, groups, bot_last_move, corners, r_corners, strategy

    if last_move == 0: # Means that the bot is starting the game
        strategy = choice([1, 2])
    
    elif last_move != 0 and plays == 1:
        if last_move == 5:
            strategy = 3
        else:
            strategy = 4

    if strategy == 1: # The bot is starting, and the strategy is start from center
        if plays == 1:
            board[5] = 'X'
            plays += 1
            bot_last_move = 5
            return board
    
        elif plays == 2: # If this is the second bot's move
            if last_move in corners: # If the player's first move was in the corners
                move = r_corners[corners.index(last_move)]
                board[move] = 'X'
                plays += 1
                bot_last_move = move
                return board
                
            else: # If the player's first move was in the middles
                if last_move == 4:
                    move = choice([9, 3])
                    board[move] = 'X'
                    plays += 1
                    bot_last_move = move
                    return board
                elif last_move == 8:
                    move = choice([1, 3])
                    board[move] = 'X'
                    plays += 1
                    bot_last_move = move
                    return board
                elif last_move == 6:
                    move = choice([1, 7])
                    print(move)
                    board[move] = 'X'
                    plays += 1
                    bot_last_move = move
                    return board
                elif last_move == 2:
                    move = choice([7, 9])
                    board[move] = 'X'
                    plays += 1
                    bot_last_move = move
                    return board

        elif plays == 3: # If this is the third bot's move
            for possibility in groups:
                group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
                if group.count('X') == 2 and group.count(' ') == 1: # Means that the bot is near to a win
                    move = group.index(' ') # Finding where to move to win
                    plays += 1
                    bot_last_move = move
                    board[possibility[move]] = 'X'
                    return board
            
            for possibility in groups:
                group = (board[possibility[0]], board[possibility[1]], board[possibility[2]])
                if group.count('O') == 2 and group.count(' ') == 1: # Means that the player is near to a win
                    move = group.index(' ') # Finding where to block the player
                    board[possibility[move]] = 'X'
                    plays += 1
                    bot_last_move = move
                    return board
            
            if last_move == 4:
                if board[9] == ' ':
                    board[9] = 'X'
                    plays += 1
                    bot_last_move = 9
                    return board
                elif board[3] == ' ':
                    board[3] = 'X'
                    plays += 1
                    bot_last_move = 3
                    return board
            elif last_move == 8:
                if board[1] == ' ':
                    board[1] = 'X'
                    plays += 1
                    bot_last_move = 1
                    return board
                elif board[3] == ' ':
                    board[3] = 'X'
                    plays += 1
                    bot_last_move = 3
                    return board
            elif last_move == 6:
                if board[1] == ' ':
                    board[1] = 'X'
                    plays += 1
                    bot_last_move = 1
                    return board
                elif board[7] == ' ':
                    board[7] = 'X'
                    plays += 1
                    bot_last_move = 7
                    return board
            elif last_move == 2:
                if board[7] == ' ':
                    board[7] = 'X'
                    plays += 1
                    bot_last_move = 7
                    return board
                elif board[9] == ' ':
                    board[9] = 'X'
                    plays += 1
                    bot_last_move = 9
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
