# name of the character.

define Ann = Character("Announcer")
define 948 = Character("Sparky")
define 3786 = Character("Charlie")
define 6696 = Character("Corbin")
default pronounsSub = ""
default pronounsPos = ""
default pronounsObj = ""
default adjPos = ""

# The game starts here.

label start:
    $ inv = []
    $ bordAffectionMeter = 0
    $ pengAffectionMeter = 0
    $ goneToPits = false
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
    "???""Hey, watch where you're going!"
    menu:
        "Sorry, I didn't see you there":
            "???""Just keep an eye out, okay? It can get pretty dangerous here."
            hide hidden placeholder
            show placeholder mascot
            with dissolve
            "By the way, my name is , feel free to come say hi in the pits if you have a moment."
            hide placeholder mascot
        "Why don't you watch where YOU'RE going!":
            "???""Oh, so that’s how it’s going to be? Watch your step, don’t want you hitting our robot."
            hide hidden placeholder
            show placeholder mascot
            with dissolve
            "My name’s , let's hope our next encounter goes better."
            hide placeholder mascot


            "There you are!"

    "Teammate""Everyone's looking for you, let's head down to the pits"
    jump PitsIntro

label PitsIntro:
    "Teammate""Hey everyone, I found [pronounsObj]!"
    "Teammate 2""Great"
    "name""We were almost worried that you got lost or something"
label PitsMenu:

    if goneToPits = false:
        "As you walk around the busy area, you spot different teams' booths"
        "Where do you want to go?"
        goneToPits = true
        menu:
            "Your pit":
                jump homePit
            "NRG 948":
                jump NRGPit
            "Saints 1899":
                jump SaintsPit
            "Flying Hedgehogs 2989":
                jump FlyingPit
            "Chargers 3786":
                jump ChargersPit
            "Cardinal Dynamics 6696":
                jump CardinalPit
            "Sushi Squad 7461":
                jump SushiPit
    elif:
        "Where do you want to go?"
        menu:
            "Your pit":
                jump homePit
            "NRG 948":
                jump NRGPit
            "Saints 1899":
                jump SaintsPit
            "Flying Hedgehogs 2989":
                jump FlyingPit
            "Chargers 3786":
                jump ChargersPit
            "Cardinal Dynamics 6696":
                jump CardinalPit
            "Sushi Squad 7461":
                jump SushiPit
            "Exit Pits"
                jump LocationSelector
label homePit:
label NRGPit:
label SaintsPit:
label FlyingPit:
label ChargersPit:
label CardinalPit:
label SushiPit:
label LocationSelector
#idk if we're using this tbh
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
    credits = ('Writing', '' ),('Writing', '' ), ('Backgrounds', ''), ('Sprites and CG', ''), ('GUI', '') , ('Programming', ''), ('Music', ''), ('Music', '')
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
