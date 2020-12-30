red = 0
black = 1
empty = 2

#Expected Outcome: True
row_win = [
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, red, red, red, red, empty, empty],
        [red, black, red, black, red, empty, empty],
        [black, red, black, red, black, black, empty],
        [black, black, red, black, black, red, black],
    ]
#Expected Outcome: True
col_win = [
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, red, empty, empty, empty, empty, empty],
        [black, red, empty, empty, empty, empty, empty],
        [black, red, empty, empty, empty, empty, empty],
        [black, red, black, empty, empty, empty, empty],
    ]
#Expected Outcome: True
pos_diagonal_win = [
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, red, empty, empty, empty],
        [empty, empty, red, black, empty, empty, empty],
        [black, red, red, black, black, empty, empty],
        [red, red, black, black, black, empty, empty],
    ]
#Expected Outcome: True
neg_diagonal_win = [
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty],
        [red, black, empty, empty, empty, empty, empty],
        [black, red, empty, empty, empty, empty, empty],
        [black, red, red, black, empty, empty, empty],
        [black, red, black, red, empty, empty, empty],
    ]
#Expected Outcome: True
almost_row_win = [
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, red, red, red, empty, empty, red],
        [red, black, red, black, red, black, black],
        [black, red, black, red, black, black, red],
        [black, black, red, black, black, red, black],
    ]
#Expected Outcome: True
almost_col_win = [
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty],
        [black, red, empty, empty, empty, empty, empty],
        [black, red, empty, empty, empty, empty, empty],
        [black, red, black, empty, empty, empty, empty],
    ]
#Expected Outcome: True
almost_pos_diagonal_win = [
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty],
        [black, red, red, black, empty, empty, empty],
        [black, red, red, black, empty, empty, empty],
        [red, red, black, black, black, empty, empty],
    ]
#Expected Outcome: True
almost_neg_diagonal_win = [
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty],
        [red, empty, empty, empty, empty, empty, empty],
        [black, red, empty, empty, empty, empty, empty],
        [black, red, red, empty, empty, empty, empty],
        [black, red, black, empty, empty, empty, empty],
    ]
#Expected Outcome: False    
col_loss = [
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty],
        [black, empty, empty, empty, empty, empty, empty],
        [black, red, empty, empty, empty, empty, empty],
        [black, red, empty, empty, empty, empty, empty],
        [black, red, empty, empty, empty, empty, empty],
    ]
#Expected Outcome: False (invalid board)
col_black_won_first = [
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty],
        [black, red, empty, empty, empty, empty, empty],
        [black, red, empty, empty, empty, empty, empty],
        [black, red, empty, empty, empty, empty, empty],
        [black, red, empty, empty, empty, empty, empty],
    ]
#Expected Outcome: False
black_won = [
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty],
        [black, empty, empty, empty, empty, empty, empty],
        [black, red, empty, empty, empty, empty, empty],
        [black, red, empty, empty, empty, empty, empty],
        [black, red, empty, empty, empty, empty, empty],
    ]