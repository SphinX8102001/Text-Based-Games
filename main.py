from tictactoe import PlayTicTacToe
from wordle import PlayWordle
import os

prompt = r'''1.Type 1 to play Wordle
2.Type 2 to play Tic-Tac-Toe
3.Type 3 to exit

>'''

loop = True
while loop:
    print()
    abc = input(prompt)
    os.system('cls')
    if abc == '3':
        loop = False
    elif abc == '1':
        PlayWordle()
    elif abc == '2':
        PlayTicTacToe()