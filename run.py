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


def display_result(self, ships, display):
    for x, y in ships:
            if self.guesses_made[-1] == [x, y]:
                print(
                    f"\n{self.username} guessed: ({self.guesses_made[-1][0]}" +
                    f",{self.guesses_made[-1][1]})"
                )
                print(f"{self.username} scores a direct hit!!!")
                display[x][y] = "x  "
                self.increment_score()
                return True

        display[self.guesses_made[-1][0]][self.guesses_made[-1][1]] = "o  "
        print(
            f"{self.username} guessed: ({self.guesses_made[-1][0]}," +
            f"{self.guesses_made[-1][1]})"
        )
        print(f"{self.username} hits the water...\n")

class Board:
    def __init__(self, player, size, ships, display):
        self.player = player
        self.size = size
        self.ships = ships
        self.display = display

    def new_board(self):
        while True:
            board_size = input(
                "Please enter the number of rows/columns " +
                "for the boards(Must be between 5 and 8):\n"
            )
            if self.validate_board_size(board_size):
                print(f"You have chosen a board size of {board_size}")
                break

        self.size = int(board_size)
        return int(board_size)

    def validate_board_size(self, size):
        try:
            row_size = int(size)
            if row_size < 5 or row_size > 8:
                print("Please enter a number between 5 and 8")
                return False
        except:
            print(
                "Invalid entry: You must enter a whole number." +
                "Please try again!"
            )
            return False

        return True

    def generate_ship_location(self):
        ship_pos = set()
        while len(ship_pos) < 5:
            nums = (randint(0, self.size - 1), randint(0, self.size - 1))
            ship_pos.add(nums)

        ship_pos_list = list(ship_pos)

        self.ships = ship_pos_list

    def create_board(self):
        board = [["-  " for x in range(self.size)] for y in range(self.size)]

        self.display = board

