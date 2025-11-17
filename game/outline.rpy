default ka_hobby = None
default a_nn_together = False
default a_nn_f_together = False
default a_f_together = False
default nn_f_together = False

label outline:
    "This is an interactive walkthrough of the story structure for planning purposes."

    "ACT 1"

    nvl_narrator """
    PROLOGUE

    Kim arrives and meets Tansei and Nakoa (and Emma) on the way to campus. She bumps into Nanneyo at check-in.

    Nanneyo heads to her apartment after her volunteer shift and introduces us to Ash.

    {clear}

    CHAPTER 1: Da Capo

    Kim has met her roommate, Luziim. At orientation, she rejoins Nakoa and meets Noah and Karalún.

    Nanneyo interacts with Ash. Meets Fyorra, Blake, and Tansei for brunch.

    {clear}

    CHAPTER 2: Mount Resshan

    Kim goes to orientation (hiking) with Nakoa, Kara, and Noah.

    Noah reports back to Blake and Tansei the next day. They agree that Blake should give Kara music lessons.

    {clear}

    CHAPTER 3: Join the Chorus

    Kim introduces Karalún and Luziim to each other. Then she goes to choir and meets Blake, Nanneyo, and Fyorra.

    After class, Nanneyo sees Fyorra off to tutoring. Fyorra meets Nyarokhu.

    {clear}

    CHAPTER 4: The Club Fair

    Nanneyo helps set up the fair and meets Fyorra for lunch. They have a brief run-in with Kim, Kara, and Luziim. 

    After lunch, Karalún can't decide whether to follow Kim or Luziim at the fair...
    """

menu kara_hobby (nvl=True):
    "Kim ({b}arts{/b})":
        $ ka_hobby = "arts"

        extend " She follows Kim and signs up for a {b}fiber arts{/b} club."

    "Luziim ({b}sports{/b})":
        $ ka_hobby = "sports"

        extend " She follows Luziim and signs up for a {b}martial arts{/b} club."

label after_kara_hobby:

    nvl_narrator "We meet Rohal at the fair, who banters with Tansei. He heads home—revealing his anxiety—to collect his housemate Nyarokhu."

    nvl clear

    nvl_narrator """
    CHAPTER 5: Beauty

    Karalún receives a call from an Imperial official, then meets Kim at breakfast. The two walk to Blake's place for a lesson.

    Luziim heads to her first nan-songar practice.

    {clear}

    CHAPTER 6: Small World

    Nakoa chats w/ his advisor, Nodlun, after class. He then runs into Noah at dinner and vents about Tansei being busy; Noah invites him over at a future date.

    Nanneyo and Ash vibing. Nanneyo realizes that Ash is capable of feeling {i}bored{/i}. Gasp!

    Tansei accompanies Blake back to his room after dinner. Noah is there, and soon Nakoa shows up. There is Big Mad.

    {clear}

    CHAPTER 7: Inner Demons

    Karalún bumps into Kim at dinner. Kim is sad from flunking an audition, and Kara feels protective/big-sisterly towards her. After dinner, she heads to her club meeting but gets stalked and harassed by two zanduul; Nodlun swoops in to scare them off and comfort her.

    Nyarokhu suffers through a tutoring hour w/ Fyorra and then hurries home, needing a fix. Overhears Rohal bringing a one-night stand home.

    The next morning, Rohal abandons his partner to hurry to practice. Takes a call from the school; two of his teammates have been reprimanded for harassing Kara. Luziim tries to cheer him up.

    {clear}

    CHAPTER 8: Full of Surprises

    Nanneyo lets Ash try her lunch. It's an epiphany.

    Nakoa comes over to visit Noah, but Blake and Tansei are already there. There is tension. Resolved by Noah calling them out and/or Blake beating Nakoa at a video game???? (this is so juvenile wtf)

    Choir practice. Nanneyo is distracted.

    {i}TODO: mention upcoming street fair in one of these three scenes.{/i}

    {clear}

    CHAPTER 9: Sweets and Treats

    Kim invites Karalún and Luziim to the street fair. Luziim is fresh from practice and gushes over Rohal much of the time.

    Rohal and Tani vibing at the gym.

    After choir practice, Nanneyo stumbles upon Ash baking cookies. Gasp! Again!

    After the next choir practice, Nanneyo invites Fyorra over to talk about it. Ash grumbles about being discussed behind his back.

    {i}TODO: rearrange? There's a lot going on here. And what happened to Kara's club?{/i}

    {clear}

    CHAPTER 10: Hot and Heavy

    Nan-songar practice. The other girl in the club (Sahiriin) warns Luziim about Rohal, but she's undeterred and takes her shirt off to mess with him. NEW: Sahiriin gets her comeuppance—kind of?—by running into a teammate and forging on the spot.

    Blake invites Nakoa and Noah to CDC. Noah is outed as a freeheart in denial.

    Tutoring hour. Fyorra and Nyarokhu blow up at each other and get fired.

    {clear}

    CHAPTER 11: Lifeline

    Nanneyo and Ash discuss maturing him. They're interrupted by freshly-fired Fyorra, who's upset.

    Rohal lets Fyorra into his house to check on Nyarokhu, who has just OD'd.

    Nyarokhu vs Fyorra in the hospital.

    {clear}

    CHAPTER 12: CDC

    Blake, Noah, and Nakoa in the audience reminiscing, plus Rohal when he shows up. Some tension. Rohal has to leave early.

    Rohal picks up Nyarokhu from the hospital.

    {clear}

    CHAPTER 13: The Winter Ball

    Many characters present. Luziim and Rohal forge.

    Fyorra comes to wish Nanneyo a happy winter break, but the maturation serum has just arrived. They give it to Ash and seal him up.

    {clear}

    CHAPTER 14: All By Our Lonesome

    Noah goes home. It's not great.

    Karalún goes home. Worldbuilding.

    Nanneyo wakes Ash from hibernation. Naked sexy man jumpscare.
    """

    "ACT 2"

    nvl_narrator """
    {clear}

    CHAPTER 15: Jolly Holiday

    Kim is at home. It's not great.

    Ash experiences the Outside.

    Rohal is at home. It's passable.

    {clear}

    CHAPTER 16: A Fresh Start

    Tansei and Nakoa talk about life and faith and stuff.

    Nanneyo and Ash are vibing. He wants an allowance for hobbies.

    Kim and Luziim come back to school.

    {clear}

    CHAPTER 17: Plan B

    Ash doesn't like being home alone. Nanneyo suggests a job.

    Choir has been canceled! Blake claims the vacant hour for the group.

    {clear}

    CHAPTER 18: Bravery

    Fyorra and Nyarokhu reconvene.

    Ash applies for a job in the campus kitchen.

    {clear}

    CHAPTER 19: Uncomfortable Truths

    Blake encourages Karalún to join the new singing group. Probes Noah about his crush on Kara.

    Rohal and Luziim have a night in. When the power goes out, Rohal has a panic attack.

    {clear}

    CHAPTER 20: We Persevere

    Karalún accompanies Kim to choir practice.

    Ash injures himself and has a flashback. Nanneyo invites him to rehearsal. Order of these two events to be determined.

    {clear}

    CHAPTER 21: Looking Up

    Nakoa pitches an orientation meet-up to Noah, as a thinly veiled double date.

    Ash comes to choir practice with Nanneyo. Blake is impressed.

    Fyorra and Nyarokhu bump into each other again, despite no longer being employed together.

    {i}TODO: Does Blake offer Ash lessons?{/i}

    {clear}

    CHAPTER 22: Feelings

    The 'orientation meetup' happens, with Luziim and Rohal also in tow initially but quickly peeling off. Noah is awkward around Karalún. Nakoa asks Kim on a date.

    Fyorra comes over to Nanneyo's place and vents about life and Nyarokhu.

    Ash comes home and vents. Fyorra tries to cheer him up.

    {i}TODO: introduce VR headsets while window shopping during the double date. This'll be important when Luziim and Nakoa start working together in Act 3.{/i}

    {clear}

    CHAPTER 23: A Changed Man

    Nyarokhu and Rohal witness Luziim's lack of cooking skills.

    Tansei chats w/ Rohal at the gym before going to look for Blake. She finds the music group and is shocked by Ash, and not in a good way. Blake is upset.

    {i}TODO: mention Tansei's faith at some point, so it doesn't come out of left field next chapter.{/i}

    {clear}

    CHAPTER 24: A Changed Woman

    Game night at Blake/Noah's place. Ash comes up in conversation. Tansei is upset and leaves, but Nakoa is intrigued.

    Tansei has a religious nightmare.

    Choir rehearsal. Noah, Nakoa, and Tansei show up to express interest.

    {clear}

    CHAPTER 25: What We Truly Want

    Nakoa and Kim go on a date. Nakoa's more into it than Kim is.

    Nakoa cheerily meets Ash at the cafeteria. Ash has an accident and quits. Nanneyo comforts him that night. Booze and bad decisions are involved.

    Nanneyo rejects Ash the next morning.

    {clear}

    CHAPTER 26: Well, That's Awkward

    Kim and Karalún vibing. A TMI phone call with Luziim causes them to talk about romance (likely incl. Nakoa and Ash).

    Choir rehearsal. Ash is uncomfortable. Nakoa is High On Life these days and invites everyone to dinner and hang. Multiple people bail over the course of the night, leaving Ash, Kim, and Karalún with Noah and Nakoa. Ash is still uncomfortable.

    {clear}

    CHAPTER 27: Gestures

    Rohal shows Luziim the gym. Tansei thanks Luziim for being there for him.

    Nyarokhu does not know how to be a friend.

    The Orientation Gang is vibing again. Nakoa pitches another double date.

    {i}TODO: When does Nyarokhu follow up?{/i}

    {clear}

    CHAPTER 28: Better This Way

    Ash gets a job. He's also curious about Nanneyo's Biot care chat group.

    The Orientation Group Double Date does horrifically sideways.

    {clear}

    CHAPTER 29: No One Cares

    Choir rehearsal. Ash eagerly tries to invite the gang to his new job, oblivious about the double breakup that just happened.

    Ash has garnered attention in the Biot chat group.

    Fyorra visits Nanneyo. They overhear Ash livestreaming.

    {clear}

    CHAPTER 30: Loose Ends

    Only Kim shows up at Ash's new job. They have chemistry, but Kim slams on the brakes. Nanneyo tries to cheer Ash up.

    Karalún opens up to Blake (about being in the closet and about her homeland) at their lesson.

    Nakoa and Kim try to reconcile as friends.

    {i}TODO: Is Ash attending these lessons or separate ones? Or not doing them?{/i}

    {clear}

    CHAPTER 31: Advancements in Learning

    Choir practice. Ash and Karalún stick around to chat, and decide to take up sparring together.

    Fyorra visits Ash to chat. Feelings!

    Kim, Karalún, and Luziim hang out and discuss their academic future.

    {clear}

    CHAPTER 32: The Truth of the Matter

    Tansei checks on Nakoa. They talk about relationships and faith.

    After a sparring session, Karalún comes out of the closet to Ash. He goes home to Nanneyo to vent, and they get in a fight. He asks: does she want him or not?
    """

menu ash_nanneyo_together (nvl=True):
    "Yes":
        $ a_nn_together = True
        $ renpy.notify("Now following the Paired track")

        extend " She does, and they make up."

        nvl_narrator "Fyorra seems a little too happy about this the next morning."

    "No":
        $ renpy.notify("Now following the Single track")

        extend " She turns him down, and he dutifully agrees."

        nvl_narrator "Fyorra seems surprisingly bummed about this development."

label after_ash_nanneyo_together:

    nvl clear

    nvl_narrator """
    CHAPTER 33: Secrecy

    Ash and Nanneyo receive a C&D about his blog. He tells her about his flashbacks.

    Nakoa (followed by Noah) storms into a choir rehearsal, demanding to help Ash. Blake agrees, and the Biot Liberation is formed.

    Karalún fields another call from Imperial officials. She reports it to Nodlun, but their chat is interrupted by Nakoa, who is suddenly interested in Biots.

    {i}TODO: What spurred Nakoa to act? Something Ash told Blake? (When?) Something related to his conversion?{/i}

    {clear}

    CHAPTER 34: Open to Negotiation

    Fyorra and Nyarokhu chat. Ash is mentioned.

    Ash finds a contact in the Biot group who wants to meet him.

    Choir/strategy meeting. Luziim drags Rohal along, mad that Kim/Kara told her nothing about this club. Nyarokhu shows up too after Fyorra's comments. The gang's all here!

    {i}TODO: is this where Nyarokhu follows up with a gesture of friendship? What is it?{/i}

    {clear}

    CHAPTER 35: Out with a Bang

    Blake and Noah chat about finals and summer break being scary.

    Nanneyo and Ash have a video chat w/ their contact (Cameron). Then they host an end-of-semester party for the crew.

    Fyorra wakes up at Rohal's place the next day with a hangover. Nyarokho commiserates.
    """

    "ACT 3"

    nvl_narrator """
    {clear}
    
    CHAPTER 36: Everything's Changing

    Nanneyo takes Ash home. It sucks.

    Kim comes home. It's uncomfortable; she confides in Noah.

    Noah pushes back against his dad.

    {clear}

    CHAPTER 37: New Territory

    Karalún discusses politics at home.

    Ash commiserates with Nanneyo's family's Biots. He goes to a doctor for some tests, but Nanneyo's app objects.

    Tansei and Nakoa are home. A dinner goes extremely poorly, ending in Nakoa's disownment. Tansei helps him pack and leave.

    {clear}

    CHAPTER 38: Data Collection

    Fyorra muses about attraction (specifically to Ash and Nanneyo) and tries booze and coffee. NOTE: will vary based on whether Ash and Nanneyo are together or not.

    Blake discusses politics at home and probes his geneticist dad about Divinity's methods.

    Kim's parents are divorcing. She confides in Karalún and Noah.

    {clear}

    CHAPTER 39: Upended

    Rohal and Luziim trying the LDR thing with mutually overprotective parents.

    Karalún is still getting harassed by the Empire.

    Ash gets back the confidential test results that he's genetically almost human. Nakoa calls and asks if he can crash at Nanneyo's place for the summer.

    {clear}

    CHAPTER 40: Into the Unknown

    Luziim visits Rohal.

    Noah visits his mom.

    Ash and Nanneyo leave to meet their contact. Nakoa calls about the Piyan module Ash apparently had shipped to the apartment.

    {clear}

    CHAPTER 41: Revelations

    Luziim goes to a service w/ Rohal and hears him sing.

    Ash and Nanneyo investigate Cameron's Biot breeding business. He comes clean about the Piyan module and ask Nakoa to investigate.

    Kim returns to campus early and bumps into Nakoa. They bond over feeling lost in life and vow that, despite being exes, they will always be good friends.

    {clear}

    CHAPTER 42: Soul-searching

    The Biot Liberation is back for a new semester! Ash and Nanneyo share their findings, as does Nakoa.

    Blake and Tansei get in a fight and break up.

    {i}TODO: didn't I want to include Luziim in Nakoa's research somehow?{/i}
    
    {clear}
    """

    if a_nn_together:
        jump ch_43_paired
    else:
        jump ch_43_single

label ch_43_paired:

    nvl_narrator "CHAPTER 43: Bonds Broken"

    nvl_narrator "Choir practice. Blake has a bad time and storms out; Kim takes over. Fyorra follows Ash and Nanneyo home..."

## TBD: was going to give Fyorra a choice here, but it feels odd to let em clam up in this 
## branch but NOT the "single" branch. Additionally, keeping NanAsh blissfully ignorant here 
## messes with story pacing later; see below.
# menu fyor_confess_paired (nvl=True):
#     "Confess":
#         $ a_nn_together = False
#         $ a_nn_f_together = True

#         extend " and confesses eir double-crush on them. Nanneyo is a little too excited by this; Ash is hurt and storms out."

#         jump after_fyor_confess_paired_y

#     "Keep quiet (NOT YET WRITTEN)":
#         extend " but ey keeps eir feelings for eir friends suppressed."

#         jump after_fyor_confess_paired_n
    
# label after_fyor_confess_paired_y:

    extend " and confesses eir double-crush on them. Nanneyo is a little too excited by this; Ash is hurt and storms out."

    nvl_narrator """
    Noah and Kim chat about the music group and other things.
    
    {clear}

    CHAPTER 44: Rain

    Karalún hangs out with an upset Ash.

    Kim leads rehearsal again. Ash snaps at Blake for being a flake; Kim agrees with Ash to find a new bass.

    Ash and Nanneyo make up...
    """

menu ash_poly_ok (nvl=True):
    "He's OK with poly":
        $ a_nn_together = False
        $ a_nn_f_together = True
        $ renpy.notify("Paired track -> Golden Trio")

        extend " he's decided that he understands and respects Nanneyo's polyamory and is willing to give it a try."

        jump after_ash_poly_ok
    
    "He's monogamous":
        $ renpy.notify("Paired track -> NanAsh")

        extend " he explains that he's uncomfortable with polyamory, and Nanneyo agrees to be exclusive for him."

        jump after_ash_poly_ok

label after_ash_poly_ok:
    
    extend " But both still miss Fyorra."

    """
    {clear}

    CHAPTER 45: Bonds Mended

    Nyarokhu and Luziim chat.

    Ash and Fyorra reconcile, followed by Fyorra and Nanneyo.
    """

    if a_nn_f_together:
        extend " The Golden Trio is a go!"
    else:
        extend " Fyorra respects the pair's \"no,\" simply glad to have the confession off eir chest."

    jump ch_46

## This version, where Fyorra lets NanAsh be, feels undercooked and underwhelming.
# label after_fyor_confess_paired_n:

#     nvl_narrator """
#     Noah and Kim chat about the music group and other things.
    
#     {clear}

#     CHAPTER 44: TBD

#     Karalún and Ash hang out ig

#     Kim leads rehearsal again. Kim lectures Blake for being a flake?

#     What else...??? Ash and Nanneyo do something fluffy? idk

#     {clear}

#     CHAPTER 45: TBD

#     Nyarokhu and Luziim chat.

#     Uhhhhhhh something with Fyorra here ig
#     """

#     jump ch_46

label ch_43_single:

    nvl_narrator "CHAPTER 43: The Reckoning"

    nvl_narrator "Choir practice. Blake has a bad time and storms out; Kim takes over. Fyorra..."

menu fyor_confess_single (nvl=True):
    "confesses to Ash (NOT YET WRITTEN)":
        $ a_f_together = True
        $ renpy.notify("Single track -> FyorAsh")

        extend " confesses to Ash, dunno yet how or where"

        jump after_fyor_confess_single_a

    "confesses to Nanneyo (NOT YET WRITTEN)":
        $ nn_f_together = True
        $ renpy.notify("Single track -> NanFyor")

        extend " confesses to Nanneyo, dunno yet how or where"

        jump after_fyor_confess_single_nn
    
label after_fyor_confess_single_a:

    nvl_narrator """
    Noah and Kim chat about the music group and other things.
    
    {clear}

    CHAPTER 44: Thunder

    Karalún and Ash hang out and it's chill

    Kim leads rehearsal again. {b}Nanneyo{/b} snaps at Blake for being a flake, while Kim tries to mediate.

    Ash and Fyorra go on a date, but remark on Nanneyo's recent state.

    {clear}

    CHAPTER 45: TBD

    Nyarokhu and Luziim chat.

    Nanneyo seeks out Blake to apologize for the blowup.
    """

    jump ch_46

label after_fyor_confess_single_nn:

    nvl_narrator """
    Noah and Kim chat about the music group and other things.
    
    {clear}

    CHAPTER 44: Storm

    Karalún and Ash hang out. He's probably a little glum because he's still single... maybe she tries to cheer him up and offer ideas?

    Kim leads rehearsal again. Ash snaps at Blake for being a flake, while Kim tries to mediate.

    Nanneyo and Fyorra have a bonding night, but remark on Ash's recent state.

    {clear}

    CHAPTER 45: TBD

    Nyarokhu and Luziim chat.

    Ash seeks out Kim to apologize for the blowup.
    """

    jump ch_46

label ch_46:

    # WE'VE RECONVENED AFTER THE 4-WAY SPLIT THANK GOD

    nvl_narrator """
    {clear}

    CHAPTER 46: Moving Forward

    Noah is lonely because Nakoa and Kim are all in on Biot stuff

    Ash and Kim pitch performing at the street fair this year. Luziim floats a hypothesis about episodic memory and mentions that Rohal is a singer.

    {clear}

    CHAPTER 47: Pet Projects

    Nakoa and Tansei sync up.

    Karalún, Kim, and Ash all ambush Rohal together to recruit him as the new bass and learn the hymn he taught Luziim.

    {clear}

    CHAPTER 48: Big Shoes to Fill

    Kim + Kara + Luziim hangout. Luziim thanks the girls for bullying Rohal, Kim appreciates having her mind taken off her family, and Kara gushes over the hymn project she and Ash are working on. Kim...
    """

menu kim_choice (nvl=True):
    "worries about Noah":
        extend " remembers Noah's family woes and texts him afterwards."

    "feels jealous of Kara and Ash":
        extend " feels a pang of jealousy for Kara's closeness with Ash, prompting Kara to finally come out of the closet to ease her worry."

label after_kim_choice:

    "Stopping for now because it's come to my painful realization that my outline is not nearly as up-to-date as I thought. Will return to Google Slides to iron everything out first"

    return