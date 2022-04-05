def separateMoveInput(move: str) -> tuple[tuple[int, int], tuple[int, int]]:
    alphabet = ' abcdefghijklmnopqrstuvwxyz'

    for i in range(1, len(move)):
        if move[i].isalpha():
            prev = move[0:i]
            nex = move[i:]
            return ((alphabet.index(prev[0]), int(prev[1:])), (alphabet.index(nex[0]), int(nex[1:])))
