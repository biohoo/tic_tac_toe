import numpy as np
import webbrowser


class TicTacToe():
    def __init__(self):
        player1 = Player(input('Player 1, What is your name?'), 'x')
        player2 = Player(input('Player 2, What is your name?'), 'o')
        self.players = [player1, player2]

        for p in self.players:
            print(f"Welcome to the game, {p.name}! You are playing {p.marker}'s")

        self.game_board = Board()

        instructions = '''
        Welcome to Tic Tac Toe (It's fun playing a game...of tic...tac toe).
        
        Press q to quit.
        
        '''
        print(instructions)

    def ask_and_validate(self):
        response = input("Pick a Row and column like '12' (q to quit) >>> ")

        if len(response) == 2:
            return response
        else:
            return (response[0], None)

    def play(self):
        '''
        Plays tic tac toe.
        '''

        running = True
        round = 1

        while running:
            current_player = self.players[round % 2]

            print(f"Player: {current_player.name}")

            self.game_board.display_board()



            chosen_row, chosen_column = self.ask_and_validate()

            try:
                chosen_row, chosen_column = int(chosen_row), int(chosen_column)
            except:
                pass


            if chosen_column == 'q' or chosen_row == 'q':                           #   quit game.
                break
            elif chosen_column == 'g' or chosen_row == 'g':
                self.browser()
            elif type(chosen_column) is not int and type(chosen_row) is not int:    #   Anything other than integer...
                pass

            else:
                self.play_turn(chosen_row, chosen_column, current_player)


            print("Check winning conditions and decide to end game.")

            winning_condition = self.game_board.check_winning_conditions()

            if winning_condition != False:
                self.game_board.display_board()
                for p in self.players:
                    if p.marker == winning_condition:
                        print(f'{p.name} is the winner.')
                break

            round += 1

    def play_turn(self, chosen_row, chosen_column, current_player):
        print(f"{current_player.name} has chosen to place a marker at {chosen_row, chosen_column}")
        self.game_board.place_marker(current_player.draw_marker(), chosen_row, chosen_column)

    def browser(self):
        webbrowser.open('https://www.youtube.com/watch?v=JlBx-t7iKYY&t=0m40s')


class Marker():
    def __init__(self, icon):
        self.icon = icon

    def underline_icon(self):
        return self.icon + '\n__'

    def pretty_starry_icon(self):
        return '**' + self.icon + '**'


class Board():
    def __init__(self):
        self.board = self.draw_board()


    def draw_board(self):
        '''Generates a NEW board (consider changing the function name...'''

        board = []

        for r in range(3):
            board.append([])

        for r in range(3):
            for c in range(3):
                board[r].append('')
        print(board)
        return board

    def display_board(self):
        '''Prints the board as it exists in the current state.'''

        for row in self.board:
            print('\t'.join([x.replace('','_') for x in row]))



    def place_marker(self, marker_object, row, column):

        #   Correct for "human" row and column numbers... (avoid 'off by one' errors).
        row -= 1
        column -= 1

        self.board[row][column] = marker_object.pretty_starry_icon()
        return self.board

    def check_rows(self, board=None):

        #   Since self is checked at function call time, it's impossible to use it when defining a variable.
        if board == None:
            board = self.board

        rownum = 1
        for row in board:
            if len(set(row)) == 1 and set(row) != {''}:
                return set(row).pop()
            else:
                rownum += 1
        return False

    def check_columns(self):
        numpy_array = np.array(self.board)
        transpose = numpy_array.T
        transpose_list = transpose.tolist()
        print('Checking Columns:')
        return self.check_rows(transpose_list)

    def check_diagonals(self, board = None):

        if board == None:
            board = self.board

        diagonals = [[],[]]
        for i in range(len(board)):
            diagonals[0].append(self.board[i][i])

        row = 0
        for i in reversed(range(len(board))):
            diagonals[1].append(self.board[row][i])
            row += 1

        print('checking diagonals, which means checking rows...')
        return self.check_rows(diagonals)


    def check_winning_conditions(self):
        (rows, columns, diagonals) = self.check_rows(), self.check_columns(), self.check_diagonals()

        winning_conditions = {rows, columns, diagonals}
        if len(winning_conditions) > 1:
            print('checking winning conditions', winning_conditions)
            return winning_conditions.difference({False}).pop()
        else:
            return False


class Player():
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def draw_marker(self):
        return Marker(self.marker)


game = TicTacToe()
game.play()
