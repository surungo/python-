trycounts=0

def isNumInRow(board,num,row):
 for x in board[row]:
  if x == num:
   return True
 return False
 
def isNumInCol(board,num,col):
 for x in board:
  if x[col] == num:
   return True
 return False

def isNumInBox(board,num,row,col):
 bxRow = (row - row % 3)
 bxCol = (col - col % 3)
 for i in range(bxRow,bxRow+3,1):
  for j in range(bxCol,bxCol+3,1):
   if board[i][j] == num:
    return True
 return False

def isValid2(board,num,row,col):
 if isNumInRow(board,num,row) or isNumInCol(board,num,col) or isNumInBox(board,num,row,col):
  return False
 else:
  return True
  
def isValid(board,num,row,col):
 return not(isNumInRow(board,num,row)) and not(isNumInCol(board,num,col)) and not(isNumInBox(board,num,row,col))
 
def printTest(board,num,row,col):
 print("nrc",num,row,col)
 if isNumInRow(board,num,row):
  print("row invalido")
 else:
  print("row valido")

 if isNumInCol(board,num,col):
  print("col invalido")
 else:
  print("col valido")

 if isNumInBox(board,num,row,col):
  print("box invalido")
 else:
  print("box valido")
 
 if isValid(board,num,row,col):
  print("valido")
 else:
  print("invalido")
  
def solver(board):
 global trycounts
 for row in range(0,9,1):
  for col in range(0,9,1):
   if board[row][col] == 0:
    for num in range(1,10,1):
     if isValid(board,num,row,col):
      board[row][col]=num
      if solver(board):
       return True
      else:
       board[row][col]=0
    trycounts+=1
    print(trycounts, end = "\r")
    return False
 return True

def printBoard(board):
 for i in range(0,9,1):
  print(board[i])



board = [
[7,0,2,0,5,0,6,0,0],
[0,4,3,0,0,0,7,5,0],
[0,0,0,0,0,3,0,0,0],
[1,0,0,0,0,9,5,0,0],
[8,0,0,0,0,0,0,9,0],
[0,9,0,0,0,0,0,0,8],
[0,0,9,7,0,0,0,0,5],
[0,0,0,2,0,0,0,0,0],
[0,0,7,0,4,0,2,0,3]
]

board1 = [
[7,0,2,0,5,0,6,0,0],
[0,0,0,0,0,3,0,0,0],
[1,0,0,0,0,9,5,0,0],
[8,0,0,0,0,0,0,9,0],
[0,4,3,0,0,0,7,5,0],
[0,9,0,0,0,0,0,0,8],
[0,0,9,7,0,0,0,0,5],
[0,0,0,2,0,0,0,0,0],
[0,0,7,0,4,0,2,0,3]
]

num=1
row=5
col=5

printTest(board,num,row,col) 
printBoard(board)
solver(board)
print(trycounts )
printBoard(board)

