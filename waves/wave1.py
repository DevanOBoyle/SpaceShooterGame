import pygame
import sys
sys.path.append('..')
from triangle import Triangle
from enemy import Enemy
from player import Player

class Wave_1:
    def __init__(self, screen_width, screen_height):
        self.enemies = []
        self.enemies.append(Enemy([[screen_width//2, screen_height//5],
                    [screen_width//2-30, screen_height//5 - 50],
                    [screen_width//2+30, screen_height//5 - 50]], -20, 100))

        self.enemies.append(Enemy([[screen_width//2-140, screen_height//5+25],
                    [screen_width//2-30-140, screen_height//5 - 50+25],
                    [screen_width//2+30-140, screen_height//5 - 50+25]], -20, 100))

        self.enemies.append(Enemy([[screen_width//2+140, screen_height//5+25],
                    [screen_width//2-30+140, screen_height//5 - 50+25],
                    [screen_width//2+30+140, screen_height//5 - 50+25]], -20, 100))

        self.times = [len(self.enemies)] * 0

    def update_blasts(self, screen, color):
        for enemy in self.enemies:
            enemy.update_blasts(screen, color)
    
    def check_collisions(self, player, screen, cooldown):
        for enemy in self.enemies:
            cooldown = enemy.check_collisions(player, screen, cooldown)
        return cooldown
    
    def check_power_collision(self, player):
        for enemy in self.enemies:
            if enemy.check_power_collision(player):
                self.enemies.remove(enemy)

    def shoot(self, shoot_times):
        for i in range(len(self.enemies)):
            shoot_times[i] = self.enemies[i].shoot(shoot_times[i])
        return shoot_times
    
    def draw_ship(self, screen, color):
        for enemy in self.enemies:
            enemy.draw_ship(screen, color)
    
    def hit(self, player):
        for enemy in self.enemies:
            if enemy.hit(player):
                self.enemies.remove(enemy)
    
    def move(self, velocity, width, height, frame):
        for enemy in self.enemies:
            enemy.move(velocity, width, height, frame)
    
    def all_dead(self):
        if len(self.enemies) == 0:
            return True
        return False
            
    def size(self):
        return len(self.enemies)
        