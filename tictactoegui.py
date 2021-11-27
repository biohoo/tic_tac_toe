import PySimpleGUI as sg
import webbrowser

class IntroductionScreen:

    def __init__(self):
        self.layout = [
            [sg.Text("Please enter your Name and your opponent's name")],
            [sg.Text('Name', size=(15, 1)), sg.InputText('', key='player')],
            [sg.Text('Name of opponent', size=(15, 1)), sg.InputText('', key='opponent')],
            [sg.Frame(layout=[
                [sg.Radio('X', "RADIO1", default=True, size=(10, 1), key='player_is_x'), sg.Radio('O', "RADIO1", key='player_is_o')]], title='Options',
                title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
            [sg.Submit(), sg.Cancel(), sg.Checkbox('tictactoe', key='secret')]
        ]

        window = sg.Window('Tic Tac Toe Game').Layout(self.layout)

        button, events = window.Read()
        print(button, events)

        self.player = events['player']
        self.opponent = events['opponent']
        self.player_tile = "X" if events['player_is_x'] else "O"
        self.opponent_tile = "O" if events['player_is_x'] else "X"

        if events['secret']:
            self.play_tic_tac_toe_secret()

        window.close()

    def __str__(self):
        return f'Player is {self.player}, icon {self.player_tile}\nOpponent is {self.opponent}, icon {self.opponent_tile}'

    def play_tic_tac_toe_secret(self):
        webbrowser.open('https://www.youtube.com/watch?v=JlBx-t7iKYY&t=0m40s')

class Board:

    def __init__(self):
        pass

Board()
print(IntroductionScreen())