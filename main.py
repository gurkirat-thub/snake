import random

# Snakes and ladders positions
snakes = {
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}

ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100
}

def roll_dice():
    return random.randint(1, 6)

def move_player(position, dice):
    position += dice

    if position > 100:
        return position - dice

    if position in snakes:
        print(f"🐍 Oops! Bitten by a snake at {position}")
        position = snakes[position]

    if position in ladders:
        print(f"🪜 Yay! Climbed a ladder at {position}")
        position = ladders[position]

    return position

def play_game():
    player1 = 0
    player2 = 0

    turn = 1

    while True:
        input(f"\nPlayer {turn}, press Enter to roll dice...")

        dice = roll_dice()
        print(f"🎲 Player {turn} rolled {dice}")

        if turn == 1:
            player1 = move_player(player1, dice)
            print(f"Player 1 position: {player1}")

            if player1 == 100:
                print("\n🏆 Player 1 Wins!")
                break

            turn = 2

        else:
            player2 = move_player(player2, dice)
            print(f"Player 2 position: {player2}")

            if player2 == 100:
                print("\n🏆 Player 2 Wins!")
                break

            turn = 1

if __name__ == "__main__":
    print("🐍 Welcome to Snake and Ladder Game 🪜")
    play_game()
