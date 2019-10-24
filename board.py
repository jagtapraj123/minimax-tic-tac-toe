# This file controls the board data structure used for Tic Tac Toe.
# It contains the class Board which stores game state.
# This class also has all the functions which are required for checking win/lose, draw.
# Also contains functions to place X/O on the board.

# 25 Oct 2019, IIT Goa, GEC Campus, Farmagudi, Ponda, Goa, India

# Created by :-
# Raj S. Jagtap
# Neeraj Khatri
# Ujjawal Tiwari


AI = +1
OPP = -1


class Board():
    def __init__(self, n, OPP_marker, board=[]):
        self.n = n
        self.OPP_marker = OPP_marker
        self.AI_marker = 'X' if OPP_marker == 'O' else 'O'
        if board == []:
            self.board = []
            for i in range(n):
                temp = []
                for j in range(n):
                    temp.append(0)
                self.board.append(temp)
        else:
            self.board = board

        self.win_states = self.calc_win_states()

    def calc_win_states(self):
        win_states = []
        for i in range(self.n):
            temp_hor = []
            temp_ver = []
            for j in range(self.n):
                temp_hor.append(self.board[i][j])
                temp_ver.append(self.board[j][i])
            win_states.append(temp_hor)
            win_states.append(temp_ver)

        temp_cross1 = []
        temp_cross2 = []
        for i in range(self.n):
            temp_cross1.append(self.board[i][i])
            temp_cross2.append(self.board[i][self.n-i-1])
        win_states.append(temp_cross1)
        win_states.append(temp_cross2)
        return win_states

    def print_board(self):
        symbols = {0: ' ', AI: self.AI_marker, OPP: self.OPP_marker}
        dashes = "----------------"
        for row in self.board:
            # print('|'),
            for elem in row:
                symbol = symbols[elem]
                print(f'| {symbol} |', end='')
            print('\n', dashes)

    def get_empty(self):
        empty = []
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 0:
                    empty.append([i, j])
        return empty

    def isValid(self, i, j):
        if [i, j] in self.get_empty():
            return True
        else:
            return False

    def check_win(self, player):
        expected = []
        for i in range(self.n):
            expected.append(player)

        if expected in self.calc_win_states():
            return True
        else:
            return False

    def check_DRAW(self):
        if self.get_empty() == []:
            return True
        else:
            return False

    def check_game_over(self):
        if self.check_win(AI) or self.check_win(OPP) or self.check_DRAW():
            return True
        else:
            return False

    def make_move(self, i, j, player):
        if self.isValid(i, j):
            if player == AI:
                self.board[i][j] = AI
            else:
                self.board[i][j] = OPP

    def getSize(self):
        return self.n

    def getAI_marker(self):
        return self.AI_marker

    def getOPP_marker(self):
        return self.OPP_marker

    def getBoardState(self):
        temp = []
        for row in range(self.n):
            t1 = []
            for col in range(self.n):
                t1.append(self.board[row][col])
            temp.append(t1)
        return temp

    def reset_board(self):
        for i in range(self.n):
            for j in range(self.n):
                self.board[i][j] = 0
