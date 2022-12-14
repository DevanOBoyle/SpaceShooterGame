import pygame
from triangle import Triangle
from player import Player

class Enemy:
    def __init__(self, coords, firespeed, firerate):
        self.ship = Triangle(coords)
        self.firespeed = firespeed
        self.firerate = firerate
        self.blasts = []

    def blast(self):
        self.blasts.append(pygame.Rect(
            self.ship.x_shoot-5, self.ship.y_shoot+30, 5, 20))

    def update_blasts(self, screen, color, player):
        for blast in self.blasts:
            pygame.Rect.move_ip(blast, 0, 5)
            if blast.top > 790:
                self.blasts.remove(blast)
            else:
                pygame.draw.rect(screen, color, blast)
                if player.ship.collide_point(blast.topleft):
                    print(player.health)
                    player.hit()
                    self.blasts.remove(blast)
                elif player.ship.collide_point(blast.topright):
                    print(player.health)
                    player.hit()
                    self.blasts.remove(blast)
                elif player.ship.collide_point(blast.bottomleft):
                    print(player.health)
                    player.hit()
                    self.blasts.remove(blast)
                elif player.ship.collide_point(blast.bottomright):
                    print(player.health)
                    player.hit()
                    self.blasts.remove(blast)

    def shoot(self, shoot_time):
        #print(self.firerate)
        if shoot_time == 0:
            self.blast()
            shoot_time += 1
        elif shoot_time < self.firerate:
            shoot_time += 1
        else:
            shoot_time = 0
        return shoot_time
    
    def hit(self, player):
        for blast in player.get_blasts():
            if self.ship.collide_point(blast.topleft):
                player.remove_blast(blast)
                return True
            elif self.ship.collide_point(blast.topright):
                player.remove_blast(blast)
                return True
            elif self.ship.collide_point(blast.bottomleft):
                player.remove_blast(blast)
                return True
            elif self.ship.collide_point(blast.bottomright):
                player.remove_blast(blast)
                return True
                
        return False

    def get_ship(self):
        return self.ship

    def get_blasts(self):
        return self.blasts
    
    def draw_ship(self, screen, color):
        pygame.draw.polygon(screen, color, self.ship.get_coords())
