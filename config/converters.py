from config.pieces import *
alphabet = ' abcdefghijklmnopqrstuvwxyz'

#     wKing = '\u2654'     #♔
#     wRook = '\u2656'     #♖
#     wBishop = '\u2657'   #♗
#     bKing = '\u265A'     #♚
#     bRook = '\u265C'     #♜
#     bBishop = '\u265D'   #♝
#     blankSpace = '\u2001'


def location2index(loc: str) -> tuple[int, int]:
    '''converts chess location to corresponding x and y coordinates'''
    return (alphabet.index(loc[0]), int(loc[1:]))


def index2location(x: int, y: int) -> str:
    '''converts  pair of coordinates to corresponding location'''
    return f'{alphabet[x]}{y}'


def conf2unicode(board: Board) -> str:
    '''converts board cofiguration B to unicode format string (see section Unicode board configurations)'''
    boardSize = board[0]
    piecesPosition = board[1]

    whitePieces = {'King': '\u2654', 'Rook': '\u2656', 'Bishop': '\u2657'}
    blackPieces = {'King': '\u265A', 'Rook': '\u265C', 'Bishop': '\u265D'}
    blankSpace = '\u2001'

    BOARD = [[blankSpace]*boardSize for _ in range(boardSize)]

    for pos in piecesPosition:
        column = pos.position()[0]
        row = pos.position()[1]
        side = pos.position()[2]
        pieceName = pos.position()[3]

        if side == True:
            BOARD[boardSize - row][column - 1] = whitePieces[pieceName]
        else:
            BOARD[boardSize - row][column - 1] = blackPieces[pieceName]

    unicodeBoard = ''

    for i in BOARD:
        unicodeBoard += ''.join(i) + '\n'

    # Add the avaliable pieces positions at the botton of the board
    # getWhiteMoves = [f'{x.position()[3][0]}{alphabet[x.position()[0]]}{x.position()[1]}'
    #                  for x in filter(lambda x: x.position()[2] == True, piecesPosition)]
    # getBlackMoves = [f'{x.position()[3][0]}{alphabet[x.position()[0]]}{x.position()[1]}'
    #                  for x in filter(lambda x: x.position()[2] == False, piecesPosition)]
    # unicodeBoard += f"Whites: {getWhiteMoves}" + '\n'
    # unicodeBoard += f"Blacks: {getBlackMoves}" + '\n'

    return unicodeBoard[:-1]
