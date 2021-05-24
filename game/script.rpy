# The script of the game goes in this file
image darkness = "#000000"
define CW = Character (' ', what_font="courbd.ttf",what_size=40,what_xalign=0.5,what_yalign=0.5,what_color="#ffffff",window_yalign=0.5,window_xalign=0.5,justify=True)
define e = Character("Morart")
image e 4 = Image("morart4.png", ypos=780)
image e 5 = Image("morart5.png", ypos=780)
image mat = Image("mat.png")
image flower = Image("flower.png")
image yellow = Image("yellow.png")
image trolltarot = Image("Tarot_2_B.png")

image mural = Image("Disciple - Mural.png")

#----
screen tarot:
    vbox xalign 1.0
    imagebutton:
        idle "Tarot_2_G.png"
        hover "Tarot_2_G.png"
        xpos 110
        ypos 100
        action Jump("tarot_selection")
        focus_mask True
    imagebutton:
        idle "Tarot_2_G.png"
        hover "Tarot_2_G.png"
        xpos 470
        ypos 100
        action Jump("tarot_selection")
        focus_mask True
    imagebutton:
        idle "Tarot_2_G.png"
        hover "Tarot_2_G.png"
        xpos 830
        ypos 100
        action Jump("tarot_selection")
        focus_mask True



label start:
    scene mat
    jump nvl_phone_example
    e "This is nice I guess..."
    call screen tarot
label tarot_selection:
    $ trolltarot = renpy.random.choice(['1', '2', '3','4','5'])

    if trolltarot == "1":
        jump hold
    elif trolltarot == "2":
        jump holder
    elif trolltarot == "3":
        jump holder2
    elif trolltarot == "4":
        jump holder3
    elif trolltarot == "5":
        jump holder4

label hold:
    scene mat with dissolve
    e "And your card is"
    show flower with dissolve
    e "This card is the Fool"
    return

label holder:
    scene mat
    e "And your card is"
    show yellow with dissolve
    e "This card is the Empress"
    e "Of course."
    return

label holder2:
    scene mat
    e "And your card is"
    show yellow with dissolve
    e "This card is the Sun"
    e "Of course."
    return

label holder3:
    scene mat
    e "And your card is"
    show yellow with dissolve
    e "This card is the Devil"
    e "Of course."
    return

label holder4:
    scene mat
    e "And your card is"
    show yellow with dissolve
    e "This card is the World"
    e "Of course."
    return
