from nnf import Var, true, false, Or
from lib204 import Encoding
import sampleboards

# This project will return true if the player (red circle) has won the game.
# If this model does not exist, then the player has not won (yet).
# As regular rules, black goes first


#####################
# IMPORT YOUR BOARD INTO HERE!!!!!!!
# Use sampleboards.py to create your own boards, or use some of the pre-created ones
initial_board = sampleboards.row_win
######################

red = 0
black = 1
empty = 2

Zij = false
Xij = true

# Initializing variables
Xij = Var('Red disk mark')
Yij = Var('Black disk mark')  # NEED TO MAKE X, Y, AND Z LIST TO USE COORDINATES PROPERLY
Zij = Var('Empty mark')

Rij = Var('Row win')
Cij = Var('Column win')
D1ij = Var('Diagonal win w. positive slope')
D2ij = Var('Diagonal win w. negative slope')

Eij = Var('Almost winning row')
Fij = Var('Almost winning column')
G1ij = Var('Almost winning diagonal w. positive slope')
G2ij = Var('Almost winning diagonal w. negative slope')

# This is for black, because red cannot win in its next turn if black has already won
Mij = Var('Almost winning row')
Nij = Var('Almost winning column')
O1ij = Var('Almost winning diagonal w. positive slope')
O2ij = Var('Almost winning diagonal w. negative slope')


# This creates a model for red, and for black
def create_boards(board):
    Yij = false
    Xij = true
    Zij = false

    boardXij = [[Zij, Zij, Zij, Zij, Zij, Zij, Zij],
                [Zij, Zij, Zij, Zij, Zij, Zij, Zij],
                [Zij, Zij, Zij, Zij, Zij, Zij, Zij],
                [Zij, Zij, Zij, Zij, Zij, Zij, Zij],
                [Zij, Zij, Zij, Zij, Zij, Zij, Zij],
                [Zij, Zij, Zij, Zij, Zij, Zij, Zij]]

    boardYij = [[Zij, Zij, Zij, Zij, Zij, Zij, Zij],
                [Zij, Zij, Zij, Zij, Zij, Zij, Zij],
                [Zij, Zij, Zij, Zij, Zij, Zij, Zij],
                [Zij, Zij, Zij, Zij, Zij, Zij, Zij],
                [Zij, Zij, Zij, Zij, Zij, Zij, Zij],
                [Zij, Zij, Zij, Zij, Zij, Zij, Zij]]

    for i in range(6):
        for j in range(7):
            if board[i][j] == 0:
                boardXij[i][j] = Xij
                boardYij[i][j] = Yij

            elif board[i][j] == 1:
                boardXij[i][j] = Yij
                boardYij[i][j] = Xij

    return [boardXij, boardYij]


# The model where Xij is true
boardXij = create_boards(initial_board)[0]

# The model where Yij is true
boardYij = create_boards(initial_board)[1]


# Finds the first empty position for a given column. Returns None if it is full
def position_of_first_empty(coloumn):
    for i in [5, 4, 3, 2, 1, 0]:
        if (boardXij[i][coloumn] == Zij) & (boardYij[i][coloumn] == Zij):
            return i
    return None


# Creates a possibility for every next possible move for red
def create_almost_win_boards():
    current_list = []

    for j in range(7):
        new_board = boardXij
        if position_of_first_empty(j) is None:
            continue
        else:
            row = position_of_first_empty(j)
            new_board[row][j] = Xij
        current_list.append(new_board)

    return current_list


almost_win_list = create_almost_win_boards()


# Returns true if it is reds turn next
def is_reds_turn_next():
    red_counter = 0
    black_counter = 0

    for i in range(6):
        for j in range(7):
            if boardXij[i][j] == Xij:  # NEED TO MAKE SURE ITS COMPARING XIJ WITH XIJ AND NOT XIJ WITH FALSE!!!!!
                red_counter += 1
            elif boardYij[i][j] == Xij:
                black_counter += 1

    if red_counter == black_counter:
        return false
    elif (red_counter + 1) == black_counter:
        return true

    # Comment out the next 3 lines if you wish to ignore this problem
    else:
        print("Attention! The board you have inputted does not have a legal amount of chips!")
        return false


# Creates the theory
# It is mainly composed of 3 parts
# - Regular player wins
# ------ If it is reds turn to play next, then:
# - Add constraints for almost wins
# - Make constraints so that black could not have previously won
def example_theory(board, boardYij):
    Xij = true
    Zij = false
    Yij = false

    E = Encoding()

    ######################
    # Opponent wins (negated) #
    # If Opponent has won, red can not win on its next turn #
    ######################

    opponent_cannot_win_constraints = []
    for i in range(6):
        for j in range(4):
            Mij = (boardYij[i][j] & boardYij[i][j + 1]) & (boardYij[i][j + 2] & boardYij[i][j + 3])
            opponent_cannot_win_constraints.append(Mij)

    # column win constraints
    for j in range(7):
        for i in range(3):
            Nij = (boardYij[i][j] & boardYij[i + 1][j]) & (boardYij[i + 2][j] & boardYij[i + 3][j])
            opponent_cannot_win_constraints.append(Nij)

    # Diagonal win w. positive slope
    for i in range(3):
        for j in range(4):
            O1ij = (boardYij[i + 3][j] & boardYij[i + 2][j + 1]) & (boardYij[i + 1][j + 2] & boardYij[i][j + 3])
            opponent_cannot_win_constraints.append(O1ij)

    # Diagonal win w. negative slope
    for i in range(3):
        for j in range(4):
            O2ij = (boardYij[i][j] & boardYij[i + 1][j + 1]) & (boardYij[i + 2][j + 2] & boardYij[i + 3][j + 3])
            opponent_cannot_win_constraints.append(O2ij)

    # MOST IMPORTANT LINE is beLOW!!!!!!!!!!!!!
    for c in opponent_cannot_win_constraints:
        E.add_constraint(c.negate())

    ######################
    #  Our Player wins   #
    ######################

    # row win constraints
    total_constraints = []

    for i in range(6):
        for j in range(4):
            Rij = (board[i][j] & board[i][j + 1]) & (board[i][j + 2] & board[i][j + 3])
            total_constraints.append(Rij)

    # column win constraints
    for j in range(7):
        for i in range(3):
            Cij = ((board[i][j] & board[i + 1][j]) & (board[i + 2][j] & board[i + 3][j]))
            total_constraints.append(Cij)

    # Diagonal win w. positive slope
    for i in range(3):
        for j in range(4):
            D1ij = (board[i + 3][j] & board[i + 2][j + 1] & board[i + 1][j + 2] & board[i][j + 3])
            total_constraints.append(D1ij)

    # Diagonal win w. negative slope
    for i in range(3):
        for j in range(4):
            D2ij = (board[i][j] & board[i + 1][j + 1] & board[i + 2][j + 2] & board[i + 3][j + 3])
            total_constraints.append(D2ij)

    #
    if not is_reds_turn_next():
        for i in range(len(total_constraints)):
            disjunct_total_constraints = Or(total_constraints)
            E.add_constraint(disjunct_total_constraints)
        return E

    ####################
    # ALMOST WINS #
    ####################
    for newBoard in almost_win_list:
        for i in range(6):
            for j in range(4):
                Eij = (newBoard[i][j] & newBoard[i][j + 1]) & (newBoard[i][j + 2] & newBoard[i][j + 3])
                total_constraints.append(Eij)

        # coloumn win constraints

        for j in range(7):
            for i in range(3):
                Cij = ((newBoard[i][j] & newBoard[i + 1][j]) & (newBoard[i + 2][j] & newBoard[i + 3][j]))
                total_constraints.append(Cij)

        # Diagonal win w. positive slope

        for i in range(3):
            for j in range(4):
                D1ij = (newBoard[i + 3][j] & newBoard[i + 2][j + 1] & newBoard[i + 1][j + 2] & newBoard[i][j + 3])
                total_constraints.append(D1ij)

        # Diagonal win w. negative slope

        for i in range(3):
            for j in range(4):
                D2ij = (newBoard[i][j] & newBoard[i + 1][j + 1] & newBoard[i + 2][j + 2] & newBoard[i + 3][j + 3])
                total_constraints.append(D2ij)

        for i in range(len(total_constraints)):
            disjunct_total_constraints = Or(total_constraints)
            E.add_constraint(disjunct_total_constraints)
    return E

if __name__ == "__main__":
    almost_win_list = create_almost_win_boards()

    Xij = true
    Zij = false
    Yij = false

    Model = example_theory(boardXij, boardYij)

    print("\nSatisfiable: %s" % Model.is_satisfiable())
