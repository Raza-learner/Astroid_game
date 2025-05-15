import pygame
from constants  import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot
def main():
        pygame.init()
        print("Starting Asteroids!")
        # print(SCREEN_WIDTH)
        # print(SCREEN_HEIGHT)
        clock =pygame.time.Clock()
        dt=0
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids=pygame.sprite.Group()
        shots = pygame.sprite.Group()
        Shot.containers = (shots,updatable,drawable)
        AsteroidField.containers = (updatable)
        Asteroid.containers = (asteroids, updatable, drawable)
        Player.containers = (updatable, drawable)
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        astroid_field = AsteroidField()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            screen.fill("black")
            updatable.update(dt)
            for asteroid in asteroids:
                if player.collide(asteroid):
                    print("Game over!")
                    return
                for shot in shots:
                    if shot.collide(asteroid):
                        shot.kill()
                        asteroid.split()
             
                
            for obj in drawable:
                obj.draw(screen)
            pygame.display.flip()
            dt= clock.tick(60)/1000
if __name__ == "__main__":
    main()