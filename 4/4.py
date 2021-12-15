bingo = open('input').readlines()

numbers = list(map(int,bingo[0].strip().split(",")))
boards = []
for i in range(2,len(bingo),6):
    boards.append([
        list(map(int,row.strip().split())) for row in
        bingo[i:i+5]
        ]
    )



def board_complete(board):
    for i in range(len(board)):
        if all(_ < 0 for _ in board[i]):
            return f"row {i}"
        if all(board[_][i] < 0 for _ in range(len(board))):
            return f"column {i}"
    # if all(board[i][i] < 0 for i in range(len(board))) or all(board[i][i] < 0 for i in range(len(board))):
    #     return "main diag"
    # if all(board[i][len(board)-1-i] < 0 for i in range(len(board))) or all(board[i][i] < 0 for i in range(len(board))):
    #     return "2nd diag"
    return False


def update_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == n:
                board[i][j] = board[i][j] = -0.001 if n == 0 else -n
                return board_complete(board)
    return False

complete = [False]*len(boards)
for n in numbers:

    for b,board in enumerate(boards):
        if complete[b]: continue
        complete[b] = update_board(board)
        if complete[b]:
            if sum(bool(_) for _ in complete) in (len(boards),1) :
                s = sum(board[i][j] for i in range(len(board)) for j in range(len(board)) if board[i][j] > 0)
                print(s * n)
