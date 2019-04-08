import random

#test

def rock_paper_scissors():

    """
    rock beats scissors
    paper beats rock
    scissors beats paper
    """

    choice_list = ["rock", "paper", "scissors"]
    who_beats_who = {"rock": "scissors", "paper": "rock", "scissors" : "paper"}

    while True:
        player_choice = input("Rock, Paper or Scissors?\n").lower()

        if player_choice not in choice_list:
            print("Not a valid value, choose one of the options below:")
            continue
        else:
            ai_choice = random.choice(choice_list)
            print(f"AI chose {ai_choice}")

            if player_choice == ai_choice:
                print("It's a tie")
            elif who_beats_who[player_choice] == ai_choice:
                print("Player wins")
            else:
                print("AI wins")
            break

rock_paper_scissors()
