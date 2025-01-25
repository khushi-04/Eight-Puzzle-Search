import numpy as np
import hashlib
# import TreeNode
repeated_states = set()

goal_state = [[1,2,3],
              [4,5,6],
              [7,8,0]]
very_easy = [[1,2,3],
              [5,0,6],
              [4,7,8]]
easy = [[1,2,3],
        [5,0,6],
        [4,7,8]]
medium = [[1,2,3],
          [5,0,6],
          [4,7,8]]
hard = [[1,2,3],
        [5,0,6],
        [4,7,8]]
very_hard = [[1,2,3],
             [5,0,6],
             [4,7,8]]


def main():
    mode = input("Welcome to the 8-puzzle solver. Please type your preferred mode: '1' for default puzzle, '2' for custom puzzle" + "\n")    
    
    if mode == "1": 
        # call the function for a default puzzle? idk if this is required but good for testing
        solver_type(pick_difficulty())
        return
    
    # build-a-bear (but a puzzle)
    print("Please enter your puzzle, using 0 to stand for the blank tile! Make sure your puzzle is a valid 8-puzzle (it should have a valid solution).")
    
    print("Enter the puzzle by row, seperating the numbers with a space and press enter to submit each row.")

    row_one = input("Enter: \n[][][]\n")
    row_two = input("Enter:\n " + row_one + "\n[][][]\n")
    row_three = input("Enter:\n" + row_one + "\n" + row_two + "\n[][][]\n")

    row_one = row_one.split()
    row_two = row_two.split()
    row_three = row_three.split()

    for i in range(0, 3):
        row_one[i] = int(row_one[i])
        row_two[i] = int(row_two[i])
        row_three[i] = int(row_three[i])
    puzzle = [row_one, row_two, row_three]

    # now we ask user what kind of algorithm they want and run the game from that function
    solver_type(puzzle)


# allows user to pick difficulty if they selected default puzzles
def pick_difficulty():
    difficulty = input("Please select the difficulty of the default puzzle: Type a number between 1-5, 1 being very easy and 5 being very hard: ")
    while(int(difficulty) < 1 or int(difficulty) > 5):
        print("Please select a valid difficulty.")
        difficulty = input("Please select the difficulty of the default puzzle: Type a number between 1-5, 1 being very easy and 5 being very hard: ")
    print("You have selected...")
    if(difficulty == '1'):
        print("Very easy.")
        return(very_easy)
    elif(difficulty == '2'):
        print("Easy.")
        return(easy)
    elif(difficulty == '3'):
        print("Medium.")
        return(medium)
    elif(difficulty == '4'):
        print("Hard.")
        return(hard)
    else:
        print("Very hard.")
        return(very_hard)


# asks user for the algorithm they want the program to use
def solver_type(puzzle):
    type = input("Which algorithm would you like me to use? (1) for Uniform Cost Search, (2) for Misplaced Tile Heuristic, (3) for Manhattan Distance Heuristic")
    if(type == "1"):
        run_game(puzzle, 0)
    elif(type == "2"):
        run_game(puzzle, get_hueristic(puzzle, 2))
    elif(type == "3"):
        run_game(puzzle, get_hueristic(puzzle, 3))

# calculates hueristic for either misplaced or manhattan (specified by type)
def get_hueristic(puzzle, type):
    hueristic = 0
    if(type == 2):
        for i in range(len(puzzle)):
            for j in range(len(puzzle)):
                if( (puzzle[i][j]) and (puzzle[i][j] != goal_state[i][j])):
                    hueristic += 1
    if(type == 3):
        for i in range(len(puzzle)):
            for j in range(len(puzzle)):
                if(puzzle[i][j]):
                    x,y = find_actual_pos(goal_state, puzzle[i][j])
                    hueristic += abs(i - x) + abs(j-y)
    return hueristic

def find_actual_pos(goal_state, num):
  for i in range(len(goal_state)):
    for j in range(len(goal_state[i])):
      if goal_state[i][j] == num:
        return i, j

def create_hash(puzzle):
    puzzle_str = str(puzzle)
    hash = hashlib.sha256(puzzle_str.encode())
    digit = hash.hexdigest()
    return(digit)

def state_exists(puzzle):
    if(create_hash(puzzle) in repeated_states):
        return True
    return False

def run_game(puzzle, hueristic):

    print("Here is your starting puzzle: ")
    print_puzzle(puzzle)
    throw_away = create_hash(puzzle)
    repeated_states.add(puzzle)

    puzzle_test = puzzle
    print(state_exists(puzzle_test))


def print_puzzle(puzzle):
    print(np.array(puzzle))

if __name__ == "__main__":
    main()