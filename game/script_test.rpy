label test_scene:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    
    show kim at leftish_2
    show ash at rightish_2

    ki "Here we are as 2"

    show kim at leftish_3
    show ash at center
    show rohal at rightish_3

    a "and as 3"

    show kim at left
    show ash at leftish_4
    show rohal at rightish_4
    show tansei at right

    r "and as 4!"

    jump test_game_3

label test_game_1:
    
    show screen alpha_magic

    "Can you find the sprite?"

    hide screen alpha_magic

    r "Did you guys have fun?"

    ki "Ah, that was too fast!"

    a "Let's play something that hides the text screen."

label test_game_2:

    window hide  # Hide the window and quick menu while in pong
    $ quick_menu = False

    call screen pong

    $ quick_menu = True
    window show

    if _return == "kim":

        ki "I win! Good game!"

    else:

        a "Phew, can't believe I won that!"

    r "Now that was a match!"

label test_game_3:

    show dummy patrol

    a "But first, this thingy."

    hide dummy
    
    r "Now how about your custom version?"

    window hide
    $ quick_menu = False

    # call screen minigame("sprites/dummy_front_idle.png")
    call screen minigame("testbg", "dummy", ["dummy"])

    $ quick_menu = True
    window show

    if _return == "spacebar":

        a "Oooh, the spacebar worked!"
    
    else:
        r "Yeow! Kim, you're on fire!"

    # This ends the game.

    return