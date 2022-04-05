def allPosToReachKing(kingPosition, boardSize):
    KingRow = kingPosition[0]
    KingCol = kingPosition[1]
    posSum = KingRow + KingCol

    allPosInSameRow = [(x, kingPosition[1]) for x in range(1, boardSize + 1)]

    allPosInSameColumn = [(kingPosition[0], y)
                          for y in range(1, boardSize + 1)]

    allPosInDiagonalDes = [(x + 1, x - 1)
                           for x in range(KingRow, boardSize + 1)]
    allPosInDiagonalAsc = [(x - 1, x + 1)
                           for x in range(KingRow, boardSize + 1)]

    allPosInDiagonalDes2 = [(x + 1, x + 1)
                            for x in range(KingRow, boardSize + 1)]
    allPosInDiagonalAsc2 = [(x - 1, x - 1)
                            for x in range(KingRow, boardSize + 1)]

    allPosToReachKing = set([*allPosInSameRow, *allPosInSameColumn, *allPosInDiagonalDes,
                         *allPosInDiagonalAsc, *allPosInDiagonalDes2, *allPosInDiagonalAsc2])
    
    return list(allPosToReachKing)
    
    
