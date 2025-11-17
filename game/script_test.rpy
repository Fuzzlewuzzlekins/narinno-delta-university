label test_scene:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    
    show kim happy talk at leftish_2
    show fyorra at rightish_2

    ki "Here we are as 2"

    show kim happy at leftish_3
    show fyorra at center_1
    show nakoa happy at rightish_3

    f "and as 3"

    show kim happy at left_4
    show fyorra at leftish_4
    show nakoa happy talk at rightish_4
    show ash at right_4

    nk "and as 4!"

    show nakoa happy

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
    call screen minigame(bg="testbg", hero=("dummy", 500, 500), npcs=[
                    (
                        "dummy", 300, 600, [
                            {"direction":"down","speed":500.0,"duration":1.0,"text":None},
                            {"direction":"down","speed":0.0,"duration":1.0,"text":"WHOA"},
                            {"direction":"up","speed":500.0,"duration":1.0,"text":None},
                            {"direction":"up","speed":0.0,"duration":1.0,"text":None}
                        ],
                        [
                            "Oh, hello! Is it working?",
                            "They gave me custom dialogue!"
                        ]
                    ),
                    (
                        "dummy", 800, 200, [
                            {"direction":"left","speed":0.0,"duration":1.5,"text":None},
                            {"direction":"right","speed":500.0,"duration":1.0,"text":None},
                            {"direction":"right","speed":0.0,"duration":2.0,"text":None},
                            {"direction":"left","speed":500.0,"duration":1.0,"text":"I'm talking while moving! That's pretty neat."},
                            {"direction":"left","speed":0.0,"duration":0.5,"text":None}
                        ],
                        [
                            "Hey there!",
                            "No, I'm a different NPC."
                        ]
                    )
                ],
                goals=[
                    ("goal", 1000, 1000)
                ],
                _with_none=False) with flash
    with flash

    $ quick_menu = True
    window show

    if _return == "spacebar":

        a "Oooh, the spacebar worked!"
    
    else:
        r "Huh? Not sure what it returned."

    # This ends the game.

    return