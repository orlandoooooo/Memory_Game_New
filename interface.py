# Ask user whether to continue y/n, reprompting until a valid answer is given
# Return True if ready and False if not ready
def ask_ready_to_continue():
    while True:
        answer = input("Ready to continue? y/n\n").strip().lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Invalid response")


def clear_screen():
    for _ in range(40):
        print("")


# Prompt user for number of players until valid answer given, returning number given
def get_players(max):
    # Don't ask if max is 0 or 1
    if max == 0:
        return 0
    if max == 1:
        return 1
    while True:
        try:
            players = int(input("Number of players: "))
            if players not in range(1, max + 1):
                print(f"Must be a number between 1 and {max}")
                continue
            return players
        except:
            print("Must be a number")
            continue


# Print line to signal new phase
def new_phase():
    print("----------")

