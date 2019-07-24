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
define resetti = Character("Mr.Resetti")
define tom = Character("Tom Nook")
define hazel = Character("Hazel")
define doctor = Character("Doctor")
default searchedbody = False
default searcheddesk = False
default searchedTrash = False
default talkedisabelle = False
default talkedresetti = False
#Evidence

default hasBody = False
default hasDeath = False
default hasAlmond = False
default hasNote = False
default hasRole = False
default hasPamphelet = False
default hasReceipt = False
default hasThankYou = False
default hasDoctor = False
default hasEpipen = False
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
    return

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
            "Waste Basket" if not searchedTrash:
                $ searchedTrash = True
                player "Urg, I hate this part of the job."
                #play sound
                player "Huh, whats this?"
                #show note
                player "Looks like a doctor's note... But I can't read this."
                "{i}{b}Illegible doctor's note{/b} is recorded in your notebook{/i}"
                jump investigation
            "Talk to Isabelle" if not talkedisabelle:
                $ talkedisabelle = True
                isabelle "I cannot believe this..."
                jump isabelleinvest
            "Talk to Mr.Resetti" if not talkedresetti:
                resetti "Urg... what a mess"
                jump resettiinvest
    jump endofscene1
    #jump finishedoffice
    return

label body:
    $ searchedbody = True
    "You approch the body and begin your examination."
    player "Hmmm, strange. I don't see any injuries on the body."
    "{i}{b}Victim's Body {/b} is recorded in your notebook{/i}"
    $ player "I should note everything in my notebook and take a picture for evidence."
    $ hasBody = True
    "You put your face closer to the corpse, trying to get a closer look."
    player "Sniff, Sniff. What's that smell in his mouth? Is that... almonds?"
    "You realize the smell also originate from a muffin, next to the mayor, half eaten."
    "{i}{b}Smell of almonds{/b} is recorded in your notebook{/i}"
    $ hasAlmond = True
    player "Interesting..."
    jump investigation
    return

label desk:
    $ searcheddesk = True
    player "Hmm, what's this basket on the desk?"
    show basket
    isabelle "Oh, that was a gift the mayor got for his birthday. I think he received it during his last meeting."
    "You take a closer look at the basket, it is filled with muffins, fruits and chocolate."
    player "Interesting."
    "You notice a note on the basket."
    #show note
    "{i}{b} Basket note{/b} is recorded in your notebook{/i}"
    $ hasNote = True
    player "I should probabaly also check the drawers."
    "{i} Raddle Raddle {/i}"
    player "Huh locked."
    player "Hey Mr. Resetti, do you have a key for this?"
    resetti "SOrry man, I didn't bring that desk in, so i don't have the key, only the mayor has it."
    jump investigation
    return

default askedSchedule = False
default askedIsabelleEnnemy = False

label isabelleinvest:
    if not askedSchedule or not askedIsabelleEnnemy:
        menu:
            "Who did the mayor met with today?" if not askedSchedule:
                $ askedSchedule = True
                isabelle "Well, I do not have his meetings memorized, but I do have a list of it."
                jump isabelleinvest
            "Did the mayor have any ennemies?" if not askedIsabelleEnnemy:
                $ askedIsabelleEnnemy = True
                isabelle "Oh heavens no, the mayor is very popular."
                isabelle "In fact, he is always actively involved with the community. Every body loves him."
                player "Well, he is a mayor, doesn't that mean he has to be the bad guy at times? Like firing staff or denying legislation?"
                isabelle "Well, since mayor is always trying to please everyone, he doesn't enjoy bringing bad news."
                player "So who does then?"
                isabelle "That would be me... I'm in charge of everything the mayor does not want to handle."
                player "I see, thank you for your time."
                "{i}{b}Role of Isabelle{/b} is recorded in your notebook{/i}"
                $ hasRole = True
                jump isabelleinvest
    jump investigation
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


default talkedHazel = False
default checkedHospital = False
default currentHospital = False
default checkedShop = False
default currentShop = False 
label choicemenu:
    if checkedHospital and checkedShop and talkedHazel and hasReceipt:
        menu:
            "Where should I go next?"

            "Go to Tom Nook's shop" if not currentShop:
                jump nookShop

            "Go to the hospital" if not currentHospital:
                jump hospital

            "Go talk to Hazel" if not talkedHazel:
                jump hazelpicnic
    else:
        player "Well, I think that is all the evidences I am going to get."
        player "I should probably head back to the crime scene."
        jump officeagain
        
    
    return


# scene two
label nookShop:
    if checkedShop:
        "You enter the shop again, the scent of almond still overwhelming."
        player "Hey Tom, you there? I need to talk with you again."
        tom "Coming!"
        #show nook
        tom "What did you need?"
        jump nookmenu
    else:
        jump nookShopinitial

label nookShopinitial:
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
    player "My name is Detective [name], I'm in charge o fthe ongoing investigation for the Mayor's death."
    tom "THE MAYOR DIED?!?!"
    tom "I can't believe it... I just saw him this morning too..."
    player "I just need to ask you a few questions, if you don't mind."
    tom "Sure..."
    jump nookmenu
    return
default chosenEvidence = 0
label nookmenu:
    menu:
        "What is that smell?":
            tom "Oh, I'm making some new products in the back, starting my own clothes line."
            menu:
                "What are you using to make the clothes?":
                    tom "Oh... well, you know, some chemicals, nothing wild."
                "I know what this smell is! (present evidence)":
                    jump evidencemenu
                    if chosenEvidence == 5:
                        player "{i}Ah, I know what smell this is, the pamphelet mentioned it{/i}"
                        player "Are you using cyanide?"
                        tom "Wha- How did you know?!?"
                        tom "Truth be told, I am using it. It's a dangerous substance, so I didnt tell people about it."
                        tom "BUT don't worry! I'm using it very carefully, so the fumes aren't poisonous, you don't need to worry!"
                        "{i}{b}Tom uses cyanide{/b} is recorded in your notebook.{/i}"
                        $ hascyanide = True
                    else:
                        tom "Um... Im'm not sure how I can help you with that."
                        player "{i}I don't think this evidence applies here{/i}"
            jump nookmenu
        "Why did you go see the mayor this morning?":
            tom "Oh, well, it's been 18 years since he's been living in this town, so I gave him a token of my appreciation."
            player "What was it?"
            tom "Well, I can't really tell you what the gift was. It's a secret."
            giftproof1
            

        "Goodbye.":
            player "Thank you for your time"
            $ currentHospital = False
            $ checkedShop = True
            $ currentShop = True 
            jump choicemenu

label giftproof1:
     menu:
        "{i}Do I have any proof of Tom's gift?{/i}"
        "Yes":
            jump evidencemenu
            if chosenEvidence == 3:
                player "You gave the mayor a gift basket with muffins didn't you?"
                tom "I don't know what you are talking about."
                player "QUIT LYING! I HAVE A NOTE RIGHT HERE! The basket came from you!"
                tom "What? This isnt mine!"
                player "Well, how do you explain the note?"
                tom "I swear to god, I don't know where it came from. Plus, it's not like it matters! How does the gift basket plays in the mayor's death?"
                jump giftproof2
            else:
                tom "Um... what is that?"
                player "Sorry, wrong item."
                jump giftproof1

        "No":
            player "{i}I need to gather more evidence to pursue this line of questioning.{/i}"
            player "I understand."
            jump nookmenu

label giftproof2:
    player "{i}I do have proof the basket are linked to the mayor's death. I'll present it now!{/i}"
    jump evidencemenu
    if chosenEvidence == 2:
        player "A half-eaten muffin from the gift basket was found next to the body!"
        player "Plus, his breath clearly smelled of almonds, the same smell from the muffin!"
        tom "SO?! HOW DOES A MUFFIN KILL SOMEONE! DON'T JUST ACCUSE ME OF SH#T!"
        jump giftproof3
    else:
        tom "How does this link the basket to the death?"
        player "Sorry, wrong item."
        jump giftproof2
    return

label giftproof3:
     menu:
        "{i}Do I have any proof that the muffin killed the mayor?{/i}"
        "Yes":
            jump evidencemenu
            if chosenEvidence == 13:
                player "The cyanide."
                tom "Pardon me?"
                player "The muffin had an almond smell to it, much like the rest of this room... and the muffin."
                player "Cyanide produce a smell very similar to almonds and is a lethal poison when injested... making it a perfect murder weapon."
                tom "What are you trying to say?"
                player "I think you know very well what i'm tring to say."
                player "I am accusing you of givig poisonned muffin to the mayor!"
                tom "Look, I swear, I didn't give the mayor the gift basket!"
                player "The evidence doesn't lie! unless you can prove to me you didn't give the basket, I'm arresting you for murder."
                tom "Fine... I'll give you proof."
                tom "I didn't want to do this, to save the mayor's reputation, but I don't have a choice at this point."
                "From the pocket of his apron, Tom pulled out a piece of paper."
                #show paper
                player "What is this?"
                tom "A settlement contract."
                player "What?"
                tom "It's basically just a contract whihc nullifies the debt of the mayor."
                player "Wait, the mayor owed you money?!"
                tom "Quite a bit too, he never managed to pay it off. It was his biggest shame."
                tom "However, overtime, I saw how much his presence benifited the community, so I decided to nullify his debt, as a gitf to him."
                tom "You see? Signed by me and him, this morning. I did not give him the dumb basket!"
                "{i}{b}Tom's Contract{/b} is recorded in your notebook.{/i}"
                $ hasReceipt = True
                player "I see, thank you for the information"
                jump nookmenu
            else:
                tom "Um... what is that?"
                player "Sorry, wrong item."
                jump giftproof3

        "No":
            player "{i}I need to gather more evidence to pursue this line of questioning.{/i}"
            player "I understand."
            jump nookmenu
#scene 3
label hospital:
    if checkedHospital:
        "raddle" "Oh you're back."
        player "yeah, I wanted to talk to you more."
        jump doctorchoices
    else:
        jump hospitalinitial
    
label hospitalinitial:
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
    player "Anyways, Raddle, I am Detective [name] and I need to ask you a few questions on an ongoing investigation."
    "Raddle" "Oh my goodness. What happened?"
    player "The mayor passed away this morning."
    "Raddle" "Good god... Unbelievable..."
    player "So for my investigation, I need you to cooperate with me."
    "Raddle" "Oh, of course detective, how may I help?"
    jump doctorchoices
    return

default askedMayorRaddle = False
label doctorchoices:
    menu:
        "Does the mayor comes here often?" if not askedMayorRaddle:
            askedMayorRaddle = True
            "Raddle" "Well, not more than usual. The last time I saw him for for his yearly check-up a few weeks ago."
            player "Oh, was there anything unusual about him?"
            "Raddle" "Sorry, but I cannot divulge that information. Client confidentiality."
            "Raddle" "I will say that the mayor sure is a scatter brain."
            player "What do you mean?"
            "Raddle" "You see, the very next day after his appointment, he already lost his doctor's note for a prescription. So i had to fax a new copy to his assistant."
            "{i}{b}Faxed Doctor Notes{/b} is recorded in your notebook.{/i}"
            jump doctorchoices
        "Can I ask your opinion on this evidence?":
            jump evidencemenu
            if chosenEvidence == 0:
                player "I found the body of the president and I was wondering if you could help me determine the cause of death."
                player "Here's a picture of the body."
                "Raddle" "Hmm, well, from what i can see here, the mayor seemed to have died from lack of oxygen."
                player "Really?"
                "Raddle" "Yeah. I cant really see well because of the picture quality, but the skin's tint is a bit blue, sign of oxygen deprivation."
                "Raddle" "Tho, I don't really see any bruises on the neck area, making me believe that he wasnt starngled, rather, something caused him to asphyxiate"
                player "I see."
                "{i}{b}Victim's Body{/b} is updated to {b}Cause of death{/b} in your notebook.{/i}"
                $ hasBody = False
                $ hasDeath = True
            elif chosenEvidence == 9:
                player "Can you take a look at this doctor note?"
                "Raddle" "Sure"
                "Raddle" "Oh boy... I can read any of these."
                player "... didn't you write it?"
                "Raddle" "Yeah... about that, sometime I come to work in a... sub-optimal state."
                "Raddle" "That, coupled wth my bad handwriting... makes it that even I cant read my own headwritins at times."
                "Raddle" "It's never been a problem so far becasuethe local phramacist was always able to read it."
                "Raddle" "Plus, the mayor's handwriting is as bad as mine, so he can his assistant were always able to read my writing."
            else:
                "Raddle" "Sorry, I don't know anything about that."
            jump doctorchoices
        "Goodbye":
            $ currentHospital = True
            $ checkedHospital = True
            $ currentShop = False 
            jump choicemenu
            
label hazelpicnic:
    "You walk toward the address Isabelle gave you for Hazel."
    "{i}Knock Knock{/i}"
    "The door opens and a homanoid squirrel comes out."
    "???" "Hello, may I help you?"
    player "Good morning ma'am, I'm Detective [name] and I'm here to talk with Hazel."
    hazel "That would be me."
    player "Hello Ms.Hazel. I would just like to ask you a few questions, if you don't mind."
    hazel "Um... sure, please go ahead."
    player "What is your relationship with the mayor?":
    hazel "We are... really good friends."
    "You notice a blush on Hazel's cheeks"
    hazel "We meet up almost everyday at the park to eat lunch together!"
    player "Oh that's lovely, did you meet him today as well?"
    hazel "Not yet, but we did have lunch plans, so I was making my lunch right now."
    hazel "I love making food and cooking. In fact, I suggested on many occasions to make the mayor's lunch."
    player "I'm sure the mayor appreciated that, it should save him time to make food."
    hazel "Actually, he never took me up on my offer. For some reason, he always kept his food away from mine."
    hazel "He won't even taste my famous nut muffins."
    hazel "I don't know why though, even Isabelle likes them."
    player "Really?"
    hazel "Yeah, she even asked me to show her the recipe a while back. We had a fun day cooking."
    hazel "She even sent me a thank you note."
    #show note
    $ hasThankYou = True
    hazel "Um, if you don't mind, Detective, can I ask you a question of my own."
    player "Sure, no problem."
    hazel "Why are you questionning me? Did something happen?"
    player "..."
    hazel "Detective?"
    player "I'm sorry... But the mayor was found dead this morning in this office."
    hazel "Oh no... Mayor..."
    "Hazel falls to her knees, collapsing in tears."
    hazel "C-can you tell me what happened to him?"
    player "He died in his office, we don't know what happened to him, so I'm investigating it."
    player "I'm sorry to be the bearer of bad news, but I needed to gather information for the investigation."
    hazel "Actually, I might have something that may help you."
    "Hazel gets a key out from her pocket."
    hazel "The mayor gave me this... he said it would be useful one day. Maybe it could help you in your investigation."
    player "Thank you very much. I really appreciate your help."
    hazel "No need to thank me, just promise me: please find oyt what happened to him... please."
    player "I will try my best hazel, trust me."
    hazel "Thank you... Now if you could excuse me, I need time alone."
    "The door closes and you could hear lund weeping from the other side."
    jump choicemenu
    $ talkedHazel = True
    $ currentHospital = True
    $ currentShop = False 
    return

label officeagain:
    "You walk back to the crime scene."
    player "Now that I have the key, I should check out that locked drawer."
    "You opened the drawer and found some things."
    #show epipen
    player "This is weird, why in the world would he lock this?"
    player "Oh, it seems like this was already used."
    player "I wonder why he didn't just throw it away."
    player "There some more stuff."
    #show picture
    player "Awn, a picture of the mayor and hazel, they look happy."
    player "Wonder what's in this box"
    #show ring 
    player "Oh my... this seems very expensive."
    "???" "So, any progress?"
    player "AH!"
    isabelle "What's wrong?"
    player "Nothing... You just suprised me."
    isabelle "Do you have any update on the situation?"
    player "I was still investigati-"
    isabelle "Well, it's okay, I think there's no need to continue it."
    player "Excuse me?"
    isabelle " I've been doing a little bit of investigation myself, and I think it's pretty obvous who the killer is."
    player "Is it now?"
    isabelle "Oh c'mon! It's so obvious! It's that crook Tom Nook!"
    player "What makes you say that?"
    isabelle "You're kidding right? The mayor's breath smell like almond, Tom owns Cyanide, Tom gave the mayor the almond-scented muffin."\
    isabelle "He sooo obviously the killer, let's go arrest him right now."
    menu:
        "Yeah, let's go.":
            player "{i} Wait, I don't think that's correct, I need to correct her {/i}"
            jump next2
        "I don't think so.":
            jump next2
    return

label next2:
    player "I talked with Tom and I don't think he's the killer."
    isabelle "Excuse me?"
    player "He told me he never gave the gift basket. The gift he did give was something else."
    isabelle "Oh cmon detective, you dont honestly belive that right? He was definitely lying!"
    menu:
        "Yeah you're right, let's go arrest the bastard":
            player  "{i} Wait, that can't be right, Tom gave me proof of his real gift {/i}"
            jump next3
        "I do believe Tom":
            jump next3
    return

label next3:
    player "I believe Tom's words."
    isabelle "What? How? Do you have any proof?"
    player "I do."
    jump next4
    return

label next4:
    jump evidencemenu
    if chosenEvidence == 6:
        player "He did not give a gift basket, he gave the mayor this."
        isabelle "What's this?"
        player "A debt nullification contract. He made all of the mayor's debts null."
        isabelle "SO? he could have given two gifts!"
        player "That's impossible, and I have proof of it"
        jump next5
    else:
        isabelle "What's that?"
        player "Whoops, sorry wrong item."
    return

label next5:
    jump evidencemenu
    if chosenEvidence == 6 or chosenEvidence == 3:
        player "Take a look at the signature."
        isabelle "Yeah, I saw that, both were signed by him. Doesn't that support my argument?"
        player "Just take a closer look to the signatures."
        isabelle "AH! The handwritings..."
        player "Exactly, the handwriting are differengt on both papers."
        isabelle "What does that mean?"
        player "I think that means someone as trying to frame our good local merchant."
        isabelle "Oh my, if only there was a way to figure out who wrote the basket note"
        player "Actually, I think we can."
        jump next6
    else:
        isabelle "What's that?"
        player "Whoops, sorry wrong item."
    return

label next6:
    jump evidencemenu
     jump evidencemenu
    if chosenEvidence == 7:
        player "Isabelle. You spent some time with Hazel recently haven't you?"
        isabelle "Oh, yes, we spend a day baking."
        player "I see, well, it seems you also sent her a thank you note."
        iabelle "Of course, it is good manners after all!"
        player "Well then, can you please explain why your signature on the thank you note is IDENTICAL to the one on the goft basket"
        isabelle "AH!"
        player "You were the one that gave the poisoned muffins to the myor wasn't it?"
        player "You tried to frame Tom Nook because you knew he brought a gift for the mayor!"
        isabelle "NO! you're wrong!"
        isabelle "The mayor died from the cyanide! remember? Only Tom had access to it! How could I have killed him?"
        jump next7
    else:
        isabelle "How does that help us?"
        player "Whoops, sorry wrong evidence."
    return

label next7:
    jump evidencemenu
    if chosenEvidence == 10:
        player "Who said the mayor was killed by cyanide?"
        isabelle "Huh?"
        player "I'm asking you, why do you think the mayor died from cyanide?"
        isabelle "Well, obviously the almond scent."
        "You walk toward the muffins and pick one up."
        player "You're talking about these \"poisoned\" muffins?"
        isabelle "Um, you should not touch tha-"
        "You take a bite from the muffin."
        isabelle "WAIT NO!"
        player "Miam, delicious, the almonds REALLY brings out the flavors."
        player "Sadly, I taste no cyanide..."
        isabelle "Oh... Looks like you were lucky there... the killer probabky only poisoned one of them..."
        player "Mmmm, I have a different theory."
        "You pull out the epipen from your pockets."
        player "I think these are just normal muffin, but they kiolled the mayor due to his deadly nuts allergies."
        isabelle "The mayor had nuts allergies? Who would have known?"
        player "Exactly! The mayor kept it pretty under wraps. Only him and his doctor would know."
        player "Except... according to the doctor, they called the mayor's office with his allergy results and you were the one who picked up."
        player "Meaning, you, Isabelle, also knows."
        isabelle "Wha- No, it.. I never got a call! I don't get calls!"
        player "Admit it! you found out about the mayor's allergies, had Hazel teach you a nut muffin recipe, gave it to the mayor and tied to frame Tom."
        player "YOU, ISABELLE, ARE THE KILLER!"
        isabelle "I...I'm sorry....."
        isabelle "I... I JUST COULDN'T TAKE IT ANYMORE!"
        isabelle "The mayor is never here and I walways have to deal with his mess!"
        isabelle "I alwysy have to do all of his work! And I am never appreciated!"
        isabelle "He gets love from the communityfor the work I do! All he ever does is slack off!"
        isabelle "I-I just couldn't take it anymore..."
        player "Save it for the court, sweetie."
        "And so, Isabelle was sentenced to 15 years in prison, and the town elected a new mayor: Tom Nook."
        "The End"
        return
    else:
        isabelle "How does that help us?"
        player "Whoops, sorry wrong evidence."
    return






label evidencemenu:
    $ chosenEvidence = 0
    menu:
        "What evidence should I present?"
        "Victim's Body" if hasBody:
            $ chosenEvidence = 0
        "Cause of death" if hasDeath:
            $ chosenEvidence = 1
        "Smell of almonds on mouth and muffin" if hasAlmond:
            $ chosenEvidence = 2
        "Note of the basket" if hasNote:
            $ chosenEvidence = 3
        "Role of Isabelle" if hasRole:
            $ chosenEvidence = 4
        "Pamphelet" if hasPamphelet:
            $ chosenEvidence = 5
        "Tom Nook's contract" if hasReceipt:
            $ chosenEvidence = 6
        "Isabelle's Thank you note" if hasThankYou:
            $ chosenEvidence = 7
        "Doctor's note" if hasDoctor:
            $ chosenEvidence = 9
        "Epipen" if hasEpipen:
            $ chosenEvidence = 10
        "Cyanide" if hascyanide:
            $ chosenEvidence = 13
    return
