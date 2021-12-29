#!/usr/bin/env python
# coding: utf-8

# In[3]:



#TICTACTOE PROJECT


import random

class tictactoe:
    
    def __init__(self):
        self.board = []
       
    def create_board(self):
        for i in range(0,3):
            row = []
            for j in range(0,3):
                row.append('*')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def select_move(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # check the rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # check the columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # check the diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '*':
                    return False
        return True
    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '*':
                    return False
        return True
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()
    def swap_player_turn(self, player):
        return 'A' if player == 'Z' else 'Z'

    def start(self):
        self.create_board()

        player = 'A' if self.get_random_first_player() == 1 else 'Z'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # taking the player input
            row, col = list(map(int, input("Enter row and column numbers to fix the spot(1 to 6): ").split()))
            print()

            # fixing the move
            self.select_move(row - 1, col - 1, player)

            # checking the current player is win or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking the game is draw or not
            if self.is_board_filled():
                print(" Match Draw!")
                break

                
            # here we are swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


# starting the game
tic_tac_toe = tictactoe()
tic_tac_toe.start()


# In[ ]:




