import numpy as np

def main():
    mode = input("Welcome to the 8-puzzle solver. Please type your preferred mode: '1' for default puzzle, '2' for custom puzzle" + "\n")    
    
    if mode == "1": 
        # call the function for a default puzzle?
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

def pick_difficulty():
    difficulty = input("Please select the difficulty of the default puzzle: Type a number between 1-5, 1 being very easy and 5 being very hard: ")
    if(difficulty == '1'):
        print("You have selected ...")
        return("yum")


def run_game(puzzle):
    print(puzzle)



if __name__ == "__main__":
    main()