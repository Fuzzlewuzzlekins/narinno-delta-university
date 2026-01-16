# Start out by setting up character sprites and backgrounds.
# define frame_rate = 10.0
define frame_rate = 8.0
define anim_speed = 1.0 / frame_rate

image testbg = "testgamebg.png"
image dummy f_idle = "sprites/minigame/dummy_front_idle.png"
image dummy b_idle = "sprites/minigame/dummy_back_idle.png"
image dummy l_idle = "sprites/minigame/dummy_left_idle.png"
image dummy r_idle = "sprites/minigame/dummy_right_idle.png"

image dummy f_walk:
    "sprites/minigame/dummy_front_walk1.png"
    pause anim_speed
    "sprites/minigame/dummy_front_walk2.png"
    pause anim_speed
    repeat

image dummy b_walk:
    "sprites/minigame/dummy_back_walk1.png"
    pause anim_speed
    "sprites/minigame/dummy_back_walk2.png"
    pause anim_speed
    repeat

image dummy l_walk:
    "sprites/minigame/dummy_left_walk1.png"
    pause anim_speed
    "sprites/minigame/dummy_left_walk2.png"
    pause anim_speed
    repeat

image dummy r_walk:
    "sprites/minigame/dummy_right_walk1.png"
    pause anim_speed
    "sprites/minigame/dummy_right_walk2.png"
    pause anim_speed
    repeat

image mg_kim f_idle = "sprites/minigame/kim_front_idle.png"
image mg_kim b_idle = "sprites/minigame/kim_back_idle.png"
image mg_kim l_idle = "sprites/minigame/kim_left_idle.png"
image mg_kim r_idle = "sprites/minigame/kim_right_idle.png"

# image mg_nakoa f_idle = "sprites/minigame/nakoa_front_idle.png"
# image mg_nakoa b_idle = "sprites/minigame/nakoa_back_idle.png"
image mg_nakoa f_b_idle_tails:
    "sprites/minigame/nakoa_front_back_idle_tails1.png"
    pause anim_speed
    "sprites/minigame/nakoa_front_back_idle_tails2.png"
    pause anim_speed
    "sprites/minigame/nakoa_front_back_idle_tails3.png"
    pause anim_speed
    "sprites/minigame/nakoa_front_back_idle_tails4.png"
    pause anim_speed
    "sprites/minigame/nakoa_front_back_idle_tails5.png"
    pause anim_speed
    "sprites/minigame/nakoa_front_back_idle_tails6.png"
    pause anim_speed
    "sprites/minigame/nakoa_front_back_idle_tails7.png"
    pause anim_speed
    "sprites/minigame/nakoa_front_back_idle_tails8.png"
    pause anim_speed
    repeat
image mg_nakoa f_idle = Composite((200,300), (0,0), "mg_nakoa f_b_idle_tails", (0,0), "sprites/minigame/nakoa_front_idle_base.png")
image mg_nakoa b_idle = Composite((200,300), (0,0), "sprites/minigame/nakoa_back_idle_base.png", (0,0), "mg_nakoa f_b_idle_tails")
# image mg_nakoa l_idle = "sprites/minigame/nakoa_left_idle.png"
image mg_nakoa l_idle_tails:
    "sprites/minigame/nakoa_left_idle_tails1.png"
    pause anim_speed
    "sprites/minigame/nakoa_left_idle_tails2.png"
    pause anim_speed
    "sprites/minigame/nakoa_left_idle_tails3.png"
    pause anim_speed
    "sprites/minigame/nakoa_left_idle_tails4.png"
    pause anim_speed
    "sprites/minigame/nakoa_left_idle_tails5.png"
    pause anim_speed
    "sprites/minigame/nakoa_left_idle_tails6.png"
    pause anim_speed
    "sprites/minigame/nakoa_left_idle_tails7.png"
    pause anim_speed
    "sprites/minigame/nakoa_left_idle_tails8.png"
    pause anim_speed
    repeat
image mg_nakoa l_idle = Composite((200,300), (0,0), "mg_nakoa l_idle_tails", (0,0), "sprites/minigame/nakoa_left_idle_base.png")
# image mg_nakoa r_idle = "sprites/minigame/nakoa_right_idle.png"
image mg_nakoa r_idle_tails:
    "sprites/minigame/nakoa_right_idle_tails1.png"
    pause anim_speed
    "sprites/minigame/nakoa_right_idle_tails2.png"
    pause anim_speed
    "sprites/minigame/nakoa_right_idle_tails3.png"
    pause anim_speed
    "sprites/minigame/nakoa_right_idle_tails4.png"
    pause anim_speed
    "sprites/minigame/nakoa_right_idle_tails5.png"
    pause anim_speed
    "sprites/minigame/nakoa_right_idle_tails6.png"
    pause anim_speed
    "sprites/minigame/nakoa_right_idle_tails7.png"
    pause anim_speed
    "sprites/minigame/nakoa_right_idle_tails8.png"
    pause anim_speed
    repeat
image mg_nakoa r_idle = Composite((200,300), (0,0), "mg_nakoa r_idle_tails", (0,0), "sprites/minigame/nakoa_right_idle_base.png")

image mg_tansei f_idle = "sprites/minigame/tansei_front_idle.png"
image mg_tansei b_idle = "sprites/minigame/tansei_back_idle.png"
image mg_tansei l_idle = "sprites/minigame/tansei_left_idle.png"
image mg_tansei r_idle = "sprites/minigame/tansei_right_idle.png"

image mg_kim f_walk = "sprites/minigame/kim_front_idle.png"
image mg_kim b_walk = "sprites/minigame/kim_back_idle.png"
image mg_kim l_walk = "sprites/minigame/kim_left_idle.png"
image mg_kim r_walk = "sprites/minigame/kim_right_idle.png"

# image mg_nakoa f_walk = "sprites/minigame/nakoa_front_idle.png"
image mg_nakoa f_walk:
    "sprites/minigame/nakoa_front_walk1.png"
    pause anim_speed
    "sprites/minigame/nakoa_front_walk2.png"
    pause anim_speed
    "sprites/minigame/nakoa_front_walk3.png"
    pause anim_speed
    "sprites/minigame/nakoa_front_walk4.png"
    pause anim_speed
    "sprites/minigame/nakoa_front_walk5.png"
    pause anim_speed
    "sprites/minigame/nakoa_front_walk6.png"
    pause anim_speed
    "sprites/minigame/nakoa_front_walk7.png"
    pause anim_speed
    "sprites/minigame/nakoa_front_walk8.png"
    pause anim_speed
    repeat
image mg_nakoa b_walk = "sprites/minigame/nakoa_back_idle.png"
image mg_nakoa l_walk = "sprites/minigame/nakoa_left_idle.png"
image mg_nakoa r_walk = "sprites/minigame/nakoa_right_idle.png"

image mg_tansei f_walk = "sprites/minigame/tansei_front_idle.png"
image mg_tansei b_walk = "sprites/minigame/tansei_back_idle.png"
image mg_tansei l_walk = "sprites/minigame/tansei_left_idle.png"
image mg_tansei r_walk = "sprites/minigame/tansei_right_idle.png"

image goal = Solid("#ff0000", xsize=100, ysize=100)

# Not used in minigame, just as a test
image dummy patrol:
    pos (800, 300)
    parallel:
        "dummy f_walk"
    parallel:
        linear 3.0 ypos 800
    pass
    "dummy f_idle"
    pause 2.0
    parallel:
        "dummy b_walk"
    parallel:
        linear 3.0 ypos 300
    pass
    "dummy b_idle"
    pause 2.0
    repeat

# Unused
screen popup_frame(who, what):
    window:
        has vbox

        spacing 10
        text what id "what"
    
# Start of the minigame code.
# Based off of Pong (from Ren'Py tutorial) and Appearing (from Ren'Py docs).

init python:

    import pygame
    import math

    # This class is for grouping character images together. 
    # Each character has 8 animations (directional walk/idle).
    class MinigameCharacterSprite(renpy.Displayable):

        def __init__(self, name, x=400.0, y=400.0, speed=800.0, behavior=None, dialogue=None, direction="down", **kwargs):

            # Pass any kwargs back to renpy.Displayable constructor.
            super(MinigameCharacterSprite, self).__init__(**kwargs)
            
            self.name = name

            # Sprites and animations.
            self.idle_sprites = {
                "up" : renpy.displayable(name + " b_idle"),
                "down" : renpy.displayable(name + " f_idle"),
                "left" : renpy.displayable(name + " l_idle"),
                "right" : renpy.displayable(name + " r_idle")
            }
            self.walk_sprites = {
                "up" : renpy.displayable(name + " b_walk"),
                "down" : renpy.displayable(name + " f_walk"),
                "left" : renpy.displayable(name + " l_walk"),
                "right" : renpy.displayable(name + " r_walk")
            }

            # The current facing direction.
            # self.spritedir = direction
            self.spritedir = behavior[0]["direction"] if behavior else direction

            # Player sprite position, delta-position, speed
            self.spritex = x
            self.spritey = y
            self.spritedx = .5
            self.spritedy = .5
            # self.spritespeed = speed
            self.spritespeed = behavior[0]["speed"] if behavior else speed

            # NPC behavior stuff
            self.behaviors = behavior
            self.lastbehaviorstart = pygame.time.get_ticks()
            self.lastbehaviorpause = pygame.time.get_ticks()
            self.paused = False
            self.dialogue = dialogue

        # Not sure if needed?
        def visit(self):
            return [ self.idle_sprites[self.spritedir], self.walk_sprites[self.spritedir] ]

        # Currently unused
        def update_direction(direction):
            self.spritedir = direction
        
        # Currently unused
        def idle_sprite():
            return self.idle_sprites[self.spritedir]

        # Currently unused
        def walk_sprite():
            return self.walk_sprites[self.spritedir]

    # This class is a container for objects in the minigame 
    # (goals, obstacles, interactibles, etc). It's simpler 
    # than MinigameCharacterSprite but should behave similarly.
    class MinigameObjectSprite(renpy.Displayable):

        def __init__(self, name, x=400.0, y=400.0, **kwargs):
            
            # Pass any kwargs back to renpy.Displayable constructor.
            super(MinigameObjectSprite, self).__init__(**kwargs)

            # We want to track our own sprite (displayable) and our 
            # position in the "map space".
            self.name = name
            self.sprite = renpy.displayable(name)
            self.spritex = x
            self.spritey = y

        def visit(self):
            return [ self.sprite ]

        # render() override. Not sure why I didn't have to do this
        # for MinigameCharacterSprite, but whatever
        def render(self, width, height, st, at):

            # Create render of sprite
            spriterender = renpy.render(self.sprite, width, height, st, at)
            spritewidth, spriteheight = spriterender.get_size()

            # The Render object we'll draw into/return
            # r = renpy.Render(spritewidth, spriteheight)
            r = renpy.Render(width, height)

            # Draw the sprite to the class render. No positioning 
            # needed yet, since this isn't the full map
            r.blit(spriterender, (0, 0))

            return spriterender

    # This class is the base container for the minigame. 
    # Contains logic for background and player movement.
    class MinigameDisplayable(renpy.Displayable):
        
        def __init__(self, map=None, hero=("dummy",500,500), npcs=[], goals=[], timeout=None, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(MinigameDisplayable, self).__init__(**kwargs)

            # Some constants.
            self.FIELD_BORDER = 100
            self.map = renpy.displayable(map)
            self.mapx = 0
            self.mapy = 0
            self.hero = hero
            self.herosprite = MinigameCharacterSprite(hero[0], x=hero[1], y=hero[2])
            self.npcsprites = []
            for character in npcs:
                # TEMP schema: 0 - name, 1 - x, 2 - y, 3 - behavior, 4 - dialogue. TODO: switch to names instead of indexes
                self.npcsprites.append(MinigameCharacterSprite(character[0], x=character[1], y=character[2],
                                behavior=character[3], dialogue=character[4]))
            self.goalsprites = []
            for goal in goals:
                self.goalsprites.append(MinigameObjectSprite(goal[0], x=goal[1], y=goal[2]))
            # If the arrow keys are pressed.
            self.keyleft = False
            self.keyright = False
            self.keyup = False
            self.keydown = False
            
            # The current player sprite, based on direction.
            self.chosensprite = self.herosprite.idle_sprites[self.herosprite.spritedir]

            # The time of the past render-frame.
            self.oldst = None

            # The win condition.
            self.win_condition = None
            self.goal_reached = None

            # Interaction: is key pressed, is window open, who's talking, etc.
            self.interact = False
            self.dialog_open = False
            self.dialog_object = None
            self.dialog_npc = None
            self.dialog_coords = [0,0]

            # NEW: "automatic" dialog boxes spoken without interaction
            self.bg_dialog_objects = [None for i in range(len(self.npcsprites))]
            self.bg_dialog_coords = [[0,0] for i in range(len(self.npcsprites))]

        def visit(self):
            return [ self.chosensprite ]

        # Recomputes the position of the background and sprites, and
        # draws the screen.
        def render(self, width, height, st, at):
            
            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)

            # Update player sprite direction based on movement direction.
            if not self.dialog_open:
                if self.keyleft and not(self.keyright):
                    self.herosprite.spritedir = "left"
                if self.keyright and not(self.keyleft):
                    self.herosprite.spritedir = "right"
                if self.keyup:
                    self.herosprite.spritedir = "up"
                if self.keydown:
                    self.herosprite.spritedir = "down"
            
            # If moving sprite is leftover and key is not held down,
            # replace with idle sprite.
            if (self.keyleft or self.keyright or self.keyup or self.keydown) and not self.dialog_open:
                self.chosensprite = self.herosprite.walk_sprites[self.herosprite.spritedir]
            else:
                self.chosensprite = self.herosprite.idle_sprites[self.herosprite.spritedir]

            # Create whichever sprite(s) we've decided on
            mapsprite = renpy.render(self.map, width, height, st, at)
            mapwidth, mapheight = mapsprite.get_size()
            playersprite = renpy.render(self.chosensprite, width, height, st, at)
            playerwidth, playerheight = playersprite.get_size()

            # Figure out the time elapsed since the previous frame.
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            # Figure out how to move the player sprite/background.
            speed = dtime * self.herosprite.spritespeed
            # oldpspritex = self.herosprite.spritex

            # Only allow the player to move if the dialog box isn't open
            if not self.dialog_open:
                if self.keyleft:
                    self.herosprite.spritex -= self.herosprite.spritedx * speed
                    self.mapx += self.herosprite.spritedx * speed
                if self.keyright:
                    self.herosprite.spritex += self.herosprite.spritedx * speed
                    self.mapx -= self.herosprite.spritedx * speed
                if self.keyup:
                    self.herosprite.spritey -= self.herosprite.spritedy * speed
                    self.mapy += self.herosprite.spritedy * speed
                if self.keydown:
                    self.herosprite.spritey += self.herosprite.spritedy * speed
                    self.mapy -= self.herosprite.spritedy * speed

            # Limit player sprite to the map boundaries.
            player_top = self.FIELD_BORDER + playerheight / 2
            if self.herosprite.spritey < player_top:
                self.herosprite.spritey = player_top

            player_bot = mapheight - self.FIELD_BORDER - playerheight / 2
            if self.herosprite.spritey > player_bot:
                self.herosprite.spritey = player_bot

            player_lef = self.FIELD_BORDER + playerwidth / 2
            if self.herosprite.spritex < player_lef:
                self.herosprite.spritex = player_lef

            player_rig = mapwidth - self.FIELD_BORDER - playerwidth / 2
            if self.herosprite.spritex > player_rig:
                self.herosprite.spritex = player_rig

            # Limit map scroll to the screen boundaries.
            if self.mapx > 0 or self.herosprite.spritex < width / 2:
                self.mapx = 0
            if self.mapx < (width - mapwidth) or self.herosprite.spritex > mapwidth - width / 2:
                self.mapx = (width - mapwidth)
            if self.mapy > 0 or self.herosprite.spritey < height / 2:
                self.mapy = 0
            if self.mapy < (height - mapheight) or self.herosprite.spritey > mapheight - height / 2:
                self.mapy = height - mapheight

            # Figure out what the NPCs are doing
            charsprites = []
            for character in self.npcsprites:
                charspeed = dtime * character.spritespeed
                # If it's time for the next behavior, update list and values
                currenttime = pygame.time.get_ticks()
                if (currenttime - character.lastbehaviorstart > character.behaviors[0]["duration"] * 1000 
                                and not character.paused):
                    character.lastbehaviorstart = currenttime
                    oldbehavior = character.behaviors.pop(0)
                    character.behaviors.append(oldbehavior)
                    character.spritedir = character.behaviors[0]["direction"]
                    character.spritespeed = character.behaviors[0]["speed"]
                # Move sprite according to same procedure as hero
                charspeed = dtime * character.spritespeed
                if not character.paused:
                    if character.spritedir == "left":
                        character.spritex -= character.spritedx * charspeed
                    if character.spritedir == "right":
                        character.spritex += character.spritedx * charspeed
                    if character.spritedir == "up":
                        character.spritey -= character.spritedy * charspeed
                    if character.spritedir == "down":
                        character.spritey += character.spritedy * charspeed
                else:
                    # NEW: if NPC is talking, rotate to face the player
                    xdiff = self.herosprite.spritex - character.spritex
                    ydiff = self.herosprite.spritey - character.spritey
                    if xdiff < 0 and abs(xdiff) > abs(ydiff):
                        character.spritedir = "left"
                    elif xdiff >= 0 and abs(xdiff) > abs(ydiff):
                        character.spritedir = "right"
                    else:
                        if ydiff < 0:
                            character.spritedir = "up"
                        else:
                            character.spritedir = "down"
                # Select walking or idle animation
                charsprite = None
                if character.spritespeed == 0.0 or character.paused:
                    charsprite = renpy.render(character.idle_sprites[character.spritedir], width, height, st, at)
                else:
                    charsprite = renpy.render(character.walk_sprites[character.spritedir], width, height, st, at)
                charwidth, charheight = charsprite.get_size()
                charsprites.append((charsprite, (int(character.spritex - charwidth/2 + self.mapx), 
                                int(character.spritey - charheight/2 + self.mapy))))

            # Add hero to sprite list
            charsprites.append((playersprite, (int(self.herosprite.spritex - playerwidth/2 + self.mapx),
                            int(self.herosprite.spritey - playerheight/2 + self.mapy))))
            
            # Has the interaction button just been pressed?
            if self.interact:
                self.interact = False
                # If the dialog popup isn't open, see if it can be opened
                if not self.dialog_open:
                    # Loop through NPC sprites and find collisions
                    collisions = []
                    herox, heroy = charsprites[len(charsprites)-1][1]
                    for i in range(len(charsprites)-1):
                        npcx, npcy = charsprites[i][1]
                        npcwidth, npcheight = charsprites[i][0].get_size()
                        if ((npcx-herox <= playerwidth and herox-npcx <= npcwidth)
                                        and (npcy-heroy <= playerheight and heroy-npcy <= npcheight)):
                            collisions.append(i)
                    # If there is at least one collision...
                    if len(collisions) > 0:
                        # Loop through collisions and find closest NPC
                        closestdist = math.dist([0,0], [mapwidth, mapheight])
                        for i in collisions:
                            charx, chary = charsprites[i][1]
                            charwidth, charheight = charsprites[i][0].get_size()
                            tempdist = math.dist([herox + playerwidth/2, heroy + playerheight/2],
                                            [charx + charwidth/2, chary + charheight/2])
                            if tempdist < closestdist:
                                self.dialog_npc = i
                                closestdist = tempdist
                        # You found the NPC who talked! Pause them.
                        self.npcsprites[self.dialog_npc].paused = True
                        self.npcsprites[self.dialog_npc].lastbehaviorpause = pygame.time.get_ticks()
                        # Now build the dialog window.
                        self.dialog_open = True
                        dialogtext = Text(self.npcsprites[self.dialog_npc].dialogue[0], size=20, color=gui.interface_text_color, xalign=0.5, yalign=0.5)
                        self.dialog_object = Window(dialogtext, background=bubble.thoughtframe, xsize=300, ysize=200, padding=(20,20))
                        # Center the dialog box on the NPC sprite, above their head (may move later)
                        self.dialog_coords = [self.npcsprites[self.dialog_npc].spritex, 
                                        self.npcsprites[self.dialog_npc].spritey - (charsprites[self.dialog_npc][0].get_size()[1]) + 100]
                # Otherwise, close the popup
                else:
                    self.dialog_open = False
                    # Unpause NPC
                    self.npcsprites[self.dialog_npc].paused = False
                    self.npcsprites[self.dialog_npc].lastbehaviorstart += pygame.time.get_ticks() - self.npcsprites[self.dialog_npc].lastbehaviorpause
                    # Advance speaking NPC's dialogue by 1 line for next time
                    oldtext = self.npcsprites[self.dialog_npc].dialogue.pop(0)
                    self.npcsprites[self.dialog_npc].dialogue.append(oldtext)

            # NEW: create "idle" dialog windows for NPCs not being interacted with
            for i in range(len(self.npcsprites)):
                # TODO: give NPCs a "cooldown" so they don't redisplay this idle text right after being spoken to
                if self.npcsprites[i].behaviors[0]["text"] and not self.npcsprites[i].paused:
                    dialogtext = Text(self.npcsprites[i].behaviors[0]["text"], size=18, color=gui.interface_text_color, xalign=0.5, yalign=0.5)
                    self.bg_dialog_objects[i] = Window(dialogtext, background=bubble.thoughtframe, xsize=240, ysize=160, padding=(20,20))
                    self.bg_dialog_coords[i] = [self.npcsprites[i].spritex, self.npcsprites[i].spritey - (charsprites[i][0].get_size()[1]) + 100]
                else:
                    self.bg_dialog_objects[i] = None

            # See if the player has reached a goal
            objsprites = []
            for goal in self.goalsprites:
                goalsprite = renpy.render(goal, width, height, st, at)
                goalwidth, goalheight = goalsprite.get_size()
                objsprites.append((goalsprite, (int(goal.spritex - goalwidth/2 + self.mapx), int(goal.spritey - goalheight/2 + self.mapy))))
            if len(objsprites) > 0:
                # Loop through goals and find collisions
                collisions = []
                herox, heroy = charsprites[len(charsprites)-1][1]
                for i in range(len(objsprites)):
                    goalx, goaly = objsprites[i][1]
                    goalwidth, goalheight = objsprites[i][0].get_size()
                    if ((goalx-herox <= playerwidth and herox-goalx <= goalwidth)
                                    and (goaly-heroy <= playerheight and heroy-goaly <= goalheight)):
                        collisions.append(i)
                # If there is at least one collision...
                if len(collisions) > 0:
                    # Loop through collisions and find closest goal
                    closestdist = math.dist([0,0], [mapwidth, mapheight])
                    for i in collisions:
                        goalx, goaly = objsprites[i][1]
                        goalwidth, goalheight = objsprites[i][0].get_size()
                        tempdist = math.dist([herox + playerwidth/2, heroy + playerheight/2],
                                        [goalx + goalwidth/2, goaly + goalheight/2])
                        if tempdist < closestdist:
                            self.goal_reached = i
                            closestdist = tempdist
                    # You found the goal that was reached! Log it as the win condition.
                    self.win_condition = self.goalsprites[self.goal_reached].name

            # Draw the background
            r.blit(mapsprite, (int(self.mapx), int(self.mapy)))

            # Draw each character and object sprite, sorted by 
            # y coordinate of bottom edge
            allsprites = charsprites + objsprites
            # allsprites.sort(key=lambda x: x[1][1] + x[0].get_size()[1])
            for i in range(len(allsprites)):
                highest = height * 2 # Hopefully no sprites are taller than the screen...
                currentchar = None
                for j in range(len(allsprites)):
                    tempchar = allsprites[j]
                    temppos = tempchar[1][1] + (tempchar[0].get_size()[1]/2)
                    if temppos < highest:
                        highest = temppos
                        currentchar = tempchar
                allsprites.remove(currentchar)
                r.blit(currentchar[0], currentchar[1])

            # NEW: show idle popup windows
            for i in range(len(self.bg_dialog_objects)):
                if self.bg_dialog_objects[i]:
                    popupsprite = renpy.render(self.bg_dialog_objects[i], width, height, st, at) 
                    popupwidth, popupheight = popupsprite.get_size()
                    popupx = self.bg_dialog_coords[i][0] - popupwidth/2 + self.mapx
                    popupy = self.bg_dialog_coords[i][1] - popupheight/2 + self.mapy
                    # Adjust popup location to fit within screen bounds if necessary
                    popupx = max([popupx, 50])
                    popupx = min([popupx, width-popupwidth-50])
                    popupy = max([popupy, 50])
                    popupy = min([popupy, height-popupheight-50])
                    r.blit(popupsprite, (int(popupx), int(popupy)))

            # show main popup window
            if self.dialog_open:
                popupsprite = renpy.render(self.dialog_object, width, height, st, at) 
                popupwidth, popupheight = popupsprite.get_size()
                popupx = self.dialog_coords[0] - popupwidth/2 + self.mapx
                popupy = self.dialog_coords[1] - popupheight/2 + self.mapy
                # Adjust popup location to fit within screen bounds if necessary
                popupx = max([popupx, 50])
                popupx = min([popupx, width-popupwidth-50])
                popupy = max([popupy, 50])
                popupy = min([popupy, height-popupheight-50])
                r.blit(popupsprite, (int(popupx), int(popupy)))

            # If we have a win condition, call event to notice it.
            if self.win_condition:
                renpy.timeout(0)

            # Ask that we be re-rendered ASAP, so we can show the next
            # frame.
            renpy.redraw(self, 0)

            # Return the Render object.
            return r

        # Handles events.
        def event(self, ev, x, y, st):

            # Detect key presses.
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_UP:
                    self.keyup = True
                elif ev.key == pygame.K_DOWN:
                    self.keydown = True
                elif ev.key == pygame.K_LEFT:
                    self.keyleft = True
                elif ev.key == pygame.K_RIGHT:
                    self.keyright = True
                elif ev.key == pygame.K_SPACE:
                    self.interact = True
                # TODO: remove escape skip (or implement fair bypass)
                elif ev.key == pygame.K_ESCAPE:
                    self.win_condition = "escape"
            
            # Detect key releases.
            if ev.type == pygame.KEYUP:
                if ev.key == pygame.K_UP:
                    self.keyup = False
                elif ev.key == pygame.K_DOWN:
                    self.keydown = False
                elif ev.key == pygame.K_LEFT:
                    self.keyleft = False
                elif ev.key == pygame.K_RIGHT:
                    self.keyright = False

            # Return the win condition (goal reached, timeout, or escape),
            # otherwise ignore event
            if self.win_condition:
                return self.win_condition
            else:
                raise renpy.IgnoreEvent()

# screen minigame():
screen minigame(bg, hero, npcs=[], goals=[], timeout=None):

    default minigame = MinigameDisplayable(bg, hero, npcs, goals, timeout)

    add minigame
    
    # Display instructions/keypresses available in this instance
    # TODO: make this respond to parameters (and be in a less obtrusive place)
    text _("Use arrow keys and spacebar"):
        at truecenter
        xanchor 0.5
        size 40

