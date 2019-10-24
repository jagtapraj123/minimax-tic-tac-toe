# This file controls the AI.
# It contains the class AI_player which can play Tic Tac Toe.
# The AI uses Mini-Max algorithm to find the best possible move.
# This class has functions which can find moves for AI.

# 25 Oct 2019, IIT Goa, GEC Campus, Farmagudi, Ponda, Goa, India

# Created by :-
# Raj S. Jagtap
# Neeraj Khatri
# Ujjawal Tiwari


from board import Board

AI = +1
OPP = -1


class AI_player():
    def __init__(self, board):
        self.board = board
        self.n = board.getSize()
        self.AI_marker = board.getAI_marker()
        self.OPP_marker = board.getOPP_marker()

    def play_move(self):
        self.num = 0
        possibilities = self.board.get_empty()
        if possibilities == []:
            return False
        possibilities_outcome = []
        for possibility in possibilities:
            new_board = Board(self.board.getSize(),
                              self.OPP_marker, self.board.getBoardState())

            possibilities_outcome.append(
                [self.findBestMove(OPP, new_board, possibility, 0), possibility])

        possibilities_outcome.sort(reverse=True)

        best_move = possibilities_outcome[0][1]

        self.board.make_move(best_move[0], best_move[1], AI)
        self.board.print_board()
        return best_move

    def findBestMove(self, player, board, move, depth):
        new_board = Board(board.getSize(),
                          self.OPP_marker, board.getBoardState())

        new_board.make_move(move[0], move[1], -player)

        if new_board.check_win(AI):
            return +1
        elif new_board.check_win(OPP):
            return -1
        elif new_board.check_DRAW():
            return 0

        possibilities = new_board.get_empty()
        possible_outcomes = []
        for possibility in possibilities:
            possible_outcomes.append(
                self.findBestMove(-player, new_board, possibility, depth+1))

        if player == +1:
            if +1 in possible_outcomes:
                return +1
            elif 0 in possible_outcomes:
                return 0
            else:
                return -1
        elif player == -1:
            if -1 in possible_outcomes:
                return -1
            elif 0 in possible_outcomes:
                return 0
            else:
                return +1
