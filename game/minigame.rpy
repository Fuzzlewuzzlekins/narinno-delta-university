# Start out by setting up character sprites and backgrounds.
define frame_rate = 10.0
define anim_speed = 1.0 / frame_rate

image testbg = "testgamebg.png"
image dummy f_idle = "sprites/dummy_front_idle.png"
image dummy b_idle = "sprites/dummy_back_idle.png"
image dummy l_idle = "sprites/dummy_left_idle.png"
image dummy r_idle = "sprites/dummy_right_idle.png"

image dummy f_walk:
    "sprites/dummy_front_walk1.png"
    pause anim_speed
    "sprites/dummy_front_walk2.png"
    pause anim_speed
    repeat

image dummy b_walk:
    "sprites/dummy_back_walk1.png"
    pause anim_speed
    "sprites/dummy_back_walk2.png"
    pause anim_speed
    repeat

image dummy l_walk:
    "sprites/dummy_left_walk1.png"
    pause anim_speed
    "sprites/dummy_left_walk2.png"
    pause anim_speed
    repeat

image dummy r_walk:
    "sprites/dummy_right_walk1.png"
    pause anim_speed
    "sprites/dummy_right_walk2.png"
    pause anim_speed
    repeat

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

        def __init__(self, name, start_x=400.0, start_y=400.0, speed=800.0, behavior=None, dialogue=None, direction="down", **kwargs):

            # Pass any kwargs back to renpy.Displayable constructor.
            super(MinigameCharacterSprite, self).__init__(**kwargs)
            
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
            self.spritex = start_x
            self.spritey = start_y
            self.spritedx = .5
            self.spritedy = .5
            # self.spritespeed = speed
            self.spritespeed = behavior[0]["speed"] if behavior else speed

            # NPC behavior stuff
            self.behaviors = behavior
            self.lastbehaviorstart = pygame.time.get_ticks()
            self.lastbehaviorpause = pygame.time.get_ticks()
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

    # This class is the base container for the minigame. 
    # Contains logic for background and player movement.
    # Extend this class to handle unique NPC logic per 
    # instance of the game.
    class MinigameDisplayable(renpy.Displayable):
        
        def __init__(self, map=None, hero=("dummy",500,500), npcs=[], **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(MinigameDisplayable, self).__init__(**kwargs)

            # Some constants.
            self.FIELD_BORDER = 100
            self.map = renpy.displayable(map)
            self.mapx = 0
            self.mapy = 0
            self.hero = hero
            self.herosprite = MinigameCharacterSprite(hero[0], start_x=hero[1], start_y=hero[2])
            self.npcsprites = []
            for character in npcs:
                # TEMP schema: 0 - name, 1 - x, 2 - y, 3 - behavior, 4 - dialogue. TODO: switch to names instead of indexes
                self.npcsprites.append(MinigameCharacterSprite(character[0], start_x=character[1], start_y=character[2],
                                behavior=character[3], dialogue=character[4]))

            # If the arrow keys are pressed.
            self.keyleft = False
            self.keyright = False
            self.keyup = False
            self.keydown = False
            
            # The current player sprite, based on direction.
            self.chosensprite = self.herosprite.idle_sprites[self.herosprite.spritedir]

            # The time of the past render-frame.
            self.oldst = None

            # The winner.
            self.winner = None
            self.interact = False
            self.dialog_open = False
            self.dialog_object = None
            self.dialog_npc = None
            self.dialog_coords = [0,0]

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

            # player_bot = height - self.FIELD_BORDER - playerheight / 2
            player_bot = mapheight - self.FIELD_BORDER - playerheight / 2
            if self.herosprite.spritey > player_bot:
                self.herosprite.spritey = player_bot

            player_lef = self.FIELD_BORDER + playerwidth / 2
            if self.herosprite.spritex < player_lef:
                self.herosprite.spritex = player_lef

            # player_rig = width - self.FIELD_BORDER - playerwidth / 2
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

            # New: figure out what the NPCs are doing
            charsprites = []
            for character in self.npcsprites:
                # TODO: Don't update character if they're the one who's talking
                charspeed = dtime * character.spritespeed
                # If it's time for the next behavior, update list and values
                currenttime = pygame.time.get_ticks()
                if (currenttime - character.lastbehaviorstart > character.behaviors[0]["duration"] * 1000 
                                and not self.dialog_open):
                    character.lastbehaviorstart = currenttime
                    oldbehavior = character.behaviors.pop(0)
                    character.behaviors.append(oldbehavior)
                    character.spritedir = character.behaviors[0]["direction"]
                    character.spritespeed = character.behaviors[0]["speed"]
                # Move sprite according to same procedure as hero
                charspeed = dtime * character.spritespeed
                if not self.dialog_open:
                    if character.spritedir == "left":
                        character.spritex -= character.spritedx * charspeed
                    if character.spritedir == "right":
                        character.spritex += character.spritedx * charspeed
                    if character.spritedir == "up":
                        character.spritey -= character.spritedy * charspeed
                    if character.spritedir == "down":
                        character.spritey += character.spritedy * charspeed
                # Select walking or idle
                charsprite = None
                if character.spritespeed == 0.0 or self.dialog_open:
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
                        self.npcsprites[self.dialog_npc].lastbehaviorpause = pygame.time.get_ticks()
                        # Now build the dialog window.
                        self.dialog_open = True
                        dialogtext = Text(self.npcsprites[self.dialog_npc].dialogue[0], size=20, xalign=0.5, yalign=0.5)
                        self.dialog_object = Window(dialogtext, background='#ffffff', xsize=300, ysize=200)
                        # Center the dialog box on the NPC sprite, above their head (may move later)
                        self.dialog_coords = [self.npcsprites[self.dialog_npc].spritex, 
                                        self.npcsprites[self.dialog_npc].spritey - (charsprites[self.dialog_npc][0].get_size()[1])]
                # Otherwise, close the popup
                else:
                    self.dialog_open = False
                    # Unpause NPC
                    # self.npcsprites[self.dialog_npc].behaviors.pop(0)
                    self.npcsprites[self.dialog_npc].lastbehaviorstart += pygame.time.get_ticks() - self.npcsprites[self.dialog_npc].lastbehaviorpause
                    # Advance speaking NPC's dialogue by 1 line for next time
                    oldtext = self.npcsprites[self.dialog_npc].dialogue.pop(0)
                    self.npcsprites[self.dialog_npc].dialogue.append(oldtext)

            # Draw the background
            r.blit(mapsprite, (int(self.mapx), int(self.mapy)))

            # Draw each character sprite, sorted by y coordinate
            for i in range(len(charsprites)):
                highest = height
                currentchar = None
                for j in range(len(charsprites)):
                    tempchar = charsprites[j]
                    if tempchar[1][1] < highest:
                        highest = tempchar[1][1]
                        currentchar = tempchar
                charsprites.remove(currentchar)
                r.blit(currentchar[0], currentchar[1])

            # show popup window
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


            # Check for a winner.
            # if self.bx < -50:
            #     self.winner = "kim"

            #     # Needed to ensure that event is called, noticing
            #     # the winner.
            #     renpy.timeout(0)

            # elif self.bx > width + 50:
            #     self.winner = "ash"
            #     renpy.timeout(0)

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
                elif ev.key == pygame.K_ESCAPE:
                    self.winner = True
            
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

            # If we have a winner, return him or her. Otherwise, ignore
            # the current event.
            if self.winner:
                return self.winner
            else:
                raise renpy.IgnoreEvent()

# screen minigame():
screen minigame(bg, hero, npcs):

    default minigame = MinigameDisplayable(bg, hero, npcs)

    add minigame
    
    text _("Use arrow keys and spacebar"):
        at truecenter
        xanchor 0.5
        size 40

