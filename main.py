language = "python3"
run = "[run]"
def print_board(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")
 
 
def check_for_win(p_pos, cur_p):
 
    solutions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
    for x in solutions:
        if all(y in p_pos[cur_p] for y in x):
 
            return True
    return False       
 
def check_for_draw(p_pos):
    if len(p_pos['X']) + len(p_pos['O']) == 9:
        return True
    return False       
 
def game_run(cur_p):
 
    values = [' ' for x in range(9)]
     
    p_pos = {'X':[], 'O':[]}
     
    while True:
        print_board(values)
         
        try:
            print("Player ", cur_p, " turn. Which box? : ", end="")
            move = int(input()) 
        except ValueError:
            print("Try Again")
            continue
 
        if move < 1 or move > 9:
            print("Not on the board, Try Again")
            continue
 
        if values[move-1] != ' ':
            print("Place already filled. Try again!!")
            continue
 
 
        values[move-1] = cur_p
 
        p_pos[cur_p].append(move)
 
        if check_for_win(p_pos, cur_p):
            print_board(values)
            print("Player ", cur_p, " has won the game!!")     
            print("\n")
            return cur_p
 
        if check_for_draw(p_pos):
            print_board(values)
            print("Game Drawn")
            print("\n")
            return 'D'
 
        if cur_p == 'X':
            cur_p = 'O'
        else:
            cur_p = 'X'
 

  
def gameamount(games):
      print("Player 1")
      p_1 = input("Enter the name : ")
      print("\n")
 
      print("Player 2")
      p_2 = input("Enter the name : ")
      print("\n")
     
      cur_p = p_1
 
      p_choice = {'X' : "", 'O' : ""}
 
      opts = ['X', 'O']
      for x in range(games):
        print("Turn to choose for", cur_p)
        print("Enter 1 for X")
        print("Enter 2 for O")

 
        try:
            choice = int(input())   
        except ValueError:
            print("Not Applicable\n")
            continue
 
        if choice == 1:
            p_choice['X'] = cur_p
            if cur_p == p_1:
                p_choice['O'] = p_2
            else:
                p_choice['O'] = p_1
 
        elif choice == 2:
            p_choice['O'] = cur_p
            if cur_p == p_1:
                p_choice['X'] = p_2
            else:
                p_choice['X'] = p_1
         

        else:
            print("Try Again\n")
 
        win = game_run(opts[choice-1])
         

        if cur_p == p_1:
            cur_p = p_2
        else:
            cur_p = p_1
games = int(input("How many games do you want to play: "))
print("\n")
gameamount(games)