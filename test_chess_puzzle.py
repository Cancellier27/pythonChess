import pytest
from chess_puzzle import *

def test_locatio2index1():
    assert location2index("e2") == (5, 2)
def test_locatio2index2():
    assert location2index("f20") == (6, 20)
def test_locatio2index3():
    assert location2index("x5") == (24, 5)
def test_locatio2index4():
    assert location2index("a1") == (1, 1)
def test_locatio2index5():
    assert location2index("j10") == (10, 10)


def test_index2location1():
    assert index2location(5, 2) == "e2"
def test_index2location2():
    assert index2location(6, 20) == "f20"
def test_index2location3():
    assert index2location(24, 5) == "x5"
def test_index2location4():
    assert index2location(1, 1) == "a1"
def test_index2location5():
    assert index2location(10, 10) == "j10"


wb1 = Bishop(1, 1, True)
wr1 = Rook(1, 2, True)
wb2 = Bishop(5, 2, True)
bk = King(2, 3, False)
br1 = Rook(4, 3, False)
br2 = Rook(2, 4, False)
br3 = Rook(5, 4, False)
wr2 = Rook(1, 5, True)
wk = King(3, 5, True)

B1 = (5, [wb1, wr1, wb2, bk, br1, br2, br3, wr2, wk])
'''
♖ ♔  
 ♜  ♜
 ♚ ♜ 
♖   ♗
♗    
'''


def test_is_piece_at1():
    assert is_piece_at(2, 2, B1) == False
def test_is_piece_at2():
    assert is_piece_at(1, 5, B1) == True
def test_is_piece_at3():
    assert is_piece_at(4, 3, B1) == True
def test_is_piece_at4():
    assert is_piece_at(3, 5, B1) == True
def test_is_piece_at5():
    assert is_piece_at(5, 1, B1) == False


def test_piece_at1():
    assert piece_at(4, 3, B1) == br1
def test_piece_at2():
    assert piece_at(1, 5, B1) == wr2
def test_piece_at3():
    assert piece_at(2, 3, B1) == bk
def test_piece_at4():
    assert piece_at(1, 1, B1) == wb1
def test_piece_at5():
    assert piece_at(1, 2, B1) == wr1


def test_can_reach1():
    assert wr2.can_reach(4, 5, B1) == False
def test_can_reach2():
    assert wk.can_reach(2, 4, B1) == True
def test_can_reach3():
    assert wb1.can_reach(5, 5, B1) == True
def test_can_reach4():
    assert wb2.can_reach(3, 3, B1) == False
def test_can_reach5():
    assert wb2.can_reach(3, 4, B1) == False
def test_can_reach6():
    assert br3.can_reach(1, 4, B1) == False
def test_can_reach7():
    assert wb1.can_reach(2, 1, B1) == False
def test_can_reach8():
    assert wb1.can_reach(1, 2, B1) == False
def test_can_reach1():
    assert wr1.can_reach(2, 1, B1) == False


br2a = Rook(1, 5, False)
wr2a = Rook(2, 5, True)


def test_can_move_to1():
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk])
    assert wr2a.can_move_to(2, 4, B2) == False
def test_can_move_to2():
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk])
    assert wk.can_move_to(3, 4, B2) == False
def test_can_move_to3():
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk])
    assert wr1.can_move_to(1, 5, B2) == True
def test_can_move_to4():
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk])
    assert br2a.can_move_to(2, 5, B2) == True
def test_can_move_to5():
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk])
    assert br1.can_move_to(1, 3, B2) == False

wr2b = Rook(2, 4, True)

def test_is_check1():
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2b, wk])
    assert is_check(True, B2) == True
def test_is_check2():
    br2a = Rook(1, 4, False)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2b, wk])
    assert is_check(True, B2) == False
def test_is_check3():
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2b, wk])
    assert is_check(False, B2) == True
def test_is_check4():
    wr1a = Rook(2, 5, True)
    B2 = (5, [wr1a, bk, wk])
    assert is_check(False, B2) == True
def test_is_check5():
    wr1a = Rook(5, 2, True)
    wr2a = Rook(4, 5, True)
    B2 = (5, [wr1a, bk, wk, br2,wr2a])
    assert is_check(True, B2) == False
def test_is_check6():
    wr1a = Rook(1, 2, True)
    wr2a = Rook(3, 1, True)
    B2 = (5, [wr1a, bk, wk, br2,wr2a])
    assert is_check(True, B2) == False
def test_is_check7():
    wr1a = Rook(5, 2, True)
    wr2a = Rook(5, 3, True)
    B2 = (5, [wr1a, bk, wk, br2, wr2a])
    assert is_check(False, B2) == True


def test_is_checkmate1():
    br2b = Rook(4, 5, False)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2b, br3, wr2, wk])
    assert is_checkmate(True, B2) == True
def test_is_checkmate2():
    wr1a = Rook(5, 2, True)
    wr2a = Rook(5, 3, True)
    wka = King(2, 5, True)
    B2 = (5, [wr1a, bk, wka, wr2a])
    assert is_checkmate(False, B2) == True
def test_is_checkmate3():
    wr1a = Rook(5, 2, True)
    wr2a = Rook(5, 1, True)
    br1a = Rook(2, 4, False)
    bka = King(1, 1, False)
    wka = King(5, 5, True)
    B2 = (5, [wr1a, wr2a, bka, wka, br1a])
    assert is_checkmate(False, B2) == False
def test_is_checkmate4():
    wr1a = Rook(1, 5, True)
    wb1a = Bishop(5, 5, True)
    br1a = Rook(4, 3, False)
    bka = King(1, 1, False)
    B2 = (5, [wr1a, wb1a, bka, wk, br1a])
    assert is_checkmate(False, B2) == False
def test_is_checkmate5():
    wr1a = Rook(1, 5, True)
    wb1a = Bishop(5, 5, True)
    bka = King(1, 1, False)
    wk1 = King(3, 1, True)
    B2 = (5, [wr1a, wb1a, bka, wk1])
    assert is_checkmate(False, B2) == True


def test_read_board1():
    B = read_board("board_examp.txt")
    assert B[0] == 5

    for piece in B[1]:  # we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B1[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found

    # we check if every piece in B1 is also present in B; if not, the test will fail
    for piece1 in B1[1]:
        found = False
        for piece in B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found

def test_read_board2():
    with pytest.raises(ValueError):
        read_board("t1.txt")
def test_read_board3():
    with pytest.raises(IndexError):
        read_board("t2.txt")
def test_read_board4():
    with pytest.raises(IndexError):
        read_board("t3.txt")
def test_read_board5():
    with pytest.raises(FileNotFoundError):
        read_board("noFileName")
def test_read_board6():
    B = read_board("t4.txt")
    assert B == False

def test_conf2unicode1():
    assert conf2unicode(B1) == "♖ ♔  \n ♜  ♜\n ♚ ♜ \n♖   ♗\n♗    "
