﻿# The script of the game starts here with character inits.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c_base = Character("base", what_prefix='“', what_suffix='”')

define a = Character("Ash", kind=c_base, who_color="#80ec80", image="ash")
define b = Character("Blake", kind=c_base, who_color="#f3c37c", image="blake")
define f = Character("Fyorra", kind=c_base, who_color="#ad94f1", image="fyorra")
define ka = Character("Karalún", kind=c_base, who_color="#bfee67", image="kara")
define ki = Character("Kim", kind=c_base, who_color="#f1afca", image="kim")
define l = Character("Luziim", kind=c_base, who_color="#f3eb7c", image="luziim")
define nk = Character("Nakoa", kind=c_base, who_color="#f3947c", image="nakoa")
define nn = Character("Nanneyo", kind=c_base, who_color="#88c3f3", image="nan")
define no = Character("Noah", kind=c_base, who_color="#b8aa9f", image="noah")
define ny = Character("Nyarokhu", kind=c_base, who_color="#9496b1", image="nyarokhu")
define r = Character("Rohal", kind=c_base, who_color="#73d7e9", image="rohal")
define t = Character("Tansei", kind=c_base, who_color="#db89eb", image="tansei")

define a_nvl = Character("Ash", kind=nvl, who_color="#80ec80")
define b_nvl = Character("Blake", kind=nvl, who_color="#f3c37c")
define f_nvl = Character("Fyorra", kind=nvl, who_color="#ad94f1")
define ka_nvl = Character("Karalún", kind=nvl, who_color="#bfee67")
define ki_nvl = Character("Kim", kind=nvl, who_color="#f1afca")
define l_nvl = Character("Luziim", kind=nvl, who_color="#f3eb7c")
define nk_nvl = Character("Nakoa", kind=nvl, who_color="#f3947c")
define nn_nvl = Character("Nanneyo", kind=nvl, who_color="#88c3f3")
define no_nvl = Character("Noah", kind=nvl, who_color="#b8aa9f")
define ny_nvl = Character("Nyarokhu", kind=nvl, who_color="#9496b1")
define r_nvl = Character("Rohal", kind=nvl, who_color="#73d7e9")
define t_nvl = Character("Tansei", kind=nvl, who_color="#db89eb")

image ash = "sprites/ash_temp.png"
image blake = Placeholder("boy")
image fyorra = "sprites/fyorra_temp.png"
image karalun = Placeholder("girl")
image kim = "sprites/kim_temp.png"
image luziim = Placeholder("girl")
image nakoa = "sprites/nakoa_temp.png"
image nanneyo = Placeholder("girl")
image noah = Placeholder("boy")
image nyarokhu = Placeholder("boy")
image rohal = "sprites/rohal_temp.png"
image tansei = "sprites/tansei_temp.png"

# Karalún sprites: main
image kara neutral = "sprites/kara_neutral.png"
image kara neutral talk = "sprites/kara_neutral_talk.png"
image kara worried = "sprites/kara_worried.png"
image kara worried talk = "sprites/kara_worried_talk.png"
image kara happy = "sprites/kara_happy.png"
image kara grin = "sprites/kara_grin.png"
# Karalún sprites: profile
image kara pensive = "sprites/kara_pensive.png"
image kara pensive talk = "sprites/kara_pensive_talk.png"
image kara grumpy = "sprites/kara_grumpy.png"
image kara grumpy talk = "sprites/kara_grumpy_talk.png"
# Karalún sprites: alert
image kara startled = "sprites/kara_startled.png"
image kara excited = "sprites/kara_excited.png"
image kara angry = "sprites/kara_angry.png"

# Kim sprites: main
image kim happy = "sprites/kim_happy.png"
image kim happy talk = "sprites/kim_happy_talk.png"
image kim worried = "sprites/kim_worried.png"
image kim worried talk = "sprites/kim_worried_talk.png"
image kim angry = "sprites/kim_angry.png"
image kim angry talk = "sprites/kim_angry_talk.png"
image kim grin = "sprites/kim_grin.png"
# Kim sprites: stiff
image kim startled = "sprites/kim_startled.png"
image kim startled talk = "sprites/kim_startled_talk.png"
image kim stern = "sprites/kim_stern.png"
image kim stern talk = "sprites/kim_stern_talk.png"
# Kim sprites: sassy
image kim suspicious = "sprites/kim_suspicious.png"
image kim suspicious talk = "sprites/kim_suspicious_talk.png"
image kim curious = "sprites/kim_curious.png"

# Nakoa sprites: main
image nakoa happy = "sprites/nakoa_happy.png"
image nakoa happy talk = "sprites/nakoa_happy_talk.png"
image nakoa worried = "sprites/nakoa_worried.png"
image nakoa worried talk = "sprites/nakoa_worried_talk.png"
image nakoa angry = "sprites/nakoa_angry.png"
image nakoa angry talk = "sprites/nakoa_angry_talk.png"
image nakoa grin = "sprites/nakoa_grin.png"
# Nakoa sprites: slouching
image nakoa grumpy = "sprites/nakoa_grumpy.png"
image nakoa grumpy talk = "sprites/nakoa_grumpy_talk.png"
image nakoa scowl = "sprites/nakoa_scowl.png"
# Nakoa sprites: sassy
image nakoa friendly = "sprites/nakoa_friendly.png"
image nakoa smug = "sprites/nakoa_smug.png"
image nakoa stern = "sprites/nakoa_stern.png"

# Tansei sprites: main
image tansei neutral = "sprites/tansei_neutral.png"
image tansei neutral talk = "sprites/tansei_neutral_talk.png"
image tansei happy = "sprites/tansei_happy.png"
image tansei happy talk = "sprites/tansei_happy_talk.png"
image tansei stern = "sprites/tansei_stern.png"
image tansei stern talk = "sprites/tansei_stern_talk.png"
image tansei worried = "sprites/tansei_worried.png"
image tansei worried talk = "sprites/tansei_worried_talk.png"
image tansei sad = "sprites/tansei_sad.png"
# Tansei sprites: hand out
image tansei gesture = "sprites/tansei_gesture.png"
image tansei gesture talk = "sprites/tansei_gesture_talk.png"
image tansei friendly = "sprites/tansei_friendly.png"
image tansei friendly talk = "sprites/tansei_friendly_talk.png"
image tansei angry = "sprites/tansei_angry.png"
# Tansei sprites: tucking hair
image tansei excited = "sprites/tansei_excited.png"
image tansei laughing = "sprites/tansei_laughing.png"
image tansei shy = "sprites/tansei_shy.png"
# Tansei sprites: profile
image tansei pensive = "sprites/tansei_pensive.png"
image tansei crying = "sprites/tansei_crying.png"
image tansei startled = "sprites/tansei_startled.png"

define e = Character("Emma", kind=c_base)
image emma = Placeholder("girl")
# # TEMPORARY: use Kim for Emma for photo op
# image emma = "sprites/kim_temp.png"
image khurrayo = Placeholder("boy")
image allira = Placeholder("girl")
image nami = Placeholder("girl")

# Define transforms and transitions here.

transform center_1:
    xalign 0.5 yalign 1.0 yoffset 20
transform center_1_h:
    xalign 0.5 yalign 1.0 yoffset 0
transform center_1_l:
    xalign 0.5 yalign 1.0 yoffset 40

transform leftish_2:
    xalign 0.3 yalign 1.0 yoffset 20
transform leftish_2_h:
    xalign 0.3 yalign 1.0 yoffset 0
transform leftish_2_l:
    xalign 0.3 yalign 1.0 yoffset 40

transform rightish_2:
    xalign 0.7 yalign 1.0 yoffset 20
transform rightish_2_h:
    xalign 0.7 yalign 1.0 yoffset 0
transform rightish_2_l:
    xalign 0.7 yalign 1.0 yoffset 40

transform leftish_3:
    xalign 0.15 yalign 1.0 yoffset 20
transform leftish_3_h:
    xalign 0.15 yalign 1.0 yoffset 0
transform leftish_3_l:
    xalign 0.15 yalign 1.0 yoffset 40

transform rightish_3:
    xalign 0.85 yalign 1.0 yoffset 20
transform rightish_3_h:
    xalign 0.85 yalign 1.0 yoffset 0
transform rightish_3_l:
    xalign 0.85 yalign 1.0 yoffset 40

transform left_4:
    xalign 0.05 yalign 1.0 yoffset 20
transform left_4_h:
    xalign 0.05 yalign 1.0 yoffset 0
transform left_4_l:
    xalign 0.05 yalign 1.0 yoffset 40

transform leftish_4:
    xalign 0.35 yalign 1.0 yoffset 20
transform leftish_4_h:
    xalign 0.35 yalign 1.0 yoffset 0
transform leftish_4_l:
    xalign 0.35 yalign 1.0 yoffset 40

transform rightish_4:
    xalign 0.65 yalign 1.0 yoffset 20
transform rightish_4_h:
    xalign 0.65 yalign 1.0 yoffset 0
transform rightish_4_l:
    xalign 0.65 yalign 1.0 yoffset 40

transform right_4:
    xalign 0.95 yalign 1.0 yoffset 20
transform right_4_h:
    xalign 0.95 yalign 1.0 yoffset 0
transform right_4_l:
    xalign 0.95 yalign 1.0 yoffset 40

transform farleft:
    xalign 0.0 yalign 1.0 yoffset 20
transform farleft_h:
    xalign 0.0 yalign 1.0 yoffset 0
transform farleft_l:
    xalign 0.0 yalign 1.0 yoffset 40

transform farright:
    xalign 1.0 yalign 1.0 yoffset 20
transform farright_h:
    xalign 1.0 yalign 1.0 yoffset 0
transform farright_l:
    xalign 1.0 yalign 1.0 yoffset 40

# Default 'dissolve' lasts 0.5 secs, let's make more
define dissolve_f = Dissolve(0.1)
define dissolve_s = Dissolve(1.0)

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
    # one per act/chapter(?). Start by jumping to chapter_0 (prologue).

    # jump test_scene
    # jump chapter_0
    # jump testytest
    jump chapter_1
    # jump photoop
