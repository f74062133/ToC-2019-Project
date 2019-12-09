import os

from linebot import LineBotApi, WebhookParser
from linebot.models import *

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"
def send_image(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token,ImageSendMessage(
		original_content_url = text,
		preview_image_url = text
            )
        )
    return "OK"
def button(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token,TemplateSendMessage(
                altText = "Example buttons template", template = ButtonsTemplate(
                            thumbnailImageUrl = "https://api.reh.tw/line/bot/example/assets/images/example.jpg", 
                            title = "Example Menu", 
                            text = "Please select", 
                            actions = [
                                        PostbackAction(
                                                    display_text = "postback text", 
                                                    label = "postback",
                                                    data = "action=buy&itemid=123"  
                                        ),
                                        MessageAction( 
                                                    label = "message",
                                                    text = "Message example"  
                                        ),
                                        URIAction(
                                                    label = "uri",
                                                    uri = "https://github.com/GoneTone/line-example-bot-php" 
                                        )
                            ]
                )
            )
        )
    return "OK"

"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
