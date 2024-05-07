import random
import os.path
import json
random.seed()

def draw_board(board):
    """Prints the current game board."""
    # Draw top border
    print('--' * len(board[0]) + '-')
    
    # Draw cells
    for i, row in enumerate(board):
        print('|' + '|'.join(row) + '|')
        if i != len(board) - 1:
            print('--' * len(row) + '-')
    
    # Draw bottom border
    print('--' * len(board[0]) + '-')
    pass

def welcome(board):
    """Prints the current game board."""
    print('Welcome to the "Unbeatable Noughts and Crosses" game.')
    print('\nThe board layout is shown below: ')
    draw_board(board)
    print('\nWhen prompted, enter the number corresponding to the square you want.')
    pass

def initialise_board(board):
    """Prints the current game board."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board

def get_player_move(board):
    """Gets the player's move."""
    while True:
        try:
            move = int(input('\t\t    1 2 3\n\t\t    4 5 6\nChoose your square: 7 8 9 : '))
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] == ' ':
                return row, col
            else:
                print('Cell already occupied. Try again.')
        except (ValueError, IndexError) as e:
            print(f'Error: {e}')

def choose_computer_move(board):
    """Gets the player's move."""
    available_moves = [(i,j) for i in range(3) for j in range(3) 
                       if board[i][j] == ' ']
    row, col = random.choice(available_moves)
    return row, col

def check_for_win(board, mark):
    """Checks if the player or the computer has won."""
    for i in range(3):
        # checks row
        if all (board[i][j] == mark for j in range(3)):
            # j takes the value of current element (0,1,2) 
            # on each iteration.
            return True
        
        # checks column
    for j in range(3):
        if all(board[i][j] == mark for i in range (3)):
            return True
        
    if all(board[i][i] == mark for i in range(3)):
        return True
    if all(board[i][2-i] == mark for i in range(3)):
        return True
    return False

def check_for_draw(board):
    """Checks for a draw."""
    for row in board:
        if ' ' in row:
            return False
    return True
        
def play_game(board):
    """Plays the game."""
    initialise_board(board)
    board = [[" " for _ in range(3)] for _ in range(3)]
    draw_board(board)
   
    while True: 
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)
        if check_for_win(board, 'X'):
            print('You win.')
            return 1
        if check_for_draw(board):
            print('Its a draw.')
            return 0

        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        draw_board(board)
        if check_for_win(board, 'O'):
            print('The computer wins.')
            return -1
        if check_for_draw(board):
            print('Its a draw.')
            return 0
                                
def menu():
    """Plays the game."""
    print('Enter one of the following options: ')
    print('\t1 - Play the game')
    print('\t2 - Save score in file "leaderboard.txt"')
    print('\t3 - Load and display the scores from the "leaderboard.txt"')
    print('\tq - End the program')
    print('1 , 2 , 3 or q?')
    choice = input('Enter your choice: ')
    return choice

def load_scores():
    """Plays the game."""
    leaders = {}
    if not os.path.exists('leaderboard.txt'):
        return leaders
    try:
        with open('leaderboard.txt', 'r') as file:
            leaders = json.load(file)
    except json.decoder.JSONDecodeError:
        print('Error: Unable to decode JSON data from "leaderboard.txt". File may contain invalid format.')
    return leaders
    
def save_score(score):
    """Saves the current score to the file 'leaderboard.txt'."""
    name = input('Enter your name: ')
    leaders = load_scores()
    leaders[name] = score
    with open('leaderboard.txt', 'w' ) as file:
        json.dump(leaders,file)
    return

def display_leaderboard(leaders):
    """Displays the leaderboard scores."""
    print('Leaderboard: ')
    for name, score in leaders.items():
        print(f'{name} : {score}')
    pass

