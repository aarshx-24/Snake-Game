import pygame
import time
import random

pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Aarsh')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 25

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("Timenewroman", 35)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        # This was the missing piece
        x1 += x1_change
        y1 += y1_change
        
        dis.fill(blue)
        pygame.draw.rect(dis, black, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()


# from tkinter import *
# root = Tk()
# root.geometry("500x500")
# root.title("TIC TAC TOE")

# #Game Name: TIC TACT TOE

# frame1 = Frame(root)
# frame1.pack()
# titlelabel1 = Label(frame1, text="Tic Tac Toe", font=("Comic sans ms", 30), bg="red")
# titlelabel1.pack()

# #GAME BOARD

# turn ="x"

# def play(event):
#     global turn
#     button = event.widget

#     if turn== "x":
#         button["text"] = "X"
#         turn = "o"
#     else:
#         button["text"] ="O"
#         turn = "x"
# frame2 = Frame(root)
# frame2.pack()

# #First Row

# button = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg ="yellow", relief=RAISED, borderwidth=5)
# button.grid(row = 0, column=0)
# button.bind("<Button-1>", play)

# button = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg ="yellow", relief=RAISED, borderwidth=5)
# button.grid(row = 0, column=1)
# button.bind("<Button-1>", play)

# button = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg ="yellow", relief=RAISED, borderwidth=5)
# button.grid(row = 0, column=2)
# button.bind("<Button-1>", play)

# #Second Row

# button = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg ="yellow", relief=RAISED, borderwidth=5)
# button.grid(row = 1, column=0)
# button.bind("<Button-1>", play)

# button = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg ="yellow", relief=RAISED, borderwidth=5)
# button.grid(row = 1, column=1)
# button.bind("<Button-1>", play)

# button = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg ="yellow", relief=RAISED, borderwidth=5)
# button.grid(row = 1, column=2)
# button.bind("<Button-1>", play)

# #Third Row


# button = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg ="yellow", relief=RAISED, borderwidth=5)
# button.grid(row = 3, column=0)
# button.bind("<Button-1>", play)

# button = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg ="yellow", relief=RAISED, borderwidth=5)
# button.grid(row = 3, column=1)
# button.bind("<Button-1>", play)

# button = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg ="yellow", relief=RAISED, borderwidth=5)
# button.grid(row = 3, column=2)
# button.bind("<Button-1>", play)

# root.mainloop()


# import random

# options = ["rock", "paper", "scissors"]

# while True:
#     user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()

#     if user_choice == "quit":
#         print("Thanks for playing!")
#         break

#     if user_choice not in options:
#         print("Invalid choice, try again!")
#         continue

#     computer_choice = random.choice(options)
#     print(f"Computer chose: {computer_choice}")

#     if user_choice == computer_choice:
#         print("It's a tie!")
#     elif:
        
#        (user_choice == "rock" and computer_choice == "scissors") or
#        (user_choice == "paper" and computer_choice == "rock") or
#        (user_choice == "scissors" and computer_choice == "paper")
    
#         print("You win!")
#     else:
#         print("You lose!")
        
#     print()
