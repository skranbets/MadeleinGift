# The script of the game goes in this file.
#python:
#    class DeskInvestigation:
#       def __init__(self):
#            self.searchedbody = False
#            self.searcheddesk = False
#            self.talkedisabelle = False
#            self.talkedresetti = False

#       def isFinished(self):
#           return self.searchedbody and self.searcheddesk and self.talkedisabelle and self.talkedresetti


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define isabelle = Character("Isabelle")
define kitty = Character("Kitty")
define resetti = Character("Mr.Resetti")
define tom = Character("Tom Nook")
define hazel = Character("Hazel")
define doctor = Character("Doctor")
default searchedbody = False
default searcheddesk = False
#Evidence
default talkedisabelle = False
default talkedresetti = False
default hasDeath = False
default hasAlmond = False
default hasNote = False
default hasRole = False
default hasPamphelet = False
default hasReceipt = False
default hasThankYou = False
default hasDebt = False
default hasDoctor = False
default hasEpipen = False
default hasLunch = False
default hasRing = False
default hascyanide = False
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene frontdesk  with Dissolve(.5)
    pause .5

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
    isabelle "Okay, [name]... Oh yes, I see you on the list. You can head right in, the mayor is waiting for you."
    hide isabellehappy
    "{i}You walk to the mayor's office and you knock on the door{/i}"
    "Knock Knock Knock"
    #play sound "knock.mp3"
    "..."
    "Knock Knock Knock"
    #play sound "knock.mp3"
    "..."
    player "Um... He isn't answering."
    show worriedisabelle
    isabelle "Really? That's weird, lemme try."
    "Knock Knock Knock"
    #play sound "knock.mp3"
    isabelle "Mayor? Your 10'o clock is here!"
    "..."
    isabelle "That's weird... Well, let's just go in and see what's up, maybe he fell asleep."
    "{i}Click clang{/i}"
    #play sound "trying to open a locked door"
    
    isabelle "it's locked... well, good thing Mr.Resetti has the key. Let me call him."
    hide worriedisabelle
    #play sound "phone sound"
    "After a few minutes, Mr. Resetti came."
    show resettiangry
    resetti "So the dummy locked himself in the office again? God, I should just get rid of that lock, make thing easier."
    isabelle "I'm sorry, Mr.Resetti, may you please open the door."
    resetti "Fine."
    "{i}Click{/i}"
    #play sound "trying to open a locked door"
    scene office with Dissolve(.5)
    pause .5

    isabelle "MAYOR!!!!!" 
    menu: 
        resetti "Jesus christ... is.. is he dead?"
        "I think he is...":
            jump next

        "Nah, he's just sleeping.":
            jump joke

label joke:
    isabelle "WHAT IS WRONG WITH YOU! HOW CAN YOU JOKE AT A TIME LIKE THIS."
    resetti "Pretty sure he is dead."
    jump next
    return

label next:
    isabelle "Poor mayor... How could this happen."
    player "We need to investigate what happened here. Everyone please stay away from the body."
    jump investigation
    return

label investigation:
    if not searchedbody or not searcheddesk or not talkedisabelle or not talkedresetti:
        menu:
            "What should I investigate?"
            
            "Body" if not searchedbody:
                jump body
            "Desk" if not searcheddesk:
                jump desk
            "Waste Basket" if not searchedTrash
            "Talk to Isabelle" if not talkedisabelle:
                $ talkedisabelle = True
                isabelle "I cannot believe this..."
                jump isabelleinvest
            "Talk to Mr.Resetti" if not talkedresetti:
                resetti "Urg... what a mess"
                jump resettiinvest
    #jump finishedoffice
    return

label body:
    $ searchedbody = True
    "You approch the body and notice several things:"
    "1) The victim appear to have died from asphyxiation"
	"{i}{b}Cause of death {\b} is recorded in your notebook{/i}"
	$ hasDeath = True
    "2) There is a smell of almonds near the victim's mouth"
    "3) That same almond smell is on a muffin, next to the mayor, half eaten"
	"{i}{b}Smell of almonds{\b} is recorded in your notebook{/i}"
	$ hasAlmond = True
    jump investigation
    return

label desk:
    $ searcheddesk = True
    player "Hmm, what's this basket on the desk?"
    show basket
    isabelle "Oh, that was a gift the mayor got for his birthday. I think he received it during his last meeting."
    player "Interesting."
	"You notice a note on the basket."
	#show note
	"{i}{b} Basket note{\b} is recorded in your notebook{/i}"
	$ hasNote = True
	return

default askedSchedule = False
default askedIsabelleEnnemy = False

label isabelleinvest:
	if not askedSchedule or not askedIsabelleEnnemy:
	    menu:
		    "Who did the mayor met with today?" is not askedSchedule:
			    $ askedSchedule = True
				isabelle "Well, I do not have his meetings memorized, but I do have a list of it."
				jump isabelleinvest
			"Did the mayor have any ennemies?" is not askedIsabelleEnnemy:
			    $ askedIsabelleEnnemy = True
				isabelle "Oh heavens no, the mayor is very popular."
				isabelle "In fact, he is always actively involved with the community. Every body loves him."
				player "Well, he is a mayor, doesn't that mean he has to be the bad guy at times? Like firing staff or denying legislation?"
				isabelle "Well, since mayor is always trying to please everyone, he doesn't enjoy bringing bad news."
				player "So who does then?"
				isabelle "That would be me... I'm in charge of everything the mayor does not want to handle."
				player "I see, thank you for your time."
	            "{i}{b}Role of Isabelle{\b} is recorded in your notebook{/i}"
				$ hasRole = True
				jump isabelleinvest
	jump endofscene1
	return



label resettiinvest:
    player "This is a true tragedy."
	resetti "Yeah... I feel really bad about my comment now."
	player "About that, does the mayor lock himself in his office a lot?"
	resetti "Not exactly, he rarely locks himself in, but he does lock the doors when he isn't supposed to."
	player "What do you mean?"
	resetti "Look, between us two, the mayor isn't exactly your model employee."
	resetti "More often than not, the guy leaves halfway through the day and leaves everything to the secretary."
	resetti "However, he alwasy locks his office and since he's the only one with the key, that leaves poor Isabelle locked out."
	resetti "And since she needs some documents in the office, she calls me to unlock the office, it's become a routine at this point."
	player "Ahh, I see what you mean. I now understand your frustration."
	player "Thank you for your time"
	jump endofscene1
	return

label endofscene1:
    isabelle "Excuse me Detective [name], but have you reached a conclusion yet?"
	player "It's a bit early for me to pass judgement right now, I think I need to follow up a few more leads."
	jump choicemenu
	return


default currentKitty = False
default currentHazel = False
default currentHospital = False
default currentShop = False 
label choicemenu:
    
    menu:
		"Where should I go next?"

	    "Go to Tom Nook's shop" if not currentShop:
		jump nookShop

	    "Go to the hospital" if not currentHospital:
		jump hospital

		"Go talk to Hazel" if not currentHazel:
		jump hazelpicnic

		"Go talk to Kitty" if not currentKitty:
		jump kitty
	return


# scene two
label nookShop:
    #new sceneries
	#tom nook enters
	"As you enters the shop, a strong scent of almonds assualts your senses."
	"The shop is empty, no traces of any customer nor shopkeepers."
	player "Hello? Is anyone here?"
	"???" "Just a moment, be right there!"
	"From the backroom behind the counter, a tanuki appearsk, with a little blue apron."
	"???" "Sorry to keep you waiting. I was working in the back."
	"???" "Hmm. I never seen your face around here, you must be new around town."
	"???" "Lemme introduce myself, I'm Tom Nook, the local shopkeeper."
	player "Nice to meet you Tom."
	tom "So, what can I do for ya?"
	player "I just need to ask you a few questions, if you mind."
	tom "Sure, I have a little bit of time."
	jump nookmenu
	return

# default chosenDeath = False
# default chosenAlmond = False
# default chosenNote = False
# default chosenRole = False
# default chosenPamphelet = False
# default chosenReceipt = False
# default chosenThankYou = False
# default chosenDebt = False
# default chosenDoctor = False
# default chosenEpipen = False
# default chosenLunch = False
# default chosenRing = False
default chosenEvidence = 0
label nookmenu:
    menu:
	    "What is that smell?":
		    tom "Oh, I'm making some new products in the back, starting my own clothes line."
			menu:
			    "What are you using to make the clothes?":
				    tom "Oh... well, you know, some chemicals, nothing wild."
				"Present evidence":
				     jump evidencemenu
					 if chosenEvidence == 5:
					     player "{i}Ah, i know what smell this is, the pamphelet mentioned it{/i}"
					     player "Are you using cyanide?"
						 tom "Wha- How did you know?!?"
						 tom "Truth be told, I am using it. It's a dangerous substance, so I didnt tell people about it."
						 tom "BUT don't worry! I'm using it very carefully, so the fumes aren't poisonous, you don't need to worry!"
						 "{i}{b}Tom uses cyanide{\b} is recorded in your notebook.{/i}"
						 $ hascyanide = True
			jump nookmenu
		"Did you give the mayor a gift this morning?":
		    tom "I did! It's been 18 years since he's been living in this town, so I gave him a token of my appreciation."
			player "Was it a gift basket?"
			tom "Well, I can't really tell you what the gift was. It's a secret."
			menu:
			    "{i}Do I have any prrof of Tom's gift?{/i}"
				"Yes":
				    jump evidencemenu
					if chosenEvidence == 3:
						player ""
				"No":
				    player "I understand."
			jump nookmenu

		"Goodbye.":
		    player "Thank you for your time"
			$ currentKitty = False
            $ currentHazel = False
            $ currentHospital = False
            $ currentShop = True 
			jump choicemenu

#scene 3

label hospital:
    "Nurse" "Hi, please fill in this form with your personal information and the reason for your visit and the doctor will get to you shortly."
	"The nurse left quickly"
	player "Wait, I'm not - And she's gone... darnit."
	player "I guess I'll go to the receptionist."
	player "Hi, I need to talk to the doctor."
	"Receptionist" "Oh, no problem, here."
	#show form
	"Receptionist" "Please fill in this form with your personal information and the reason for your visit and the doctor wi-"
	player "Wait, no, I'm not here for a consultation, I'm not sick! I just wanna talk."
	"Receptionist" "Oh? Um... Ma'am, this is a hospital, we don't really do social events for the doctors."
	player "No, I am a detective, I'm currently investigating a crime and I need to speak with the doctor."
	"Receptionist" "Suuuuure... well, the doctor is going on his lunch break in a few minutes, so if you want, you can wait in the lobby, I'll tell him you're here"
	player "Okay."
	"As you are waiting, you pick up a pampthlet and start readin to pass the time."
	#show pampthlet
	#have pampthlet text here
	"???" "Hello detective? I heard you were looking for me."
	"You stopped reading and direct your attention to the voice."
	player "Ah, hello, you must be the doctor."
	"Doctor" "Yes, I'm the local town's doctor, Raddle, did you need anything?"
	player "Well, Dr.Raddle- "
	"Raddle" "Actually, just Raddle."
	player "Ah... okay"
	player "{i} Note to self, don't get sick here {/i}"
	player "Anyways, Raddle, I am Detective [name]"




label evidencemenu:
    $ chosenEvidence = 0
    menu:
	    "What evidence should I present?"
	    "Cause of death" if hasDeath:
		    $ chosenEvidence = 1
	    "Smell of almonds" if hasAlmond:
		    $ chosenEvidence = 2
	    "Note of the basket" if hasNote:
		    $ chosenEvidence = 3
	    "Role of Isabelle" if hasRole:
		    $ chosenEvidence = 4
	    "Pamphelet" if hasPamphelet:
		    $ chosenEvidence = 5
	    "Tom Nook's receipt" if hasReceipt:
		    $ chosenEvidence = 6
	    "Isabelle's Thank you note" if hasThankYou:
		    $ chosenEvidence = 7
	    "Kitty's testimony on the mayor's debt" if hasDebt:
		    $ chosenEvidence = 8
	    "Doctor's note" if hasDoctor:
		    $ chosenEvidence = 9
	    "Epipen" if hasEpipen:
		    $ chosenEvidence = 10
	    "Hazel's testimony" if hasLunch:
		    $ chosenEvidence = 11
	    "Ring" if hasRing:
		    $ chosenEvidence = 12
		"Cyanide" if hascyanide:
	        $ chosenEvidence = 13
	return
    # This ends the game.
return
    