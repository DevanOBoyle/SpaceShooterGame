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
        self.health = 3

    def blast(self):
        self.blasts.append(pygame.Rect(
            self.ship.x_shoot-5, self.ship.y_shoot-30, 5, 20))

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
        self.health -= 1
    
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
