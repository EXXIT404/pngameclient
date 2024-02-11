import pygame
import account
# from pygame_textinput import TextInput

pygame.font.init()
font = pygame.font.Font(None, 25)
running = True
sideMenu = False
screenSize = (400,750)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Pn Game")
mainSurface = pygame.Surface(screenSize)
mainSurface.fill((255,0,0))
mainRect = mainSurface.get_rect()
mainRect.center = (screenSize[0]//2 , screenSize[1]//2)
subSideMenu = pygame.Surface(screenSize)
subSideMenu.set_alpha(80)
sideMenuSurface = pygame.Surface((screenSize[0] - 100, screenSize[1]))
sideMenuSurface.fill((0,0,255))
userTest = account.User()

while running :

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_b:
                sideMenu = not sideMenu
    userTest.login()
    if userTest.loggedIn:
        textWelcome = font.render('Bienvenue ' + userTest.name, True, (0, 0, 0) )
        textWelcomeRect = textWelcome.get_rect()
        textWelcomeRect.center = (screenSize[0] // 2, textWelcomeRect[3] // 2)
        mainSurface.blit(textWelcome, textWelcomeRect)
        screen.blit(mainSurface, mainRect)
        if sideMenu :
            screen.blit(subSideMenu, mainRect)
            screen.blit(sideMenuSurface, (0,0))
        else:
            pass


    pygame.display.flip()