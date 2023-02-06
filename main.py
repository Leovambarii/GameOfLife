import pygame, sys, time
import numpy as np

WIDTH = 500
HEIGHT = 500
CELL_SIZE = 10
FPS = 10
COLORS = {
    "BACKGROUND": (10, 10, 10),
    "CELL_ALIVE": (64, 191, 64),
    "CELL_DYING": (38, 115, 38),
    "GRID": (100, 100, 100)
}

def update(screen, cells, size, progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive_neighbors = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        cell_color = COLORS["BACKGROUND"] if cells[row, col] == 0 else COLORS["CELL_ALIVE"]

        if cells[row, col] == 1:
            if alive_neighbors < 2 or alive_neighbors > 3:
                if progress:
                    cell_color = COLORS["CELL_DYING"]
            elif 2 <= alive_neighbors <= 3:
                updated_cells[row, col] = 1
                if progress:
                    cell_color = COLORS["CELL_ALIVE"]
        else:
            if alive_neighbors == 3:
                updated_cells[row, col] = 1
                if progress:
                    cell_color = COLORS["CELL_ALIVE"]

        pygame.draw.rect(screen, cell_color, (col*size, row*size, size-1, size-1))

    return updated_cells


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    cells = np.zeros((HEIGHT//CELL_SIZE, WIDTH//CELL_SIZE))
    screen.fill(COLORS["GRID"])
    update(screen, cells, CELL_SIZE)
    pygame.display.flip()
    pygame.display.update()

    clock = pygame.time.Clock()
    pause = False
    while True:
        screen.fill(COLORS["GRID"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_r:
                    cells = np.zeros((HEIGHT//CELL_SIZE, WIDTH//CELL_SIZE))
                    update(screen, cells, CELL_SIZE)
                    pygame.display.update()
                elif event.key == pygame.K_SPACE:
                    pause = not pause
                    update(screen, cells, CELL_SIZE)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1]//CELL_SIZE, pos[0]//CELL_SIZE] = 1
                update(screen, cells, CELL_SIZE)
                pygame.display.update()
        if pause:
            cells = update(screen, cells, CELL_SIZE, progress=True)
            pygame.display.flip()
            pygame.display.update()
            clock.tick(FPS)

if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()