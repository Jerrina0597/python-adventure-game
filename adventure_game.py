# adventure_game-for developing text-based adventure games 
print("adventure game setup is working")
def start_game():
    # introduce the game and ask the players for thier names and store it in a variable.
    # provide the players with initial choices either (explore forest or enter the cave path)call the right function based on the player's choice

    name=input("welcome to the adventure game!what is your name? ")
    print(f"Hello {name},Your adventure begins now!")
    choice = input("What would you like to do? (explore forest/enter cave): ")
    if choice == "explore forest":
        explore_forest()
    elif choice == "enter cave":
        enter_cave()
    else:
        print("Invalid choice. Please try again.")
        start_game()

def explore_forest():
    #provide the player with choices (follow a river or climb a tree).
    # give player a choice between two actions.
    # use if-else to decide the result of each choice in print statements
    choice = input("What would you like to do? (follow river/climb tree): ")
    if choice == "follow river":
        print("You follow the river and find a hidden waterfall.")
        end_game("win")
    elif choice == "climb tree":
        print("You climb the tree and spot a deer in the distance.")
        end_game("lose")
    else:
        print("Invalid choice. Please try again.")
        explore_forest()
def enter_cave():
    #provide the player with choices (light a torch or proceed in the dark).
    # give player a choice between two actions.
    # use if-else to decide the result of each choice in print statements
    choice = input("What would you like to do? (light torch/proceed in dark): ")
    if choice == "light torch":
        print("You light a torch and discover ancient cave paintings.")
        end_game("win")
    elif choice == "proceed in dark":
        print("You proceed in the dark and stumble upon a sleeping bear.")
        end_game("lose")
    else:
        print("Invalid choice. Please try again.")
        enter_cave()
def end_game(result):
    #The game ends in one of the following three ways:
    # Winning: Finding the treasure
    # Losing: Making a poor decision that ends the adventure
    # Restarting: Choosing to replay the game after an unsuccessful attempt
    if result == "win":
        print("Congratulations! You've found the treasure and won the game!")
    elif result == "lose":
        print("Oh no! Your adventure has come to an end.")
        result = input("Would you like to play again? (yes/no): ")
        if result=="yes":
            start_game()
        else:
            print("Thank you for playing!")
start_game()



