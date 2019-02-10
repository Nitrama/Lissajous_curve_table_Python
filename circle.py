import pygame
import math
class circle:
    def __init__(self,size,color,time):
        self.angle = 0
        self.color = color
        self.size = size
        self.time = time
        self.time_save = time
        self.x = 0
        self.y = 0
        self.size_half = int(size/2)
        self.surface = pygame.Surface((self.size+10, self.size+10))
        self.radius = self.size_half
        pygame.draw.circle(self.surface, self.color, (self.size_half+5,self.size_half+5),self.size_half , 2)
    def draw(self):
        return self.surface_1
    def tick_surface(self):
        self.surface_1 = pygame.Surface((self.size+10, self.size+10))
        self.surface_1 .blit(self.surface,(0,0))
        self.x = int(self.radius * math.cos(self.angle * math.pi / -180) + self.size_half)
        self.y = int(self.radius * math.sin(self.angle * math.pi / -180) + self.size_half)
        pygame.draw.circle(self.surface_1, (200,200,200), (self.x+5,self.y+5),5)
    def set_time(self,time):
        self.time_save -= time
        #print (self.time_save)
        while True:
            if self.time_save <= 0:
                self.angle += 1
                self.time_save += self.time
                if self.angle > 360:
                    self.angle = 0
            else:
                break
        self.tick_surface()
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
class points:
    def __init__(self,x,y,size,color):
        self.x = x
        self.y = y
        self.surface = pygame.Surface((size+10, size+10))
        self.color = color
        self.size = size
    def draw_pixel(self):
        self.surface.set_at((self.x.get_x() ,self.y.get_y() ),(200,200,200))
    def draw(self):
        return self.surface
