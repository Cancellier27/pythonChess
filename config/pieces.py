import copy
from typing import NewType
from config.all_pos_to_king import *


class Piece:
    pos_x: int
    pos_y: int
    side: bool  # True for White and False for Black

    def __init__(self, pos_X: int, pos_Y: int, side_: bool):
        '''sets initial values'''
        self.pos_x = pos_X
        self.pos_y = pos_Y
        self.side = side_

    def can_reach_standard(self, pos_X: int, pos_Y: int, B):
        # check if the position is out of the board
        if pos_X > B[0] or pos_X < 1 or pos_Y > B[0] or pos_Y < 1:
            return False
        else:
            # checks the diff in x and y, it will be always 1 or -1 or 0
            DifferenceInX = int(0 if self._pos_X == pos_X else (
                (pos_X - self._pos_X) / abs(pos_X - self._pos_X)))
            DifferenceInY = int(0 if self._pos_Y == pos_Y else (
                (pos_Y - self._pos_Y) / abs(pos_Y - self._pos_Y)))

            nextMovedPos = (self._pos_X + DifferenceInX,
                            self._pos_Y + DifferenceInY)

            for _ in range(B[0]):
                finalMovedPos = nextMovedPos == (pos_X, pos_Y)

                for piece in B[1]:
                    side = piece.position()[2]
                    posChecked = piece.position()[0:2]

                    if posChecked == nextMovedPos and side == self._side:
                        return False
                    if posChecked == nextMovedPos and side != self._side:
                        return True if finalMovedPos else False

                if finalMovedPos:
                    return True

                nextMovedPos = (nextMovedPos[0] + DifferenceInX,
                                nextMovedPos[1] + DifferenceInY)

    def can_move_to_standard(self, pos_X: int, pos_Y: int, B):
        # making a copy of the board
        copyBoard = (B[0], [])
        captured = False

        for piece in B[1]:
            copyPiece = copy.deepcopy(piece)
            copyBoard[1].append(copyPiece)

        # catching the same piece in the copied board
        samePieceInCopyBoard = [x for x in filter(
            lambda x: x.position()[0:2] == (self._pos_X, self._pos_Y), copyBoard[1])][0]

        if self.can_reach(pos_X, pos_Y, B):
            if is_piece_at(pos_X, pos_Y, B):
                captured = piece_at(pos_X, pos_Y, B)
                
                captureCopy = piece_at(pos_X, pos_Y, copyBoard)
                copyBoard[1].remove(captureCopy)
            # using is_check in the copied board
            if is_check(self.side, samePieceInCopyBoard.move_to(pos_X, pos_Y, copyBoard)):
                return False

            if captured:
                B[1].remove(captured)
            return True
        return False

    def can_move_to_for_checks(self, pos_X: int, pos_Y: int, B):
        # basic the same func and move_to but without deleting itens from the original board
        # to be used in is_checkmate tests
        copyBoard = (B[0], [])

        for piece in B[1]:
            copyPiece = copy.deepcopy(piece)
            copyBoard[1].append(copyPiece)

        samePieceInCopyBoard = [x for x in filter(
            lambda x: x.position()[0:2] == (self._pos_X, self._pos_Y), copyBoard[1])][0]

        if self.can_reach(pos_X, pos_Y, B):
            if is_piece_at(pos_X, pos_Y, B):
                captureCopy = piece_at(pos_X, pos_Y, copyBoard)
                copyBoard[1].remove(captureCopy)

            if is_check(self.side, samePieceInCopyBoard.move_to(pos_X, pos_Y, copyBoard)):
                return False
            return True
        return False


Board = tuple[int, list[Piece]]


class Rook(Piece):
    _pos_X: int
    _pos_Y: int
    _side: bool

    def __init__(self, pos_X: int, pos_Y: int, side_: bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X, pos_Y, side_)
        self._pos_X = pos_X
        self._pos_Y = pos_Y
        self._side = side_

    def position(self):
        return (self._pos_X, self._pos_Y, self._side, 'Rook')

    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''
        checks if this rook can move to coordinates pos_X, pos_Y
        on board B according to rule [Rule2] and [Rule4](see section Intro)
        Hint: use is_piece_at
        '''
        if self._pos_X != pos_X and self._pos_Y != pos_Y:
            return False
        else:
            return Piece.can_reach_standard(self, pos_X, pos_Y, B)

    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''
        checks if this rook can move to coordinates pos_X, pos_Y
        on board B according to all chess rules

        Hints:
        - firstly, check [Rule2] and [Rule4] using can_reach
        - secondly, check if result of move is capture using is_piece_at
        - if yes, find the piece captured using piece_at
        - thirdly, construct new board resulting from move
        - finally, to check [Rule5], use is_check on new board
        '''
        return Piece.can_move_to_standard(self, pos_X, pos_Y, B)

    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''``
        returns new board resulting from move of this rook to coordinates pos_X, pos_Y on board B
        assumes this move is valid according to chess rules
        '''
        self._pos_X = pos_X
        self._pos_Y = pos_Y

        return B


class Bishop(Piece):
    def __init__(self, pos_X: int, pos_Y: int, side_: bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X, pos_Y, side_)
        self._pos_X = pos_X
        self._pos_Y = pos_Y
        self._side = side_

    def position(self):
        return (self._pos_X, self._pos_Y, self._side, 'Bishop')

    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this bishop can move to coordinates pos_X, pos_Y on board B according to rule [Rule1] and [Rule4]'''
        if (self._pos_X + self._pos_Y) != (pos_X + pos_Y) and abs(self._pos_Y - pos_Y) != abs(self._pos_X - pos_X):
            return False
        else:
            return Piece.can_reach_standard(self, pos_X, pos_Y, B)

    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this bishop can move to coordinates pos_X, pos_Y on board B according to all chess rules'''
        return Piece.can_move_to_standard(self, pos_X, pos_Y, B)

    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
        returns new board resulting from move of this bishop to coordinates pos_X, pos_Y on board B
        assumes this move is valid according to chess rules
        '''
        self._pos_X = pos_X
        self._pos_Y = pos_Y

        return B


class King(Piece):
    def __init__(self, pos_X: int, pos_Y: int, side_: bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X, pos_Y, side_)
        self._pos_X = pos_X
        self._pos_Y = pos_Y
        self._side = side_

    def position(self):
        return (self._pos_X, self._pos_Y, self._side, 'King')

    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to rule [Rule3] and [Rule4]'''
        if abs(self._pos_X - pos_X) > 1 or abs(self._pos_Y - pos_Y) > 1:
            return False
        else:
            return Piece.can_reach_standard(self, pos_X, pos_Y, B)

    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to all chess rules'''
        return Piece.can_move_to_standard(self, pos_X, pos_Y, B)

    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
        returns new board resulting from move of this king to coordinates pos_X, pos_Y on board B 
        assumes this move is valid according to chess rules
        '''
        self._pos_X = pos_X
        self._pos_Y = pos_Y

        return B


def is_piece_at(pos_X: int, pos_Y: int, B: Board) -> bool:
    '''checks if there is piece at coordinates pox_X, pos_Y of board B'''
    for piece in B[1]:
        if piece.position()[0:2] == (pos_X, pos_Y):
            return True
    return False


def piece_at(pos_X: int, pos_Y: int, B: Board) -> Piece:
    '''
    returns the piece at coordinates pox_X, pos_Y of board B 
    assumes some piece at coordinates pox_X, pos_Y of board B is present
    '''
    return [p for p in filter(lambda x: x.position()[0:2] == (pos_X, pos_Y), B[1])][0]


def is_check(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is check for side
    Hint: use can_reach
    '''
    getKing = [king for king in filter(lambda x: x.position()[2:] == (side, 'King'), B[1])][0]
    oppositeSide = not side

    for piece in B[1]:
        if piece.position()[2] == oppositeSide:
            if piece.can_reach(*getKing.position()[0:2], B):
                return True
    return False


def is_checkmate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is checkmate for side

    Hints: 
    - use is_check
    - use can_reach 
    '''
    # get the king in check
    getKing = [king for king in filter(lambda x: x.position()[2:] == (side, 'King'), B[1])][0]
    # get all the pieces left from the king's color
    colorPieces = [x for x in filter(lambda x: x.position()[2] == side, B[1])]
    posKing = getKing.position()[0:2]
    avaliableMove = []
    
    # all avaliable moves for a king
    p1 = [posKing[0]-1, posKing[1]-1]
    p2 = [posKing[0], posKing[1]-1]
    p3 = [posKing[0]+1, posKing[1]-1]
    p4 = [posKing[0]+1, posKing[1]]
    p5 = [posKing[0]+1, posKing[1]+1]
    p6 = [posKing[0], posKing[1]+1]
    p7 = [posKing[0]-1, posKing[1]+1]
    p8 = [posKing[0]-1, posKing[1]]

    allPos = [posKing, p1, p2, p3, p4, p5, p6, p7, p8]

    # if there is only the king left on the side
    if len(colorPieces) == 1:
        for pos in allPos[1:]:
            if getKing.can_move_to_for_checks(*pos, B):
                return False
        return True
    
    for pos in allPos:
        if getKing.can_move_to_for_checks(*pos, B):
            avaliableMove.append('NOT Checkmate')

    if not is_check(side, B):
        avaliableMove.append('NOT Checkmate')

    # if is checkmate check if a piece from the same side can block the way to the king
    if len(avaliableMove) == 0:
        listWithPositionsToReachKing = allPosToReachKing(posKing, B[0])
        for piece in B[1]:
            if piece.position()[2] == side:
                for position in listWithPositionsToReachKing:
                    if piece.can_move_to_for_checks(*position, B):
                        return False
        return True
    return False
