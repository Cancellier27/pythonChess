from config.pieces import *
import os

def read_board(filename: str) -> Board:
    '''
    reads board configuration from file in current directory in plain format
    raises IOError exception if file is not valid (see section Plain board configurations)
    '''
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
#     not valid message function

    def notValidMessage(string):
        print(
            f'---------------------\nThe file is not valid: {string}\n---------------------')

    fileSize = os.path.getsize(f'boards/{filename}')  
    if fileSize == 0:
        print(">> >>> The file is empty... ")
        return False
    
    openFile = open(f'boards/{filename}')
    fin = openFile.readlines()

    try:
        firstLine = int(fin[0][:-1])
    except ValueError as v:
        raise ValueError(f">> >>> ValueError: {v}\n>> >>> First line must be a number.")
    try:
        secondLine = fin[1][:-1].split(',')
    except IndexError as I:
        raise IndexError(f">> >>> IndexError: {I}\n>> >>> Second line must be the pieces positions.")
    try:
        thirdLine = fin[2].split(',')
    except IndexError as I:
        raise IndexError(f">> >>> IndexError: {I}\n>> >>> Third line must be the pieces positions.")

#     checking len of columns, rows and positions
    if firstLine > 26 or firstLine < 2:
        notValidMessage('Number of rows or columns out of range (2 - 26)')
        return False


#  checking all positions characters
    allPositions = [*[x.strip() for x in secondLine], *[x.strip()
                                                        for x in thirdLine]]

    for mov in allPositions:
        piece = mov[0]
        column = mov[1]
        try:
            row = int(mov[2:])
        except:
            notValidMessage(
                f'Number for rows should be and integer, expected row between 1 - 26, received row={mov[2:]}')
            return False

        if len(mov) > 4 or len(mov) < 3:
            notValidMessage(f'Length of position "{mov}" is wrong, must be between 3 and 4 "PxN" or "PxNN"')
            return False

        if piece not in 'KBR':
            notValidMessage(
                f"Not accepted letter {piece} in {mov}, must be only K, B or R")
            return False

        if not column.islower() or not column.isalpha():
            notValidMessage(
                f"Not accepted character {column} in {mov}, must be alphabetical and lower case")
            return False

        if row > 26 or row < 1 or row > firstLine:
            notValidMessage(
                f"Number of rows out of range in {mov}, expected to be equal or less than {firstLine}, and between 1 - 26 ")
            return False

        if alphabet.index(column) > firstLine:
            notValidMessage(
                f"Piece {mov} is out of the board, check the coordinates")
            return False


#     Counting numbers of Kings 'K' and checking if there are different letters
    kingWhiteLocations = [x.strip()[0] for x in secondLine].count('K')
    kingBlackLocations = [x.strip()[0] for x in thirdLine].count('K')

    if kingWhiteLocations != 1 and kingBlackLocations != 1:
        notValidMessage("Invalid number of Kings ('K') on Both sides")
        return False

    elif kingWhiteLocations != 1:
        notValidMessage("Invalid number of Kings ('K') on White side")
        return False

    elif kingBlackLocations != 1:
        notValidMessage("Invalid number of Kings ('K') on Black side")
        return False


#     checking if there are any pieces over each other
    allPieces = [x.strip()[1:] for x in secondLine]
    allPieces.extend([x.strip()[1:] for x in thirdLine])

    if len(allPieces) != len(set(allPieces)):
        notValidMessage('There are more than one piece in one square')
        return False

    pieces = []
    whitePieces = [x.strip() for x in secondLine]
    blackPieces = [x.strip() for x in thirdLine]
    alphabet = ' abcdefghijklmnopqrstuvwxyz'

    for wp in whitePieces:
        w = Piece(alphabet.index(wp[1]), int(wp[2:]), True)

        if wp[0] == 'K':
            pieces.append(King(w.pos_x, w.pos_y, w.side))
        elif wp[0] == 'B':
            pieces.append(Bishop(w.pos_x, w.pos_y, w.side))
        elif wp[0] == 'R':
            pieces.append(Rook(w.pos_x, w.pos_y, w.side))

    for bp in blackPieces:
        b = Piece(alphabet.index(bp[1]), int(bp[2:]), False)

        if bp[0] == 'K':
            pieces.append(King(b.pos_x, b.pos_y, b.side))
        elif bp[0] == 'B':
            pieces.append(Bishop(b.pos_x, b.pos_y, b.side))
        elif bp[0] == 'R':
            pieces.append(Rook(b.pos_x, b.pos_y, b.side))

    board = (firstLine, pieces)

    openFile.close()

    return board
