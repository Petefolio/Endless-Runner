# Endless-Runner
This code is a simple game made with Pygame library that implements a character running infinitely while dodging obstacles and collecting power-ups and score multipliers.

The game window is set to 1300x550, and the game starts with the player on the left side of the screen at a height of 410 pixels. The player can move left and right using the arrow keys and jump using the spacebar. The player's goal is to dodge the obstacles while collecting power-ups and score multipliers to increase their score. The game ends if the player hits an obstacle.

The game's elements are represented by rectangles of different colors, including the player (yellow), obstacles (red, orange, yellow), power-ups (blue), and score multipliers (green). The game background is an image of the sea, and it scrolls continuously from right to left.

The code uses a while loop to keep the game running until the player quits or loses. The loop checks for events such as key presses, and it updates the positions of the game elements accordingly. The code also keeps track of the player's score, the number of power-ups collected, and the number of jumps remaining for the current power-up.
