from youpy.code.english.everything import *

def when_program_start():
    go_to(point=Stage.center)
    while True:
        glide(5, to=Stage.pick_random_position())

def when_sprite_clicked():
    console.print("blue ball clicked")

### Should raise an exception
# def when_stage_clicked():
#     pass
