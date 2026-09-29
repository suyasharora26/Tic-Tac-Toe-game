# Tic-tac-toe project

board = [" "] * 9


# function to show the grid
def printBoard(b):
  print("\n " + b[0] + " | " + b[1] + " | " + b[2])
  print("---|---|---")
  print(" " + b[3] + " | " + b[4] + " | " + b[5])
  print("---+---+---")
  print(f" {b[6]} | {b[7]} | {b[8]}\n")


def checkWin(b):
  # row checks
  if b[0] == b[1] == b[2] and b[0] != " ":
    return b[0]
  if b[3] == b[4] and b[4] == b[5] and b[3] != " ":
    return b[3]
  if b[6] == b[7] == b[8] and b[6] != " ":
    return b[6]

  # check vertical columns using a loop
  for col in range(3):
    if b[col] == b[col + 3] == b[col + 6] and b[col] != " ":
      return b[col]

  # diagonals
  if b[0] == b[4] == b[8] and b[0] != " ":
    return b[0]
  if b[2] == b[4] == b[6] and b[4] != " ":
    return b[2]

  return None


def isFull(b):
  occupied = 0
  for i in range(len(b)):
    if b[i] != " ":
      occupied += 1

  if occupied == 9:
    return True
  else:
    return False


# main code
currentPlayer = "X"
gameRunning = True

while gameRunning:
  printBoard(board)

  userInput = input("Player " + currentPlayer + ", enter position (1-9): ")

  # validate input
  if not userInput.isdigit():
    print("Invalid input! please enter a number.")
    continue

  pos = int(userInput) - 1

  if pos < 0 or pos > 8:
    print("Number must be between 1 and 9.")
    continue

  if board[pos] != " ":
    print("Spot already occupied! Pick another.")
    continue

  # update board
  board[pos] = currentPlayer

  winner = checkWin(board)
  if winner != None:
    printBoard(board)
    print("Congratulations! Player " + winner + " wins!")
    gameRunning = False
  elif isFull(board):
    printBoard(board)
    print("Match ended in a draw.")
    break
  else:
    # switch player turn
    if currentPlayer == "X":
      currentPlayer = "O"
    else:
      currentPlayer = "X"