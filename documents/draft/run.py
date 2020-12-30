
from nnf import Var
from lib204 import Encoding

#This project will return the position of the win if the player (red circle) has won the game. 
#The positions of the red circle will correlate with a model where the red circles must make up a #line of four red circles to win a game. 
#If this model does not exist, then the player has not won (yet).

#This function will take an encoding of the board and test it against the variables to see if
# it is a model of red winning
def check_win(map_of_board):

# Call your variables whatever you want
Xij = Var('Red disk mark')
Yij = Var('Black disk mark')    #NEED TO MAKE X, Y, AND Z LIST TO USE COORDINATES PROPERLY
Zij = Var('Empty mark')

Rij = Var('Row win')
Cij = Var('Column win')
D1ij = Var('Diagonal win w. positive slope')
D2ij = Var('Diagonal win w. negative slope')
Eij = Var('Almost winning row')
Fij = Var('Almost winning column')
G1ij = Var('Almost winning diagonal w. positive slope')
G2ij = Var('Almost winning diagonal w. negative slope')

x = [][]
for i in range(6):
    for j in range(7):
        x[i][j] =  nil)

def run_project():

    #this function will run a simulation to see how many possible solutions there is to the 
    #model
    #returns int
    def count_total_solutions():
	
		#This will create all possible models (2d mappings) of the game
		#returns a list of models

#
# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():
    Rij = Encoding()
    Rij.add_constraint(x[i][j] & x[i][j+1] & x[i][j+2] & x[i][j+3])
    return Rij

    Cij = Encoding()
    Cij.add_constraint(x[i][j] & x[i+1][j] & x[i+2][j] & x[i+3][j])
    return Cij

    D1ij = Encoding()
    D1ij.add_constraint(x[i][j] & x[i+1][j+1] & x[i+2][j+2] & x[i+3][j+3])
    return D1ij

    D2ij = Encoding()
    D2ij.add_constraint(x[i][j] & x[i+1][j-1] & x[i+2][j-2] & x[i+3][j-3])
    return D2ij

    #Eij = Encoding()
    #Eij.add_constraint(x[i][j] & x[i][j+1] & x[i][j+2] & Zi(j-1) & Zi(j+3))
    #return Eij

    #Fij = Encoding()
    #Fij.add_constraint(x[(i,j)] & x[(i+1,j)]& x[(i+2,j)] & Z(i-1)j & Z(i+3)j)
    #return Fij

    #G1ij = Encoding()
    #G1ij.add_constraint(x[(i,j)] & x[(i+1,j+1)] & x[(i+2,j+2)] & Z(i+3)(j+3) & Z(i-1)(j-1))
    #return G1ij

    #G2ij = Encoding()
    #G2ij.add_constraint(x[(i,j)] & x[(i+1,j-1)] & x[(i+2,j-2)] & Z(i+3)(j-3) & Z(i-1)(j+1))
    #return G2ij

#QUESTION: given that there is 3 possibilities for any position (red,black,empty), this
#would mean that are (7x6 sized board) = 3^(42) possibilities, that is too much for a
#computer to handle how would you want us to find all the solutions to our model?
def create_models():

    Var(all_possibilities) = create_models()
    Var(number_of_solutions):
    int = 0

#Add a for loop here:
for index in all_possibilities:
    if check_win(index) == true
	Number_of_solutions +=1

return number_of_solutions


def print_statements():
#add any other print statements below
    Total_solutions = count_total_solutions

    print(“The total number of solutions are” + total_solutions)

print_statements()

# Other Questions below
#How would we compute the likelihood a variable is true across all satisfying assignments?
#does this mean we would compute how likely it is that a variable is true with all it's constraints as 
#in for every row? In connect-4 there can only be one win so if maybe we can compute how likely it is #for a certain model, for our variable to be true, for example if the model was all empty except for #the bottom row, the variable signifying row_wins will be a certain number, but vertical and all other #wins will be 0%?

if __name__ == "__main__":

    T = example_theory()

    print("\nSatisfiable: %s" % T.is_satisfiable())
    print("# Solutions: %d" % T.count_solutions())
    print("   Solution: %s" % T.solve())

    print("\nVariable likelihoods:")
    for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        print(" %s: %.2f" % (vn, T.likelihood(v)))
    print()
