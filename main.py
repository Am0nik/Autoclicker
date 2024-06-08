from pygame import *
import keyboard
import mouse
from time import sleep
import win2

font.init()
win = display.set_mode((500, 700))
display.set_caption('Autoclicker')

icon = image.load('img/icon.png') 
display.set_icon(icon)



bg = (245, 245, 220)
butt = (0, 51, 102)
c_t = (255, 255, 255)

def working():
    global work
    work = not work

work = False
keyboard.add_hotkey('q', working)

button_width = 100
button_height = 30
button_x = 200
button_y = 600
button_x2 = 205
button_y2 = 300
button_rect = Rect(button_x, button_y, button_width, button_height)
ok_rect = Rect(button_x2, button_y2, button_width, button_height)
font_m = font.SysFont('Arial', 30)
text_surface = font_m.render('exit', True, c_t)
text_rect = text_surface.get_rect(center=button_rect.center)
text_surface2 = font_m.render('OK', True, c_t)
text_ok = text_surface2.get_rect(center=ok_rect.center)
text_s = font_m.render('s', True, (0, 0, 0))

input_active = False
input_text = ""




clock = time.Clock()
FPS = 60
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == MOUSEBUTTONDOWN:
            if button_rect.collidepoint(e.pos):
                run = False
            mouse_x, mouse_y = e.pos
            if 155 <= mouse_x <= 155 + 200 and 200 <= mouse_y <= 200 + 50:
                input_active = True
            else:
                input_active = False
            if ok_rect.collidepoint(e.pos):
                display.iconify()

        elif e.type == KEYDOWN:
            if input_active:
                if e.key == K_RETURN:
                    try:
                        input_value = float(input_text) 
                    except:
                        win2.box()
                elif e.key == K_BACKSPACE:
                    input_text = input_text[:-1]  
                else:
                    input_text += e.unicode  

    win.fill(bg)
    draw.rect(win, butt, button_rect)
    draw.rect(win, (100,100,100), ok_rect)
    win.blit(text_surface, text_rect)
    win.blit(text_surface2, text_ok)
    win.blit(text_s, (360, 205))
    draw.rect(win, (0, 0, 0), (155, 200, 200, 50), 3)
    text_i = font_m.render(input_text, True, (20, 20, 20))
    win.blit(text_i, (160, 200))
    
    text_ii = font_m.render('q - start', True, (100, 100, 120))
    win.blit(text_ii, (210, 250))
    

    if work:
        mouse.click(button='left')
        sleep(float(input_text))
        
    display.update()
    clock.tick(FPS)
