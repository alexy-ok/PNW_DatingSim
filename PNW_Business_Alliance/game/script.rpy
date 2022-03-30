# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Bord")
define p = Character("Peng")

# The game starts here.

label start:
    $ inv = []
    $ bordAffectionMeter = 0
    $ pengAffectionMeter = 0
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene sammamish

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show bord at left
    show peng ourple at right
    # These display lines of dialogue.

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
    # This ends the game.

    return
