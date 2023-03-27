# GAME OF LIFE

This is a Python implementation of Conway's Game of Life using the Pygame library.
## Getting Started

Before running the program, make sure to have Pygame installed. You can install Pygame using pip:

```
pip install pygame
```



To run the program, simply run the file `main.py`:

```
python3 main.py
```


## How to Play
- Press SPACE to pause/continue the game.
- Press R to reset the grid.
- Click on cells to draw/erase them.
- Press ESC or close the window to quit the game.
## Rules

The rules of Conway's Game of Life are simple:
- Any live cell with fewer than two live neighbors dies, as if by underpopulation.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by overpopulation.
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
## Credits 
- Pygame documentation: [https://www.pygame.org/docs/](https://www.pygame.org/docs/) 
- Conway's Game of Life: [https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
