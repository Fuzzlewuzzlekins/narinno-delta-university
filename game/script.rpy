# The script of the game starts here with character inits.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c_base = Character("base", what_prefix='"', what_suffix='"')

define a = Character("Ash", kind=c_base, who_color="#80ec80")
define b = Character("Blake", kind=c_base, who_color="#f3c37c")
define f = Character("Fyorra", kind=c_base, who_color="#ad94f1")
define ka = Character("Karalún", kind=c_base, who_color="#bfee67")
define ki = Character("Kim", kind=c_base, who_color="#f1afca")
define l = Character("Luziim", kind=c_base, who_color="#f3eb7c")
define nk = Character("Nakoa", kind=c_base, who_color="#f3947c")
define nn = Character("Nanneyo", kind=c_base, who_color="#88c3f3")
define no = Character("Noah", kind=c_base, who_color="#b8aa9f")
define ny = Character("Nyarokhu", kind=c_base, who_color="#9496b1")
define r = Character("Rohal", kind=c_base, who_color="#73d7e9")
define t = Character("Tansei", kind=c_base, who_color="#db89eb")

image ash = Placeholder("boy")
image blake = Placeholder("boy")
image fyorra = Placeholder("girl")
image karalun = Placeholder("girl")
image kim = "sprites/kim_temp.png"
image luziim = Placeholder("girl")
image nakoa = "sprites/nakoa_temp.png"
image nanneyo = Placeholder("girl")
image noah = Placeholder("boy")
image nyarokhu = Placeholder("boy")
image rohal = Placeholder("boy")
image tansei = "sprites/tansei_temp.png"

define e = Character("Emma", kind=c_base)
# TEMPORARY: use Kim for Emma for photo op
# image emma = Placeholder("girl")
image emma = "sprites/kim_temp.png"

# Define transforms and transitions here.

transform leftish_2:
    xalign 0.3 yalign 1.0

transform rightish_2:
    xalign 0.7 yalign 1.0

transform leftish_3:
    xalign 0.15 yalign 1.0

transform rightish_3:
    xalign 0.85 yalign 1.0

transform leftish_4:
    xalign 0.33 yalign 1.0

transform rightish_4:
    xalign 0.67 yalign 1.0

define dissolveinleft = ComposeTransition(dissolve, after=easeinleft)
define dissolveinright = ComposeTransition(dissolve, after=easeinright)
define dissolveinbottom = ComposeTransition(dissolve, after=easeinbottom)

define dissolveoutleft = ComposeTransition(dissolve, before=easeoutleft)
define dissolveoutright = ComposeTransition(dissolve, before=easeoutright)
define dissolveoutbottom = ComposeTransition(dissolve, before=easeoutbottom)

# ???

# define scootinleft = MoveTransition(0.5, enter=scootleft, time_warp=ease)
# define fadeinleft = ComposeTransition(dissolve, after=scootinleft)

# TRYING A NEW THING

transform scootoutleft:
    easeout 0.5 xoffset -50

define scootoutleft2 = MoveTransition(0.5, leave=scootoutleft, old=True)
define fadeoutleft = ComposeTransition(dissolve, scootoutleft2, Pause(0.5))

transform scootinleft:
    xoffset -50
    easein 0.5 xoffset 0

define scootinleft2 = MoveTransition(0.5, enter=scootinleft, old=False)
define fadeinleft = ComposeTransition(dissolve, scootoutleft2, scootinleft2)

transform scootoutright:
    easeout 0.5 xoffset 50

define scootoutright2 = MoveTransition(0.5, leave=scootoutright, old=True)
define fadeoutright = ComposeTransition(dissolve, scootoutright2, Pause(0.5))

transform scootinright:
    xoffset 50
    easein 0.5 xoffset 0

define scootinright2 = MoveTransition(0.5, enter=scootinright, old=False)
define fadeinright = ComposeTransition(dissolve, scootoutright2, scootinright2)

# Old way (transforms instead of transitions)

# transform subtleinleft:
#     alpha 0.0 xoffset -50
#     parallel:
#         easein 0.5 xoffset 0
#     parallel:
#         linear 0.5 alpha 1.0

transform subtleoutleft:
    alpha 1.0 xoffset 0
    parallel:
        easeout 0.5 xoffset -50
    parallel:
        linear 0.5 alpha 0.0

transform subtleinright:
    alpha 0.0 xoffset 50
    parallel:
        easein 0.5 xoffset 0
    parallel:
        linear 0.5 alpha 1.0

transform subtleoutright:
    alpha 1.0 xoffset 0
    parallel:
        easeout 0.5 xoffset 50
    parallel:
        linear 0.5 alpha 0.0

# What if I did ATL transitions?

# transform subtleinleft(duration=0.5, new_widget=None, old_widget=None):
#     delay duration
#     xoffset -50
#     parallel:
#         old_widget
#         alpha 1.0
#         events False
#         parallel:
#             easein 0.5 xoffset 0
#         parallel:
#             linear 0.5 alpha 0.0
#     parallel:
#         new_widget
#         alpha 0.0
#         events True
#         parallel:
#             easein 0.5 xoffset 0
#         parallel:
#             linear 0.5 alpha 1.0

transform newscootinleft(duration=0.5, new_widget=None, old_widget=None):
    delay duration
    old_widget
    xoffset -50
    easeout (duration/2) xoffset -25
    new_widget
    easein (duration/2) xoffset 0

define newfadeinleft = ComposeTransition(dissolve, before=newscootinleft, after=newscootinleft)

# The game starts here.

label start:

    # All actual scripts of the game will be handled in separate files, 
    # one per act/chapter(?). Start by jumping to act_1.

    jump act_1
    # jump test_scene
    # jump testytest
