import pygame
import random
from pygame import mixer 

pygame.init()

score = 0
screen = pygame.display.set_mode((1280, 720))
icon = pygame.image.load('/Users/yuvraaj/Desktop/random ball collector/my_icon.png') 
pygame.display.set_icon(icon)
pygame.display.set_caption("Random Ball game")


running = True

#Epic sounds
mixer.init() 
mixer.music.load("/Users/yuvraaj/Desktop/random ball collector/Background_sound.mp3") 
mixer.music.set_volume(0.9)
def check_collision(ball_group, guy):
    global score 
    collisions = pygame.sprite.spritecollide(guy, ball_group, True)
    for collided_ball in collisions:
        print("Collision detected!")
        # Generate new ball
        x_new = random.randint(0, 1200)
        y_new = random.randint(0, 700)
        new_ball = Ball(x_new, y_new)
        ball_group.add(new_ball)
        score=score+1
        print(score)

class Guy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("guy.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

    def Right(self, pixels):
        self.rect.x += pixels
        if self.rect.x + self.rect.width > 1280:
            self.rect.x = 1280 - self.rect.width

    def Left(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def Forward(self, pixels):
        self.rect.y += pixels
        if self.rect.y + self.rect.height > 720:
            self.rect.y = 720 - self.rect.height

    def Back(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.image.load("/Users/yuvraaj/Desktop/random ball collector/ball.png").convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (50, 50))  # Resize image to 50x50
        self.rect = self.image.get_rect(center=(x, y))

# Create groups for sprites
guy_group = pygame.sprite.Group()
ball_group = pygame.sprite.Group()

# Create instances of guy and initial ball
jack = Guy(640, 360)
guy_group.add(jack)

x_c = random.randint(0, 1200)
y_c = random.randint(0, 700)
nemo = Ball(x_c, y_c) #nemo is the name of the ball cuz its adorable
ball_group.add(nemo)


mixer.music.play() 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

   
    # Draw sprites
    guy_group.draw(screen)
    for ball in ball_group:
        screen.blit(ball.image, ball.rect)

    # Check collisions and spawn new balls
    
    check_collision(ball_group, jack)
    font = pygame.font.Font(None, 30)
    score_text = font.render(f'Score: {score}', True, (0, 0, 255))  
    screen.blit(score_text, (100, 10))


    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        jack.Left(4)
    if keys[pygame.K_RIGHT]:
        jack.Right(4)
    if keys[pygame.K_DOWN]:
        jack.Forward(4)
    if keys[pygame.K_UP]:
        jack.Back(4)

    pygame.display.update()

pygame.quit()