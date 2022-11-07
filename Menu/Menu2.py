#Setup de Entrada - Import Bibliotecas-----------------------------------------#
from pip import main
import pygame, sys
from tkinter import *
from random import *
import tkinter.messagebox

#Setup de Entrada - Definições ----------------------------------------------- #


mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Tela de Entrada')
screen = pygame.display.set_mode((1440, 720),0,32)
BACKGROUND = pygame.image.load('c:/Users/david_vasel-junior/Documents/Godshi/godshi/Menu/menu2.PNG')

WIDTH = 1440
HEIGHT = 720


font = pygame.font.SysFont(None, 30)

#Definição de Escrita de Texto-------------------------------------------------#
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

#Definição de ações do Menu Inicial--------------------------------------------#
def main_menu():
    while True:

        screen.fill((0,0,0))
        screen.blit(BACKGROUND, (0, 0))
      
        draw_text('', font, (255, 255, 255), screen, 330, 40)

        
     

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(275, 191, 180, 55)
        button_2 = pygame.Rect(633, 191, 180, 55)
        button_3 = pygame.Rect(33, 44, 180, 55)
        button_4 = pygame.Rect(973, 191, 180, 55)
        if button_1.collidepoint((mx, my)):
            if click:
                game1()
        if button_2.collidepoint((mx, my)):
            if click:
                game2()
        if button_3.collidepoint((mx, my)):
            if click:
                exite()
        if button_4.collidepoint((mx, my)):
            if click:
                game3()
        pygame.draw.rect(screen, (0, 0, 0), button_1)
        pygame.draw.rect(screen, (0, 0, 0), button_2)
        pygame.draw.rect(screen, (0, 0, 0), button_3)
        draw_text('Jogar', font, (255, 255, 255), screen, 338, 208)
        draw_text('Jogar', font, (255, 255, 255), screen, 695, 208)
        draw_text('Sair', font, (255, 255, 255), screen, 103, 60)
        draw_text('Jogar', font, (255, 255, 255), screen, 1038, 208)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)
        
#Definições dos Submenus dos Botões - Game - Opções - Sair --------------------#
def game1():
    exit

def game2():
    class ScoreBoard():
        
        def __init__(self,parent):
            self.parent = parent       
            self.initGUI()        
            self.reset()
            
        def initGUI(self):
            # Lives
            self.livesVar = IntVar()
            Label(self.parent, text="Lives:", font=("Helvetica", 16, "bold")).grid(row=1, column=2, padx=35, pady=100, sticky=N+W)        
            Label(self.parent, textvariable=self.livesVar, font=("Helvetica", 16, "bold")).grid(row=1, column=2, padx=60, pady=150, sticky=N+W)        
            
            # Score
            self.scoreVar = IntVar()
            Label(self.parent, text="Score:", font=("Helvetica", 16, "bold")).grid(row=1, column=2, padx=35, pady=250, sticky=N+W)
            Label(self.parent, textvariable=self.scoreVar, font=("Helvetica", 16, "bold")).grid(row=1, column=2, padx=50, pady=300, sticky=N+W)        
            
            # High score
            self.highScoreVar = IntVar()
            Label(self.parent, text="Highest Score:", font=("Helvetica", 16, "bold")).grid(row=1, column=2, padx=0, pady=400, sticky=N+W)
            Label(self.parent, textvariable=self.highScoreVar, font=("Helvetica", 16, "bold")).grid(row=1, column=2, padx=50, pady=450, sticky=N+W)

        def reset(self):
            self.lives = 5
            self.score = 0
            self.highScore = self.loadScore()
            
            self.livesVar.set(self.lives)
            self.scoreVar.set(self.score)
            self.highScoreVar.set(self.highScore)

        def loadScore(self):
            with open("high-score.txt", "r") as data:
                return int(data.read())                
            
        def saveScore(self):
            if self.score > self.highScore:
                with open("high-score.txt", "w") as data:
                    data.write(str(self.score))
            
        def gameOver(self):
            self.saveScore()
            tkinter.messagebox.showinfo("SYSTEM", "GAME OVER !")        
            if tkinter.messagebox.askyesno("SYSTEM", "Play Again ?"):
                self.reset()
            else:
                exit()
                
        def updateBoard(self, livesStatus, scoreStatus):
            self.lives += livesStatus; self.score += scoreStatus
            if self.lives < 0: self.gameOver()        
            self.livesVar.set(self.lives); self.scoreVar.set(self.score)



    class ItemsFallingFromSky():
        
        def __init__(self,parent,canvas,player,board):
            self.parent = parent                    
            self.canvas = canvas                    
            self.player = player                    
            self.board = board                      
            
            self.fallSpeed = 50                          
            self.xPosition = randint(50, 750)       
            self.isgood = randint(0, 1)             
            
            self.goodItems = ["ananas.gif","apple.gif","orange.gif"]
            self.badItems = ["candy1.gif","candy2.gif","lollypop.gif"]
            
            
            if self.isgood:   
                self.itemPhoto = tkinter.PhotoImage(file = "images/{}" .format( choice(self.goodItems) ) )
                self.fallItem = self.canvas.create_image( (self.xPosition, 50) , image=self.itemPhoto , tag="good" )
            else:
                self.itemPhoto = tkinter.PhotoImage(file = "images/{}" . format( choice(self.badItems) ) )
                self.fallItem = self.canvas.create_image( (self.xPosition, 50) , image=self.itemPhoto , tag="bad" )
                
            
            self.move_object()
            
            
        def move_object(self):
            
            self.canvas.move(self.fallItem, 0, 15)
            
            if (self.check_touching()) or (self.canvas.coords(self.fallItem)[1] > 650):     # [ x0, y0, x1, y1 ]
                self.canvas.delete(self.fallItem)                                           # delete if out of canvas
            else:
                self.parent.after(self.fallSpeed, self.move_object)                         # after some time move object
                
            
        def check_touching(self):
            
            x0, y0 = self.canvas.coords(self.fallItem)
            x1, y1 = x0 + 50, y0 + 50
            
            
            overlaps = self.canvas.find_overlapping(x0, y0, x1, y1)
            
            if (self.canvas.gettags(self.fallItem)[0] == "good") and (len(overlaps) > 1) and (self.board.lives >= 0):   # gettags : ("good",)
                self.board.updateBoard(0, 100)                                              # (lives, score)
                return True                                                                 # touching yes
                
            elif (self.canvas.gettags(self.fallItem)[0] == "bad") and (len(overlaps) > 1) and (self.board.lives >= 0):  # gettags : ("bad",)
                self.board.updateBoard(-1, 0)                                               # (lives, score)
                return True                                                                 # touching yes
                
            return False                                                                    # touching not
        


    class TheGame(ItemsFallingFromSky,ScoreBoard):
        
        def __init__(self,parent):
            self.parent = parent
            
        
            self.parent.geometry("1024x650")
            self.parent.title("Catch My Food Game")

            
            self.canvas = Canvas(self.parent, width=800, height=600)
            self.canvas.config(background="blue")
            self.canvas.bind("<Key>", self.keyMoving)       
            self.canvas.focus_set()
            self.canvas.grid(row=1, column=1, padx=25, pady=25, sticky=W+N)

            
            self.playerPhoto = tkinter.PhotoImage(file = "images/{}" .format( "jew.gif" ) )
            self.playerChar = self.canvas.create_image( (475, 560) , image=self.playerPhoto , tag="player" )

        
            self.personalboard = ScoreBoard(self.parent)

            
            self.createEnemies()
            
            
        def keyMoving(self, event):        
            if (event.char == "a") and (self.canvas.coords(self.playerChar)[0] > 50):
                self.canvas.move(self.playerChar, -50, 0)            
            if (event.char == "d") and (self.canvas.coords(self.playerChar)[0] < 750):
                self.canvas.move(self.playerChar, 50, 0)


        def createEnemies(self):
            ItemsFallingFromSky(self.parent, self.canvas, self.playerChar, self.personalboard)
            self.parent.after(1100, self.createEnemies)
            

            
    if __name__ == "__main__":
        root = Tk()
        TheGame(root)
        root.mainloop()


def game3():
    
    from tkinter import Image
    import pygame, random

    WIDTH = 1440
    HEIGHT = 720
    SPEED = 10
    GAME_SPEED = 10
    GROUND_WIDTH = 2 * WIDTH
    GROUND_HEIGHT = 30


    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image_run = [pygame.image.load('c:/Users/david_vasel-junior/Documents/Godshi/godshi/Game_01/sprites/Run__000.png').convert_alpha(),
                            pygame.image.load('c:/Users/david_vasel-junior/Documents/Godshi/godshi/Game_01/sprites/Run__001.png').convert_alpha(),
                            pygame.image.load('c:/Users/david_vasel-junior/Documents/Godshi/godshi/Game_01/sprites/Run__002.png').convert_alpha(),
                            pygame.image.load('c:/Users/david_vasel-junior/Documents/Godshi/godshi/Game_01/sprites/Run__003.png').convert_alpha(),
                            pygame.image.load('c:/Users/david_vasel-junior/Documents/Godshi/godshi/Game_01/sprites/Run__004.png').convert_alpha(),
                            pygame.image.load('c:/Users/david_vasel-junior/Documents/Godshi/godshi/Game_01/sprites/Run__005.png').convert_alpha(),
                            pygame.image.load('c:/Users/david_vasel-junior/Documents/Godshi/godshi/Game_01/sprites/Run__006.png').convert_alpha(),
                            pygame.image.load('c:/Users/david_vasel-junior/Documents/Godshi/godshi/Game_01/sprites/Run__007.png').convert_alpha(),
                            pygame.image.load('c:/Users/david_vasel-junior/Documents/Godshi/godshi/Game_01/sprites/Run__008.png').convert_alpha(),
                            pygame.image.load('c:/Users/david_vasel-junior/Documents/Godshi/godshi/Game_01/sprites/Run__009.png').convert_alpha(),
                            ]
            self.image_fall = pygame.image.load('c:/Users/david_vasel-junior/Documents/Godshi/godshi/Game_01/sprites/Fall.png').convert_alpha()
            self.image = pygame.image.load('c:/Users/david_vasel-junior/Documents/Godshi/godshi/Game_01/sprites/Run__000.png').convert_alpha()
            self.rect = pygame.Rect(100, 100, 100, 100)
            self.mask = pygame.mask.from_surface(self.image)
            self.current_image = 0


        def update(self, *args):
            def move_player(self):
                key = pygame.key.get_pressed()
                if key[pygame.K_d]:
                    self.rect[0] += GAME_SPEED
                if key[pygame.K_a]:
                    self.rect[0] -= GAME_SPEED
                self.current_image = (self.current_image + 1) % 10
                self.image = self.image_run[self.current_image]
                self.image = pygame.transform.scale(self.image,[50, 50])
            move_player(self)
            self.rect[1] += SPEED

            def fly(self):
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE]:
                    self.rect[1] -= 30
                    self.image = pygame.image.load('c:/Users/david_vasel-junior/Documents/Godshi/godshi/Game_01/sprites/Fly.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [50, 50])
                    print('fly')
            fly(self)

            def fall(self):
                key = pygame.key.get_pressed()
                if not pygame.sprite.groupcollide(playerGroup, groundGroup, False, False) and not key[pygame.K_SPACE]:
                    self.image = self.image_fall
                    self.image = pygame.transform.scale(self.image, [50, 50])
                    print('falling')
            fall(self)

            def evo(self):
                if (placar > 39):
                    self.image = pygame.image.load('c:/Users/david_vasel-junior/Documents/Godshi/godshi/Game_01/sprites/Run__000-1.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [200, 200]) 
                    print('evolution')
            evo(self)

            def evo(self):
                if (placar > 69):
                    self.image = pygame.image.load('c:/Users/david_vasel-junior/Documents/Godshi/godshi/Game_01/sprites/Fly-1.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, [300, 300]) 
                    print('evolution')

                    if (placar > 99):
                        
                        pygame.quit()
                    
            evo(self)

        


    class Ground(pygame.sprite.Sprite):
        def __init__(self, xpos):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('c:/Users/david_vasel-junior/Documents/Godshi/godshi/Game_01/sprites/ground.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(GROUND_WIDTH, GROUND_HEIGHT))
            self.rect = self.image.get_rect()
            self.rect[0] = xpos
            self.rect[1] = HEIGHT - GROUND_HEIGHT

        def update(self, *args):
            self.rect[0] -= GAME_SPEED

    class Obstacles(pygame.sprite.Sprite):
        def __init__(self, xpos, ysize):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('c:/Users/david_vasel-junior/Documents/Godshi/godshi/Game_01/sprites/Box.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, [100, 100])
            self.rect = pygame.Rect(50, 50, 50, 50)
            self.rect[0] = xpos
            self.mask = pygame.mask.from_surface(self.image)
            self.rect[1] = HEIGHT - ysize

        def update(self, *args):
            self.rect[0] -= GAME_SPEED
            print('obstacle')

    class Coins(pygame.sprite.Sprite):
        def __init__(self, xpos, ysize):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('c:/Users/david_vasel-junior/Documents/Godshi/godshi/Game_01/sprites/coin.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, [40, 40])
            self.rect = pygame.Rect(100, 100, 20, 20)
            self.mask = pygame.mask.from_surface(self.image)
            self.rect[0] = xpos
            self.rect[1] = HEIGHT - ysize

        def update(self, *args):
            self.rect[0] -= GAME_SPEED
            print('coin')



    def get_random_obstacles(xpos):
        size = random.randint(120, 600)
        box = Obstacles(xpos, size)
        return box

    def get_random_coins(xpos):
        size = random.randint(60, 500)
        coin = Coins(xpos, size)
        return coin

    def is_off_screen(sprite):
        return sprite.rect[0] < -(sprite.rect[2])

    pygame.init()
    game_window = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption('Jogo 01')

    BACKGROUND = pygame.image.load('c:/Users/david_vasel-junior/Documents/Godshi/godshi/Game_01/sprites/background_03.jpg')
    BACKGROUND = pygame.transform.scale(BACKGROUND,[WIDTH, HEIGHT])

    playerGroup = pygame.sprite.Group()
    player = Player()
    playerGroup.add(player)

    groundGroup = pygame.sprite.Group()
    for i in range(2):
        ground = Ground(WIDTH * i)
        groundGroup.add(ground)

    coinsGroup = pygame.sprite.Group()
    for i in range(2):
        coin = get_random_coins(WIDTH * i + 1000)
        coinsGroup.add(coin)

    obstacleGroup = pygame.sprite.Group()
    for i in range(2):
        obstacle = get_random_obstacles(WIDTH * i + 1000)
        obstacleGroup.add(obstacle)

    gameloop = True
    def draw():
        playerGroup.draw(game_window)
        groundGroup.draw(game_window)
        obstacleGroup.draw(game_window)
        coinsGroup.draw(game_window)
    def update():
        groundGroup.update()
        playerGroup.update()
        obstacleGroup.update()
        coinsGroup.update()
    clock = pygame.time.Clock()
    placar = 0
    while gameloop:
        game_window.blit(BACKGROUND, (0, 0))
        font = pygame.font.SysFont('Arial',30)
        text = font.render('Placar', True, [255,255,255])
        game_window.blit(text, [1100, 20])
        contador = font.render(f'{placar}', True, [255,255,255])
        game_window.blit(contador, [1125, 50])
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        if is_off_screen(groundGroup.sprites()[0]):
            groundGroup.remove(groundGroup.sprites()[0])
            newGround = Ground(WIDTH - 40)
            groundGroup.add(newGround)

        if is_off_screen(obstacleGroup.sprites()[0]):
            obstacleGroup.remove(obstacleGroup.sprites()[0])
            newObstacle = get_random_obstacles(WIDTH * 1.5)
            obstacleGroup.add(newObstacle)
            newCoin = get_random_coins(WIDTH * 2)
            newCoin1 = get_random_coins(WIDTH * 2.2)
            newCoin2 = get_random_coins(WIDTH * 2.4)
            newCoin3 = get_random_coins(WIDTH * 2.6)
            newCoin4 = get_random_coins(WIDTH * 2.8)
            coinsGroup.add(newCoin)
            coinsGroup.add(newCoin1)
            coinsGroup.add(newCoin2)
            coinsGroup.add(newCoin3)
            coinsGroup.add(newCoin4)

        if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
            SPEED = 0
            print('collision')
        else:
            SPEED = 10

        if pygame.sprite.groupcollide(playerGroup, coinsGroup, False, True):
            placar += 1

        
        if placar % 5 == 0 and placar != 0:
            GAME_SPEED += 0.02
            print('GAMESPEED ALTERADA')

        if pygame.sprite.groupcollide(playerGroup, obstacleGroup, False, False):
            break

        update()
        draw()
        pygame.display.update()





def options():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('Opções', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def exite():
    pygame.quit()
    sys.exit()

           
main_menu()
