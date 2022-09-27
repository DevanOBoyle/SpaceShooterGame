import sys
import pygame
from triangle import Triangle
from player import Player

blue = (81, 61, 255)
red = (255, 38, 38)
black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()


def main():
    pygame.init()
    screen_width, screen_height = 1200, 790
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Game")
    game_frame = [[300, 0], [900, 790]]
    game_screen = pygame.Rect([300, 0], [600, 790])

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

    while True:
        screen.fill(black)
        pygame.draw.rect(screen, white, game_screen)

        if moving_right and player.ship.check_right_boundary(game_frame):
            player.get_ship().move_right(6)
        if moving_left and player.ship.check_left_boundary(game_frame):
            player.get_ship().move_left(6)
        if moving_up and player.ship.check_upper_boundary(game_frame):
            player.get_ship().move_up(6)
        if moving_down and player.ship.check_lower_boundary(game_frame):
            player.get_ship().move_down(6)

        pygame.draw.polygon(screen, blue, player.ship.get_coords())

        if shooting:
            player.shoot()
            # pygame.time.set_timer(1000)

        player.update_blasts()
        for blast in player.get_blasts():
            pygame.draw.rect(screen, red, blast)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moving_right = True
                if event.key == pygame.K_LEFT:
                    moving_left = True
                if event.key == pygame.K_UP:
                    moving_up = True
                if event.key == pygame.K_DOWN:
                    moving_down = True
                if event.key == pygame.K_SPACE:
                    shooting = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    moving_right = False
                if event.key == pygame.K_LEFT:
                    moving_left = False
                if event.key == pygame.K_UP:
                    moving_up = False
                if event.key == pygame.K_DOWN:
                    moving_down = False
                if event.key == pygame.K_SPACE:
                    shooting = False

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
