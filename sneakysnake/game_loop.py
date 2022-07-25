"""
Snake
Made with PyGame
adapted from https://github.com/rajatdiptabiswas/snake-pygame
"""

import pygame, sys, time, random

# Window size
frame_size_x = 720
frame_size_y = 480


# Checks for errors encountered
check_errors = pygame.init()
#pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')


# Initialise game window
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))


# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(200, 0, 0)
bright_red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 200, 0)
bright_green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


# FPS (frames per second) controller
fps_controller = pygame.time.Clock()

#difficulty
global difficulty 
difficulty = 10


buttons = pygame.sprite.Group()
 
class Button(pygame.sprite.Sprite):
    def __init__(self, position, text, size, font, 
        colors=(white,blue),
        hover_colors=(black,red),
        style=1, borderc=(255,255,255),
        command=lambda: print("No command activated for this button")):
        # the hover_colors attribute needs to be fixed
        super().__init__()
        self.text = text
        self.command = command
        # --- colors ---
        self.colors = colors
        self.original_colors = colors
        self.fg, self.bg = self.colors[0], self.colors[1]
        if hover_colors == (red,green):
            self.hover_colors = (red,green)
        else:
            self.hover_colors = hover_colors
        self.style = style
        self.borderc = borderc # for the style2
        # font
        self.font = pygame.font.SysFont('times new roman', 90)
        self.render()
        self.x, self.y, self.w , self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.position = position
        self.pressed = 1
        buttons.add(self)
 
    def render(self):
        self.text_render = self.font.render(self.text, 1, self.fg)
        self.image = self.text_render
 
    def update(self):
        self.fg, self.bg = self.colors[0], self.colors[1]
        if self.style == 1:
            self.draw_button1()
        elif self.style == 2:
            self.draw_button2()
        self.hover()
        self.click()
 
    def draw_button1(self):
        ''' draws 4 lines around the button and the background '''
        # horizontal up
        pygame.draw.line(game_window, (150, 150, 150), (self.x, self.y), (self.x + self.w , self.y), 5)
        pygame.draw.line(game_window, (150, 150, 150), (self.x, self.y - 2), (self.x, self.y + self.h), 5)
        # horizontal down
        pygame.draw.line(game_window, (50, 50, 50), (self.x, self.y + self.h), (self.x + self.w , self.y + self.h), 5)
        pygame.draw.line(game_window, (50, 50, 50), (self.x + self.w , self.y + self.h), [self.x + self.w , self.y], 5)
        # background of the button
        pygame.draw.rect(game_window, self.bg, (self.x, self.y, self.w , self.h))  
 
    def draw_button2(self):
        ''' a linear border '''
        # horizontal up
        pygame.draw.line(game_window, (150, 150, 150), (self.x, self.y), (self.x + self.w , self.y), 5)
        pygame.draw.line(game_window, (150, 150, 150), (self.x, self.y - 2), (self.x, self.y + self.h), 5)
        # horizontal down
        pygame.draw.line(game_window, (50, 50, 50), (self.x, self.y + self.h), (self.x + self.w , self.y + self.h), 5)
        pygame.draw.line(game_window, (50, 50, 50), (self.x + self.w , self.y + self.h), [self.x + self.w , self.y], 5)
        # background of the button
        pygame.draw.rect(game_window, self.bg, (self.x, self.y, self.w , self.h)) 
 
    def hover(self):
        ''' checks if the mouse is over the button and changes the color if it is true '''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            # you can change the colors when the pointer is on the button if you want
            self.colors = self.hover_colors
            # pygame.mouse.set_cursor(*pygame.cursors.diamond)
        else:
            self.colors = self.original_colors
            
        self.render()
 
    def click(self):
        ''' checks if you click on the button and makes the call to the action just one time'''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 1:
                print("Execunting code for button '" + self.text + "'")
                self.command()
                self.pressed = 0
            if pygame.mouse.get_pressed() == (0,0,0):
                self.pressed = 1


def exit_game():
    pygame.quit()
    sys.exit()

def buttons_def():
    buttons.empty()
    b0 = Button((25,(2*frame_size_y/4)), "Play", 10,"times new roman", (red,black),
        command=game_loop)
    b1 = Button((250,(2*frame_size_y/4)), "Mode", 10,"times new roman", (red,black),
        command=game_modes)
    b2 = Button((535,(2*frame_size_y/4)), "Quit", 10,"times new roman", (red,black),
        command=exit_game)

def buttons_def2():
    buttons.empty()
    b1 = Button(((frame_size_x/3),20), "Easy", 10,"times new roman", (red,black),
        command=easy)
    b2 = Button(((frame_size_x/4),130), "Medium", 10,"times new roman", (red,black),
        command=medium)
    b3 = Button(((frame_size_x/3),240), "Hard", 10,"times new roman", (red,black),
        command=hard)
    b4 = Button(((frame_size_x/4.5),350), "Very Hard", 10,"times new roman", (red,black),
        command=very_hard)




def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def easy():
    global difficulty 
    difficulty = 10
    time.sleep(0.1)
    game_intro()

def medium():
    global difficulty 
    difficulty = 25
    time.sleep(0.1)
    game_intro()

def hard():
    global difficulty 
    difficulty = 40
    time.sleep(0.1)
    game_intro()

def very_hard():
    global difficulty 
    difficulty = 80
    time.sleep(0.1)
    game_intro()

# Intro game_window
def game_intro():
    buttons_def()
    game_window.fill(black)
    largeText = pygame.font.SysFont("times new roman",115)
    TextSurf, TextRect = text_objects("Snake", largeText)
    TextRect.center = ((frame_size_x/2),(frame_size_y/4))
    game_window.blit(TextSurf, TextRect)

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                exit_game()
                
        buttons.update()
        buttons.draw(game_window)
        pygame.display.flip()
        fps_controller.tick(15)
        pygame.display.update()

# Game modes
def game_modes():
    time.sleep(0.1)  
    buttons_def2()
    game_window.fill(black)

    modes = True

    while modes:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        buttons.update()
        buttons.draw(game_window)
        pygame.display.flip()
        fps_controller.tick(15)
        pygame.display.update()

# Game Over
def game_over(score):
    buttons_def()
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface, game_over_rect = text_objects("YOU DIED", my_font)
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/6)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(score, 0, red, 'times', 20)

    game_over = True

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        buttons.update()
        buttons.draw(game_window)
        pygame.display.flip()
        fps_controller.tick(15)
        pygame.display.update()

# Score
def show_score(score, choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x/10, 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)
    # pygame.display.flip()

def game_loop():

    # Difficulty settings
    # Easy      ->  10
    # Medium    ->  25
    # Hard      ->  40
    # Harder    ->  60    

    # Game variables
    snake_pos = [100, 50]
    snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

    food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
    food_spawn = True

    direction = 'RIGHT'
    change_to = direction

    score = 0
    # Main logic
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Whenever a key is pressed down
            elif event.type == pygame.KEYDOWN:
                # W -> Up; S -> Down; A -> Left; D -> Right
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'
                # Esc -> Create event to quit the game
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))


        # Making sure the snake cannot move in the opposite direction instantaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        # Snake body growing mechanism
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        # Spawning food on the game_window
        if not food_spawn:
            food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
        food_spawn = True

        # GFX
        game_window.fill(black)
        for pos in snake_body:
            # Snake body
            # .draw.rect(play_surface, color, xy-coordinate)
            # xy-coordinate -> .Rect(x, y, size_x, size_y)
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        # Snake food
        pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        # Game Over conditions
        # Getting out of bounds
        if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
            game_over(score)
        if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
            game_over(score)
        # Touching the snake body
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over(score)

        show_score(score, 1, white, 'consolas', 20)
        # Refresh game game_window
        pygame.display.update()
        # Refresh rate
        fps_controller.tick(difficulty)

def main():
    pygame.init()
    game_intro()