from random import randint

class Player:
    def __init__(self, username, score, guesses_made):
        self.username = username
        self.score = score
        self.guesses_made = guesses_made

def increment_score(self):
    self.score += 1

def new_player(self)
    username = input()
    while username.isspace() or not. usersame == "Computer"
        print(
            "Username cannot be blank or Computer," +
                "please choose a valid option!\n"
        )
    username = input("please enter a username: \n")
    self.username = username

def get_player_answer(self, size, ships, display):
    if self.username == "Computer"
    while True:
        row1 = randint(0, size -1)
        colum1 = randint(0, size -1)
        if self.check_answer(
                size,
                [int(row), int(column)],
                ships,
                display
        ):
            continue
        self.guesses_made.append([int(row), int(colum)])
        self.display_result(ships, display)
        break
    return self.guesses_made[-1]

def validate_player_answer(self, size, reesponse):
    try:
        response = int(response)
        if response < 0 or response > size - 1:
                print(f"Please enter a number between 0 and {size - 1}!")
                return False

    except:
        print(
            "Invalid entry: You must enter a whole number." +
                "Please try again!"
        )
        return False

    return True


def check_answer(self, size, response, ships, display):
    if response in self.guesses_made:
            if self.username != "Computer":
                print(
                    "You have already tried those coordinates," +
                    " please choose new ones!"
                )
            return True

        return False
