def printboard(xstate,zstt):
    zero = 'O' if zstt[0] else ('X' if xstate[0] else 0)
    one =  'X' if xstate[1] else('O' if zstt[1] else 1)
    two =  'X' if xstate[2] else('O' if zstt[2] else 2)
    thre = 'X' if xstate[3] else('O' if zstt[3] else 3)
    four = 'X' if xstate[4] else('O' if zstt[4] else 4)
    five = 'X' if xstate[5] else('O' if zstt[5] else 5)
    six =  'X' if xstate[6] else('O' if zstt[6] else 6)
    seven = 'X' if xstate[7] else('O'if zstt[7] else 7)
    eight = 'X' if xstate[8] else('O'if zstt[8] else 8)
    print(f"{zero}| {one}  | {two}")
    print(f'    -         - ')
    print(f"{thre}| {four}  | {five}")
    print(f'    -         -   ')
    print(f"{six}|  {seven} | {eight}")

def sum(a,b,c):
    return a+b+c


def checkwin(xst,zst):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xst[win[0]],xst[win[1]],xst[win[2]]) == 3):
            print("X's wins")
            return 1
        if(sum(zst[win[0]],zst[win[1]],zst[win[2]]) == 3):
            print("O's wins")
            return 0
        
    return -1

if __name__ == '__main__':
    xstate = [0,0,0,0,0,0,0,0,0]
    zstate = [0,0,0,0,0,0,0,0,0]
    turn = 1 # 1 for x 0 - o
    count = 0
    while True:
        printboard(xstate,zstate)
        if(turn == 1):
            print("x's choice")
            try:
                value = int(input("please Value: "))
                if xstate[value] == 0:
                    xstate[value] = 1
                    turn = 0
                else:
                    print("Already Filled")
            except ValueError:
                print("Ivalid Value")
        elif(turn == 0):
            print("O's value")
            value = int(input("please Value: "))
            if zstate[value] == 0:
                zstate[value] = 1
                turn = 1 
            else:
                print("Already Filled")
        chk = checkwin(xstate,zstate)
        if(chk!=-1):
            break





