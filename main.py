# any code that was pulled from an online source will include the link
# any code from slides or other resources will be credited

import numpy as np
import hashlib
import copy
from heapq import heappush, heappop 
import time

repeated_states = set()

# default puzzles are from the project instructions or randomly generated from: https://deniz.co/8-puzzle-solver/
goal_state = [[1,2,3],
              [4,5,6],
              [7,8,0]]
very_easy = [[1,2,3],
              [5,0,6],
              [4,7,8]]
easy = [[1,3,6],
        [5,0,2],
        [4,7,8]]
medium = [[1,3,6],
          [5,0,7],
          [4,8,2]]
hard = [[7,1,2],
        [4,8,5],
        [6,3,0]]
very_hard = [[0,7,2],
             [4,6,1],
             [3,5,8]]

# https://www.tutorialspoint.com/python/python_nodes.htm
# used to find syntax and build a basic node class
class Node(): 
    def __init__ (self, value):
        self.value = value
        self.level = 0
        self.heuristic = 0
        self.parent = None
        self.board1 = None
        self.board2 = None
        self.board3 = None
        self.board4 = None
    # https://martinheinz.dev/blog/1
    # for custom comparison operator and print operator
    def __lt__(self, other):
        return (self.heuristic + self.level) < (other.heuristic + other.level)
    def __repr__(self):
        return f"{self.value}"
    
def print_puzzle(puzzle):
    print(np.array(puzzle))

def main():
    # code outline used from the sample report from instructions for intro
    mode = input("Welcome to the 8-puzzle solver. Please type your preferred mode: \n'1' for default puzzle \n'2' for custom puzzle\n")    
    
    if mode == "1": 
        # asks for difficulty of default puzzle -- good for testing 
        difficulty = input("Please select the difficulty of the default puzzle: Type a number between 1-5, 1 being very easy and 5 being very hard:\n")
        while(int(difficulty) < 1 or int(difficulty) > 5):
            print("Please select a valid difficulty.")
            difficulty = input("Please select the difficulty of the default puzzle: Type a number between 1-5, 1 being very easy and 5 being very hard:\n")
        print("You have selected...")
        if(difficulty == '1'):
            print("Very easy.")
            puzzle = very_easy
        elif(difficulty == '2'):
            print("Easy.")
            puzzle = easy
        elif(difficulty == '3'):
            print("Medium.")
            puzzle = medium
        elif(difficulty == '4'):
            print("Hard.")
            puzzle = hard
        else:
            print("Very hard.")
            puzzle = very_hard    
    
    # build-a-bear (but a puzzle)
    else:
        print("Please enter your puzzle, using 0 to stand for the blank tile. Make sure your puzzle is a valid 8-puzzle.")
        
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
    type = input("Which algorithm would you like me to use? \n(1) for Uniform Cost Search \n(2) for Misplaced Tile Heuristic, \n(3) for Manhattan Distance Heuristic\n")
    if(type == "1"):
        run_game(puzzle, 1)
    elif(type == "2"):
        run_game(puzzle, 2)
    elif(type == "3"):
        run_game(puzzle, 3)
    return

# calculates heuristic for either misplaced or manhattan (specified by type)
def get_heuristic(puzzle, type):
    heuristic = 0
    if(type == 2):
        for i in range(len(puzzle)):
            for j in range(len(puzzle)):
                if( (puzzle[i][j]) and (puzzle[i][j] != goal_state[i][j])):
                    heuristic += 1
    if(type == 3):
        for i in range(len(puzzle)):
            for j in range(len(puzzle)):
                if(puzzle[i][j]):
                    x,y = find_actual_pos(goal_state, puzzle[i][j])
                    heuristic += abs(i - x) + abs(j-y)
    return heuristic

# used to find the row and column position of the number in the goal state (used for distances)
def find_actual_pos(goal_state, num):
  for i in range(len(goal_state)):
    for j in range(len(goal_state[i])):
      if goal_state[i][j] == num:
        return i, j

# used for repeated states -- https://www.geeksforgeeks.org/python-hash-method/
def create_hash(puzzle):
    puzzle_str = str(puzzle)
    hash = hashlib.sha256(puzzle_str.encode())
    digit = hash.hexdigest()
    return(digit)

# checks for repeated state
def state_exists(puzzle):
    if create_hash(puzzle) in repeated_states:
        return True
    return False

# custom expand function that adds all possible child nodes (all the possible ways empty tile could move)
# https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/
# used deep copy function to create the children
def expand_node(current_node):
    row = 0
    column = 0
    row, column = find_actual_pos(current_node.value, 0)
    # 0 not in the very left column, left
    if column > 0:
        left_node = copy.deepcopy(current_node.value)
        left_node[row][column], left_node[row][column-1] = left_node[row][column-1], left_node[row][column]
        if create_hash(left_node) not in repeated_states:
            current_node.board1 = Node(left_node)
            current_node.board1.parent = current_node

    # 0 not in very right column, right
    if column < 2:
        right_node = copy.deepcopy(current_node.value)
        right_node[row][column], right_node[row][column+1] = right_node[row][column+1], right_node[row][column]
        if create_hash(right_node) not in repeated_states:
            current_node.board2 = Node(right_node)
            current_node.board2.parent = current_node

    # 0 not in very top row, up
    if row > 0:
        top_node = copy.deepcopy(current_node.value)
        top_node[row][column], top_node[row-1][column] = top_node[row-1][column], top_node[row][column]
        if create_hash(top_node) not in repeated_states:
            current_node.board3 = Node(top_node)
            current_node.board3.parent = current_node

    # 0 not in very bottom row, down
    if row < 2:
        bottom_node = copy.deepcopy(current_node.value)
        bottom_node[row][column], bottom_node[row+1][column] = bottom_node[row+1][column], bottom_node[row][column]
        if create_hash(bottom_node) not in repeated_states:
            current_node.board4 = Node(bottom_node)
            current_node.board4.parent = current_node

def run_game(puzzle, search_type):
    # geeksforgeeks.org/python-measure-time-taken-by-program-to-execute/ 
    # to measure how long the search takes
    begin = time.perf_counter()
    
    # getting the search type
    if search_type == 1:
        heuristic = 0
    elif search_type == 2:
        heuristic = get_heuristic(puzzle, 2)
    else:
        heuristic = get_heuristic(puzzle,3)

    # declaring variables, most of which are needed at the end
    nodes_expanded = 0
    max_queue = 0
    node = Node(puzzle)
    node.level = 0
    node.heuristic = heuristic
    # https://www.geeksforgeeks.org/min-heap-in-python/
    # used for min heap functions and syntax
    # create heap
    game = []
    heappush(game,node)

    while game:
        # checks if queue is empty -- game over
        if not game:
            print("Sadness. There is no solution to your 8-puzzle.")
            break
        # checking for max queue size
        max_queue = max(len(game), max_queue)

        # current node is the puzzle state we observe in this loop instance
        current_node = heappop(game)

        # used for tracing back the puzzle for solution path in order
        if current_node.value == goal_state:
            trace = current_node
            trace_set = []
            while trace != None:
                trace_set.append(trace)
                trace = trace.parent
            trace_set.reverse()
            i = 0
            while(i < len(trace_set)):
                print_puzzle(trace_set[i].value)
                i += 1
            
            # prints all the stats and then breaks out of the loop
            print("YIPPEE! We found a solution to your 8-puzzle. \nSolution depth: " +  str(current_node.level) + "\n" + str(nodes_expanded) + " nodes expanded \nMax queue length: " + str(max_queue) + "\nThe search took "+ str(round(time.perf_counter() - begin, 3)) + " seconds " )
            break
        # print_puzzle(current_node.value)

        # checks that it is not a repeated state, adds to repeated states, then calls expand
        if not state_exists(current_node.value):
            nodes_expanded += 1
            repeated_states.add(create_hash(current_node.value))            
            expand_node(current_node)
            
        # goes through generated expanded children, calculates depth and heuristic
        boards = [current_node.board1, current_node.board2, current_node.board3, current_node.board4]
        for board in boards:
            if board is not None:
                new_node = copy.deepcopy(board)
                new_node.level = current_node.level + 1
                if search_type == 1:
                    new_node.heuristic = 0
                elif search_type == 2:
                    new_node.heuristic = get_heuristic(new_node.value, 2)
                elif search_type == 3:
                    new_node.heuristic = get_heuristic(new_node.value, 3)
                # adds node to queue
                heappush(game, new_node)

if __name__ == "__main__":
    main()
