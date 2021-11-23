##CW1 - Queens Problem

## By Sehra Elahi, sc17s2e

##===============================================================

from __future__ import print_function
from copy import deepcopy

##===============================================================

## Make the function to print out problem info
def make_queen_problem_info(x,y):
    def queen_problem_info():
        print( "The Fill Problem -- 2D version\n",
              "Array Size: ",x,"by", y)
    return queen_problem_info

##===============================================================

#sets the board with the matrix
def queen_get_initial_state(x,y):
    return  matrix_of_zeros(y,x)

##===============================================================

## Specify the initial state (board), set to zeros:
def matrix_of_zeros(X,Y):
        return [[0 for x in range(X)] for y in range(Y)]

##===============================================================

##  Define the possible actions, set 0's (in list) to 1 in the particular position
def queen_possible_actions(state):
    ans = []
    for i in range(BOARD_X):                    # For each row
            for j in range(BOARD_Y):            # For each column
                    if state[i][j] == 0:        # if in ith row and jth col is zero, then:
                            ans.append((i,j))
    for i in range(BOARD_X):                    # add the tuple (i,j) to the answer
            for j in range(BOARD_Y):
                    if state[i][j] == 1:
                            ans.append((i,j))
    return ans                                  # return the answer, which will be a list of tuples

##===============================================================

#Successor state function
def queen_successor_state( action, state ):
    row = action[0] #sideways
    col = action[1] #up and down

    # Find the row and column that the action refers to
    newstate = deepcopy(state)
    newstate[row][col] = 2
  # Change the state in that position only to a 1
  #i is up and down
  #j is sideways

	#checking up and down, the columns
    for i in range (BOARD_X):
        if (newstate[i][col] == 0):
            newstate[i][col]= 1

    #checking sideways, the rows
    for j in range (BOARD_Y):
        if(newstate[row][j] == 0):
            newstate[row][j] = 1

    #checking downright diagonal
    i = row
    j = col
    while i<BOARD_X-1 and j<BOARD_Y-1:
        i += 1
        j += 1
        if newstate[i][j] == 0:
            newstate[i][j] = 1

    #checking upleft diagonal
    i = row
    j = col
    while i>0 and j>0:
        i -= 1
        j -= 1
        if newstate[i][j] == 0:
            newstate[i][j] = 1

    #checking upright diagonal
    i = row
    j = col
    while i<BOARD_X-1 and j<BOARD_Y-1:
        i -= 1
        j += 1
        if i >=0 and j<BOARD_Y:
            if newstate[i][j] == 0:
                newstate[i][j] = 1

    #checking downleft diagonal
    i = row
    j = col
    while i<BOARD_X-1 and j>0:
        i += 1
        j -= 1
        if j >=0 and i<BOARD_X:
            if newstate[i][j] == 0:
                newstate[i][j] = 1

    return newstate

##===============================================================

##initial successor function
def queen_initial_successor( action ):
    board = deepcopy(queen_initial_state[2])
    board[action[0]][action[1]] = 1
    return( 1, action, board )

##===============================================================

## test for goal: no 0s are left, test goal state
#check if every square is 1 or 2
def queen_goal_state( state ):
	for i in range(BOARD_X):
		for j in range(BOARD_Y):
			if state[i][j] == 0:
				return False
	print("\n")
	print ("GOAL STATE")
	print_board_state( state )
	return True

##===============================================================

##function to print out the board
def print_board_state( state ):
	board = state
	for row in board:
		for square in row:
			print( "%2i" % square, end = '' )
		print()

##===============================================================

##print problem info function
def queen_print_problem_info():
    print( "The Queens Problem (", BOARD_X, "x", BOARD_Y, "board)" )

##===============================================================

## problem specification
def make_queen_problem(x,y):
        global BOARD_X, BOARD_Y,queen_initial_state
        BOARD_X = x
        BOARD_Y = y
        queen_initial_state = queen_get_initial_state(x,y)
        return ( None,
                 make_queen_problem_info(x,y),
                 queen_initial_state,
                 queen_possible_actions,
                 queen_successor_state,
                 queen_goal_state,
                 )

##===============================================================
