import pygame
pygame.mixer.init()


def checkkeys(mydata):
    circle = pygame.mixer.Sound("circle.ogg")
    rectangle = pygame.mixer.Sound("rectangle.ogg")
    ellipse = pygame.mixer.Sound("ellipse.ogg")
    (event, background, drawcolor, linewidth, keepgoing) = mydata
    
    if event.key == pygame.K_q:
        keepgoing = False
    elif event.key == pygame.K_c:
        background.fill((255,255,255))
    elif event.key == pygame.K_s:
        pygame.image.save(background, "untitled.bmp")
    elif event.key == pygame.K_l:
        background = pygame.image.load("untitled.bmp")
    elif event.key == pygame.K_r:
        drawcolor = (255,0,0)
    elif event.key == pygame.K_g:
        drawcolor = (0,255,0)
    elif event.key == pygame.K_b:
        drawcolor = (0,0,255)
    elif event.key == pygame.K_e:
        drawcolor = (255,255,255)
    elif event.key == pygame.K_k:
        drawcolor = (0,0,0)
    elif event.key == pygame.K_y:
        drawcolor = (255,255,0)
    elif event.key == pygame.K_t:
        drawcolor = (0,255,255)
    elif event.key == pygame.K_p:
        drawcolor = (255,0,255)

    elif event.key == pygame.K_o:
        circle.play()
        radius = input("give radius for circle :")
        radius = int(radius)
        choice = input("Enter 'f' for filled circle and 'o' for empty circle:")
        start = pygame.mouse.get_pos()
        if choice == 'f':
            pygame.draw.circle(background, drawcolor, start, radius)
        elif choice == 'o':
            pygame.draw.circle(background, drawcolor, start, radius)
            rad = radius - linewidth
            pygame.draw.circle(background, (255,255,255), start, rad)

    elif event.key == pygame.K_n:
        rectangle.play()
        length = input("give length of rectangle :")
        length = int(length)
        breadth = input("give breadth of rectangle :")
        breadth = int(breadth)
        start = pygame.mouse.get_pos()
        pygame.draw.rect(background, drawcolor, (start,(length,breadth)), linewidth)
    
    elif event.key == pygame.K_i:
        ellipse.play()
        start = pygame.mouse.get_pos()
        length = input("give length of ellipse :")
        length = int(length)
        breadth = input("give breadth of ellipse :")
        breadth = int(breadth)
        pygame.draw.ellipse(background, drawcolor, (start,(length,breadth)), linewidth)
      
    elif event.key == pygame.K_1:
        linewidth = 1
    elif event.key == pygame.K_2:
        linewidth = 2
    elif event.key == pygame.K_3:
        linewidth = 3
    elif event.key == pygame.K_4:
        linewidth = 4
    elif event.key == pygame.K_5:
        linewidth = 5
    elif event.key == pygame.K_6:
        linewidth = 6
    elif event.key == pygame.K_7:
        linewidth = 7
    elif event.key == pygame.K_8:
        linewidth = 8
    elif event.key == pygame.K_9:
        linewidth = 9

    mydata = (event, background, drawcolor, linewidth, keepgoing)
    return mydata

def showstats(drawcolor, linewidth):
    myfont = pygame.font.SysFont("None",20)
    stats = "color: %s, width:%d" % (drawcolor, linewidth)
    statsurf = myfont.render(stats, 1, (drawcolor))
    return statsurf

def main():
    print("Welcome to Paint")
    print("action       - command ")
    print("Red          - R")
    print("Blue         - B")
    print("Green        - G")
    print("Yellow       - Y")
    print("Torquoise    - T")
    print("Pink         - P")
    print("Black        - K")
    print("Eraser       - E")
    print("Width        - 1-9")
    
    print("Circle       - O")
    print("Rectangle    - N")
    print("Ellipse      - I")
        
    print("Clear        - C")
    print("Save         - S")
    print("Load         - L")
    print("Quit         - Q")
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("paint: (r)ed, (g)reen, (t)urquoise, (p)ink, (y)ellow, (b)lue, (e)raser, blac(k), (1-9)width, (c)lear, (s)ave, (l)oad, (q)uit")

    background = pygame.Surface(screen.get_size())
    background.fill((255,255,255))

    circle = pygame.mixer.Sound("circle.ogg")
    
    clock = pygame.time.Clock()
    keepgoing = True
    linestart = (0,0)
    drawcolor = (0,0,0)
    linewidth = 3
    
    while keepgoing:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Thank You! Have a nice day!")
                keepgoing = False
            elif event.type == pygame.MOUSEMOTION:
                lineend = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed() == (1,0,0):
                    pygame.draw.line(background, drawcolor, linestart, lineend, linewidth)    
                linestart = lineend
            elif event.type == pygame.KEYDOWN:
                mydata = (event, background, drawcolor, linewidth, keepgoing)
                mydata = checkkeys(mydata)
                (event, background, drawcolor, linewidth, keepgoing) = mydata
                
        screen.blit(background, (0,0))
        mylabel = showstats(drawcolor, linewidth)
        screen.blit(mylabel, (450,450))
        pygame.display.flip()

if __name__ == "__main__":
    main()
