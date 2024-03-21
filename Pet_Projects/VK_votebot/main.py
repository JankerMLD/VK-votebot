# id 224606869
# ключ vk1.a.l1-hDX_RdQh67WabeW2GS0VPAU2j-lQ-G-L5jTOGGXas7QfNdCom81vxwbk1_jq-uISnHBdD9Z-VD-eFPxRP7W3h-IXM--KOd
# vJO6kntXWpr7nZ7hvtLB9pJLJVCvdd9iiqQjQ8OSlu_A4nWRfCObcNHRL6q1zyJtMAkdkJT5Ekxiq1pkfRsdEwiJCAi9VVuJC007wbLqbLTrYypk3eSJQ

import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType 

TOKEN = '''vk1.a.l1-hDX_RdQh67WabeW2GS0VPAU2j-lQ-G-L5jTOGGXas7QfNdCom81vxwbk1_jq-uISnHBdD9Z-VD-eFPxRP7W3h-IXM--KOdvJO6kntXWpr7nZ7hvtLB9p
JLJVCvdd9iiqQjQ8OSlu_A4nWRfCObcNHRL6q1zyJtMAkdkJT5Ekxiq1pkfRsdEwiJCAi9VVuJC007wbLqbLTrYypk3eSJQ'''
ID = "224606869"

vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkBotLongPoll(vk_session, ID)
vk = vk_session.get_api()

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            