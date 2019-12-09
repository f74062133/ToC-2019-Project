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

    def is_going_to_ask(self, event):
        if event.get("message"):
            if event['message'].get('text'):
                text = event['message']['text']
                return text.lower() == "睡覺睡到自然醒"
        return False
        #text = event.message.text
        
        #return text.lower() ==  or text.lower() == "成為荒野女神" or text.lower() == "以上皆是"

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

    def on_exit_state2(self):
        print("Leaving state2")

    def on_enter_fsm(self, event):
        print("I'm entering fsm")

        reply_token = event.reply_token
        send_image(reply_token, "https://i.imgur.com/7vliJBA.png")
        self.go_back()

    def on_exit_fsm(self):
        print("Leaving fsm")
    def on_enter_ask(self, event):
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

    def on_exit_ask(self):
        print("Leaving state1")
