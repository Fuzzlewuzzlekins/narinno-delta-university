# The script of the game starts here with character inits.

# Declare characters used by this game. The color argument colorizes the
# name of the character. (See gui.rpy for character_colors declarations)

define c_base = Character("base", what_prefix='“', what_suffix='”', ctc_position="fixed")

define a = Character("Ash", kind=c_base, who_color=character_colors["Ash"], image="ash")
define a_y = Character("Ash", kind=c_base, who_color=character_colors["Ash"], image="youngash")
define b = Character("Blake", kind=c_base, who_color=character_colors["Blake"], image="blake")
define f = Character("Fyorra", kind=c_base, who_color=character_colors["Fyorra"], image="fyorra")
define ka = Character("Karalún", kind=c_base, who_color=character_colors["Karalún"], image="kara")
define ki = Character("Kim", kind=c_base, who_color=character_colors["Kim"], image="kim")
define l = Character("Luziim", kind=c_base, who_color=character_colors["Luziim"], image="luziim")
define nk = Character("Nakoa", kind=c_base, who_color=character_colors["Nakoa"], image="nakoa")
define nn = Character("Nanneyo", kind=c_base, who_color=character_colors["Nanneyo"], image="nanneyo")
define no = Character("Noah", kind=c_base, who_color=character_colors["Noah"], image="noah")
define ny = Character("Nyarokhu", kind=c_base, who_color=character_colors["Nyarokhu"], image="nyarokhu")
define r = Character("Rohal", kind=c_base, who_color=character_colors["Rohal"], image="rohal")
define t = Character("Tansei", kind=c_base, who_color=character_colors["Tansei"], image="tansei")

define a_nvl = Character("Ash", kind=nvl, who_color=character_colors["Ash"])
define b_nvl = Character("Blake", kind=nvl, who_color=character_colors["Blake"])
define f_nvl = Character("Fyorra", kind=nvl, who_color=character_colors["Fyorra"])
define ka_nvl = Character("Karalún", kind=nvl, who_color=character_colors["Karalún"])
define ki_nvl = Character("Kim", kind=nvl, who_color=character_colors["Kim"])
define l_nvl = Character("Luziim", kind=nvl, who_color=character_colors["Luziim"])
define nk_nvl = Character("Nakoa", kind=nvl, who_color=character_colors["Nakoa"])
define nn_nvl = Character("Nanneyo", kind=nvl, who_color=character_colors["Nanneyo"])
define no_nvl = Character("Noah", kind=nvl, who_color=character_colors["Noah"])
define ny_nvl = Character("Nyarokhu", kind=nvl, who_color=character_colors["Nyarokhu"])
define r_nvl = Character("Rohal", kind=nvl, who_color=character_colors["Rohal"])
define t_nvl = Character("Tansei", kind=nvl, who_color=character_colors["Tansei"])

# Declare main character sprites.

image ash = "sprites/ash_temp.png"
image blake = Placeholder("boy")
image fyorra = "sprites/fyorra_temp.png"
image luziim = Placeholder("girl")
image nyarokhu = Placeholder("boy")
image rohal = "sprites/rohal_temp.png"

# # Karalún sprites: main
# image kara neutral = "sprites/kara_neutral.png"
# image kara neutral talk = "sprites/kara_neutral_talk.png"
# image kara worried = "sprites/kara_worried.png"
# image kara worried talk = "sprites/kara_worried_talk.png"
# image kara happy = "sprites/kara_happy.png"
# image kara grin = "sprites/kara_grin.png"
# Karalún sprites: profile
image kara pensive = "sprites/kara_pensive.png"
image kara pensive talk = "sprites/kara_pensive_talk.png"
image kara grumpy = "sprites/kara_grumpy.png"
image kara grumpy talk = "sprites/kara_grumpy_talk.png"
# Karalún sprites: alert
image kara startled = "sprites/kara_startled.png"
image kara excited = "sprites/kara_excited.png"
image kara angry = "sprites/kara_angry.png"
# Karalún sprites: layered image
layeredimage kara:
    attribute base1 default:
        when (neutral or neutral_talk or worried or worried_talk or happy or happy_talk or grin or grin_talk)
    group face auto:
        attribute neutral default

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

# Young Ash sprites: layered image
layeredimage youngash:
    group ears auto:
        attribute neutral default
        attribute neutral_talk: 
            "youngash_ears_neutral"
        attribute worried_talk: 
            "youngash_ears_worried"
        attribute happy_talk: 
            "youngash_ears_happy"
        attribute sleepy_talk: 
            "youngash_ears_sleepy"
        attribute confused_talk: 
            "youngash_ears_confused"
    attribute base1a default:
        when (neutral or neutral_talk or worried or worried_talk or happy or happy_talk) and not salute
    attribute base1b default:
        when (neutral or neutral_talk or worried or worried_talk or happy or happy_talk) and salute
    attribute base2 default:
        when (sleepy or sleepy_talk or confused or confused_talk)
    group face auto:
        attribute neutral default
    attribute salute:
        "youngash_arm1b" when (neutral or neutral_talk or worried or worried_talk or happy or happy_talk)
    # attribute arm1b default:
    #     when (neutral or neutral_talk or worried or worried_talk or happy or happy_talk) and salute

# Nakoa sprites: slouching
image nakoa grumpy = "sprites/nakoa_grumpy.png"
image nakoa grumpy talk = "sprites/nakoa_grumpy_talk.png"
image nakoa scowl = "sprites/nakoa_scowl.png"
# Nakoa sprites: layered image
layeredimage nakoa:
    attribute base1 default:
        when (neutral or neutral_talk or happy or happy_talk or worried or worried_talk or angry or angry_talk or grin or grin_talk or grimace or grimace_talk)
    attribute base2 default:
        when (friendly or smug or stern or offended or offended_talk)
    group face auto:
        attribute neutral default

# Nanneyo sprites: layered image
layeredimage nanneyo:
    attribute base1 default:
        when (neutral or neutral_talk or happy or happy_talk or worried or worried_talk or stern or stern_talk)
    attribute base2 default:
        when (flirting or flirting_talk or angry or angry_talk or thinking or thinking_talk or friendly or friendly_talk or laughing or laughing_talk)
    group face auto:
        attribute neutral default
    if nn_nametag:
        "nanneyo_nametag1" when (neutral or neutral_talk or happy or happy_talk or worried or worried_talk or stern or stern_talk)
    if nn_nametag:
        "nanneyo_nametag2" when (flirting or flirting_talk or angry or angry_talk or thinking or thinking_talk or friendly or friendly_talk or laughing or laughing_talk)

# Noah sprites: layered image
layeredimage noah:
    attribute base1 default:
        when (neutral or neutral_talk or happy or happy_talk or worried or worried_talk or stern or stern_talk)
    attribute base2 default:
        when (thinking or smug)
    attribute base3 default:
        when (grin or grin_talk or angry or angry_talk)
    group face auto:
        attribute neutral default
    if no_nametag:
        "noah_nametag1" when (neutral or neutral_talk or happy or happy_talk or worried or worried_talk or stern or stern_talk)
    if no_nametag:
        "noah_nametag2" when (thinking or smug)
    if no_nametag:
        "noah_nametag3" when (grin or grin_talk or angry or angry_talk)
    attribute glasses1 default:
        when (neutral or neutral_talk or happy or happy_talk or worried or worried_talk or stern or stern_talk)
    attribute glasses2 default:
        when (thinking or smug)
    attribute glasses3 default:
        when (grin or grin_talk or angry or angry_talk)
    attribute arm2 default:
        when (thinking or smug)
    attribute arm3 default:
        when (grin or grin_talk or angry or angry_talk)

# Tansei sprites: profile
image tansei pensive = "sprites/tansei_pensive.png"
image tansei crying = "sprites/tansei_crying.png"
image tansei startled = "sprites/tansei_startled.png"
# Tansei sprites: layered image
layeredimage tansei:
    attribute base1 default:
        when (neutral or neutral_talk or happy or happy_talk or stern or stern_talk or worried or worried_talk or sad or sad_talk)
    attribute base2 default:
        when (gesture or gesture_talk or friendly or friendly_talk or angry or angry_talk)
    attribute base3 default:
        when (excited or excited_talk or laughing or shy or shy_talk)
    group face auto:
        attribute neutral default
    attribute hair1 default:
        when (neutral or neutral_talk or happy or happy_talk or stern or stern_talk or worried or worried_talk or sad or sad_talk)
    attribute hair2 default:
        when (gesture or gesture_talk or friendly or friendly_talk or angry or angry_talk)
    attribute hair3 default:
        when (excited or excited_talk or laughing or shy or shy_talk)

# Declare minor characters and sprites.

define e = Character("Emma", kind=c_base, image="emma")
layeredimage emma:
    attribute base default
    group face auto:
        attribute neutral default
define kr = Character("Khurrayo", kind=c_base, image="khurrayo")
layeredimage khurrayo:
    attribute base default
    group face auto:
        attribute neutral default
define nm = Character("Nami", kind=c_base, image="nami")
layeredimage nami:
    attribute base default
    group face auto:
        attribute neutral default
define al = Character("Allira", kind=c_base, image="allira")
layeredimage allira:
    attribute base default
    group face auto:
        attribute neutral default

# Declare backgrounds.

image bg starport_gate = "backgrounds/bg_starport_gate.png"
image bg starport_baggage = "backgrounds/bg_starport_baggage.png"
image bg starport_station = "backgrounds/bg_starport_station.png"
image bg monorail = "backgrounds/bg_monorail.png"
image bg school_station = "backgrounds/bg_school_station.png"
image bg school_exterior = "backgrounds/bg_school_exterior.png"

# Declare (default) narrative flags here.
default pov_character = "Kim"
default nn_nametag = False
default no_nametag = False
default kim_walk_pick = None

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

# Custom dissolve and fade variants
define dissolve_f = Dissolve(0.1)
define dissolve_s = Dissolve(1.0)
define flash = Fade(0.1, 0.0, 0.1, color="#ffffff")
define fade_scene = Fade(1.0, 0.5, 1.0)

define dissolveinleft = ComposeTransition(dissolve, after=easeinleft)
define dissolveinright = ComposeTransition(dissolve, after=easeinright)
define dissolveinbottom = ComposeTransition(dissolve, after=easeinbottom)

define dissolveoutleft = ComposeTransition(dissolve, before=easeoutleft)
define dissolveoutright = ComposeTransition(dissolve, before=easeoutright)
define dissolveoutbottom = ComposeTransition(dissolve, before=easeoutbottom)

define eyesopen = ImageDissolve("imagedissolve_eyes.png", 0.5, ramplen=64)
define eyesclose = ImageDissolve("imagedissolve_eyes.png", 0.5, ramplen=64, reverse=True)

# Custom character in/out transitions that combine a 50-pixel ease with a dissolve.

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

# Slower variants. TODO: make these general instead of copying and pasting, if possible

transform scootoutleft_s:
    easeout 0.8 xoffset -150

define scootoutleft2_s = MoveTransition(0.8, leave=scootoutleft_s, old=True)
define fadeoutleft_s = ComposeTransition(dissolve, scootoutleft2_s, Pause(0.8))

transform scootinleft_s:
    xoffset -150
    easein 0.8 xoffset 0

define scootinleft2_s = MoveTransition(0.8, enter=scootinleft_s, old=False)
define fadeinleft_s = ComposeTransition(dissolve, scootoutleft2_s, scootinleft2_s)

transform scootoutright_s:
    easeout 0.8 xoffset 150

define scootoutright2_s = MoveTransition(0.8, leave=scootoutright_s, old=True)
define fadeoutright_s = ComposeTransition(dissolve, scootoutright2_s, Pause(0.8))

transform scootinright_s:
    xoffset 150
    easein 0.8 xoffset 0

define scootinright2_s = MoveTransition(0.8, enter=scootinright_s, old=False)
define fadeinright_s = ComposeTransition(dissolve, scootoutright2_s, scootinright2_s)

# The game starts here.

window auto True

label start:

    # All actual scripts of the game will be handled in separate files, 
    # one per act/chapter(?). Start by jumping to chapter_0 (prologue).

    # jump test_scene
    # jump outline
    # jump chapter_0
    # jump quickstart
    # jump testytest
    # jump hi_nan
    # jump chapter_0_b
    # jump photoop
    # jump chapter_1_b
    jump chapter_2
    # jump nvl_monologue_test
