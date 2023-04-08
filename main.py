import pygame
from pygame.locals import QUIT, KEYDOWN, K_e, K_f, K_m, FULLSCREEN, SCALED, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_1, K_2, K_a, K_s, K_d, K_w
from time import time
from random import randint
pygame.init()
def move_x(*objects: pygame.Rect, plus_x: int):
    for object in objects:
        object.x += plus_x
pygame.display.set_caption("Factory")
screen = pygame.display.set_mode((1050, 750))
font = pygame.font.SysFont("arial", 36, True)
big_font = pygame.font.SysFont("arial", 192, True)
clock = pygame.time.Clock()
stage = 0
stage_2_enemies = 86
update = 43 + time()
stage_3_rect = None
stage_3_target = None
stage_3_plus = [75, 75]
target_3_plus = [0, 0]
work_comp = False
worked_comp = True
stage_4_attack = {}
break_mage = 15
fullscreen = False
rotation = 0
lives = 10
boss_lives = 20
boss_defense = 2
walls = []
enemies = []
enemies_go = {}
enemy_speed = 1
mage_speed = 1
player = None
in_hand = None
in_hand_shape = None
backs = []
back_x = []
for number in range(1, 6):
    backs.append(pygame.transform.scale(pygame.image.load("images/back" + str(number) + ".png"), (750, 750)))
    back_x.append(pygame.Rect(750 * (len(backs) - 1), 0, 750, 750))
for number in range(1, 4):
    backs.append(pygame.transform.scale(pygame.image.load("images/back" + str(number) + ".png"), (750, 750)))
    back_x.append(pygame.Rect(750 * (len(backs) - 1), 0, 750, 750))
shapes = {'wall': pygame.transform.scale(pygame.image.load("images/wall.png"), (75, 75)),
          'heart': pygame.transform.scale(pygame.image.load("images/heart.png"), (45, 45)),
          '1/2heart': pygame.transform.scale(pygame.image.load("images/0.5heart.png"), (22.5, 45)),
          'player': pygame.transform.scale(pygame.image.load("images/Cale.png"), (75, 75)),
          'mage': pygame.transform.scale(pygame.image.load("images/mage.png"), (75, 75)),
          'enemy': pygame.transform.scale(pygame.image.load("images/enemy.png"), (75, 75)),
          'ballista': pygame.transform.scale(pygame.image.load("images/ballista.png"), (130, 100)),
          'knife': pygame.transform.scale(pygame.image.load("images/knife.png"), (30, 15)),
          'gun': pygame.transform.scale(pygame.image.load("images/gun.png"), (30, 10)),
          'comp': pygame.transform.scale(pygame.image.load("images/computer.png"), (75, 75)),
          'aim': pygame.transform.scale(pygame.image.load("images/aim.png"), (37.5, 37.5)),
          'project2803': pygame.transform.scale(pygame.image.load("images/project2803.png"), (300, 300)),
          'settings': pygame.transform.scale(pygame.image.load("images/settings.png"), (50, 50))}
level = ['wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
         'w     w  ew          ewe          we         w   w            w',
         'w wwwww wwwww       wwwww       wwwww        w   w            w',
         'w w           wwwww       wwwww       wwwww  www www wwwwwwwwww',
         'w   www wwwww      ewwwww      ewwwww            w            w',
         'w   w         wwwww      ewwwww      ewwwww      w   wwwwwwwwww',
         'w   w wwwww         wwwww       wwwww       wwww w            w',
         'ww ww w   wwww wwwww      wwwww       wwwww      w   wwwwwwwwww',
         'wp w    w    w  ewe         w          ewe       w            w',
         'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
         '                                                 w            w',
         '                                                 w            w',
         '                                                 w            w',
         '                                                 w            w',
         '                                                 w            w',
         '                                                 w            w',
         '                                                 w            w',
         '                                                 w            w',
         '                                                 w            w',
         '                                                 w            w',
         '                                                 w    wwwwwwwwwwwwwwwwwwwww',
         '                                                 w    w    w              w',
         '                                                 w    w ww    wwwwwwwwwww w',
         '                                                 w    w  wwwwww    w      w',
         '                                                 w    ww      w    w wwwwww',
         '                                                 w    wwwwwww w    w     ww',
         '                                                 w    w       w    wwwww  w',
         '                                                 w    w wwwwwwwwwww    ww w',
         '                                                 w                   w    w',
         '                                                 wwwwwwwwwwwwwwwwwwwwwwwwww',
         '                                                 w            w',
         '                                                 w            w',
         '                                                 wwwwwwwwwwwwww',
         '                                                 w            w',
         '                                                 w            w',
         '                                                 w            w',
         '                                                 w            w',
         '                                                 w            w',
         '                                                 wwwwwwwwwwwwww']
pre_level = ['wwwwwwwwwwwwww',
             'w            w',
             'w    wwwwww  w',
             'w    w    w  w',
             'w    w    w  w',
             'w    w    w  w',
             'w    w    w  w',
             'wwwwwwwwwwwwww',
             'w            w',
             'wwwwwwwwwwwwww']
y = 0
for line in level:
    x = 0
    for el in list(line):
        if el == 'w':
            walls.append(pygame.Rect(x, y, 75, 75))
        elif el == 'e':
            enemies.append(pygame.Rect(x, y, 75, 75))
        elif el == 'p':
            player = pygame.Rect(x, y, 75, 75)
        x += 75
    y += 75
pre_walls = []
y = 0
for line in pre_level:
    x = 0
    for el in list(line):
        if el == 'w':
            pre_walls.append(pygame.Rect(x, y, 75, 75))
        x += 75
    y += 75
ballista = pygame.Rect(3815, 125, 117, 90)
pygame.mixer.Sound("sounds/prehistory.mp3").play()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_e:
                exit()
            elif event.key == K_m:
                pygame.mixer.music.set_volume(0.0 if pygame.mixer.music.get_volume() > 0 else 0.15)
            elif event.key == K_f and not fullscreen:
                screen = pygame.display.set_mode((1050, 750), FULLSCREEN | SCALED)
                fullscreen = True
            elif event.key == K_f:
                screen = pygame.display.set_mode((1050, 750))
                fullscreen = False
            elif event.key == K_1:
                in_hand = shapes['knife'] if rotation else pygame.transform.flip(shapes['knife'], True, False)
                in_hand_shape = 'k'
            elif event.key == K_2:
                in_hand = shapes['gun'] if rotation else pygame.transform.flip(shapes['gun'], True, False)
                in_hand_shape = 'g'
            elif stage not in [0, 'lose', 'win']:
                if event.key == K_SPACE:
                    if stage == 1 and in_hand_shape is not None:
                        if in_hand_shape == 'k':
                            attack = pygame.Rect(player.x if rotation else -150, player.y, 150, 75)
                        else:
                            attack = pygame.Rect(player.x + 150 if rotation else -150, player.y, 150, 75)
                        for enemy in enemies:
                            if attack.colliderect(enemy):
                                del enemies[enemies.index(enemy)]
                                enemy_speed -= 0.03
                                enemies_go.clear()
                                pygame.mixer.Sound("sounds/target.mp3").play()
                                if len(enemies) in [0, 1]:
                                    del walls[93]
                                    enemies.clear()
                                    enemy_speed = 1
                                    pygame.mixer.Sound("sounds/block1.mp3").play()
                    elif stage == 2:
                        for enemy in enemies:
                            if ballista.y + 25 == enemy.y:
                                del enemies[enemies.index(enemy)]
                                stage_2_enemies -= 1
                                pygame.mixer.Sound("sounds/target.mp3").play()
                                if stage_2_enemies == 0:
                                    enemies.clear()
                                    walls[115].y, walls[116].y, ballista.y, player.y = 675, 675, 580, 600
                                enemy_speed -= 0.009
                                break
                    elif stage == 3 and stage_3_rect.colliderect(stage_3_target):
                        target_3_plus = [37.5 * randint(1, 8), 37.5 * randint(1, 8)]
                        worked_comp = True
                        boss_lives -= 1
                        pygame.mixer.Sound("sounds/target.mp3").play()
                        if boss_lives == 0:
                            pygame.mixer.Sound("sounds/after-project.mp3").play()
                    elif stage == 4 and boss_defense <= 0 and player.x == 75 and player.y == 600:
                        boss_lives -= 1
                        pygame.mixer.Sound("sounds/target.mp3").play()
                        if boss_lives <= 0:
                            stage = 'win'
                            pygame.mixer.Sound("sounds/lose.mp3").play()
                elif event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT] and (stage != 2 or stage_2_enemies > 0):
                    start = pygame.Rect(player.x, player.y, 75, 75)
                    player.x += 75 if event.key == K_RIGHT and stage != 2 else -75 if event.key == K_LEFT else 0
                    player.y += 75 if event.key == K_DOWN else -75 if event.key == K_UP and stage != 2 else 0
                    for wall in walls:
                        if player.colliderect(wall) and stage != 2:
                            player = start
                            pygame.mixer.Sound("sounds/collision.mp3").play()
                    if not rotation and event.key == K_RIGHT or rotation and event.key == K_LEFT:
                        shapes['player'] = pygame.transform.flip(shapes['player'], True, False)
                        rotation = not rotation
                        if in_hand is not None:
                            in_hand = pygame.transform.flip(in_hand, True, False)
                    if player.x == 75 and player.y == 150 and back_x[0].x == -3675 and stage == 1:
                        stage = 2
                    elif stage == 2:
                        player = start
                        if event.key == K_LEFT and player != start:
                            stage = 1
                        elif event.key == K_UP and walls[115].y > 225:
                            walls[115].y, walls[116].y, ballista.y, player.y = walls[115].y - 150, walls[116].y - 150, ballista.y - 150, player.y - 150
                        elif event.key == K_DOWN and walls[115].y < 675:
                            walls[115].y, walls[116].y, ballista.y, player.y = walls[115].y + 150, walls[116].y + 150, ballista.y + 150, player.y + 150
                    if player.x >= 925 and back_x[0].x == -2700:
                        move_x(player, ballista, *walls, *back_x, *enemies, plus_x=-975)
                    elif player.x <= 0 and back_x[0].x == -3675:
                        move_x(player, ballista, *walls, *back_x, *enemies, plus_x=975)
                    elif player.x >= 1000:
                        move_x(player, ballista, *walls, *back_x, *enemies, plus_x=-300)
                    elif player.x <= 0:
                        move_x(player, ballista, *walls, *back_x, *enemies, plus_x=300)
                elif event.key in [K_a, K_s, K_d, K_w] and stage == 3 and (player.x == walls[356].x - 150 and player.y == walls[356].y and work_comp or player.x == walls[422].x + 150 and player.y == walls[422].y and not work_comp):
                    start = pygame.Rect(stage_3_rect.x, stage_3_rect.y, 75, 75)
                    stage_3_rect.x += 37.5 if event.key == K_d else -37.5 if event.key == K_a else 0
                    stage_3_rect.y += 37.5 if event.key == K_s else -37.5 if event.key == K_w else 0
                    if stage_3_rect.x in range(walls[356].x + 75, walls[356].x + 413) and stage_3_rect.y in range(walls[356].y + 75, walls[356].y + 413):
                        stage_3_plus = [stage_3_rect.x - walls[356].x, stage_3_rect.y - walls[356].y]
    for num in range(len(backs)):
        screen.blit(backs[num], (back_x[num].x, 0))
    for wall in walls:
        screen.blit(shapes['wall'], wall)
    for enemy in enemies:
        screen.blit(shapes['enemy'], enemy)
    screen.blit(shapes['player'], player)
    screen.blit(shapes['ballista'], ballista)
    live_x = 10
    if lives > 0:
        for _ in range(lives // 2):
            screen.blit(shapes['heart'], (live_x, 10))
            live_x += 55
        if lives % 2 == 1:
            screen.blit(shapes['1/2heart'], (live_x, 10))
    elif lives == 0:
        stage = 'lose'
        lives = -1
        pygame.mixer.Sound("sounds/lose.mp3").play()
    if stage == 0:
        for num in range(len(backs)):
            screen.blit(backs[num], (back_x[num].x, 0))
        screen.blit(shapes['mage'], (225, 450, 75, 75))
        screen.blit(shapes['project2803'], (450, 225, 300, 300))
        for pre_wall in pre_walls:
            screen.blit(shapes['wall'], pre_wall)
        if time() > update:
            stage = 1
            pygame.mixer.Sound("sounds/block2.mp3").play()
            pygame.mixer.music.load("sounds/background.mp3")
            pygame.mixer.music.set_volume(0.15)
            pygame.mixer.music.play(-1)
    elif stage == 1:
        if in_hand is not None:
            if rotation:
                screen.blit(in_hand, (player.x + 60, player.y + 37, 20, 10))
            else:
                screen.blit(in_hand, (player.x - 20, player.y + 37, 20, 10))
        left_rect = pygame.Rect(player.x - 375, player.y, 450, 75)
        right_rect = pygame.Rect(player.x, player.y, 450, 75)
        up_rect = pygame.Rect(player.x, player.y - 450, 75, 450)
        down_rect = pygame.Rect(player.x, player.y + 75, 75, 450)
        for enemy in enemies:
            if enemy.colliderect(player):
                del enemies[enemies.index(enemy)]
                lives -= 1
                enemies_go.clear()
                pygame.mixer.Sound("sounds/fail.mp3").play()
            elif enemy.colliderect(left_rect):
                enemies_go[enemies.index(enemy)] = {'x': 75, 'y': 0}
            elif enemy.colliderect(right_rect):
                enemies_go[enemies.index(enemy)] = {'x': -75, 'y': 0}
            elif enemy.colliderect(down_rect):
                enemies_go[enemies.index(enemy)] = {'x': 0, 'y': -75}
            elif enemy.colliderect(up_rect):
                enemies_go[enemies.index(enemy)] = {'x': 0, 'y': 75}
        del_list = []
        if time() > update:
            for enemy in enemies_go:
                next_step = pygame.Rect(enemies[enemy].x + enemies_go[enemy]['x'], enemies[enemy].y + enemies_go[enemy]['y'], 75, 75)
                for wall in walls:
                    if next_step.colliderect(wall) or enemies[enemy].collidelist([left_rect, right_rect, down_rect, up_rect]) == -1:
                        del_list.append(enemy)
                        next_step = enemies[enemy]
                        break
                enemies[enemy] = next_step
        if len(enemies) != 0 and time() > update:
            update = time() + enemy_speed
        for delete in del_list:
            del enemies_go[delete]
    elif stage == 2:
        enemy_text = font.render("Ворогів: " + str(stage_2_enemies), 1, (45, 3, 32))
        screen.blit(enemy_text, (475, 5, 75, 75))
        if time() > update and stage_2_enemies > 0:
            for enemy in enemies:
                enemy.x -= 75
                if enemy.x <= 150:
                    del enemies[enemies.index(enemy)]
                    pygame.mixer.Sound("sounds/fail.mp3").play()
                    lives -= 1
            enemies.append(pygame.Rect(900, 150 * randint(1, 4), 75, 75))
            update = time() + enemy_speed
        elif stage_2_enemies <= 0 and walls[116].y == 675:
            for wall in walls:
                wall.y -= 30
            for wall in walls[115:117]:
                wall.y = player.y + player.height
            if walls[0].y == -1500:
                stage = 3
                pygame.mixer.Sound("sounds/block0.mp3").play()
                target_3_plus = [37.5 * randint(1, 8), 37.5 * randint(1, 8)]
    elif stage == 3:
        screen.blit(pygame.transform.flip(shapes['comp'], True, False), (walls[356].x - 75, walls[356].y, 75, 75))
        screen.blit(shapes['comp'], (walls[422].x + 75, walls[422].y, 75, 75))
        if boss_lives > 0:
            screen.blit(shapes['project2803'], (walls[356].x + 75, walls[356].y + 75, 75, 75))
            stage_3_rect = pygame.Rect(walls[356].x + stage_3_plus[0], walls[356].y + stage_3_plus[1], 37.5, 37.5)
            stage_3_target = pygame.Rect(walls[356].x + target_3_plus[0] + 37.5, walls[356].y + target_3_plus[1] + 37.5, 37.5, 37.5)
            pygame.draw.rect(screen, (255, 0, 0), stage_3_target)
            pygame.draw.rect(screen, (255, 0, 0), (walls[356].x + 37.5, walls[356].y - 37.5, boss_lives * 375 / 20, 15))
            pygame.draw.rect(screen, (0, 0, 0), (walls[356].x + 37.5, walls[356].y - 37.5, 375, 15), 2)
            if time() > update:
                update = 25 + time()
                work_comp = not work_comp
                if not worked_comp:
                    lives -= 1
                    boss_lives += 1
                boss_lives += 1
                boss_lives = 20 if boss_lives > 20 else boss_lives
                worked_comp = False
            if player.x == walls[356].x - 150 and player.y == walls[356].y and work_comp or player.x == walls[422].x + 150 and player.y == walls[422].y and not work_comp:
                screen.blit(shapes['aim'], stage_3_rect)
        else:
            if player.x + 65 == ballista.x:
                for wall in walls:
                    wall.y -= 45
                for wall in walls[115:117]:
                    wall.y = player.y + player.height
                if walls[0].y == -2175:
                    stage = 4
                    boss_lives = 250
                    break_mage = time() + randint(20, 30)
                    update = time() + 10
                    pygame.mixer.Sound("sounds/mage-say.mp3").play()
    elif stage == 4:
        screen.blit(shapes['mage'], (487.5, 150 if boss_defense > 0 else 600))
        pygame.draw.rect(screen, (255, 0, 0), (225, 90, boss_lives * 2.4, 15))
        pygame.draw.rect(screen, (128, 128, 128), (450, 120, boss_defense * 75, 15))
        pygame.draw.rect(screen, (0, 0, 0), (225, 90, 600, 15), 2)
        pygame.draw.rect(screen, (0, 0, 0), (450, 120, 150, 15), 2)
        if time() > update:
            pygame.mixer.Sound("sounds/laser.mp3").play()
            stage_4_attack[time() + 1 * mage_speed] = pygame.Rect(randint(1, 9) * 75, 300, 75, 375)
            stage_4_attack[time() + 1.5 * mage_speed] = pygame.Rect(randint(1, 9) * 75, 300, 75, 375)
            stage_4_attack[time() + 2 * mage_speed] = pygame.Rect(randint(1, 9) * 75, 300, 75, 375)
            stage_4_attack[time() + 2.5 * mage_speed] = pygame.Rect(randint(1, 9) * 75, 300, 75, 375)
            update = time() + 2
            if boss_defense == 0:
                boss_defense = 2
        if time() > break_mage:
            boss_defense -= 1
            break_mage = time() + randint(10, 20) if boss_defense != 0 else time() + 25
            if boss_defense == 0:
                update = time() + 10
                stage_4_attack.clear()
                pygame.mixer.Sound("sounds/mage-power-down.mp3").play()
        del_list = []
        for attack in stage_4_attack:
            pygame.draw.rect(screen, (255, 255, 51), stage_4_attack[attack])
            if time() > attack:
                del_list.append(attack)
                mage_speed -= 0.002
                if player.colliderect(stage_4_attack[attack]):
                    lives -= 1
                    pygame.mixer.Sound("sounds/fail.mp3").play()
        for delete in del_list:
            del stage_4_attack[delete]
    elif stage == 'win':
        for num in range(len(backs)):
            screen.blit(backs[num], (back_x[num].x, 0))
        screen.blit(shapes['player'], (225, 450, 75, 75))
        screen.blit(pygame.transform.scale(shapes['project2803'], (150, 150)), (450, 375, 150, 150))
        screen.blit(shapes['mage'], (675, 450, 75, 75))
        for pre_wall in pre_walls:
            screen.blit(shapes['wall'], pre_wall)
        text1 = big_font.render("You", 1, (132, 226, 150))
        text2 = big_font.render("Win", 1, (132, 226, 150))
        screen.blit(text1, text1.get_rect(center=(525, 150)))
        screen.blit(text2, text2.get_rect(center=(525, 600)))
    elif stage == 'lose':
        for num in range(len(backs)):
            screen.blit(backs[num], (back_x[num].x, 0))
        screen.blit(shapes['mage'], (225, 450, 75, 75))
        screen.blit(pygame.transform.scale(shapes['project2803'], (150, 150)), (450, 375, 150, 150))
        screen.blit(shapes['player'], (675, 450, 75, 75))
        for pre_wall in pre_walls:
            screen.blit(shapes['wall'], pre_wall)
        text1 = big_font.render("You", 1, (132, 226, 150))
        text2 = big_font.render("Lose", 1, (132, 226, 150))
        screen.blit(text1, text1.get_rect(center=(525, 150)))
        screen.blit(text2, text2.get_rect(center=(525, 600)))
    pygame.display.update()
    clock.tick(10)
