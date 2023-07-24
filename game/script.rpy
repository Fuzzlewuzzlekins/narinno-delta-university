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

# The game starts here.

label start:

    # All actual scripts of the game will be handled in separate files, 
    # one per act. Start by jumping to act_1.

    jump act_1
