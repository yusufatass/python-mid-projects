import random


def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)


while True:
    players = input("Enter number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Please enter a number between 2 and 4.")
    else:
        print("Invalid, try again.")

max_score = 50
# Using an underscore '_' is a standard Python convention when the loop variable isn't used
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print(f"\n--- Player {player_idx + 1}'s Turn ---")
        print(f"Your starting score this turn is: {player_scores[player_idx]}\n")
        current_score = 0

        while True:
            # Moved the input INSIDE the loop so the player decides every single roll
            should_roll = input("Would you like to roll (y/n)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}!")

            print(f"Your current accumulated turn score is: {current_score}")

        # Changed '=' to '+=' to add the turn score to the total game score
        player_scores[player_idx] += current_score
        print(f"Your total game score is now: {player_scores[player_idx]}")

        # Optional: Stop the round immediately if someone wins,
        # so subsequent players don't get an unnecessary extra turn
        if player_scores[player_idx] >= max_score:
            break

winning_score = max(player_scores)
winning_idx = player_scores.index(winning_score)
print(f"\n🏆 The winner is Player {winning_idx + 1} with a score of: {winning_score} 🏆")