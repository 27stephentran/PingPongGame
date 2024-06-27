from pygame import *


win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))

background_color = (230, 255, 255)
display.set_caption("Ping Pong Game")
window.fill(background_color)

paddle_path = "racket.png"
ball_path = "tenis_ball.png"

class GameSprite(sprite.Sprite):
    def __init__(self, image_path, x, y, width, height, speed):
        self.image = transform.scale(image.load(image_path), (width, height))
        self.speed = speed
        self.image_path = image_path
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.width = width
        self.height = height

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def ball_draw(self, angle):
        rotate_image = transform.rotate(self.image, angle)
        window.blit(rotate_image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_s] and self.rect.y < win_height - self.height:
            self.rect.y += self.speed
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
    
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_DOWN] and self.rect.y < win_height - self.height:
            self.rect.y += self.speed
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed




player_1 = Player(paddle_path, 30, 200, 50, 150, 4)
player_2 = Player(paddle_path, win_width - 60, 200, 50, 150, 4)
ball = GameSprite(ball_path, 200, 200, 50, 50, 4)

game_over = False 
FPS = 60
clock = time.Clock()
finish = False

dx = ball.speed
dy = ball.speed
angle = 0

while not game_over:
    for e in event.get():
        if e.type == QUIT:
            game_over = True
    
    if not finish:
        # to make the ball move
        ball.rect.x += dx
        ball.rect.y += dy

        # to make the paddles move
        player_1.update_l()
        player_2.update_r()

        if ball.rect.y < 0 or ball.rect.y > win_height - ball.height:
            dy *= -1 

        if sprite.collide_rect(player_1, ball):
            dx *= -1
        if sprite.collide_rect(player_2, ball):
            dx *= -1
        
        window.fill(background_color)
        player_1.draw()
        player_2.draw()
        ball.ball_draw(angle)
        angle += 10
    
    display.update()
    clock.tick(FPS)
