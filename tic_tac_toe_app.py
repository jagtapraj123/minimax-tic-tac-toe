# This file controls the app window.
# It contains a class TicTacToeApp which is an extension of App class of kivy
# This handles button presses, chooses player and triggers AI to play, etc.

# We are using kivy for making interface

# 25 Oct 2019, IIT Goa, GEC Campus, Farmagudi, Ponda, Goa, India

# Created by :-
# Raj S. Jagtap
# Neeraj Khatri
# Ujjawal Tiwari


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.config import Config
from random import randint

from board import Board
from ai import AI_player

AI = +1
OPP = -1


class TicTacToeApp(App):

    def build(self):
        n = int(input("How big do you want the board to be ?"))
        self.n = n
        OPP_marker = str(input("Do you want to be X or O ?"))
        while OPP_marker != 'X' and OPP_marker != 'O':
            print(OPP_marker)
            OPP_marker = str(input(
                "Do you want to be X or O ? \nPlease select a valid input !!..."))

        self.OPP_marker = OPP_marker
        self.AI_marker = 'X' if OPP_marker == 'O' else 'O'
        self.title = 'Tic Tac Toe'
        self.board = Board(self.n, self.OPP_marker)
        self.game_over = False
        self.boardBtns = []

        diam = 150*self.n
        Config.set('graphics', 'width', str(diam))
        Config.set('graphics', 'height', str(diam))
        Config.set('graphics', 'resizable', False)

        self.layout = StackLayout()
        for x in range(self.n**2):
            bt = Button(text='', font_size=120, width=150,
                        height=150, size_hint=(None, None), id=str(x))
            bt.bind(on_release=self.btn_pressed)
            self.boardBtns.append(bt)
            self.layout.add_widget(bt)
        return self.layout

    # On application start handler
    def on_start(self):
        self.init_players()

    # On button pressed handler
    def btn_pressed(self, button):
        place = int(button.id)
        # Continue only if the button has no mark on it...
        if len(button.text.strip()) < 1:
            button.text = self.OPP_marker
            self.board.make_move(int(place/self.n), int(place % self.n), -1)
            if not self.board.check_win(OPP):
                best_move = self.AI.play_move()
                if best_move:
                    self.boardBtns[best_move[0]*self.n +
                                   best_move[1]].text = str(self.AI_marker)
                self.check_winner()
            else:
                self.check_winner()

    # Initializes players
    def init_players(self):
        self.AI = AI_player(self.board)
        greeting = "Hello Player! You are playing with AI"
        self.popup_message(greeting)

    # Checks winner after every move...
    def check_winner(self):
        if self.board.check_DRAW():
            self.game_over = True
            self.popup_message("DRAW")
        elif self.board.check_win(AI):
            self.game_over = True
            self.popup_message("AI Wins!")
        elif self.board.check_win(OPP):
            self.game_over = True
            self.popup_message("OPP Wins!")

    # Resets game state by deleting button values...
    def reset_game(self, popup):
        if self.game_over:
            for button in self.boardBtns:
                button.text = ''
            self.game_over = False
            self.board.reset_board()

    def popup_message(self, msg, title="Welcome!", reset="Hello!"):
        popup = Popup(title=title, content=Label(text=msg),
                      size=(435, 100), size_hint=(None, None))
        popup.bind(on_dismiss=self.reset_game)
        popup.open()
