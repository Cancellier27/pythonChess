from config.pieces import Board
alphabet = ' abcdefghijklmnopqrstuvwxyz'


def save_board(filename: str, B: Board) -> None:
    '''saves board configuration into file in current directory in plain format'''
    
    filename  = filename.split('.')[0] if '.txt' in filename else filename

    try:
        newFile = open(f'boards/{filename}.txt', 'x')
    except FileExistsError:
        replace = input(
            '>> This filename already exists, do you want to replace it?(y/n): ')
        while True:
            if replace == 'y':
                newFile = open(f'boards/{filename}.txt', 'w+')
                break
            elif replace == 'n':
                saveConfigFileName = input(
                    '>> File name to store the configuration: ')
                save_board(saveConfigFileName, B)
                return
            else:
                print('>> >>> I did not understand... ')
                replace = input(
                    '>> Do you want to replace the filename? (y/n): ')
    except Exception as e:
        print(f'>> >>> {e}\n')
        replace = input('>> Do you want to replace the filename? (y/n): ')
        

    getWhiteMoves = [f'{x.position()[3][0]}{alphabet[x.position()[0]]}{x.position()[1]}'
                     for x in filter(lambda x: x.position()[2] == True, B[1])]
    getBlackMoves = [f'{x.position()[3][0]}{alphabet[x.position()[0]]}{x.position()[1]}'
                     for x in filter(lambda x: x.position()[2] == False, B[1])]

    newFile.write(f'{B[0]}\n')                      # First line
    newFile.write(f"{', '.join(getWhiteMoves)}\n")  # Second Line
    newFile.write(f"{', '.join(getBlackMoves)}\n")  # Third Line

    newFile.close()
