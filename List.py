from operator import le


board = {
    '1':' ','2':' ','3':' ',
    '4':' ','5':' ','6':' ',
    '7':' ','8':' ','9':' ',
}
size = len(board)
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def play():
    turn = 'X'
    count = 0
    for i in range(10):
        printBoard(board)
        print("Its your turn, " + turn)
        move = input()

        if(board[move]== ' '):
            board[move] = turn
            count+=1
        else:
            print("That place is Already filled")
            continue


play()



