import game_framework
import stage1_state
import infinity_state
from pico2d import *
from BGM_Object import BGM


name = "MainState"
image = None
stagebutton = False
infinitybutton = False
stagebutton_image = None
infinitybutton_image = None
stagebutton_image2 = None
infinitybutton_image2 = None
bgm = None


def enter():
    global image
    global stagebutton_image
    global infinitybutton_image
    global stagebutton_image2
    global infinitybutton_image2
    global bgm
    stagebutton_image2 = load_image('Resource/stagebutton2.png')
    infinitybutton_image2 = load_image('Resource/infinitybutton2.png')
    stagebutton_image = load_image('Resource/stagebutton.png')
    infinitybutton_image = load_image('Resource/infinitybutton.png')
    image = load_image('Resource/Title.png')
    bgm = BGM(0)


def exit():
    global bgm
    del(bgm)


def update(frame_time): pass


def draw(frame_time):
    clear_canvas()
    image.draw(250,400)
    if stagebutton == True:
        stagebutton_image2.draw(250, 310)
    else:
        stagebutton_image.draw(250, 300)
    if infinitybutton == True:
        infinitybutton_image2.draw(250, 210)
    else:
        infinitybutton_image.draw(250, 200)
    update_canvas()




def handle_events(frame_time):
    global stagebutton
    global infinitybutton
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            stagebutton = False
            infinitybutton = False
            if (event.x > 80 and event.x < 420) and (event.y > 450 and event.y < 530):
                stagebutton = True
            elif (event.x > 80 and event.x < 420) and (event.y > 550 and event.y < 630):
                infinitybutton = True
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if (event.x > 80 and event.x < 420) and (event.y > 450 and event.y < 530):
                game_framework.change_state(stage1_state)
            elif (event.x > 80 and event.x < 420) and (event.y > 550 and event.y < 630):
                game_framework.change_state(infinity_state)
        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()


def pause(): pass


def resume(): pass