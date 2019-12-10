import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage, TemplateSendMessage

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
                            title = "功能選單", 
                            text = "Please select", 
                            actions = [
                                        MessageAction( 
                                                    label = "認識帥哥",
                                                    text = "認識帥哥"  
                                        ),
                                        MessageAction( 
                                                    label = "認識美眉",
                                                    text = "認識美眉"  
                                        ),
                                        MessageAction( 
                                                    label = "FSM",
                                                    text = "FSM"  
                                        ),
                                        URIAction(
                                                    label = "創作者FB",
                                                    uri = "https://www.facebook.com/profile.php?id=100001247928681" 
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
