import pygame
from circleshape import *
from constants import *
from shot import *

class Player (CircleShape):
    def __init__ (self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.triple_shot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt 

    def update(self, dt):
        self.shot_timer -= dt
        self.triple_shot_timer -= dt

        keys = pygame.key.get_pressed()
        mice = pygame.mouse.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate (dt * -1)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate (dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move (dt)
        if keys[pygame.K_s or keys[pygame.K_DOWN]]:
            self.move (dt * -1)
        if keys[pygame.K_SPACE] or mice[0]:
            self.shoot()
        if keys[pygame.K_p] or mice [2]:
            self.triple_shot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shot_timer > 0:
            return
        else:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1)
            shot.velocity = shot.velocity.rotate(self.rotation)
            shot.velocity *= PLAYER_SHOOT_SPEED
            self.shot_timer = PLAYER_SHOT_COOLDOWN

    def triple_shot(self):
        if self.triple_shot_timer > 0:
            return
        else:
            centre_shot = Shot(self.position.x, self.position.y)
            angled_shot_1 = Shot(self.position.x, self.position.y)
            angled_shot_2 = Shot(self.position.x, self.position.y)
            centre_shot.velocity = pygame.Vector2(0, 1)
            angled_shot_1.velocity = pygame.Vector2(0, 1)
            angled_shot_2.velocity = pygame.Vector2(0, 1)
            centre_shot.velocity = centre_shot.velocity.rotate(self.rotation)
            angled_shot_1.velocity = angled_shot_1.velocity.rotate(self.rotation)
            angled_shot_2.velocity = angled_shot_2.velocity.rotate(self.rotation)
            first_shot_vector = angled_shot_1.velocity.rotate(-20)
            second_shot_vector = angled_shot_2.velocity.rotate(20)
            angled_shot_1.velocity = first_shot_vector
            angled_shot_2.velocity = second_shot_vector
            centre_shot.velocity *= PLAYER_SHOOT_SPEED
            angled_shot_1.velocity *= PLAYER_SHOOT_SPEED
            angled_shot_2.velocity *= PLAYER_SHOOT_SPEED
            self.triple_shot_timer = PLAYER_TRIPLE_SHOT_COOLDOWN