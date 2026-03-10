class SnakeGame:
    def __init__(self):
        # Example init, adapt to real code
        self.player_pos = 0
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    
    # Updated move_player function with position boundary check
    def move_player(self, dice_roll):
        new_position = self.player_pos + dice_roll
        if new_position > 100:
            # Prevent moving past the board's end
            print("Move exceeds board end. Try again.")
            # Optionally, do nothing or prompt player to roll again/skip turn
         
        else:
            self.player_pos = new_position
            # Continue with snake/ladder logic if present
            if self.player_pos in self.snakes:
                print("Oops! Landed on a snake.")
                self.player_pos = self.snakes[self.player_pos]
            elif self.player_pos in self.ladders:
                print("Yay! Climbed a ladder.")
                self.player_pos = self.ladders[self.player_pos]

# Example usage
if __name__ == '__main__':
    game = SnakeGame()
    while game.player_pos < 100:
        roll = int(input('Roll dice: '))
        game.move_player(roll)
        print(f'Player at {game.player_pos}')
        if game.player_pos == 100:
            print('Congratulations, you win!')
