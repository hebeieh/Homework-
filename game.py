import pygame
import random

pygame.init()

weight = 800
height = 600
window = pygame.display.set_mode((weight, height))
pygame.display.set_caption("Избегай падающие объекты")

size = 50
position_x = weight // 2 - size // 2
position_y = height - size - 20
speed = 8

fall_objects = []
size_obj = 30
speed_obj = 5
freq = 20

score = 0
font = pygame.font.Font(None, 36)

clocks = pygame.time.Clock()
active = True
finish = False

while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and finish:
                finish = False
                score = 0
                fall_objects = []
                speed_obj = 5
                position_x = weight // 2 - size // 2

    if not finish:
        press = pygame.key.get_pressed()
        if press[pygame.K_LEFT] and position_x > 0:
            position_x -= speed
        if press[pygame.K_RIGHT] and position_x < weight - size:
            position_x += speed
        if press[pygame.K_UP] and position_y > 0:
            position_y -= speed
        if press[pygame.K_DOWN] and position_y < height - size:
            position_y += speed

        if random.randint(1, freq) == 1:
            obj_x = random.randint(0, weight - size_obj)
            obj_y = - size_obj
            obj_color = random.choice([(186, 85, 211),
                                       (219, 112, 147),
                                       (65, 105, 225),
                                       (175, 238, 238),
                                       (221, 160, 221),
                                       (255, 182, 193)]) 
            fall_objects.append([obj_x, obj_y, obj_color])

        for obj in fall_objects[:]: 
            obj[1] += speed_obj

            if (position_x < obj[0] + size_obj and
                position_x + size > obj[0] and
                position_y < obj[1] + size_obj and
                position_y + size > obj[1]):
                finish = True
            if obj[1] > height:
                fall_objects.remove(obj)
                score += 1

    window.fill((255, 239, 213))

    pygame.draw.rect(window, (152, 251, 152), (position_x, position_y, size, size))

    for obj in fall_objects:
        pygame.draw.rect(window, obj[2], (obj[0], obj[1], size_obj, size_obj))
    
    score_text = font.render(f"Счет: {score}", True, (0, 0, 0))
    window.blit(score_text, (10, 10))
    
    if finish:
        finish_text = font.render("Игра окончена! Нажми R для начала новой игры", True, (0, 0, 0))
        window.blit(finish_text, (weight // 2 - 260, height // 2))
    
    pygame.display.flip()
    clocks.tick(60)

pygame.quit()
