import pygame
from triangle import Triangle


class Player:
    def __init__(self, coords):
        self.ship = Triangle(coords)
        self.blasts = []
        self.dmg = 1
        self.health = 3
        self.firespeed = -10
        self.firerate = 20
        self.health = 10
        self.hp = []
        self.power = []
        self.power_time = 100
        self.power_width = 10
        self.power_blast = pygame.Rect(self.ship.x_shoot-50, 0, self.power_width, self.ship.y_shoot-30)
        self.p_x = 930
        self.p_y = 100
        self.parry = False
        self.parry_time = 15
        self.parry_cooldown = self.parry_time + 5
        x = 30
        y = 100
        for i in range(self.health):
            self.hp.append(pygame.Rect(x, y, 30, 20))
            if i == 5:
                x = 30
                y += 25
            else:
                x += 35


    def draw_healthbar(self, screen, color):
        for i in self.hp:
            pygame.draw.rect(screen, color, i)
    
    def draw_power(self, screen, color):
        for i in self.power:
            pygame.draw.rect(screen, color, i)

    def blast(self):
        self.blasts.append(pygame.Rect(
            self.ship.x_shoot-5, self.ship.y_shoot-30, 5, 20))
    
    def power_blasting(self, screen, color):
        self.power_blast = pygame.Rect(self.ship.x_shoot - (self.power_width//2), 0, self.power_width, self.ship.y_shoot-30)
        pygame.draw.rect(screen, color, self.power_blast)
        if self.power_width < 100:
            self.power_width += 5

    def update_blasts(self, screen, color):
        for blast in self.blasts:
            pygame.Rect.move_ip(blast, 0, self.firespeed)
            if blast.bottom < 0:
                self.blasts.remove(blast)
            else:
                pygame.draw.rect(screen, color, blast)
    
    def shoot(self, shooting, shoot_time):
        if shooting:
            if shoot_time == 0:
                self.blast()
                shoot_time += 1
            elif shoot_time < self.firerate:
                shoot_time += 1
            else:
                shoot_time = 0
        else:
            shoot_time += 1
        return shoot_time

    
    def hit(self):
        if self.parry == False:
            self.health -= 1
            self.hp.pop()
    
    def game_over(self):
        if self.health == 0:
            return True
        return False
    
    def remove_blast(self, blast):
        self.blasts.remove(blast)

    def get_ship(self):
        return self.ship

    def get_blasts(self):
        return self.blasts

    def draw_ship(self, screen, color):
        pygame.draw.polygon(screen, color, self.ship.get_coords())
    
    def parrying(self, screen):
        if len(self.power) == 0:
            self.p_x = 930
        if len(self.power) < 5:
            self.power.append(pygame.Rect(self.p_x, self.p_y, 30, 20))
            self.p_x += 35
        pygame.draw.polygon(screen, (50, 168, 82), self.ship.get_coords())
