import random
from config.pieces import *


def find_black_move(B: Board) -> tuple[Piece, int, int]:
    '''
    returns (P, x, y) where a Black piece P can move on B to coordinates x,y according to chess rules 
    assumes there is at least one black piece that can move somewhere

    Hints: 
    - use methods of random library
    - use can_move_to
    '''

    blackPieces = [x for x in filter(lambda x: x.position()[2] == False, B[1])]
    whitePieces = [x for x in filter(lambda x: x.position()[2] == True, B[1])]
    whitePositions = [x.position()[0:2] for x in whitePieces]

    for piece in blackPieces:
        for pos in whitePositions:
            if piece.can_move_to(*pos, B):
                return (piece, *pos)

    wasMoved = True
    blackPieceMoved = ()

    while wasMoved:
        x = random.randint(1, B[0])
        y = random.randint(1, B[0])

        for piece in blackPieces:
            if piece.can_move_to(x, y, B):
                blackPieceMoved = (piece, x, y)
                wasMoved = False
                break
    return blackPieceMoved


# Created a secont AI for testing purpose
# def find_white_move(B: Board) -> tuple[Piece, int, int]:
#     whitePieces = [x for x in filter(lambda x: x.position()[2] == True, B[1])]
#     blackPieces = [x for x in filter(lambda x: x.position()[2] == False, B[1])]
#     blackPositions = [x.position()[0:2] for x in blackPieces]

#     for piece in whitePieces:
#         for pos in blackPositions:
#             if piece.can_move_to(*pos, B):
#                 return (piece, *pos)

#     moved = True
#     pieceMoved = ()

#     while moved:
#         x = random.randint(1, B[0])
#         y = random.randint(1, B[0])

#         for piece in whitePieces:
#             if piece.can_move_to(x, y, B):
#                 pieceMoved = (piece, x, y)
#                 moved = False
#                 break

#     return pieceMoved
