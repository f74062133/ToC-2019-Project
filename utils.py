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
                alt_text = "Example buttons template", template = ButtonsTemplate(
                            thumbnail_image_url = "https://example.com/image.jpg", 
                            title = "Example Menu", 
                            text = "Please select", 
                            actions = [
                                        PostbackAction(
                                                    label = "postback",
                                                    display_text = "postback text", 
                                                    data = "action=buy&itemid=1"  
                                        ),
                                        MessageAction( 
                                                    label = "message",
                                                    text = "Message example"  
                                        ),
                                        URIAction(
                                                    label = "uri",
                                                    uri = "http://example.com/" 
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
