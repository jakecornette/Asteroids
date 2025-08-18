import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroifield = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_for_collisions(shot):
                    asteroid.split()
                    shot.kill()
            if asteroid.check_for_collisions(player) == True:
                raise SystemExit("Game over!")

        for shot in shots:
            for asteroid in asteroids:
                if shot.check_for_collisions(asteroid):
                    pass
                    # Handle collision (e.g., remove shot, split asteroid, etc.)

        for d in drawable:
            d.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
