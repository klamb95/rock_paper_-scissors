# function called PlayGame which takes in two players and their choice
#import pdb
def play_game(name_1, choice_1, name_2, choice_2):
    #pdb.set_trace()
    if type(name_1) or type(name_2) != str:
        return "error, please check your input"
    else:
        if type(choice_1) or type(choice_2) != str:
            return "error, please check your input"
        else:
            accept_response = ["Rock", "Paper", "Scissors"]
            if choice_1 and choice_2 in accept_response:
                if choice_1 == choice_2:
                    return "draw"
                elif choice_1 == "Rock" and choice_2 == "Paper":
                    return "Player two has won"                
            else:
                return "error, please check your input"

