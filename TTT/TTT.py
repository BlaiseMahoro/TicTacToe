'''Interesting TIc TAC TOE Game. Enjoy!'''
def main():
    board=[' ']*9
    displayboard(board)
    player1=input('Player1, enter a mark you wanna use: ')
    player2=input('Player2, enter a mark you wanna use: ')
    currPlayer=player1
    while(not isfull(board) and not winnerIsKnown(board, player1, player2)):
        move=int(input('Player' + currPlayer +', enter a position: '))
        if board[move]==' ':
            board[move]=currPlayer
        else:
            print('Spot taken! Please choose another position. ')
        displayboard(board)
        if currPlayer==player1:
            currPlayer=player2
        else:
            currPlayer=player1
    if isDraw(board, player1,player2):
        print('It''s a draw!')
    elif isWinner(board,player1):
        print('Player1 won')
    else:
        print('Player2 won')
    return 0;

def isfull(board):
    for b in board:
        if b==' ':
            return False
    return True
def isWinner(board, mark):
    return board[0]==board[1]==board[2]==mark or board[0]==board[3]==board[6] == mark or board[3]==board[4]==board[5]==mark or board[6]==board[7]==board[8]==mark or board[1]==board[4]==board[7]==mark or board[2]==board[5]==board[8]==mark or board[2]==board[4]==board[6]==mark
def winnerIsKnown(board, mark, mark_1):
    return isWinner(board, mark) or isWinner(board, mark_1)
def isDraw(board, mark, mark_1):
    return isfull(board) and not winnerIsKnown(board, mark, mark_1)

def displayboard(board):
    i=0
    j=0
    while i<9:
      print(board[i],end='')
      if i==2 or i==5:
          print('\n------\n',end='')
      elif i<8:
          print('|',end='')         
      i+=1
    print()






main()