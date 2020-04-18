import pygame, sys, random
from pygame.locals import *
pygame.init()
fps= pygame.time.Clock()
width=800
height=600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Orav")

bg=pygame.transform.scale(pygame.image.load("Backroud.png"),(width,height))
en=pygame.image.load("Owl.png")
pl=pygame.image.load("Squirrel.png")
ac=pygame.image.load("Acorn.png")

pygame.display.set_icon(ac)

class button:
    def __init__(self, x, y, width, height, text=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    def draw(self, screen):
        pygame.draw.rect(screen, (0,0,0), (self.x,self.y,self.width,self.height),0)
        if self.text != "":
            font = pygame.font.SysFont("comicsans", 20)
            text = font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    def mousebutton(self, pos):
        if pos[0]>self.x and pos[0]<self.x+self.width:
            if pos[1]>self.y and pos[1]<self.y+self.height:
                return True
        return False

class player:
    def __init__(self, x, y, collide):
        self.x = x
        self.y = y
        self.collide = collide
    def collide(x, y):
        
def mainmenu():
    Button=button(150,255,250,100,"Play")
    def redraw_window():
        screen.blit(bg,(0,0))
        screen.blit((pygame.font.SysFont("comicsans",20).render("Menu",1,(0,0,0))),(0,0))
        button.draw(screen)
        pygame.display.update()
    while True:
        fps.tick(15)
        redraw_window()
        pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if button.mousebutton(pos):
                    game()

def game():
    level = 1
    score = 0
    def redraw_window():
        pygame.font.SysFont("comicsans",20).render(f"Level: {level}",1,(0,0,0))
        pygame.font.SysFont("comicsans",20).render(f"Score: {score}",1,(0,0,0))
        screen.blit(bg,(0,0))
        screen.blit(pygame.font.SysFont("comicsans",20).render(f"Level: {level}",1,(0,0,0)),(width-pygame.font.SysFont("comicsans",20).render(f"Level: {level}",1,(0,0,0)).get_width()-10,10))
        pygame.display.update()
            
    while True:
        fps.tick(15)
        redraw_window()
        click=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    pausemenu()
        


def pausemenu():
    running=True
    click=False
    def redraw_window():
        screen.fill((0,0,0))
        drawtext("Game Paused",pygame.font.SysFont("consolas",12),(255,255,255),screen,20,20)
        mx, my = pygame.mouse.get_pos()
        exittomainmenu=pygame.Rect(50,100,200,50)
        if exittomainmenu.collidepoint((mx,my)):
            if click:
                running=False
        pygame.draw.rect(screen, (0,255,0),exittomainmenu)
        pygame.display.update()
    
    pos = pygame.mouse.get_pos()
    while running:
        fps.tick(15)
        redraw_window()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    running=False
            if event.type == MOUSEBUTTONDOWN:
                if button.mousebutton(pos):
                    mainmenu()

def options():
    running = True
    def redraw_window():
        screen.fill((0,0,0))
        drawtext("Options",pygame.font.SysFont("Consolas", 12),(255,255,255),screen,20,20)
        pygame.display.update()
    while running:
        fps.tick(15)
        redraw_window()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    running=False

mainmenu()
