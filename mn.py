# -*- coding: utf-8 -*-

# Импорт библиотек
import traceback
import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
from vk_api import VkApi
import datetime
import time
import pytz
import random
import os
import json
import sys
import threading

def get_time():
    # возвращает время формата ДД.ММ.ГГ ЧЧ:ММ:СС (по МСК)
    # например, 01.01.01 13:37:00
    return datetime.datetime.strftime(datetime.datetime.now(pytz.timezone('Europe/Moscow')), "%d.%m.%Y %H:%M:%S")


def console_log(text, symbols_amount=30):
    # выводит данные в консоль с указанием времени и интервалом после
    print("[" + get_time() + "] " + text)
    print("-" * symbols_amount)


def send_msg(peer_id=None, domain=None, chat_id=None, text=None,
             sticker_id=None, user_id=None, forward_messages=None, attachments=None, payload=None, keyboard=None):
    vk.messages.send(
        user_id=user_id,
        random_id=random.randint(-2147483648, 2147483647),
        peer_id=peer_id,
        domain=domain,
        chat_id=chat_id,
        message=text,
        sticker_id=sticker_id,
        attachment=attachments,
        forward_messages=forward_messages,
        payload=payload,
        keyboard=keyboard,
    )

try:
    vk_session = vk_api.VkApi(token="87807e5cca98de95c17c26fd4b0aa0b11ff940a4a5184f999a51590c5b7e4adfa9215d873e87267cf7fcc")
    long_poll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
except Exception as e:
    console_log("Во время подключения/получения параметров произошла ошибка: " + str(e))
def main():
    try:
        for event in long_poll.listen():
            global delay, cmd_prefix, cmd_eval, safe_eval, is_access_allowed
            try:
                #print(event.type)
                
                
                try:
                    message_text = event.text
                except:
                    message_text = "undefined"
                    
                    
                try:
                    peer_id = event.peer_id
                except:
                    peer_id = 0
                    
                    
                try:
                    user_id = event.user_id
                except:
                    user_id = 0
                    
                    
                try:
                    chat_id = peer_id-2000000000
                except:
                    chat_id = 0
                    
                    
                try:
                    message_id = event.message_id
                except:
                    message_id = 0
                    
                    
                try:
                    attachments1 = event.attachments.get('attach1_type', False)+event.attachments.get('attach1', False)
                    attachments2 = event.attachments.get('attach2_type', False)+event.attachments.get('attach2', False)
                    attachments3 = event.attachments.get('attach3_type', False)+event.attachments.get('attach3', False)
                    attachments4 = event.attachments.get('attach4_type', False)+event.attachments.get('attach4', False)
                    attachments5 = event.attachments.get('attach5_type', False)+event.attachments.get('attach5', False)
                    attachments6 = event.attachments.get('attach6_type', False)+event.attachments.get('attach6', False)
                    attachments7 = event.attachments.get('attach7_type', False)+event.attachments.get('attach7', False)
                    attachments8 = event.attachments.get('attach8_type', False)+event.attachments.get('attach8', False)
                    attachments9 = event.attachments.get('attach9_type', False)+event.attachments.get('attach9', False)
                    attachments10 = event.attachments.get('attach10_type', False)+event.attachments.get('attach10', False)
                    attachments_full = 0
                    if (attachments1 != 0):
                        attachments_full = attachments1
                    if (attachments2 != 0):
                        attachments_full = attachments_full+","+attachments2
                    if (attachments3 != 0):
                        attachments_full = attachments_full+","+attachments3
                    if (attachments4 != 0):
                        attachments_full = attachments_full+","+attachments4
                    if (attachments5 != 0):
                        attachments_full = attachments_full+","+attachments5
                    if (attachments6 != 0):
                        attachments_full = attachments_full+","+attachments6
                    if (attachments7 != 0):
                        attachments_full = attachments_full+","+attachments7
                    if (attachments8 != 0):
                        attachments_full = attachments_full+","+attachments8
                    if (attachments9 != 0):
                        attachments_full = attachments_full+","+attachments9
                    if (attachments10 != 0):
                        attachments_full = attachments_full+","+attachments10
                except Exception as vk_error:
                    attachments1 = 0
                    attachments2 = 0
                    attachments3 = 0
                    attachments4 = 0
                    attachments5 = 0
                    attachments6 = 0
                    attachments7 = 0
                    attachments8 = 0
                    attachments9 = 0
                    attachments10 = 0
                    attachments_full = 0
                    
                    
                # if event.type == VkEventType.USER_ONLINE:
                    # for i in vk.users.get(user_ids=event.user_id):
                        # stack = str(i.get('id', False)) + " " + str(i.get('first_name', False)) + " " + str(i.get('last_name', False)) + " онлайн."
                        # print(str(stack))
                # if event.type == VkEventType.USER_OFFLINE:
                    # for i in vk.users.get(user_ids=event.user_id):
                        # stack = str(i.get('id', False)) + " " + str(i.get('first_name', False)) + " " + str(i.get('last_name', False)) + " оффлайн."
                        # print(str(stack))
                if event.type == VkEventType.MESSAGE_NEW:
                    # print("---------------------------------\n" +
                          # "Event: " + str(event.type) + "\n" +
                          # "Text: " + str(message_text) + "\n" +
                          # "Peer_id: " + str(peer_id) + "\n" +
                          # "User_id: " + str(user_id) + "\n" +
                          # "Chat_id: " + str(chat_id) + "\n" +
                          # "Attachments1: " + str(attachments1) + "\n" +
                          # "Attachments2: " + str(attachments2) + "\n" +
                          # "Attachments3: " + str(attachments3) + "\n" +
                          # "Attachments4: " + str(attachments4) + "\n" +
                          # "Attachments5: " + str(attachments5) + "\n" +
                          # "Attachments6: " + str(attachments6) + "\n" +
                          # "Attachments7: " + str(attachments7) + "\n" +
                          # "Attachments8: " + str(attachments8) + "\n" +
                          # "Attachments9: " + str(attachments9) + "\n" +
                          # "Attachments10: " + str(attachments10) + "\n" +
                          # "Attachments_full: " + str(attachments_full) + "\n" +
                          # "---------------------------------\n")
                    # config['users'] += [{
                                         # 'id': usr_id, 
                                         # 'first_name': first_name, 
                                         # 'second_name': second_name, 
                                         # 'screenname': screenname, 
                                         # 'sex': sex, 
                                         # 'urltovk': urltovk, 
                                         # 'msg_count': 1, 
                                         # 'comm_count': 0
                                         # }]
                    # #if (attachments_full != 0):
                    # #    send_msg(peer_id=peer_id, attachments=attachments_full)
                    # #return print("goodbye!")
                    if (str(chat_id) != "-1394545179"):
                        continue
                    send_msg(chat_id="54", forward_messages=int(message_id))
            except Exception as vk_error:
                console_log("Ошибка: " + str(vk_error))
                traceback.print_exc()
                continue

    except Exception as vk_error:
        console_log("Ошибка: " + str(vk_error))
        print("Reloading...")
        time.sleep(10)
        print("Reloaded!")
        main()
        

# сбор инфы и вывод конфига перед запуском
if __name__ == "__main__":
    params = "Бот запущен!"
    main()
