# name of the character.

define b = Character("Bord")
define p = Character("Peng")
define A = Character("Announcer")
default pronounsSub = ""
default pronounsPos = ""
default pronounsObj = ""
default adjPos = ""

# The game starts here.

label start:
    $ inv = []
    $ bordAffectionMeter = 0
    $ pengAffectionMeter = 0

    "Before we start the game, how would you like to be referred to?"
    menu:
        "he/him":
            $ pronounsSub= "he"
            $ pronounsObj = "him"
            $ pronounsPos = "his"
            $ adjPos = "his"
            jump ParkingLot
        "she/her":
            $ pronounsSub= "she"
            $ pronounsObj = "her"
            $ pronounsPos = "hers"
            $ adjPos = "her"
            jump ParkingLot
        "they/them":
            $ pronounsSub= "they"
            $ pronounsObj = "them"
            $ pronounsPos = "theirs"
            $ adjPos = "their"
            jump ParkingLot
        "other":
            call OtherPronounSetter
            jump ParkingLot
# ^ Doesn't need tweaking
label OtherPronounSetter:
    $pronounsSub = renpy.input("please enter your subject pronouns (he, she, they, etc.)",default=u'', allow=None, exclude=None, length=None, with_none=None, pixel_width=None, screen=u'input', mask=None)
    $pronounsObj = renpy.input("please enter your object pronouns (him, her, them, etc.)",default=u'', allow=None, exclude=None, length=None, with_none=None, pixel_width=None, screen=u'input', mask=None)
    $adjPos = renpy.input("please enter your possesive adjectives (his, her, their, etc.)",default=u'', allow=None, exclude=None, length=None, with_none=None, pixel_width=None, screen=u'input', mask=None)
    $pronounsPos = renpy.input("please enter your possesive pronouns (his, hers, theirs, etc.)",default=u'', allow=None, exclude=None, length=None, with_none=None, pixel_width=None, screen=u'input', mask=None)
    jump ParkingLot
# ^ Doesn't need tweaking
label ParkingLot:
    scene sammamish

    "It's my first time at a FIRST event, I wonder what teams are competing today"
    "*Thud*"
    show hidden placeholder
    with dissolve
    "unknown""Hey, watch where you're going!"
    menu:
        "Sorry, I didn't see you there":
            "unknown""Just keep an eye out, okay? It can get pretty dangerous here."
            hide hidden placeholder
            show placeholder mascot
            with dissolve
            "By the way, my name is , feel free to come say hi in the pits if you have a moment."
            hide placeholder mascot
        "Why don't you watch where YOU'RE going!":
            "unknown""Oh, so that’s how it’s going to be? Watch your step, don’t want you hitting our robot."
            hide hidden placeholder
            show placeholder mascot
            with dissolve
            "My name’s , let's hope our next encounter goes better."
            hide placeholder mascot


            "There you are!"

    "Teammate""Everyone's looking for you, let's head down to the pits"

label PitsIntro:
    "Teammate""Hey everyone, I found [pronounsObj]!"
    "Teammate 2""Great"
    "name""We were almost worried that you got lost or something"

label mascotfair:
    A "Attention, the mascot fair will start momentarily"


    menu:
        "Look around the school":
            "The FIRST event splits the school into several sections"
            "The Pits are located in the main area, this is where teams can work on their bots"
            "The Field and Stands are in the main gym, these are where robots compete"
            "Items,food, and drinks are all sold at the Concession stand"
            "The outside area is where you can socialize and eat lunch"
            "Finally the quiet room is accessed by the pause button, this is where you can chill without affecting the time"



label bordOurple:
    show bord at left
    b "Why he ourple?"
    menu:
        "buy roober":
            b "thank you for your purchase"
            $ inv.append("roobeer")
            $ bordAffectionMeter += 1
            b "you have [inv[0]]"
            b "meter is [bordAffectionMeter]"
        "no":
            b "oh"

    return

#Credits settings (use call credits to show credits)
label credits:
    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(1)
    hide theend
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(1)
    hide thanks
    return
#Credits wording
init python:
    credits = ('Writing', 'Alexy' ),('Writing', 'MJ' ), ('Backgrounds', 'Dorktwerp'), ('Sprites and CG', 'Ballclown'), ('GUI', 'Cuddlywad') , ('Programming', 'Alexy'), ('Music', 'Grumblemuck'), ('Music', 'Headwookum')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n7.4.11.2266" #Don't forget to set this to your Ren'py version
#fonts and special stuff
init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The End", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing our Game!", text_align=0.5)












return
