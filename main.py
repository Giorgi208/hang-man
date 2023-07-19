from pygame import *
from random import choice
import sys
init()
info = display.Info()
height = info.current_h
width = info.current_w

screen = display.set_mode((width,  height))
display.set_caption("hang-man")

# logo = image.load("images/logo .png")
# display.set_icon(logo)

image_names = []
for i in range(0, 10):
    image_names.append(f"{i}.png")

images = []
for name in image_names:
    img = image.load(f"images/{name}")
    img = transform.scale(img, (300, 300))
    images.append(img)

image_rect = images[0].get_rect(centerx=width/2, centery=height * 3 / 4)

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
initial_length = len(alphabet)
#სიტყვების სია
all_words = ["none", "activate", "settings", "sound", "fish", "random", "click", "logo", "music", "correct", "ironic", "language", "irregardless", "disinterested", "related", "colonel", "worcestershire", "specific", "temperature", "united", "community"]
#სიტყვის შერჩევა შემთხვევითად
current_word = choice(all_words)
#სიტყვის სიგრძე
char_num = len(current_word)
#რამდენი დეფისი დაგც=ვჭირდება ეკრანზე
guess = []

for i in range(char_num):
    guess.append("_")




symbol_font = font.Font(None, width//30)
buttons = []
class Button():
    def __init__(self, a, x, y):
        self.symbol = a
        self.rect = Rect(x, y, width/26, width/26)
        self.rendered_symbol = symbol_font.render(self.symbol, True, (200, 200, 100))
        self.rendered_rect = self.rendered_symbol.get_rect(centerx=self.rect.centerx, centery=self.rect.centery)
    def draw(self):
        draw.rect(screen, (100, 200, 100), self.rect)
        screen.blit(self.rendered_symbol, self.rendered_rect)



i = 0
for symbol in alphabet:
    button = Button(symbol, i, width/26/2)
    i += width/26
    buttons.append(button)


word_font = font.Font(None, 90)
def render_word():
    global word_font, guess
    guess_str = ""
    for item in guess:
        guess_str += item + " "

    rendered = word_font.render(guess_str, True, (0, 0, 0))
    rendered_rect = rendered.get_rect(centerx=width/2, centery=height/3)

    screen.blit(rendered, rendered_rect)

over_font = font.Font(None, 90)
message = "Game Over!"
def game_over(message):
    screen.fill((255, 255, 255))
    render_word()
    rendered_message = over_font.render(message, True, (200, 100, 100))
    rendered_rect = rendered_message.get_rect(centerx=width/2, centery=height/2)
    screen.blit(rendered_message, rendered_rect)
    display.update()
    time.wait(3000)
i = 0

green_rect = Rect(0, int(width/26/2), width, width/26)

run = True
while run:
    current_length = len(alphabet)
    screen.fill((255, 255, 255))
    draw.rect(screen, (100, 200, 100), green_rect)
    render_word()
    for button in buttons:
        button.draw()
    for ev in event.get():
        if ev.type == QUIT:
            run = False
        #თამაშის გათიშვა ESC ღილაკით
        if ev.type == KEYDOWN:
            if ev.key == K_ESCAPE:
                run = False

        if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
            pos = mouse.get_pos()
            for index, button in enumerate(buttons):
                if button.rect.collidepoint(pos):
                    sym = buttons[index].symbol
                    if sym.lower() not in current_word and i < 9:
                        i += 1


                    for ind, character in enumerate(current_word):
                        if character == sym.lower():
                            guess[ind] = sym.lower()

                    buttons.pop(index)
                    alphabet.pop(index)

    screen.blit(images[i], image_rect)


    display.update()

    #თამაშის მოგება
    if "_" not in guess:
        message = "You Win!"
        run = False

    #თამაშის წაგება
    if initial_length - current_length > 9:
        run = False


game_over(message)
quit()
sys.exit()