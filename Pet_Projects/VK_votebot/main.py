import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType 

TOKEN = "vk1.a.l1-hDX_RdQh67WabeW"
ID = "224606869"

vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkBotLongPoll(vk_session, ID)
vk = vk_session.get_api()


# ключ vk1.a.l1-hDX_RdQh67WabeW id 224606869