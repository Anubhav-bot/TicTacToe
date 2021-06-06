
import pygame as pg


pg.init()

### VARIABLES ###

HEIGHT = 500
WIDTH = 800

GREY = (30, 30, 30)
RED = (255, 0,0)

the_board = {7: ' ', 8: ' ', 9: ' ',
            4: ' ', 5: ' ', 6: ' ',
            1: ' ', 2: ' ', 3: ' '}
#
## PYGAME SETUP ###
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Tic Tac Toe")



def render(text, size = 64, color = (0, 255, 0)):
     return pg.font.Font(None, size).render(text, True, color)

class Board(object):


    
    def __init__(self):
        self.width = 300
        self.height = 300
        self.x = (WIDTH // 2) - (self.width // 2)
        self.y = (HEIGHT // 2) - (self.height // 2)
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.board = the_board

        self.minirects ={7: pg.Rect(self.x, self.y, 95, 95), 8: pg.Rect(self.x + 100, self.y, 95, 95), 9: pg.Rect(self.x + 200, self.y, 95, 95), 
        4: pg.Rect(self.x, self.y + 100, 95, 95), 5: pg.Rect(self.x + 100, self.y + 100, 95, 95), 6: pg.Rect(self.x + 200, self.y + 100, 95, 95), 
        1: pg.Rect(self.x, self.y + 200, 95, 95), 2: pg.Rect(self.x + 100, self.y + 200, 95, 95), 3: pg.Rect(self.x + 200, self.y + 200, 95, 95)}

        #self.minisurfs = list(map(lambda x: pg.Surface(int(x.w), int(x.h)), list(self.minirects.values()) ) )

    def draw(self, turn):
        
        pg.draw.rect(screen, (0, 0, 0), self.rect, 1) # -> The '1' at the last defines border
        
        pg.draw.rect(screen, (255, 255, 255), self.minirects[1])
        pg.draw.rect(screen, (255, 255, 255), self.minirects[2])
        pg.draw.rect(screen, (255, 255, 255), self.minirects[3])
        pg.draw.rect(screen, (255, 255, 255), self.minirects[4])
        pg.draw.rect(screen, (255, 255, 255), self.minirects[5])
        pg.draw.rect(screen, (255, 255, 255), self.minirects[6])
        pg.draw.rect(screen, (255, 255, 255), self.minirects[7])
        pg.draw.rect(screen, (255, 255, 255), self.minirects[8])
        pg.draw.rect(screen, (255, 255, 255), self.minirects[9])
#show turn
        turn_text = pg.font.Font(None, 64).render(f"{turn}'s turn", True, (0, 255, 0))
        screen.blit(turn_text, ((WIDTH // 2) - (turn_text.get_size()[0] // 2), self.y - 75))

#Interact
        for i in range(1, 10):
            screen.blit(render(self.board[i], 64, (RED)), (self.minirects[i].center[0] - 15, self.minirects[i].center[1] - 15) )
        
class Game():


    def __init__(self):
        pass
    

    def restart(self, player):
        screen.fill((255, 0, 0))
        screen.blit(render('Restart?'),( (WIDTH // 2 - render('Restart?').get_size()[0] // 2), HEIGHT // 2))
        screen.blit(render(f'{player} wins!!'), ( ((WIDTH // 2) - render(f'{player} wins!!').get_size()[0] // 2), board.rect.top) )


        yes = render('Yes', 64, (0, 0, 255))
        no = render('No', 64, (0, 0, 255))
        screen.blit(yes, (250, 400))
        screen.blit(no, (550, 400))

        yes_rect = pg.Rect(250, 400, yes.get_size()[0], yes.get_size()[1])
        no_rect = pg.Rect(550, 400, no.get_size()[0], no.get_size()[1])

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if yes_rect.collidepoint(event.pos):
                    for i in range(1, 10):
                        the_board[i] = ' '
                        if player == 'X' or player == 'O':
                             global turn
                             turn = player

                elif no_rect.collidepoint(event.pos):
                    pg.quit()
                    running = False

    def tw(self, player):
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        
        self.restart(player)

    def check_winner(self, turn):
        
        if the_board[7] == the_board[8] == the_board[9] != ' ':
            self.tw(turn)
        elif the_board[4] == the_board[5] == the_board[6] != ' ':
            self.tw(turn)
        elif the_board[1] == the_board[2] == the_board[3] != ' ':
            self.tw(turn)
            
        elif the_board[7] == the_board[4] == the_board[1] != ' ':
            self.tw(turn)
        elif the_board[8] == the_board[5] == the_board[2] != ' ':
            self.tw(turn)
        elif the_board[9] == the_board[6] == the_board[3] != ' ':
            self.tw(turn)
            
        elif the_board[7] == the_board[5] == the_board[3] != ' ':
            self.tw(turn)
        elif the_board[1] == the_board[5] == the_board[9] != ' ':
            self.tw(turn)
        elif ' ' not in list(the_board.values()):
            self.restart('Noone')


board = Board()
gameGUI = Game()
### Main Loop ###
running = True
turn = 'O'
game_over = False

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}


#board_text = pg.font.Font(None, 64).render((turn), True, (0, 0, 0))





while running:


    
    screen.fill(GREY)
    board.draw(turn)

    gameGUI.check_winner(turn)


    pg.display.update()


    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
        if event.type == pg.MOUSEBUTTONDOWN:

            for i in board.minirects:

                if board.minirects[i].collidepoint(event.pos) and board.board[i] == ' ':
                    board.board[i] = turn
                    if turn == 'X':
                        turn = 'O'
                    else:
                        turn = 'X'





