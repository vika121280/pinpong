import pygame
pygame.init()
window_width, window_height = 800, 600
rocket_img = 'rocket.png'
ball_img = 'ball.png'
BG_color = (64, 64, 64)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, x=0, y=0, width=0, height=0):
        image = pygame.image.load(image)
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite):
    def __init__(
        self, image, x=0, y=0, width=0, height=0, speed=5, k_up = pygame.K_UP, k_down = pygame.K_DOWN
    ):
        super().__init__(image, x, y, width, height)
        self.speed = speed
        self.k_up = k_up
        self.k_down = k_down
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.k_up] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[self.k_down] and self.rect.y < (
            window_height - self.rect.height
        ):
            self.rect.y += self.speed


window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('pinpong')
window.fill(BG_color)
clock = pygame.time.Clock()

player_left = Player(
    rocket_img, 5, 5, 30, 100, 5, pygame.K_w, pygame.K_s
)
player_right = Player(
    rocket_img, window_width - 35, window_height - 105,
    30, 100, 5, pygame.K_UP, pygame.K_DOWN
)

game_status = 'game'
while game_status != 'off':
    window.fill(BG_color)

    player_left.update()
    player_right.update()
    player_left.draw()
    player_right.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_status = 'off'

    clock.tick(60)
    pygame.display.update()  