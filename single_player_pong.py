import pygame

#Choose speed

print("Choose one number from the speed level range:")
print(" - Low level :     1 to 3 ")
print(" - Medium level:   4 to 6")
print(" - Advanced level: 7 to 9")
print(" - Pro level:      >10")
speed = int(input("Select level speed eg 7:")) 

# The ball is moving at constant speed of:
ball_speed_x = 5
ball_speed_y = 5
tick = 50    

# The bar does not move unless moved. Therefore, speed at steady is zero
# If moved it moves at desired speed
bar_speed_x = 0
bar_speed_y = 0
desired_bar_speed_x = 6


# Colours used for this game
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
blue = (0,0,225)
green = (0,255,0)



pygame.init()

# Game display setup
pygame.display.set_caption("Single Player Pong")
screen_x_dimension = 800
screen_y_dimension = 600
screen_size = (screen_x_dimension,screen_y_dimension)
display_screen = pygame.display.set_mode(screen_size)

# Initial position for the "Black bar"
bar_x = 400
bar_y = 580

bar_length = 100
bar_width = 10

# Initial position for the ball
ball_x = 100
ball_y = 100


# Initial score
score = 0

# This function limits the movement of the "Black Bar"
def wall_restriction(display_screen, x,y):
    if x >= screen_x_dimension - bar_length:
        x = screen_x_dimension - bar_length
    if x <= 0:
        x = 0
    pygame.draw.rect(display_screen,black,[x,y,bar_length,bar_width])
    
# Game main control loop
game_over = False
clock = pygame.time.Clock()
while not game_over:
    display_screen.fill(white)
    for each_move in pygame.event.get():
        if each_move.type == pygame.QUIT:
            game_over = True
        elif each_move.type == pygame.KEYDOWN:
            if each_move.key == pygame.K_LEFT:
                bar_speed_x = -desired_bar_speed_x
            elif each_move.key == pygame.K_RIGHT:
                bar_speed_x = desired_bar_speed_x
        elif each_move.type == pygame.KEYUP:
            if each_move.key == pygame.K_LEFT or each_move.key == pygame.K_RIGHT:
                bar_speed_x = 0
            elif each_move.key == pygame.K_UP or each_move == pygame == pygame.K_DOWN:
                bar_speed_y = 0
                
    bar_x += bar_speed_x
    bar_y += bar_speed_y  # This is in case you want the bar to move up and down
    
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    if ball_x < 0:
        ball_speed_x = ball_speed_x * -1
    elif ball_x > screen_x_dimension-15:
        ball_x = screen_x_dimension-15
        ball_speed_x = ball_speed_x * -1
    elif ball_y < 0:
        ball_y = 0
        ball_speed_y = ball_speed_y * -1
    elif ball_x > bar_x and ball_x < bar_x + 100 and ball_y == screen_y_dimension - 20:
        ball_speed_y = ball_speed_y * -1
        score = score + 1
        tick += speed
    elif ball_y > screen_y_dimension:
        ball_speed_y = ball_speed_y * -1
        score = 0
        tick =50
    pygame.draw.circle(display_screen,red,[ball_x,ball_y],10,10)
    
    wall_restriction(display_screen,bar_x,bar_y)
    
    #Summary board: showing score, ball speed and game level
    font= pygame.font.SysFont('Calibri', 15, False, False)
    score_text = font.render("Score = " + str(score), True, blue)
    speed_text = font.render("Speed (pongs/second) =" + str(tick-50), True, red)
    level_text = font.render("Level = " + str(speed), True, black)
    display_screen.blit(score_text ,[30,60])
    display_screen.blit(speed_text,[30,50])
    display_screen.blit(level_text,[30,40])
       
    pygame.display.flip()         
    clock.tick(tick)