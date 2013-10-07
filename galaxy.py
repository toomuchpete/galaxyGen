import libtcodpy as libtcod
from lib import switch
import architect

LIMIT_FPS = 20
libtcod.sys_set_fps(LIMIT_FPS)

# size of the window
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

# Camera Offsets
camera_x = 0
camera_y = 0

# More globals, because I love them
mouse = libtcod.Mouse()
key = libtcod.Key()

def handle_keys():
    global key, mouse, camera_x, camera_y, entities
 
    if key.vk != libtcod.KEY_NONE:
        move_magnitude = 1
        if key.shift:
            move_magnitude = 11

        # vertical movement
        for case in switch(key.vk):
            if case(libtcod.KEY_UP): pass
            if case(libtcod.KEY_KP8): pass
            if case(libtcod.KEY_HOME): pass
            if case(libtcod.KEY_KP7): pass
            if case(libtcod.KEY_PAGEUP): pass
            if case(libtcod.KEY_KP9):
                camera_y -= move_magnitude
                break
            if case(libtcod.KEY_DOWN): pass
            if case(libtcod.KEY_KP2): pass
            if case(libtcod.KEY_END): pass
            if case(libtcod.KEY_KP1): pass
            if case(libtcod.KEY_PAGEDOWN): pass
            if case(libtcod.KEY_KP3):
                camera_y += move_magnitude
                break

        # horizontal movement
        for case in switch(key.vk):
            if case(libtcod.KEY_LEFT): pass
            if case(libtcod.KEY_KP4): pass
            if case(libtcod.KEY_HOME): pass
            if case(libtcod.KEY_KP7): pass
            if case(libtcod.KEY_END): pass
            if case(libtcod.KEY_KP1):
                camera_x -= move_magnitude
                break
            if case(libtcod.KEY_RIGHT): pass
            if case(libtcod.KEY_KP6): pass
            if case(libtcod.KEY_PAGEUP): pass
            if case(libtcod.KEY_KP9): pass
            if case(libtcod.KEY_PAGEDOWN): pass
            if case(libtcod.KEY_KP3):
                camera_x += move_magnitude
                break

        if key.vk == libtcod.KEY_ESCAPE:
            return True  #exit game
        else:
            key_char = chr(key.c)
            for case in switch(key_char):
                if case('?'):
                    pass

libtcod.console_set_custom_font('data/fonts/lord_dullard_12x12.png', libtcod.FONT_LAYOUT_ASCII_INROW)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'GALAXY', False)
libtcod.console_set_default_background(0, libtcod.Color(204,255,255))

while not libtcod.console_is_window_closed():
    libtcod.console_clear(0)
    # my_color=
    for x in xrange(0, SCREEN_WIDTH):
        for y in xrange(0, SCREEN_HEIGHT):
            probability_num = architect.random2d(camera_x + x, camera_y + y,'star_system_map')
            if probability_num > .998: 
                color_val = int(((probability_num - .998)/.002)*255)
            else:
                color_val = 0
            libtcod.console_set_char_background(0, x, y, libtcod.Color(color_val, color_val, color_val))
    libtcod.console_flush()

    #handle keys and exit game if needed
    libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS|libtcod.EVENT_MOUSE,key,mouse)
    exit = handle_keys()
    if exit:
        break
