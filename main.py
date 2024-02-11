import pygame
import account

pygame.font.init()
font = pygame.font.Font(None, 25)
running = True
sideMenu = False
screenSize = (400,750)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Pn app")
mainSurface = pygame.Surface(screenSize)
mainSurface.fill((255,0,0))
mainRect = mainSurface.get_rect()
mainRect.center = (screenSize[0]//2 , screenSize[1]//2)
subSideMenu = pygame.Surface(screenSize)
subSideMenu.set_alpha(80)
sideMenuSurface = pygame.Surface((screenSize[0] - 100, screenSize[1]))
sideMenuSurface.fill((0,0,255))
userTest = account.User()
loginMenuSurface = pygame.Surface(screenSize)
loginMenuSurface.fill((0,255,0))
loginMenuSurfaceRect = loginMenuSurface.get_rect()
loginMenuSurfaceRect.center = (screenSize[0]//2 , screenSize[1]//2)
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
textBox1 = pygame.Surface((screenSize[0]-200,25))
textBox1Rect = textBox1.get_rect()
textBox1Rect.center = (screenSize[0]//2 ,textBox1Rect[3] // 2 + 120 )
textBox2 = pygame.Surface((screenSize[0]-200,25))
textBox2Rect = textBox2.get_rect()
textBox2Rect.center = (screenSize[0]//2 ,textBox2Rect[3] // 2 + 150 )
connectBtn = pygame.Surface((screenSize[0]-300, 25))
connectBtnRect = connectBtn.get_rect()
connectBtnRect.center = (screenSize[0]//2 ,connectBtnRect[3] // 2 + 180 )
connectText = font.render('connexion', True ,(255,255,255) )
connectTextRect = connectText.get_rect()
connectTextRect.center = (connectTextRect[0]//2,connectTextRect[1]//2)
textInput1,textInput2 = '' , ''

while running :

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_b:
                sideMenu = not sideMenu
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if textBox1Rect.collidepoint(mousePos):
                print('dans 1 ')
            elif textBox2Rect.collidepoint(mousePos):
                print('dans 2 ')
            elif connectBtnRect.collidepoint(mousePos):
                userTest.login()

    if userTest.loggedIn:
        textWelcome = font.render('Bienvenue ' + userTest.name, True, (0, 0, 0) )
        textWelcomeRect = textWelcome.get_rect()
        textWelcomeRect.center = (screenSize[0] // 2, textWelcomeRect[3] // 2)
        mainSurface.blit(textWelcome, textWelcomeRect)
        screen.blit(mainSurface, mainRect)
        if sideMenu :
            sideText = font.render('menu depliant' , True ,(0, 0, 0) )
            sideTextRect = sideText.get_rect()
            sideTextRect.center = ((screenSize[0] - 100) // 2, sideTextRect[3] // 2)
            sideMenuSurface.blit(sideText , sideTextRect)
            screen.blit(subSideMenu, mainRect)
            screen.blit(sideMenuSurface, (0,0))
    else:
        loginMessage = font.render('login' , True , (0,0,0))
        loginMessageRect = loginMessage.get_rect()
        loginMessageRect.center = (screenSize[0] // 2, loginMessageRect[3] // 2 + 100)
        loginMenuSurface.blit(loginMessage, loginMessageRect)
        textInput1Render = font.render(textInput1 , True , (255,255,255))
        textInput1RenderRect = textInput1Render.get_rect()
        textInput1RenderRect.center = (textInput1RenderRect[0]//2 ,textInput1RenderRect[1]//2)
        textInput2Render = font.render(textInput2 , True , (255,255,255))
        textInput2RenderRect = textInput2Render.get_rect()
        textInput2RenderRect.center = (textInput2RenderRect[0]//2 ,textInput2RenderRect[1]//2)
        textBox1.blit(textInput1Render, (textInput1RenderRect[0]+textBox1Rect[2]//2,textInput1RenderRect[1]+textBox1Rect[3]//2))
        loginMenuSurface.blit(textBox1,textBox1Rect)
        textBox2.blit(textInput2Render, (textInput2RenderRect[0]+textBox2Rect[2]//2,textInput2RenderRect[1]+textBox2Rect[3]//2))
        loginMenuSurface.blit(textBox2,textBox2Rect)
        loginMenuSurface.blit(connectBtn,connectBtnRect)
        connectBtn.blit(connectText,(connectTextRect[0]+connectBtnRect[2]//2,connectTextRect[1]+connectBtnRect[3]//2))
        screen.blit(loginMenuSurface, loginMenuSurfaceRect)




    pygame.display.flip()