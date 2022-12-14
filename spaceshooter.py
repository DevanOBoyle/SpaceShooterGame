import sys
import pygame
from triangle import Triangle
from player import Player
from enemy import Enemy
from waves.wave1 import Wave_1
import math

blue = (81, 61, 255)
red = (255, 38, 38)
black = (0, 0, 0)
white = (255, 255, 255)
green = (50, 168, 82)

clock = pygame.time.Clock()


def main():
    pygame.init()
    screen_width, screen_height = 1200, 790
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Game")
    game_frame = [[300, 0], [900, 790]]
    game_screen = pygame.Rect([300, 0], [600, 5000])
    background = pygame.image.load('images/Background.png').convert()
    background = pygame.transform.scale(background, (600, 12000))

    # First set of points is where blast is fired from
    player_origin = [[screen_width//2, screen_height - screen_height//5],
                     [screen_width//2-30, screen_height - screen_height//5 + 50],
                     [screen_width//2+30, screen_height - screen_height//5 + 50]]

    player = Player(player_origin)

    moving_right = False
    moving_left = False
    moving_up = False
    moving_down = False
    shooting = False
    shoot_time = 0
    parry_key_up = True
    parry_time = 0
    parry_cooldown = 0
    power_time = 0
    enemy_times = []
    scroll_speed = 1
    scroll = 0
    scroll2 = 0
    bg_height = background.get_height()

    wave = Wave_1(screen_width, screen_height)
    enemy_times.append([0]*wave.size())

    over = False

    while True:
        screen.fill(black)
        pygame.draw.rect(screen, white, game_screen)
        screen.blit(background, (300, screen_height-bg_height + scroll))

        if (scroll >= bg_height-screen_height and scroll < bg_height):
            screen.blit(background, (300, -bg_height+scroll2))
            scroll2 += scroll_speed

        if abs(scroll) >= bg_height:
            scroll = 0
            scroll2 = 0

        scroll += scroll_speed

        if moving_right and player.ship.check_right_boundary(game_frame):
            player.get_ship().move_right(6)
        if moving_left and player.ship.check_left_boundary(game_frame):
            player.get_ship().move_left(6)
        if moving_up and player.ship.check_upper_boundary(game_frame):
            player.get_ship().move_up(6)
        if moving_down and player.ship.check_lower_boundary(game_frame):
            player.get_ship().move_down(6)

        player.draw_healthbar(screen, red)
        player.draw_power(screen, blue)
        player.draw_ship(screen, blue)
        wave.draw_ship(screen, red)

        if wave.all_dead():
            wave = Wave_1(screen_width, screen_height)

        if (not over):
            wave.move(1, screen_width, screen_height, game_frame)

            if power_time > 0:
                player.power_blasting(screen, green)
                wave.check_power_collision(player)
                power_time -= 1
            else:
                player.power_width = 10
                shoot_time = player.shoot(shooting, shoot_time)
            enemy_times[0] = wave.shoot(enemy_times[0])

            wave.hit(player)

            player.update_blasts(screen, green)
            wave.update_blasts(screen, red)
        
            parry_cooldown = wave.check_collisions(player, screen, parry_cooldown)

        if (parry_time > 0):
            parry_time -= 1
        else:
            player.parry = False

        if (parry_cooldown > 0):
            parry_cooldown -= 1

        if (player.game_over()):
            font = pygame.font.Font('freesansbold.ttf', 60)
            game_over_screen = font.render("Game Over", True, red)
            rect_game_over = game_over_screen.get_rect()
            rect_game_over.center = (screen_width // 2, screen_height //2)
            screen.blit(game_over_screen, rect_game_over)
            over = True
            moving_right = False
            moving_left = False
            moving_up = False
            moving_down = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if over == False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        moving_right = True
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        moving_left = True
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        moving_up = True
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        moving_down = True
                    if event.key == pygame.K_SPACE:
                        shooting = True
                    if event.key == pygame.K_k and parry_key_up and parry_cooldown == 0:
                        player.parry = True
                        parry_key_up = False
                        parry_time = player.parry_time
                        parry_cooldown = player.parry_cooldown
                    if event.key == pygame.K_j and len(player.power) == 5:
                        power_time = player.power_time
                        player.power.clear()


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        moving_right = False
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        moving_left = False
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        moving_up = False
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        moving_down = False
                    if event.key == pygame.K_SPACE:
                        shooting = False
                        shoot_time = -10
                    if event.key == pygame.K_k:
                        parry_key_up = True

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
