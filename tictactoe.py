import pygame
import sys


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
SBLUE = (0, 255, 255)
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
game = True
LEFT = 1
turn = 1


def printText(msg, s, color, pos):
  font = pygame.font.SysFont('Comic Sans MS', s)
  textSurface = font.render(msg, True, color, None)
  textRect = textSurface.get_rect()
  textRect.center = pos
  screen.blit(textSurface, textRect)
  pygame.display.update()


def drawscreen():
  screen.fill(WHITE)
  pygame.draw.line(screen, BLACK, [0, 100], [300, 100], 2)
  pygame.draw.line(screen, BLACK, [0, 200], [300, 200], 2)
  pygame.draw.line(screen, BLACK, [100, 0], [100, 300], 2)
  pygame.draw.line(screen, BLACK, [200, 0], [200, 300], 2)
  pygame.draw.line(screen, BLACK, [0, 300], [300, 300], 2)
  pygame.display.update()
  printTurn()


def mousefillter(x, y):
  new_x = 0
  new_y = 0
  indexnum = 0
  if x % 100 <= 50:
    new_x = x + (50 - (x % 100))
  else:
    new_x = x - ((x % 100) - 50)
  if y % 100 <= 50:
    new_y = y + (50 - (y % 100))
  else:
    new_y = y - ((y % 100) - 50)
  if new_y == 50:
    indexnum = new_x // 100
  elif new_y == 150:
    indexnum = new_x // 100 + 3
  elif new_y == 250:
    indexnum = new_x // 100 + 6
  return new_x, new_y, indexnum


def printTurn():
  pygame.draw.rect(screen, WHITE, [0, 300, 300, 50])
  pygame.draw.line(screen, BLACK, [0, 300], [300, 300], 2)
  if turn % 2 == 1:
    printText("O's Turn", 50, SBLUE, (150, 325))
  elif turn % 2 == 0:
    printText("X's Turn", 50, RED, (150, 325))
  pygame.display.update()


def checkgame():
  if board[0] == 1 and board[1] == 1 and board[2] == 1:
    return 1
  elif board[3] == 1 and board[4] == 1 and board[5] == 1:
    return 1
  elif board[6] == 1 and board[7] == 1 and board[8] == 1:
    return 1
  elif board[0] == 1 and board[3] == 1 and board[6] == 1:
    return 1
  elif board[1] == 1 and board[4] == 1 and board[7] == 1:
    return 1
  elif board[2] == 1 and board[5] == 1 and board[8] == 1:
    return 1
  elif board[0] == 1 and board[4] == 1 and board[8] == 1:
    return 1
  elif board[2] == 1 and board[4] == 1 and board[6] == 1:
    return 1
  elif board[0] == 2 and board[1] == 2 and board[2] == 2:
    return 2
  elif board[3] == 2 and board[4] == 2 and board[5] == 2:
    return 2
  elif board[6] == 2 and board[7] == 2 and board[8] == 2:
    return 2
  elif board[0] == 2 and board[3] == 2 and board[6] == 2:
    return 2
  elif board[1] == 2 and board[4] == 2 and board[7] == 2:
    return 2
  elif board[2] == 2 and board[5] == 2 and board[8] == 2:
    return 2
  elif board[0] == 2 and board[4] == 2 and board[8] == 2:
    return 2
  elif board[2] == 2 and board[4] == 2 and board[6] == 2:
    return 2
  else:
    return 0


def endscreen(winner):
  global game
  screen.fill(WHITE)
  game = False
  if winner == 1:
    printText("Win : Player 1!", 25, SBLUE, (150, 150))
  elif winner == 2:
    printText("Win : Player 2!", 25, RED, (150, 150))
  elif winner == 3:
    printText("DRAW!", 25, RED, (150, 150))
  pygame.draw.rect(screen, BLACK, [75, 200, 150, 50], 2)
  printText("Restart", 30, BLACK, (150, 225))
  pygame.display.update()


def gameplay():
  global board, turn
  while game:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
        mouse = mousefillter(event.pos[0], event.pos[1])
        if board[mouse[2]] == 0:
          if turn % 2 == 1:
            printText("O", 50, SBLUE, (mouse[0], mouse[1]))
            board[mouse[2]] = 1
            turn += 1
            printTurn()
          elif turn % 2 == 0:
            printText("X", 50, RED, (mouse[0], mouse[1]))
            board[mouse[2]] = 2
            turn += 1
            printTurn()
    if checkgame() > 0:
      endscreen(checkgame())
    elif turn == 10:
      endscreen(3)


pygame.init()
size = [300, 350]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("OXO game")
drawscreen()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
      if event.pos[0] > 75 and event.pos[0] < 225 and event.pos[
          1] > 200 and event.pos[1] < 250:
        turn = 1
        board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        game = True
        drawscreen()
  gameplay()
