import random
import os
import time
import msvcrt

class SnakeGame:
    def __init__(self, width=20, height=10):
        self.width = width
        self.height = height
        self.snake = [(height // 2, width // 2)]  # Wąż zaczyna w środku planszy
        self.direction = 'RIGHT'
        self.apple = (random.randint(0, height - 1), random.randint(0, width - 1))
        self.running = True
        self.score = 0

    def print_board(self):
        os.system('cls')  # Czyści ekran na Windowsie
        board = [[' ' for _ in range(self.width)] for _ in range(self.height)]

        # Rysuj węża
        for y, x in self.snake:
            board[y][x] = '$'

        # Rysuj jabłko
        y, x = self.apple
        board[y][x] = '0'

        # Rysuj planszę
        for row in board:
            print(' '.join(row))
        print(f"Score: {self.score}")

    def get_key(self):
        key = msvcrt.getch()
        if key == b'\xe0':  # Klawisze strzałek i inne specjalne klawisze
            key = msvcrt.getch()
        return key

    def move_snake(self):
        head_y, head_x = self.snake[0]
        if self.direction == 'UP':
            head_y -= 1
        elif self.direction == 'DOWN':
            head_y += 1
        elif self.direction == 'LEFT':
            head_x -= 1
        elif self.direction == 'RIGHT':
            head_x += 1

        # Sprawdź granice planszy
        head_y %= self.height
        head_x %= self.width

        new_head = (head_y, head_x)
        if new_head in self.snake:
            self.running = False  # Gra kończy się, jeśli wąż zderzy się z siebie
        else:
            self.snake.insert(0, new_head)

            if new_head == self.apple:
                self.score += 1
                self.apple = (random.randint(0, self.height - 1), random.randint(0, self.width - 1))
            else:
                self.snake.pop()

    def run(self):
        while self.running:
            self.print_board()
            key = self.get_key()
            if key == b'w' and self.direction != 'DOWN':
                self.direction = 'UP'
            elif key == b's' and self.direction != 'UP':
                self.direction = 'DOWN'
            elif key == b'a' and self.direction != 'RIGHT':
                self.direction = 'LEFT'
            elif key == b'd' and self.direction != 'LEFT':
                self.direction = 'RIGHT'
            elif key == b'q':
                self.running = False

            self.move_snake()
            time.sleep(0.1)

        print(f"Game Over! Your final score was {self.score}")

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
