
init python:
    class nvl_phone_class:
        def __init__(self):
            self.elapsed = 0
            self.typing = False
            self.times = []
            self.locked = False
            self.name = None
            self.person = None
        def tick(self):
            pass
            self.elapsed += 1
            if len(self.times):

                if self.elapsed >= self.times[0]:
                    self.elapsed = 0
                    if self.typing:
                        self.typing = False
                    else:
                        self.typing = True
                    self.times.pop(0)
            else:
                self.typing = False
                self.locked = False
                return 1
        def type(self, person, times = [10, 10, 10, 10]):
            self.person = person
            self.times = times
            self.elapsed = 0
            self.typing = True
            self.locked = True
            renpy.pause(hard = True)
        def abort_typing(self):
            self.times = []
            self.elapsed = 0
            self.typing = False
            self.locked = False
            return 1


screen nvl(dialogue, items=None):
    style_prefix "nvlphone"
    add "#0008"
    frame:
        xysize(1220,690) padding(0,0) background "#000" align .5,.5

        frame: # Top bar
            ysize 50 xfill True background "#6b00b9" yalign 0.0
            button:
                align 0.0,.5 background "#3a0064" xysize 40,40
                text "X"
                action Hide("chat_app_chat")
            text nvl_phone.name
        viewport:
            draggable True scrollbars None yinitial 1.0 align .5,1.0
            xfill False
            yfill False
            yalign 1.0
            ymaximum 519 yoffset -120
            vbox: # Chat
                xsize 1200 yalign 1.0
                spacing 12
                for n, d in enumerate(dialogue):

                    if d.who == "YOU":
                        hbox:
                            xalign 1.0
                            frame:
                                background Frame(im.Flip("phone/chat_frame_W.png", True), 8, 8, 16, 8)
                                padding 12,12,20,12 xmaximum 680 yminimum 64
                                text d.what:
                                    color "#000"

                            if not dialogue[n-1].who == d.who or n == 0:
                                add "phone {}".format(d.who)
                            else:
                                null width 64
                    elif d.who == None:
                        frame:
                            background None padding 20,40 xalign .5
                            text d.what:
                                color "#fff" size 20
                    elif d.who == "NVLIMAGE":
                        button:
                            xalign 0.0 padding 10,10 background "#3a0064" xoffset 64
                            add d.what at fit_zoom(image_fit(d.what, [300,2000]))
                            action Show("nvl_phone_image", img = d.what)
                    elif d.who == "nvl_img_send":
                        button:
                            xalign 1.0 padding 10,10 background "#3a0064" xoffset -64
                            add d.what at fit_zoom(image_fit(d.what, [300,2000]))
                            action Show("nvl_phone_image", img = d.what)
                    elif d.who == "NVLVOICE":
                        pass
                    else:
                        hbox:
                            xalign 0.0
                            if not dialogue[n-1].who == d.who or n == 0:
                                add "phone {}".format(d.who)
                            else:
                                null width 64
                            frame:
                                background Frame("phone/chat_frame.png", 16, 8, 8, 8)
                                padding 20,8,8,8 xmaximum 420 yminimum 64
                                text d.what:
                                    color "#aaa"
        text d.what: # Ignore
            id d.what_id
            yoffset -1000

        vbox: # Input
            yalign 1.0 spacing -8
            if nvl_phone.typing:
                hbox:
                    xalign 0.0 xoffset 18
                    text str(nvl_phone.person) size 16
                    text " is typing..." size 16

            frame:
                background "#3a0064" margin 20,20
                padding 8,8,16,8 xfill True yminimum 90
                text "Tap here to move on..." color "#aaa" xalign 0.0


        frame: # Choice
            align .5,.5 background "#3a0064" padding 0,0
            vbox:
                spacing 4
                for i in items:
                    button:
                        text i.caption
                        action i.action
                        background "#3a0064" yminimum 64 xsize 540 padding 10,10
    if nvl_phone.locked:

        # button: # While typing this button will keep the screen locked, comment out if you don't want it to be locked
        #     background None
        #     action NullAction()
        timer .1 repeat True action Function(nvl_phone.tick)

screen nvl_phone_image(img):
    modal True
    button:
        align .5,.5
        xysize 600,900 background "#444"
        action Hide("nvl_phone_image")
        add img at fit_zoom(image_fit(img, [580,880])) align .5,.5

style nvlphone_text:
    size 20
    align (.5,.5)


style nvlphone:
    align (.5,.5)

define config.nvl_list_length = 20 # The number of lines you can scroll back to see
# define config.nvl_adv_transition = None
# define config.adv_nvl_transition = None
define nvl_sys = Character(None, kind=nvl)
define nvl_img = Character("NVLIMAGE", kind=nvl)
define nvl_img_send = Character("NVLIMAGESEND", kind=nvl)
define nvl_voice = Character("NVLVOICE", kind=nvl)
define nvl_voice_send = Character("NVLVOICESEND", kind=nvl)
default phone_conversation_1 = nvl_phone_class()
default nvl_phone = phone_conversation_1

#-------------------------------------------------------------------- Modify below this line if you don't want to change the theme
# Define your nvl characters here, they must have `kind=nvl`
define YOU = Character("YOU", kind=nvl,what_font="courbd.ttf")
define TYp = Character("QuestionableAddendum", kind=nvl,what_font="courbd.ttf")
define may = Character("Mayo", kind=nvl,what_font="courbd.ttf")

# Define your portrait images, the name must be `phone` and the first tag must match the name of the characters defined above
image phone YOU = "phone/img2.png"
image phone QuestionableAddendum = "phone/img1.png"
image phone Mayo = "phone/mayo.png"


label nvl_phone_example:
    nvl clear
    $ preferences.transitions = 0 # set the transitions
    $ nvl_phone.name = "QuestionableAddendum"
    $ config.fast_skipping = True
    nvl_sys "16-30-XXX16HIC. "
    TYp "I know I'm coming in late, I will be there in 40, how was dinner? "
    YOU "Pretty good, Canela makes the best jambalaya"
    YOU "She says to tell you that your 'hot meeter has dropped by 29' for staying late at work."
    YOU "Again."
    YOU "She says to send the again."
    TYp "Tell her sorry. I will eat as soon as I get there."
    YOU "You think that is okay. Tyrone, you might catch us watching a movie."
    TYp "Oh, what movie?"
    YOU "You two are watching this strange movie called..."
    YOU "Canela says is called."
    YOU "Based and Jigsaw pilled."
    TYp "Ah one of those basement comedies about escaping from a crazy troll that captures you."
    TYp "A favorite."
    TYp "Keep me a seat warm."
    YOU "Will do."
    YOU ":)"
    nvl_sys "YESTERDAY."
    TYp "Don't forget, tomorrow we have a hanging out day."
    YOU "You won't! You promise."
    TYp "Good, good. You wouldn't miss it for anything."
    # # Fake a bunch of history for the previous conversations
    nvl_sys "TODAY."
    TYp "Where do you want me to pick you up after the show."
    TYp "I know this is a little late but I hope everything is alright in your end."
    TYp "My secretary recored the video of your show today so we can watch it afterwards with Canela."
    TYp "If you are mad about my cancelling I understand, I just need you to pick up."
    TYp "Friend, we are worried. The set said you left with some troll, where are you?"
    TYp "Please message me back as soon as you are able."
    TYp "I don't like doing this, but I'm gonna have to if you refuse to pick up."
    nvl_sys "LOC.AP.IP.TRACK."
    TYp "Message back."
    $ ui.interact()
    $ config.fast_skipping = False
    #disable transitions when entering nvl mode
    # it's not an elegant solution but we have to use this one till I find a better way
    # don't forget to set it back to 2 before exiting this mode

    nvl_sys "LOCATION ADQUIRED.{nw}"
    nvl_sys "SENDING.{nw}"

    TYp "That took a while.{nw}" # {nw} will automatically advance the conversation
    $ nvl_phone.type("QuestionableAddendum") # who is typing
    # pause
    TYp "Why are you down there?{nw}"
    $ nvl_phone.type("QuestionableAddendum", [10, 10, 35]) # You can give it a list of typing pauses in tenth of seconds in this case it shows [typing for 1 sec, nothing foe 2 sec, typing for 3.5 sec]
    # pause
    TYp "Hello? Please, say something."
    $ nvl_phone.type("QuestionableAddendum")
    # if you don't add a `typing...` the game advances with user input instead and {nw} is not necessary
    TYp "Or nothing{nw}"

    $ nvl_phone.abort_typing() # Put this before every menu to avoid errors in case the player skipped through the messages
    # You can use either normal or nvl menus
    menu (nvl=True): # You can have normal dialogue but letting the player click each one gives the illusion of replying
        "What?":
            YOU "What?{nw}"
        "Oh Tyrone, everything is fine?":
            YOU "Oh Tyrone, everything is fine?{nw}"
        "You didn't notifications before. The signal must be spotty at best." :
            YOU "You didn't notifications before. The signal must be spotty at best.{nw}"
    pause 1
    YOU "Sorry. {nw}"
    $ nvl_phone.type("QuestionableAddendum",[20])
    TYp "alright, alright. Don't think much about it.{nw}"
    TYp "I'm going to get you, okay?"
    $ nvl_phone.type("QuestionableAddendum",[10])
    $ renpy.block_rollback() # This stops the rollback when the player rolls back to the line after this
    TYp "Not personally but I'll send some help that I met at my meeting."
    TYp "She is good, don't worry. She will keep you safe."

    $ preferences.transitions = 2 # At the end of a conversation or before jumping to normal dialogue you need to set the transitions back to normal
    pause

    show bg room
    show aya at left
    "Something in normal dialogue."
    "Or to fake browsing the phone with a screen."

# To start a new conversation you don't need a new label
label nvl_new_conversation:
    nvl clear # Clear the nvl history
    $ preferences.transitions = 0 # set the transitions
    $ nvl_phone.name = "Mayo" # Set the chat name


    # # Fake a bunch of history for the previous conversations
    # $ config.fast_skipping = True

    # nvl_sys "21 May 2021"
    # may "Wya chan it's me, Mayo."
    # may "I've got your number from RinRin."
    # aya "Oh, Hi."
    # may "Just wanted to let you know, see you later at the school."
    # aya "Sure."
    # aya "Bye"
    # may "bye"
    # # $ ui.interact()
    # $ config.fast_skipping = False

    aya "Are you albright mayo chan?"
    aya "Did the cat attack you?"
    may "No, I didn't go near him."
    aya "Thank goodness."
    may "Am I still invited to the trip?"
    aya "Of course!"
    may "Great!"
