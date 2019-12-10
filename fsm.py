from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_image
from utils import button
import random


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text == "認識帥哥"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "認識美眉"
    def is_going_to_fsm(self, event):
        text = event.message.text
        return text.lower() == "fsm"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token

        temp = random.randint(1,5)
        if(temp==1):
            send_image(reply_token, "https://i.imgur.com/Crfclsh.jpg")
        elif(temp==2):
            send_image(reply_token, "https://i.imgur.com/RPNUZHq.jpg")
        elif(temp==3):
            send_image(reply_token, "https://i.imgur.com/xdxCt6b.jpg")
        else:
            send_image(reply_token, "https://i.imgur.com/TmZEeKT.jpg")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        temp = random.randint(1,4)
        if(temp==1):
            send_image(reply_token, "https://i.imgur.com/7YanpSm.jpg")
        elif(temp==2):
            send_image(reply_token, "https://i.imgur.com/zP0yDYr.jpg")
        else:
            send_image(reply_token, "https://i.imgur.com/Xhk0Ztk.jpg")
        reply_token = event.reply_token
        line_bot_api.reply_message(reply_token,TemplateSendMessage(
                    alt_text = "Example buttons template", template = ButtonsTemplate(
                                thumbnail_image_url = "https://example.com/image.jpg", 
                                title = "Which one is Sunny's favorite?", 
                                text = "Please select", 
                                actions = [
                                            MessageAction( 
                                                        label = "Sleep",
                                                        text = "Sleep"  
                                            ),
                                            MessageAction( 
                                                        label = "Play",
                                                        text = "Play"  
                                            ),
                                            MessageAction( 
                                                        label = "Both of All",
                                                        text = "Both of All"  
                                            )
                                ]
                    )
                )
            )
        self.go_back()


    def on_exit_state2(self):
        print("Leaving state2")

    def on_enter_fsm(self, event):
        print("I'm entering fsm")

        reply_token = event.reply_token
        send_image(reply_token, "https://i.imgur.com/7vliJBA.png")
        self.go_back()

    def on_exit_fsm(self):
        print("Leaving fsm")

