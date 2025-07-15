import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for drawables in drawable:
            drawables.draw(screen)

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player) == True:
                print("Game Over!")
                sys.exit()

        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collision_check(bullet) == True:
                    asteroid.split()
                    bullet.kill()
                    
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    print (f"""
           Starting Asteroids!
           Screen width: {SCREEN_WIDTH}
           Screen height: {SCREEN_HEIGHT} 
           """)

if __name__ == "__main__":
    main()
