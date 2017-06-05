def countBattleships(self, board):

    """
    :type board: List[List[str]]
    :rtype: int
    """

    rows = len(board)
    cols = len(board[0])
    total = 0
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'X':
                count = 1
                # check if the entery is valid, no Battleships should be adjacent
                if i>0 and board[i-1][j] == 'X':
                    count = 0
                if j>0 and board[i][j-1] == 'X':
                    count = 0
                total += count
    return total
