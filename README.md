# Pong Game by Zarin

This is a simple implementation of the classic Pong game using Python's Turtle module. The game is designed to be beginner-friendly and requires no external dependencies other than the Turtle and winsound modules.

## Game Description

The game features two paddles and a ball. The objective is to score points by hitting the ball past the opponent's paddle. Each player controls their paddle using keyboard keys.

## Features

- Single-player or two-player game mode
- Basic collision detection
- Sound effects for ball collisions
- Score tracking for both players

## Controls

- Player A (left paddle): 
  - Move up: `w`
  - Move down: `s`
- Player B (right paddle): 
  - Move up: `Up Arrow`
  - Move down: `Down Arrow`

## Requirements

- Python 3.x
- Turtle module (comes pre-installed with Python)
- winsound module (for sound effects on Windows)

## Notes
- The game uses winsound for sound effects on Windows. For Linux and Mac, uncomment the respective lines in the border checking and paddle collision detection sections.
- You can customize the keys for paddle movement in the keyboard bindings section.

## Installation

No installation is required as the game uses Python's built-in modules.

## Usage

1. Clone the repository or download the `pong.py` file.
2. Run the `pong.py` file using Python:

```sh
python pong.py

