import pygame
from triangle import Triangle


class Player:
    def __init__(self, coords):
        self.ship = Triangle(coords)
        self.blasts = []

    def shoot(self):
        self.blasts.append(pygame.Rect(
            self.ship.x_shoot-5, self.ship.y_shoot-30, 10, 30))

    def update_blasts(self):
        for blast in self.blasts:
            pygame.Rect.move_ip(blast, 0, -5)
            if blast.bottom < 0:
                self.blasts.remove(blast)

    def get_ship(self):
        return self.ship

    def get_blasts(self):
        return self.blasts
