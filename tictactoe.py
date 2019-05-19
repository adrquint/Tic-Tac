#!usr/bin/env python

# a function that displays the status of the grid
def show_grid(grid):
    row1 = grid[0]
    row2 = grid[1]
    row3 = grid[2]
    
    for space in row1:
        print(space, end = "")
    print()

    for space in row2:
        print(space, end = "")
    print()

    for space in row3:
        print(space, end = "")
    print( )
    

# a function that checks if there is a winner
# after every turn
def check_for_win(grid):
    row1 = grid[0]
    row2 = grid[1]
    row3 = grid[2]

    column1 = [row1[0],row2[0],row3[0]]
    column2 = [row1[1],row2[1],row3[1]]
    column3 = [row1[2],row2[2],row3[2]]

    diagonal_1 = [row1[0],row2[1],row3[2]]
    diagonal_2 = [row3[0],row2[1],row1[2]]

    win = False

    #checking to see if x's won
    if row1 == ["|_x_|","_x_","|_x_|"]:
        winner = 'x'
        win = True
    if row2 == ["|_x_|","_x_","|_x_|"]:
        winner = 'x'
        win = True
    if row3 == ["| x |"," x ","| x |"]:
        winner = 'x'
        win = True
    if column1 == ["|_x_|","|_x_|","| x |"]:
        winner = 'x'
        win = True
    if column2 == ["_x_","_x_"," x "]:
        winner = 'x'
        win = True
    if column3 == ["|_x_|","|_x_|","| x |"]:
        winner = 'x'
        win = True
    if diagonal_1 == ["|_x_|","_x_","| x |"]:
        winner = 'x'
        win = True
    if diagonal_2 == ["| x |","_x_","|_x_|"]:
        winner = 'x'
        win = True

    #checking to see if o's won
    if row1 == ["|_o_|","_o_","|_o_|"]:
        winner = 'o'
        win = True
    if row2 == ["|_o_|","_o_","|_o_|"]:
        winner = 'o'
        win = True
    if row3 == ["| o |"," o ","| o |"]:
        winner = 'o'
        win = True
    if column1 == ["|_o_|","|_o_|","| o |"]:
        winner = 'o'
        win = True
    if column2 == ["_o_","_o_"," o "]:
        winner = 'o'
        win = True
    if column3 == ["|_o_|","|_o_|","| o |"]:
        winner = 'o'
        win = True
    if diagonal_1 == ["|_o_|","_o_","| o |"]:
        winner = 'o'
        win = True
    if diagonal_2 == ["| o |","_o_","|_o_|"]:
        winner = 'o'
        win = True
        

    return win


# resets the grid to be empty
def reset_grid(grid):
    grid = [["|___|","___","|___|"],
            ["|___|","___","|___|"],
            ["|   |","   ","|   |"]]
    return grid


# a function that checks if a space is empty or not
def is_empty(grid, choice):
    isEmpty = True
    if choice.lower() == 'a':
        space = grid[0][0]
    if choice.lower() == 'b':
        space = grid[0][1]
    if choice.lower() == 'c':
        space = grid[0][2]
    if choice.lower() == 'd':
        space = grid[1][0]
    if choice.lower() == 'e':
        space = grid[1][1]
    if choice.lower() == 'f':
        space = grid[1][2]
    if choice.lower() == 'g':
        space = grid[2][0]
    if choice.lower() == 'h':
        space = grid[2][1]
    if choice.lower() == 'i':
        space = grid[2][2]
        
    O = "o"
    X = "x"
    if X in space:
        isEmpty = False
    if O in space:
        isEmpty = False
    

    return isEmpty
    
    



def main():

    print("Let's play some tic tac toe!\n")
    play_again = 'y'
    
    grid = [["|___|","___","|___|"],
            ["|___|","___","|___|"],
            ["|   |","   ","|   |"]]

    letterGrid = [["|_a_|","_b_","|_c_|"],
                  ["|_d_|","_e_","|_f_|"],
                  ["| g |"," h ","| i |"]]

    
    xturn = True    # a boolean variable that checks if it is x's
                    # turn or not
    
    while play_again.lower() == 'y':
        if ( (xturn == True) and (check_for_win(grid) != True) ):
            
            #x's turn
            print("***************************")
            print("x's turn!\n")
            print( )
            show_grid(letterGrid)
            print( )
            show_grid(grid)
            print( )
            choice = input("Choose a space: ")
            print( )

            # check that the space chosen by x is empty
            if is_empty(grid, choice) == False:
                print("That space has been taken!\n")
                print("***************************")
                continue

            # determine which space is chosen by x
            if (choice.lower() == 'a'):
                grid[0][0] = "|_x_|"
            elif (choice.lower() == 'b'):
                grid[0][1] = "_x_"
            elif (choice.lower() == 'c'):
                  grid[0][2] = "|_x_|"
            elif (choice.lower() == 'd'):
                  grid[1][0] = "|_x_|"
            elif (choice.lower() == 'e'):
                  grid[1][1] = "_x_"
            elif (choice.lower() == 'f'):
                  grid[1][2] = "|_x_|"
            elif (choice.lower() == 'g'):
                grid[2][0] = "| x |"
            elif (choice.lower() == 'h'):
                grid[2][1] = " x "
            elif (choice.lower() == 'i'):
                grid[2][2] = "| x |"
            else:
                print("Row or column number out of range!\n")
                print("***************************")
                continue
            # now check for a win
            check_for_win(grid)
            # now it is no longer x's turn
            xturn = False
            print("***************************")
            print( )

            
        if check_for_win(grid) != True:
            #o's turn    
            print("o's turn!\n")
            print( )
            show_grid(letterGrid)
            print( )
            show_grid(grid)
            print( )
            choice = input("Choose a space: ")
            print( )

            # check that the space chosen by o is empty
            if is_empty(grid, choice) == False:
                print("That space has been taken!\n")
                print("***************************")
                continue

            # determine which space was chosen by o    
            if (choice.lower() == 'a'):
                grid[0][0] = "|_o_|"
            elif (choice.lower() == 'b'):
                grid[0][1] = "_o_"
            elif (choice.lower() == 'c'):
                  grid[0][2] = "|_o_|"
            elif (choice.lower() == 'd'):
                  grid[1][0] = "|_o_|"
            elif (choice.lower() == 'e'):
                  grid[1][1] = "_o_"
            elif (choice.lower() == 'f'):
                  grid[1][2] = "|_o_|"
            elif (choice.lower() == 'g'):
                grid[2][0] = "| o |"
            elif (choice.lower() == 'h'):
                grid[2][1] = " o "
            elif (choice.lower() == 'i'):
                grid[2][2] = "| o |"
            else:
                print("Row or column number out of range!\n")
                print("***************************")
                continue
            # now check for a win
            check_for_win(grid)
            # now it is x's turn
            xturn = True
    

        '''if there is a win and user wants
           to play again, the grid is reset by
           the reset_grid function. Else quit the
           program'''
        
        if check_for_win(grid) == True:
            if xturn == False:
                print("x is the winner!\n")
                show_grid(grid)
            else:
                print("***************************")
                print("o is the winner!\n")
                show_grid(grid)
            print( )
            play_again = input("Play again?(y/n) ")
            if play_again == 'y':
                grid = reset_grid(grid)
                print("***************************")
                print( )

    
        
    
if __name__=="__main__":
    main()
    
    
  
    
   

