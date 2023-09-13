from art import logo
from art import vs
from game_data import data
from game_data import difficulty_dict
import random 
import os

def is_linux():
    return os.name == "posix"

def clear():
    os.system("clear") if is_linux() else os.system("cls")

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and follower counts and returns if they got it right."""
    if guess == "a":
        return a_followers > b_followers
    else:
        return b_followers > a_followers

def pick_random_account(data):
    rand_index = random.randint(0, len(data) - 1)
    account = data[rand_index]
    data.pop(rand_index)
    return account

def select_modality():
    print(logo)
    print("Welcome to the Instragram Higher-Lower Game!\n")
    print("How do you want to play?")
    print("  - Modality 1: Play the game until it has shown up all instagram accounts randomly; at which point, you win.")
    print("  - Modality 2: Play the game until you lose. Try to score as high as possible.\n")
    answer = input("Which modality of Instragram Higher-Lower Game would you want to play? Type '1' or '2': ")
    
    if answer == "1":
        print("\nChoose the difficulty:\n")
        difficulty = input("Type 'hard', 'medium', or 'easy': ").lower()
        if difficulty == "hard":
            clear()
            start_game_mod_1(difficulty_dict["hard"])
        elif difficulty == "medium":
            clear()
            start_game_mod_1(difficulty_dict["medium"])
        else:
            clear()
            start_game_mod_1(difficulty_dict["easy"])
    else:
        clear()
        start_game_mod_2()
    
def start_game_mod_1(data):
    print(logo)
    editable_data = data.copy()
    account_a = pick_random_account(editable_data)
    account_b = pick_random_account(editable_data)
    game_over = False
    
    while not game_over:
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_user_right = check_answer(guess, a_follower_count, b_follower_count)
        clear()
        print(logo)
        
        if is_user_right:
            account_a = account_b
            account_b = pick_random_account(editable_data)
            
            if len(editable_data) == 0:
                clear()
                print("Congratulations, You win!")
                game_over = True
            else:
                print("You're right! Keep going!")
                print(f"Instagram accounts left to compare: {len(editable_data)}")
        else:
            game_over = True
            clear()
            print("Sorry, You lost.\n")

    restart_game = input("Do you want to play this modality again? Type 'y' or 'n': ")

    if restart_game == 'y':
        clear()
        start_game_mod_1(data)
    else:
        clear()
        answer = input("Type 'select' to return to the modality selection screen, otherwise type 'quit' to exit program: ").lower()
        if answer == 'select':
            clear()
            select_modality()
        else:
            clear()
            print("Bye bye!")

def start_game_mod_2():
    print(logo)
    account_b = random.choice(data)
    current_score = 0
    game_over = False
    
    while not game_over:
        account_a = account_b
        account_b = random.choice(data)
        
        while account_a == account_b:
            account_b = random.choice(data)
        
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_user_right = check_answer(guess, a_follower_count, b_follower_count)
        clear()
        print(logo)
        
        if is_user_right:
            current_score += 1
            print(f"You're right! Current score: {current_score}.")
        else:
            game_over = True
            clear()
            print(f"Sorry, that's wrong. Final score: {current_score}.\n")

    restart_game = input("Do you want to play this modality again? Type 'y' or 'n': ")

    if restart_game == 'y':
        clear()
        start_game_mod_2()
    else:
        clear()
        answer = input("Type 'select' to return to the modality selection screen, otherwise type 'quit' to exit program: ").lower()
        if answer == 'select':
            clear()
            select_modality()
        else:
            clear()
            print("Bye bye!")

select_modality()
