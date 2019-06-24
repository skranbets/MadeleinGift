# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define isabelle = Character("Isabelle")
define kitty = Character("Kitty")
define resetti = Character("Mr.Resetti")
define tom = Character("Tom Nook")
define hazel = Character("Hazel")
define doctor = Character("Doctor")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene frontdesk

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show isabellehappy


    # These display lines of dialogue.

    isabelle "Hello there, Welcome to our town! You are here for your meeting with the mayor right?"

    isabelle "Can I please get the name for the meeting?"
    python:
        name = renpy.input("Please enter your name")
    define player = Character("[name]")
    isabelle "Okay, [name]... Oh yes, I see you on the list. You can head right in, the mayor is waiting for you"
    "You walk to the mayor's office and you knock on the door"
    "Knock Knock"
    
    hide isabelle
    # This ends the game.

    return
