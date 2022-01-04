import pygame
import numpy as np
from block import Block
from random import randint

pygame.init()


def shift(board, row):
    for col in range(4):
        if isinstance(board[row][col], Block):
            x = col - 1
            c = col
            while x >= 0 and board[row][x] == ' ':
                board[row][c], board[row][x] = ' ', board[row][c]
                c -= 1
                x -= 1
            if x >= 0 and isinstance(board[row][x], Block) and isinstance(board[row][c], Block) and board[row][x].value == board[row][c].value:
                board[row][x].value *= 2
                board[row][c] = ' '
    return board


class Game:
    def __init__(self):
        self.display = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("2048")
        self.board = [[' ' for _ in range(4)] for _ in range(4)]

    def draw_board(self):
        for row in range(4):
            for col in range(4):
                rect = (col * 100, row * 100, 100, 100)
                if isinstance(self.board[row][col], Block):
                    self.board[row][col].update()
                    color = self.board[row][col].color
                    font = pygame.font.Font(None, 50)
                    text = font.render(str(self.board[row][col].value), True, (0, 0, 0))
                    text_rect = text.get_rect(center=(col * 100 + 50, row * 100 + 50))
                    pygame.draw.rect(self.display, color, rect)
                    self.display.blit(text, text_rect)
                else:
                    color = (204, 192, 179)
                    pygame.draw.rect(self.display, color, rect)
        pygame.display.flip()

    def shift_left(self):
        for row in range(4):
            self.board = shift(self.board, row)

    def shift_right(self):
        for row in range(4):
            self.board[row].reverse()
            self.board = shift(self.board, row)
            self.board[row].reverse()

    def shift_up(self):
        self.board = np.transpose(self.board)
        for row in range(4):
            self.board = shift(self.board, row)
        self.board = np.transpose(self.board).tolist()

    def shift_down(self):
        self.board = np.transpose(self.board).tolist()
        for row in range(4):
            self.board[row].reverse()
            self.board = shift(self.board, row)
            self.board[row].reverse()
        self.board = np.transpose(self.board).tolist()

    def add_block(self):
        row, col = randint(0, 3), randint(0, 3)
        count = 0
        while self.board[row][col] != ' ':
            if count > 16:
                return False
            row, col = randint(0, 3), randint(0, 3)
            count += 1
        self.board[row][col] = Block()
        return True

    def play(self):
        self.board[randint(0, 3)][randint(0, 3)] = Block()
        playing = True
        while playing:
            for event in pygame.event.get():
                self.draw_board()
                if event.type == pygame.QUIT:
                    playing = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.shift_left()
                        if not self.add_block():
                            return
                    elif event.key == pygame.K_RIGHT:
                        self.shift_right()
                        if not self.add_block():
                            return
                    elif event.key == pygame.K_UP:
                        self.shift_up()
                        if not self.add_block():
                            return
                    elif event.key == pygame.K_DOWN:
                        self.shift_down()
                        if not self.add_block():
                            return


g = Game()
g.play()
