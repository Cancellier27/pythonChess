from __future__ import annotations
from os import error

from config.read_board import read_board
from config.separate_move import separateMoveInput
from config.pieces import *
from config.converters import *
from config.save_file import *
from config.AI import *

# function to restart the game after the checkmate


def restart() -> None:
    restartMsg = input('Do you want to play again?(y/n): ')

    while True:
        if restartMsg == 'y':
            main()
            break
        elif restartMsg == 'n':
            print('---------\nGAME OVER\n---------')
            return
        else:
            print('>> >>> I did not understand... ')
            restartMsg = input('>> Do you want to play again?(y/n): ')

# function to decide to play against the AI or a friend


def opponent() -> str:
    opponentMsg = input('>> Do you want to play: vs AI(c) or vs Friend(f)?: ')

    while True:
        if opponentMsg == 'f':
            return 'friend'
        elif opponentMsg == 'c':
            return 'computer'
        else:
            print('>> >>> I did not understand... ')
            opponentMsg = input(
                '>> Do you want to play: vs AI(c) or vs Friend(f)?: ')


def main() -> None:
    '''
    runs the play   Hint: implementation of this could start as follows:   filename = input("File name for initial configuration: ")
    '''
    filename = input(
        '>> File name for initial configuration, or QUIT to terminate: ')

#     terminates the game in case of "QUIT"
    if filename == 'QUIT':
        print('---------\nGAME OVER\n---------')
        return

#  catching errors when typing the filename
    try:
        # verify if the board file is valid
        if not read_board(filename):
            return main()

        gameBoard = read_board(filename)

        if type(gameBoard) != tuple:
            return

    except FileNotFoundError as f:
        print('>> >>> No file with this name was found.')
        print(f">> >>> {f}\n")
        return main()
    except Exception as e:
        print(f'>> >>> Oops we caught this error:\n{e}\n')
        return main()

    # if the code got here, it means that the file is valid
    print('\n>> >>> File successfully loaded!! \n')

    # creating a iteration with the user to give a choice to play agains the AI or a Friend
    versus = opponent()

    # printing the board with the accepted code
    print(conf2unicode(gameBoard))

#  Continuing the game after the file check
    print("\n>> >>> Let's start the game!")
    nextTurn = ''
    turn = 0

    # loop for the game, it does not stop until a player wins of in typed QUIT on the input.
    while True:
        if turn % 2 == 0:
            nextTurn = input('\n>> White player move: ')
            '''r
            # White Ai for testing the game quicker
            fbm = find_white_move(gameBoard)
            prevPos = index2location(*fbm[0].position()[0:2])
            nextPos = index2location(*fbm[1:])
            nextTurn = f'{prevPos}{nextPos}'
            print(f'\n>> White player move: {nextTurn}')
            # '''
        else:
            # check if the player wants to play against the computer of a friend
            if versus == 'friend':
                nextTurn = input('\n>> Black player move: ')
            elif versus == 'computer':
                # get the valid move from the function
                fbm = find_black_move(gameBoard)
                # breck into strings
                prevPos = index2location(*fbm[0].position()[0:2])
                nextPos = index2location(*fbm[1:])
                # assign it to the variable
                nextTurn = f'{prevPos}{nextPos}'
                # print for the user see
                print(f'\n>> Black player move: {nextTurn}')

        # Check for terminate the game when input == QUIT
        if nextTurn == 'QUIT':
            saveConfigFileName = input(
                '>> Filename to store the configuration: ')
            save_board(saveConfigFileName, gameBoard)
            print(
                f'>> >>> The game configuration was saved!')
            break

        try:
            movePositions = separateMoveInput(nextTurn)
            initialColumn = movePositions[0][0]
            initialRow = movePositions[0][1]
            moveToColumn = movePositions[1][0]
            moveToRow = movePositions[1][1]

            pieceMoved = [p for p in filter(lambda x: x.position()[0:2] == (
                initialColumn, initialRow), gameBoard[1])][0]

            side = pieceMoved.position()[2]

            # checking if the piece is White
            if pieceMoved.position()[0:3] == (*movePositions[0], False) and turn % 2 == 0:
                print('>> >>> The piece is not White, try again.\n')

            # checking if the piece is Black
            elif pieceMoved.position()[0:3] == (*movePositions[0], True) and turn % 2 == 1:
                print('>> >>> The piece is not Black, try again.\n')

            # Moving the White Piece
            elif turn % 2 == 0:
                # if can_move is true then the piece is gonna move
                if pieceMoved.can_move_to(moveToColumn, moveToRow, gameBoard):
                    # move the piece
                    pieceMoved.move_to(moveToColumn, moveToRow, gameBoard)
                    turn += 1
                    print(">> >>> The configuration after White's move is:\n")
                else:
                    print('>> >>> Moviment Not valid, try again. \n')

            # Moving the Black Piece
            elif turn % 2 == 1:
                if pieceMoved.can_move_to(moveToColumn, moveToRow, gameBoard):
                    pieceMoved.move_to(moveToColumn, moveToRow, gameBoard)
                    turn += 1
                    print(">> >>> The configuration after Black's move is:\n")
                else:
                    print('>> >>> Moviment Not valid, try again. \n')

            # checking if a draw happened with only 2 kings in the board
            if len(gameBoard[1]) == 2:
                print(conf2unicode(gameBoard))
                print(f'\n>> >>> Game Over! \n>> >>> It is a Draw!\n')
                return restart()

            # check if one of the two color kings are in checkmate
            if is_checkmate(side, gameBoard):
                # printing last configuration of the board to the player
                print(conf2unicode(gameBoard))
                color = 'Black' if side else 'White'
                print(f'\n>> >>> CHECKMATE\n>> >>> Game Over! {color} wins!\n')
                # finishing the game and asking to restart the game
                return restart()

            elif is_checkmate(not side, gameBoard):
                print(conf2unicode(gameBoard))
                color = 'White' if side else 'Black'
                print(f'\n>> >>> CHECKMATE\n>> >>> Game Over! {color} wins!\n')
                return restart()

            # check if one of the two color kings are in check
            if is_check(side, gameBoard):
                color = 'White' if side else 'Black'
                print(f'\n>> >>> King {color} is in Check!.')

            elif is_check(not side, gameBoard):
                color = 'Black' if side else 'White'
                print(f'\n>> >>> King {color} is in Check!.')

        except ValueError:
            print(
                '\n>> >>> Wrong format entered, it must be "cNcN" c = characer N = number\n')
        except IndexError:
            print(
                '\n>> >>> There is no piece in this coordinate, please try it again...\n')
        except TypeError:
            print(
                '\n>> >>> There is no piece in this coordinate, please try it again...\n')
        except Exception as e:
            print(f'\n>> >>> Oops we caught this error:\n{e}')

        print(conf2unicode(gameBoard))

    print('---------\nGAME OVER\n---------')
    return

# python chess_puzzle.py ---- runs this command to run the game

if __name__ == '__main__':  # keep this in
    main()
