from pprint import pprint
import pygame
import circle
def init():
    pygame.init()
    clock = pygame.time.Clock()
    circles = {}
    circles["x"] = {}
    circles["y"] = {}
    circles["pixel"] = {}
    myfont = pygame.font.SysFont("arial", 14)
    myfont.set_bold(True)
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 1)
    pygame.display.set_caption("Loading...INIT")
    screen = pygame.display.set_mode((1000,  1000))
    running = True
    for x in range(1,15):
        circles["x"][x] = circle.circle(50,(100,100,100),2*x)
        circles["x"][x].tick_surface()
    for y in range(1,15):
        circles["y"][y] = circle.circle(50,(100,100,100),2*y)
        circles["y"][y].tick_surface()
    for x in circles["x"]:
        circles["pixel"][x] = {}
        for y in circles["y"]:
            circles["pixel"][x][y] = circle.points(circles["x"][x],circles["y"][y],50,(100,100,100))
    while running:
        events = pygame.event.get()
        for event in events:
            mousepos = pygame.mouse.get_pos()
            mouseposx = int(mousepos[0]/10)
            mouseposy = int(mousepos[1]/10)
                # Spiel beenden, wenn wir ein QUIT-Event finden.
            if event.type == pygame.QUIT:
                print ("pressed exit")
                #p.terminate()
                pygame.display.quit()
                running = False
                break
        time = clock.get_time()
        for x in circles["x"]:
            circles["x"][x].set_time(time)
        for y in circles["y"]:
            circles["y"][y].set_time(time)
        for x in circles["pixel"]:
            for y in circles["pixel"][x]:
                circles["pixel"][x][y].draw_pixel()
        if running is True:
            pygame.display.set_caption(str(int(clock.get_fps())))

            screen.fill((0, 0, 0))
            for x in circles["x"]:
                screen.blit(circles["x"][x].draw(),(60*x,0))
            for y in circles["y"]:
                screen.blit(circles["y"][y].draw(),(0,60*y))
            for x in circles["pixel"]:
                for y in circles["pixel"][x]:
                    screen.blit(circles["pixel"][x][y].draw(),(x*60,y*60))
            clock.tick(30)
            pygame.display.flip()

if __name__ == '__main__':
    init()
