# line 1 edit
# line edit 1.5

#line 2
from random import random
from numpy import array
import pygame
from game_of_life_templates import *

pygame.init()
win_height = 750
win_width = 750
board_height = 50
board_width = 50
grid_line = 1
cell_height = (win_height - (board_height+1)*grid_line)/ board_height
cell_width = (win_width - (board_width+1)*grid_line)/ board_width
win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Game of Life")
fps = 1
clock = pygame.time.Clock()
font = pygame.font.SysFont( "comicsansms", 22 )
generations = 3
b = 4
board_neighbor_counter = array([[0 for j in range(board_width)] for i in range(board_height)])
board_new = array([[0 for j in range(board_width)] for i in range(board_height)])
info = array([[0 for j in range(board_width)] for i in range(board_height)])


#board = array([[random() < 0.7 for j in range(board_width)] for i in range(board_height)])
glider( 0, 0 )


def number_of_neighbors(board,board_neighbor_counter):
    neighbor_counter = 0
    for k in range(-1,2):
        for l in range(-1,2):
            x=i+k
            y=j+l
            if x == -1:
                x = board_height -1
            if x == board_height:
                x = 0
            if y == -1:
                y = board_width -1
            if y == board_width:
                y = 0
            neighbor_counter += board[x][y]
##            if x == -1 or y == -1 or x == board_height or y == board_width:
##                neighbor_counter += 0
##            else:
##                neighbor_counter += board[x][y]
    return neighbor_counter - board[i][j]

def gamelogic(board_neighbor_counter,board_new,board):
            if board_neighbor_counter[i][j] == 3:
                board_new[i][j] = True
                info[i][j] += 1
            elif board_neighbor_counter[i][j] == 2 and board[i][j]:
                board_new[i][j] = True
                info[i][j] += 1
            else:
                board_new[i][j] = False
                info[i][j] = 0

current_generation = 0
run = True
while current_generation <= generations and run:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0,0,0))

    for i in range(board_height):
        for j in range(board_width):
            board_neighbor_counter[i][j] = number_of_neighbors(board,board_neighbor_counter)
            gamelogic( board_neighbor_counter, board_new, board )
            textb = font.render(str( board_neighbor_counter[i][j] ), True, ( 0, 255, 0 ) )
            textw = font.render(str( board_neighbor_counter[i][j] ), True, ( 255, 0, 0 ) )

            if board[i][j] == 0:
                pygame.draw.rect(win, (0,0,0), (i*cell_width + (i+1)*grid_line, j*cell_height + (j+1)*grid_line, cell_width, cell_height))
                win.blit( textb, (i*cell_width + (i+1)*grid_line, j*cell_height + (j+1)*grid_line)  )
            elif board[i][j] == 1 and info[i][j]*b < 255:
                pygame.draw.rect(win, (255 - info[i][j]*b, 255 - info[i][j]*b, 255), (i*cell_width + (i+1)*grid_line, j*cell_height + (j+1)*grid_line, cell_width, cell_height))
                win.blit( textw, (i*cell_width + (i+1)*grid_line, j*cell_height + (j+1)*grid_line)  )
            else:
                pygame.draw.rect(win, (0, 0, 255), (i*cell_width + (i+1)*grid_line, j*cell_height + (j+1)*grid_line, cell_width, cell_height))
                win.blit( textw, (i*cell_width + (i+1)*grid_line, j*cell_height + (j+1)*grid_line)  )
    board = board_new
    pygame.display.update()
    current_generation += 1
pygame.quit()


# best program in the world
# very important stuff
