import game_framework
import main_state
import math
import stage4_state
import stage2_state
from pico2d import *
from Ball_Object import Ball
from Block_Object import Block
from BGM_Object import BGM

name = "Stage3_State"
image = None
text_image = None
circle = None
blueball = None
redball = None
blueball_effect = None
redball_effect = None
pausebutton_image = None
move = False
reverse = True
RedBall = None
BlueBall = None
blocks = None
running = None
pausemenu_image = None
redball_dead = None
blueball_dead = None
count = None
dead_animation_frame = None
blueball_dead_image = None
redball_dead_image = None
bgm = None

def enter():
    global image
    global text_image
    global pausebutton_image
    global circle
    global blueball, blueball_effect, blueball_dead_image
    global redball, redball_effect, redball_dead_image
    global running
    global RedBall, BlueBall, blocks
    global pausemenu_image
    global blueball_dead, redball_dead, dead_animation_frame, count
    global bgm
    pausemenu_image = load_image('Resource/pause_image.png')
    circle = load_image('Resource/circle.png')
    blueball = load_image('Resource/blueball.png')
    redball = load_image('Resource/redball.png')
    blueball_effect = load_image('Resource/blueball_effect.png')
    redball_effect = load_image('Resource/redball_effect.png')
    text_image = load_image('Resource/stage3.png')
    pausebutton_image = load_image('Resource/pausebutton.png')
    image = load_image('Resource/stage_background.png')
    blueball_dead_image = load_image('Resource/blueball_dead_animation.png')
    redball_dead_image = load_image('Resource/redball_dead_animation.png')
    RedBall = Ball(390, 150, 0)
    BlueBall = Ball(110, 150, 180)
    blocks = [Block(90, 1100, 2), Block(240, 1100, 2), Block(400, 1100, 2), Block(240, 1200, 2), Block(360, 1600, 1), Block(100, 1800, 0), Block(400, 2000, 0), Block(130, 2200, 1), Block(130, 2500, 1), Block(400, 2800, 0), Block(400, 3100, 0)]
    running = True
    count = 0
    dead_animation_frame = 0
    redball_dead = False
    blueball_dead = False
    bgm = BGM(3)
    pass


def exit():
    global blocks
    global RedBall, BlueBall
    global bgm
    del(bgm)
    del(RedBall)
    del(BlueBall)
    for block in blocks:
        del(block)
    pass


def update(frame_time):
    global blueball_dead, redball_dead, dead_animation_frame, count, running
    if running == True:
       for block in blocks:
           block.update(frame_time)

       if move == True:
           if reverse == True:
               BlueBall.move(True, frame_time)
               RedBall.move(True, frame_time)
           elif reverse == False:
               BlueBall.move(False, frame_time)
               RedBall.move(False, frame_time)

       BlueBall.update(frame_time)
       RedBall.update(frame_time)

       for block in blocks:
           if block.left < BlueBall.x < block.right and block.bottom < BlueBall.y < block.top:
               running = False
               blueball_dead = True
           elif block.left < RedBall.x < block.right and block.bottom < RedBall.y < block.top:
               running = False
               redball_dead = True

    if blocks[len(blocks) - 1].y < -300:
        game_framework.change_state(stage4_state)

    if running == False:
        count += 1
        if count == 6:
            if blueball_dead == True or redball_dead == True:
                dead_animation_frame += 1
                count = 0
                if dead_animation_frame == 10:
                    enter()
    pass


def draw(frame_time):
    clear_canvas()
    image.draw(250,400)

    for n in range(0 , 10):
        if blueball_dead == False:
            blueball_effect.draw(BlueBall.trace_x[n], BlueBall.trace_y[n])
        if redball_dead == False:
            redball_effect.draw(RedBall.trace_x[n], RedBall.trace_y[n])


    for block in blocks:
        block.Draw()

    text_image.draw(50,780)
    pausebutton_image.draw(470,770)
    circle.draw(250,150)
    if blueball_dead == False:
        blueball.draw(BlueBall.x, BlueBall.y)
    if redball_dead == False:
        redball.draw(RedBall.x, RedBall.y)

    if running == False:
        if blueball_dead == True:
            blueball_dead_image.clip_draw(dead_animation_frame * 106, 0, 106, 106, BlueBall.x, BlueBall.y)
        elif redball_dead == True:
            redball_dead_image.clip_draw(dead_animation_frame * 106, 0, 106, 106, RedBall.x, RedBall.y)
        else:
            pausemenu_image.draw(250, 400)
    update_canvas()
    pass


def handle_events(frame_time):
    events = get_events()
    global running
    global move,reverse
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if 450 < event.x < 490 and 750 < 800 - event.y < 790:
                if running == False:
                    resume()
                else:
                    pause()
            if 180 < event.x < 320 and 375 < 800 - event.y < 425:
                if running == False:
                    game_framework.change_state(main_state)
            if 210 < event.x < 290 and 320 < 800 - event.y < 360:
                if running == False:
                    resume()

        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_BACKSPACE:
                game_framework.change_state(stage2_state)
            elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
                move = True
                reverse = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
                move = True
                reverse = True
            elif event.type == SDL_KEYDOWN and event.key == SDLK_m:
                game_framework.change_state(stage4_state)
            elif event.type == SDL_KEYUP and event.key == SDLK_a:
                if reverse == False:
                    move = False
            elif event.type == SDL_KEYUP and event.key == SDLK_d:
                if reverse == True:
                    move = False

    pass


def pause():
    global running
    running = False
    pass


def resume():
    global running
    running = True
    pass