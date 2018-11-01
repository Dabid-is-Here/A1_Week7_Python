from random import randint

npchealth = 3
playerhealth = 3
x = 0

# available weapons => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

# make computer pick one item at random
computer = choices[randint(0, 2)]

while player is False:
    print("Choose your weapon!\n")
    player = input("Rock, Paper, or Scissors?\n")

    if (player == computer):
        print("Tie! Live to shoot another day, cowboy.")

    elif player == "Rock":
        if computer == "Paper":
            print("You lose the round!", computer, "covers", player)
            playerhealth = playerhealth - 1
        else:
            print("You win the round!", player, "smashes", computer)
            npchealth = npchealth - 1

    elif player == "Paper":
        if computer == "Scissors":
            print("You lose the round!", computer, "cuts", player)
            playerhealth = playerhealth - 1
        else:
            print("You win the round!", player, "covers", computer)
            npchealth = npchealth - 1

    elif player == "Scissors":
        if computer == "Rock":
            print("You lose the round!", computer, "smashes", player)
            playerhealth = playerhealth - 1
        else:
            print("You win the round!", player, "cuts", computer)
            npchealth = npchealth - 1

    elif player == "Quit":
        exit()

    else:
        print("Not a valid optin. Check again and check your spelling!\n")

    player = False

    if playerhealth is x:
        print("You lose! Better luck next time!")
        player = input("Would you like to play again? y / n\n")
        playerhealth = playerhealth = 3
        npchealth = playerhealth
        if player == "y":
            player = False
        if player == "n":
            print("See ya next time!")
            break

    else:
        player = False

        if npchealth is x:
            print("You win! Congragulations!")
            player = input("Would you like to play again? y / n\n")
            playerhealth = playerhealth = 3
            npchealth = playerhealth
        if player == "y":
            player = False
        if player == "n":
            print("See ya next time!")
            break

    computer = choices[randint(0, 2)]
