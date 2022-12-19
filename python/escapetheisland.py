import time
import random

# set up the game variables
resources = []
puzzles_solved = 0
game_over = False

# set up the timer
start_time = time.time()
time_limit = 60 * 10  # 10 minutes

while not game_over:
    # print the map and list of actions
    print("Map:")
    print("Resources:", resources)
    print("Puzzles solved:", puzzles_solved)
    print("Actions: explore, gather resources, solve puzzle")

    # get the player's action
    action = input("What would you like to do? ")

    # handle the player's action
    if action == "explore":
        event = random.choice(["resource", "puzzle"])
        if event == "resource":
            resources.append("resource")
            print("You found a new resource!")
        elif event == "puzzle":
            print("You stumbled upon a puzzle. Can you solve it?")
            puzzle_solved = input("Enter 1 to solve the puzzle, 0 to skip: ")
            if puzzle_solved:
                puzzles_solved += 1
                print("Great job! You solved the puzzle.")
            else:
                print("You decide to skip the puzzle.")
    elif action == "gather resources":
        gathered = random.randint(1, 3)
        resources.append(gathered)
        print(f"You gathered {gathered} resources.")
    elif action == "solve puzzle":
        if puzzles_solved > 0:
            print("You use one of your puzzle credits to solve a puzzle.")
            puzzles_solved -= 1
        else:
            print("You don't have any puzzles to solve.")

    # check if the player has won or lost
    elapsed_time = time.time() - start_time
    if elapsed_time > time_limit:
        print("Time's up! You didn't escape the island in time.")
        game_over = True
    elif puzzles_solved == 3:
        print(
            "You solved all the puzzles and found a way off the island! You win!"
        )
        game_over = True
