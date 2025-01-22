import numpy as np

def main():
    mode = input("Welcome to the 8-puzzle solver. Please type your preferred mode: '1' for default puzzle, '2' for custom puzzle" + "\n")    
    
    if mode == "1": 
        # call the function for a default puzzle? idk if this is required but good for testing
        run_game(pick_difficulty())
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
    run_game(puzzle)

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

def pick_difficulty():
    difficulty = input("Please select the difficulty of the default puzzle: Type a number between 1-5, 1 being very easy and 5 being very hard: ")
    if(difficulty < 1 or difficulty > 5):
        print("Please select a valid difficulty.")
    print("You have selected...")
    if(difficulty == '1'):
        print("Very easy.")
        return(very_easy)

def run_game(puzzle):
    puzzle = np.array(puzzle)
    print("Let's begin solving! Here is your starting puzzle: ")
    print(puzzle)


if __name__ == "__main__":
    main()