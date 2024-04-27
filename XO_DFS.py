'''
DFS Tic Tac Toe
in this code I implemented the DFS algorithm in a simple tic tac toe game.
the player starts playing and then the computer starts navigating the possible plays
to return the best move possible, through the minmax function which itrates all the 
possibilties and return the worst outcome the computer could reach if it followed this bath.
meaning it thinks you are really smart so it plays against you also depending that you would
choose the right choice so it would play upon it.
but of course if you made a stupid move it will have the way to win
give it a try <3
'''


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def check_winner(board, player):
    for row in board:
        if row.count(player) == 3:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def dfs(board, depth, O_turn):
    if check_winner(board, "X"):
        return -1
    if check_winner(board, "O"):
        return 1
    if len(get_available_moves(board)) == 0:
        return 0

    if O_turn:
        max_eval = float('-inf')
        for move in get_available_moves(board):
            row, col = move
            board[row][col] = "O"
            eval = dfs(board, depth+1, False)
            board[row][col] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(board):
            row, col = move
            board[row][col] = "X"
            eval = dfs(board, depth+1, True)
            board[row][col] = " "
            min_eval = min(min_eval, eval)
        return min_eval

def computer_move(board):
    best_score = float('-inf')
    best_move = None

    for move in get_available_moves(board):
        row, col = move
        board[row][col] = "O"
        score = dfs(board, 0, False)
        board[row][col] = " "

        if score > best_score:
            best_score = score
            best_move = move

    return best_move

def play_game():
    board = [[" " for i in range(3)] for i in range(3)]
    player = "X"
    computer = "O"
    
    while True:
        print_board(board)

        if len(get_available_moves(board)) == 0:
            print("It's a draw!")
            break
        
        if player == "X":
            while (True):
                row = int(input("Enter row (1, 2, or 3): "))-1
                col = int(input("Enter column (1, 2, or 3): "))-1
                if ((row==0 or row==1 or row==2) and (col==0 or col==1 or col==2)):
                    break
                else:
                    print("please enter the values again, and right this time")
                    continue
        else:
            row, col = computer_move(board)
            
        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"{player} wins!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    play_game()
