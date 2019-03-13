import pygame
user_poem = []
#poem_started = False
poem_draft = True
poem_title = "Untitled"
counter = [1]

pygame.init()
pygame.font.init()
text = pygame.font.SysFont('bookmanoldstyle', 12)

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#Setup screen
pygame.display.set_caption("PoemBuilder")

display_width = 520
display_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
purple = (22, 0, 64)

text_color = white
background_color = purple

screen = pygame.display.set_mode((display_width, display_height))
screen.fill(background_color)


def get_choice(chapter_list, line_counter = counter, poem = user_poem):
    display_intro()
    display_poem()

    instructions = "Line #" + str(sum(line_counter)) + " (type the number of the line you would like to choose)"
    rendered_instructions = text.render(instructions, True, (255, 255, 255))
    screen.blit(rendered_instructions, (5, 415))

    pos_y = 435

    for line in chapter_list:
        choice_string = str(chapter_list.index(line)+1) + ") " + line
        rendered_text = text.render(choice_string, True, (255, 255, 255))
        screen.blit(rendered_text, (5, pos_y))
        pos_y += 17
        pygame.display.update()

    turnover = False
    while not turnover:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                user_choice_key = pygame.key.name(event.key)
                user_choice_int = int(user_choice_key)
                if user_choice_int >= 1 and user_choice_int <= len(chapter_list):
                    user_choice = chapter_list[user_choice_int - 1]
                    poem.append(user_choice)
                    turnover = True

    counter.append(1)
    screen.fill(background_color)

    return user_choice


def display_poem():

    pygame.font.init()
    text = pygame.font.SysFont('bookmanoldstyle', 12)

    pos_y = 80
    #text = pygame.font.SysFont('bookmanoldstyle', 13)

    for line in user_poem:
        rendered_text = text.render(line, True, (255, 255, 255))
        screen.blit(rendered_text, (5, pos_y))
        pos_y += 17
        pygame.display.update()


def display_intro():
    pygame.font.init()
    text_intro = pygame.font.SysFont('rockwell', 13)
    if poem_draft:
        intro = ("Thank you for using the poem builder!")
        rendered_intro = text_intro.render(intro, True, text_color)
        intro_2 = ("This poem will be twelve lines long.")
        rendered_intro_2 = text_intro.render(intro_2, True, text_color)
        screen.blit(rendered_intro, (10, 10))
        screen.blit(rendered_intro_2, (10, 30))
    else:
        intro = ("Here is your final poem:")
        rendered_intro = text_intro.render(intro, True, text_color)
        click = ("Click to create another poem")
        rendered_click = text_intro.render(click, True, text_color)
        screen.blit(rendered_intro, (10, 10))
        screen.blit(rendered_click, (10, 530))
    pygame.display.update()
