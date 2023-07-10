import telebot
from telebot import types
from telebot.types import WebAppInfo
import os

# Создаем экземпляр бота
bot = telebot.TeleBot("5820145621:AAHComlnQz8cw8WJUuv3InbP8eMKai9IeSo")


# Обработчик команды /start или нажатия на кнопку "Меню"
@bot.message_handler(commands=["start"])
@bot.message_handler(func=lambda message: message.text == "Меню")
def handle_start(message):
    # Создаем клавиатуру с разделами
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    button1 = types.KeyboardButton("ТП")
    button2 = types.KeyboardButton(
        "Акции"
    )  # Должны отображаться только актуальные акции
    button3 = types.KeyboardButton("Команды")
    button4 = types.KeyboardButton("Устройства")
    button5 = types.KeyboardButton("Настройка")
    button6 = types.KeyboardButton("IPTV")
    button7 = types.KeyboardButton("Видео")
    button8 = types.KeyboardButton("Домофон")
    button9 = types.KeyboardButton("ЛС")
    button10 = types.KeyboardButton("Номера")
    button11 = types.KeyboardButton("VLAN")
    button12 = types.KeyboardButton("FAQ")
    keyboard.add(
        button1,
        button2,
        button3,
        button4,
        button5,
        button6,
        button7,
        button8,
        button9,
        button10,
        button11,
        button12,
    )

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выберите раздел:", reply_markup=keyboard)


# ---------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------Подразделы 1 уровня---------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# Обработчик выбора ТП
@bot.message_handler(func=lambda message: message.text == "ТП")
def handle_section_tp(message):
    # Создаем клавиатуру с подразделами ТП
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_tp_f = types.KeyboardButton(
        text="Физики",
        web_app=WebAppInfo(url="https://choigan.github.io/tpf"),
    )
    keyboard.add(btn_tp_f)
    btn_tp_y = types.KeyboardButton(
        text="Юрики", web_app=WebAppInfo(url="https://choigan.github.io/tpy")
    )
    keyboard.add(btn_tp_y)
    keyboard.add("Назад")
    bot.send_message(message.chat.id, "Нажмите на кнопку:", reply_markup=keyboard)


# Обработчик выбора Акции
@bot.message_handler(func=lambda message: message.text == "Акции")
def handle_section_prom(message):
    # Открываем файл и выводим как сообщение
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_prom_cam = types.KeyboardButton(
        text="Текущие акции",
        web_app=WebAppInfo(url="https://tuva.ru/promo/"),
    )
    keyboard.add(btn_prom_cam)
    keyboard.add("Назад")
    bot.send_message(message.chat.id, "Нажмите на кнопку:", reply_markup=keyboard)


# Обработчик выбора Команды
@bot.message_handler(func=lambda message: message.text == "Команды")
def handle_section_com(message):
    # Создаем клавиатуру с подразделами Команды
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("ETTH")
    button2 = types.KeyboardButton("GPON")
    button3 = types.KeyboardButton("ADSL")
    button4 = types.KeyboardButton("Назад")
    keyboard.add(button1, button2, button3, button4)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выберите подраздел:", reply_markup=keyboard)


# Обработчик выбора Устройства
@bot.message_handler(func=lambda message: message.text == "Устройства")
def handle_section_dev(message):
    # Создаем клавиатуру с подразделами Устройства
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    btn_dev_rout = types.KeyboardButton(
        text="Роутеры",
        web_app=WebAppInfo(url="https://choigan.github.io/rout"),
    )
    keyboard.add(btn_dev_rout)

    btn_dev_term = types.KeyboardButton(
        text="Терминалы", web_app=WebAppInfo(url="https://choigan.github.io/tpy")
    )
    keyboard.add(btn_dev_term)

    btn_dev_prist = types.KeyboardButton(
        text="Приставки", web_app=WebAppInfo(url="https://choigan.github.io/tpy")
    )
    keyboard.add(btn_dev_prist)
    btn_dev_cam = types.KeyboardButton(
        text="Камеры", web_app=WebAppInfo(url="https://choigan.github.io/tpy")
    )
    keyboard.add(btn_dev_cam)

    keyboard.add("Назад")

    bot.send_message(message.chat.id, "Нажмите на кнопку:", reply_markup=keyboard)


# Обработчик выбора Настройка
@bot.message_handler(func=lambda message: message.text == "Настройка")
def handle_section_set(message):
    # Создаем клавиатуру с подразделами Настройка
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Настройка PPPoE")
    button2 = types.KeyboardButton("Настройка WI-FI")
    button3 = types.KeyboardButton("Настройка ТВ")
    button4 = types.KeyboardButton("Проброс портов")
    button5 = types.KeyboardButton("Назад")
    keyboard.add(button1, button2, button3, button4, button5)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выберите подраздел:", reply_markup=keyboard)


# Обработчик выбора IPTV
@bot.message_handler(func=lambda message: message.text == "IPTV")
def handle_section_iptv(message):
    # Создаем клавиатуру с подразделами IPTV
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_iptv_player = types.KeyboardButton(
        text="Настройка плеера",
        web_app=WebAppInfo(url="https://choigan.github.io/tpf"),
    )
    keyboard.add(btn_iptv_player)
    keyboard.add("Каналы с TimeShift")
    keyboard.add("Назад")

    bot.send_message(message.chat.id, "Выберите подраздел:", reply_markup=keyboard)


# Обработчик выбора Видео
@bot.message_handler(func=lambda message: message.text == "Видео")
def handle_section_video(message):
    # Создаем клавиатуру с подразделами Видео
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_video_prov = types.KeyboardButton(
        text="Инструкция по проверке камер",
        web_app=WebAppInfo(url="https://choigan.github.io/my"),
    )
    keyboard.add(btn_video_prov)

    btn_video_price = types.KeyboardButton(
        text="Стоимость установки камер",
        web_app=WebAppInfo(url="https://choigan.github.io/tpy"),
    )
    keyboard.add(btn_video_price)

    keyboard.add("Назад")

    bot.send_message(message.chat.id, "Нажмите на кнопку:", reply_markup=keyboard)


# Обработчик выбора Домофон
@bot.message_handler(func=lambda message: message.text == "Домофон")
def handle_section_dom(message):
    # Создаем клавиатуру с подразделами Домофон
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_dom_prov = types.KeyboardButton(
        text="Инструкция по проверке домофона",
        web_app=WebAppInfo(url="https://choigan.github.io/my"),
    )
    keyboard.add(btn_dom_prov)

    btn_dom_price = types.KeyboardButton(
        text="Стоимость установки домофона",
        web_app=WebAppInfo(url="https://choigan.github.io/tpy"),
    )
    keyboard.add(btn_dom_price)

    keyboard.add("Назад")

    bot.send_message(message.chat.id, "Нажмите на кнопку:", reply_markup=keyboard)


# Обработчик выбора ЛС
@bot.message_handler(func=lambda message: message.text == "ЛС")
def handle_section_lc(message):
    # Создаем клавиатуру с подразделами ЛС
    with open("lc.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Лицевые счета:")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Номера
@bot.message_handler(func=lambda message: message.text == "Номера")
def handle_section_num(message):
    # Создаем клавиатуру с подразделами ЛС
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("ЦОА")
    button2 = types.KeyboardButton("КУЭС")
    button3 = types.KeyboardButton("ЦПУ")
    button4 = types.KeyboardButton("ЦЭТ")
    button5 = types.KeyboardButton("ОИТ")
    button6 = types.KeyboardButton("ПТО")
    button7 = types.KeyboardButton("СУСС")
    button8 = types.KeyboardButton("2 этаж")
    button9 = types.KeyboardButton("Назад")
    keyboard.add(
        button1, button2, button3, button4, button5, button6, button7, button8, button9
    )

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выберите подраздел:", reply_markup=keyboard)


# ---------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------Подразделы 2 уровня--------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------


# Обработчик выбора Команды -> ETTH
@bot.message_handler(func=lambda message: message.text == "ETTH")
def handle_subsection_com_etth(message):
    # Создаем клавиатуру с подразделами Команды -> ETTH
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_com_etth_qtech = types.KeyboardButton(
        text="QTech ETTH",
        web_app=WebAppInfo(url="https://choigan.github.io/qtechetth"),
    )
    keyboard.add(btn_com_etth_qtech)
    btn_com_etth_zyxel = types.KeyboardButton(
        text="Zyxel ETTH", web_app=WebAppInfo(url="https://choigan.github.io/zyxeletth")
    )
    keyboard.add(btn_com_etth_zyxel)
    keyboard.add("Назад")
    bot.send_message(message.chat.id, "Нажмите на кнопку:", reply_markup=keyboard)


# Обработчик выбора Команды -> GPON
@bot.message_handler(func=lambda message: message.text == "GPON")
def handle_subsection_com_gpon(message):
    # Обработка действий Команды -> GPON
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_com_gpon_city = types.KeyboardButton(
        text="Город",
        web_app=WebAppInfo(url="https://choigan.github.io/gponcity"),
    )
    keyboard.add(btn_com_gpon_city)
    btn_com_gpon_district = types.KeyboardButton(
        text="Районы", web_app=WebAppInfo(url="https://choigan.github.io/gpondist")
    )
    keyboard.add(btn_com_gpon_district)
    keyboard.add("Назад")
    bot.send_message(message.chat.id, "Нажмите на кнопку:", reply_markup=keyboard)


# Обработчик выбора Команды -> ADSL
@bot.message_handler(func=lambda message: message.text == "ADSL")
def handle_subsection_com_adsl(message):
    # Обработка действий Команды -> ADSL
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_com_adsl_qtech = types.KeyboardButton(
        text="QTech ADSL",
        web_app=WebAppInfo(url="https://choigan.github.io/qtechdsl"),
    )
    keyboard.add(btn_com_adsl_qtech)
    btn_com_adsl_zyxel = types.KeyboardButton(
        text="Zyxel ADSL", web_app=WebAppInfo(url="https://choigan.github.io/zyxeldsl")
    )
    keyboard.add(btn_com_adsl_zyxel)
    keyboard.add("Назад")
    bot.send_message(message.chat.id, "Нажмите на кнопку:", reply_markup=keyboard)


# Обработчик выбора Настройки -> Настройка PPPoE
@bot.message_handler(func=lambda message: message.text == "Настройка PPPoE")
def handle_subsection_set_pppoe(message):
    # Обработка действий Настройки -> Настройка PPPoE
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add("ПК")
    keyboard.add("Keenetic")
    keyboard.add("TP-LINK")

    btn_set_pppoe_qtech = types.KeyboardButton(
        text="QTech",
        web_app=WebAppInfo(url="https://choigan.github.io/qtechppp"),
    )
    keyboard.add(btn_set_pppoe_qtech)

    btn_set_pppoe_asus = types.KeyboardButton(
        text="ASUS", web_app=WebAppInfo(url="https://choigan.github.io/asusppp")
    )
    keyboard.add(btn_set_pppoe_asus)

    btn_set_pppoe_dlink = types.KeyboardButton(
        text="D-LINK", web_app=WebAppInfo(url="https://choigan.github.io/dlinkppp")
    )
    keyboard.add(btn_set_pppoe_dlink)

    btn_set_pppoe_xiaomi = types.KeyboardButton(
        text="Xiaomi", web_app=WebAppInfo(url="https://choigan.github.io/xiaomippp")
    )
    keyboard.add(btn_set_pppoe_xiaomi)

    btn_set_pppoe_mercysus = types.KeyboardButton(
        text="Mercusys", web_app=WebAppInfo(url="https://choigan.github.io/mercppp")
    )
    keyboard.add(btn_set_pppoe_mercysus)

    keyboard.add("Назад")

    bot.send_message(message.chat.id, "Нажмите на кнопку:", reply_markup=keyboard)


# Обработчик выбора Настройки -> Настройка WI-FI
@bot.message_handler(func=lambda message: message.text == "Настройка WI-FI")
def handle_subsection_set_wifi(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add("Keenetic.")
    keyboard.add("TP-LINK.")

    btn_set_wifi_qtech = types.KeyboardButton(
        text="QTech.",
        web_app=WebAppInfo(url="https://choigan.github.io/my"),
    )
    keyboard.add(btn_set_wifi_qtech)

    btn_set_wifi_asus = types.KeyboardButton(
        text="ASUS.", web_app=WebAppInfo(url="https://choigan.github.io/tpy")
    )
    keyboard.add(btn_set_wifi_asus)

    btn_set_wifi_dlink = types.KeyboardButton(
        text="D-LINK.", web_app=WebAppInfo(url="https://choigan.github.io/tpy")
    )
    keyboard.add(btn_set_wifi_dlink)

    btn_set_wifi_xiaomi = types.KeyboardButton(
        text="Xiaomi.", web_app=WebAppInfo(url="https://choigan.github.io/tpy")
    )
    keyboard.add(btn_set_wifi_xiaomi)

    btn_set_wifi_mercysus = types.KeyboardButton(
        text="Mercusys.", web_app=WebAppInfo(url="https://choigan.github.io/tpy")
    )
    keyboard.add(btn_set_wifi_mercysus)

    keyboard.add("Назад")

    bot.send_message(message.chat.id, "Нажмите на кнопку:", reply_markup=keyboard)


# Обработчик выбора Настройки -> Настройка ТВ
@bot.message_handler(func=lambda message: message.text == "Настройка ТВ")
def handle_subsection_set_tv(message):
    # Обработка действий Настройки -> Настройка ТВ
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_set_tv_android = types.KeyboardButton(
        text="Android",
        web_app=WebAppInfo(url="https://choigan.github.io/android"),
    )
    keyboard.add(btn_set_tv_android)
    btn_set_tv_samsung = types.KeyboardButton(
        text="Samsung", web_app=WebAppInfo(url="https://choigan.github.io/samsung")
    )
    keyboard.add(btn_set_tv_samsung)
    btn_set_tv_lg = types.KeyboardButton(
        text="LG", web_app=WebAppInfo(url="https://choigan.github.io/lg")
    )
    keyboard.add(btn_set_tv_lg)
    keyboard.add("Назад")
    bot.send_message(message.chat.id, "Нажмите на кнопку:", reply_markup=keyboard)


# Обработчик выбора Настройки -> Проброс портов
@bot.message_handler(func=lambda message: message.text == "Проброс портов")
def handle_subsection_set_pp(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_set_pp = types.KeyboardButton(
        text="Инструкция по пробросу портов",
        web_app=WebAppInfo(url="https://choigan.github.io/my"),
    )
    keyboard.add(btn_set_pp)

    keyboard.add("Назад")

    bot.send_message(message.chat.id, "Нажмите на кнопку:", reply_markup=keyboard)


# Обработчик выбора IPTV -> Каналы с TimeShift
@bot.message_handler(func=lambda message: message.text == "Каналы с TimeShift")
def handle_subsection_iptv_timeshift(message):
    # Обработка действий IPTV -> Каналы с TimeShift
    with open("timeshift.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Список каналов с TimeShift:")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Номера -> ЦОА
@bot.message_handler(func=lambda message: message.text == "ЦОА")
def handle_subsection_num_coa(message):
    # Обработка действий Номера -> ЦОА
    with open("num_coa.txt", "r", encoding="utf-8") as file:
        file_content = file.read().splitlines()

    num_message = "Телефоны отдела ЦОА:\n\n"
    for i, content in enumerate(file_content):
        data = content.strip().split(" ")
        if len(data) >= 3:
            number = data[0].strip()
            name = data[1].strip()
            surname = data[2].strip()
            full_name = f"{name} {surname}"
            num_message += f"{number} - {full_name}\n"

        elif len(data) >= 2:
            number = data[0].strip()
            name = data[1].strip()
            num_message += f"{number} - {name}\n"

            if i == 6:
                num_message += "\n Сотовые номера:\n\n"
    bot.send_message(message.chat.id, text=num_message, parse_mode="HTML")


# Обработчик выбора Номера -> КУЭС
@bot.message_handler(func=lambda message: message.text == "КУЭС")
def handle_subsection_num_kues(message):
    # Обработка действий Номера -> КУЭС
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Телефоны КУЭСов:")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Номера -> ЦПУ
@bot.message_handler(func=lambda message: message.text == "ЦПУ")
def handle_subsection_num_cpu(message):
    # Обработка действий Номера -> ЦПУ
    with open("num_cpu.txt", "r", encoding="utf-8") as file:
        file_content = file.read().splitlines()

    num_message = "Телефоны отдела ЦПУ:\n\n"
    for i, content in enumerate(file_content):
        data = content.strip().split(" ")
        if len(data) >= 3:
            number = data[0].strip()
            name = data[1].strip()
            surname = data[2].strip()
            full_name = f"{name} {surname}"
            num_message += f"{number} - {full_name}\n"

            if i == 2:
                num_message += "\n Менеджеры по юр. лицам:\n\n"
            elif i == 6:
                num_message += "\n Менеджеры по физ. лицам:\n\n"

        elif len(data) >= 2:
            number = data[0].strip()
            name = data[1].strip()
            num_message += f"{number} - {name}\n"

    bot.send_message(message.chat.id, text=num_message, parse_mode="HTML")


# Обработчик выбора Номера -> ЦЭТ
@bot.message_handler(func=lambda message: message.text == "ЦЭТ")
def handle_subsection_num_aps(message):
    # Обработка действий Номера -> ЦЭТ
    with open("num_set.txt", "r", encoding="utf-8") as file:
        file_content = file.read().splitlines()

    num_message = "Телефоны отдела ЦЭТ:\n\n"
    for i, content in enumerate(file_content):
        data = content.strip().split(" ")
        if len(data) >= 3:
            number = data[0].strip()
            name = data[1].strip()
            surname = data[2].strip()
            full_name = f"{name} {surname}"
            num_message += f"{number} - {full_name}\n"

            if i == 1:
                num_message += "\n Номера СЭТТС:\n\n"
            elif i == 5:
                num_message += "\n Номера АПС:\n\n"
            elif i == 8:
                num_message += "\n Номера ОЛКС:\n\n"

        elif len(data) >= 2:
            number = data[0].strip()
            name = data[1].strip()
            num_message += f"{number} - {name}\n"

    bot.send_message(message.chat.id, text=num_message, parse_mode="HTML")


# Обработчик выбора Номера -> ОИТ
@bot.message_handler(func=lambda message: message.text == "ОИТ")
def handle_subsection_num_oit(message):
    # Обработка действий Номера -> ОИТ
    with open("num_oit.txt", "r", encoding="utf-8") as file:
        file_content = file.read().splitlines()

    num_message = "Телефоны отдела ОИТ:\n\n"
    for i, content in enumerate(file_content):
        data = content.strip().split(" ")
        if len(data) >= 3:
            number = data[0].strip()
            name = data[1].strip()
            surname = data[2].strip()
            full_name = f"{name} {surname}"
            num_message += f"{number} - {full_name}\n"

            if i == 1:
                num_message += "\n Программисты:\n\n"
            elif i == 5:
                num_message += "\n Системные инженера:\n\n"

        elif len(data) >= 2:
            number = data[0].strip()
            name = data[1].strip()
            num_message += f"{number} - {name}\n"

    bot.send_message(message.chat.id, text=num_message, parse_mode="HTML")


# Обработчик выбора Номера -> ПТО
@bot.message_handler(func=lambda message: message.text == "ПТО")
def handle_subsection_num_pto(message):
    # Обработка действий Номера -> ПТО
    with open("num_pto.txt", "r", encoding="utf-8") as file:
        file_content = file.read().splitlines()

    num_message = "Телефоны отдела ПТО:\n\n"
    for i, content in enumerate(file_content):
        data = content.strip().split(" ")
        if len(data) >= 3:
            number = data[0].strip()
            name = data[1].strip()
            surname = data[2].strip()
            full_name = f"{name} {surname}"
            num_message += f"{number} - {full_name}\n"

        elif len(data) >= 2:
            number = data[0].strip()
            name = data[1].strip()
            num_message += f"{number} - {name}\n"

    bot.send_message(message.chat.id, text=num_message, parse_mode="HTML")


# Обработчик выбора Номера -> СУСС
@bot.message_handler(func=lambda message: message.text == "СУСС")
def handle_subsection_num_suss(message):
    # Обработка действий Номера -> СУСС
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Телефоны отдела СУСС:")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Номера -> 2 этаж
@bot.message_handler(func=lambda message: message.text == "2 этаж")
def handle_subsection_num_2floor(message):
    # Обработка действий Номера -> 2 этаж
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Телефоны 2 этажа:")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------Подразделы 3 уровня-----------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------


# Обработчик выбора Настройки -> Настройка PPPoE -> ПК
@bot.message_handler(func=lambda message: message.text == "ПК")
def handle_subsection_set_pppoe_pc(message):
    # Обработка действий Настройки -> Настройка PPPoE -> ПК
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_set_pppoe_pc_win7 = types.KeyboardButton(
        text="Windows 7",
        web_app=WebAppInfo(url="https://choigan.github.io/win7ppp"),
    )
    keyboard.add(btn_set_pppoe_pc_win7)

    btn_set_pppoe_pc_win10 = types.KeyboardButton(
        text="Windows 10", web_app=WebAppInfo(url="https://choigan.github.io/win10ppp")
    )
    keyboard.add(btn_set_pppoe_pc_win10)

    keyboard.add("Назад")

    bot.send_message(message.chat.id, "Нажмите на кнопку:", reply_markup=keyboard)


# Обработчик выбора Настройки -> Настройка PPPoE -> Keenetic
@bot.message_handler(func=lambda message: message.text == "Keenetic")
def handle_subsection_set_pppoe_keenetic(message):
    # Обработка действий Настройки -> Настройка PPPoE -> Keenetic
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_set_pppoe_keenetic_start = types.KeyboardButton(
        text="Keenetic Start",
        web_app=WebAppInfo(url="https://choigan.github.io/startppp"),
    )
    keyboard.add(btn_set_pppoe_keenetic_start)

    btn_set_pppoe_keenetic_lite = types.KeyboardButton(
        text="Keenetic Zyxel Lite",
        web_app=WebAppInfo(url="https://choigan.github.io/liteppp"),
    )
    keyboard.add(btn_set_pppoe_keenetic_lite)

    keyboard.add("Назад")

    bot.send_message(message.chat.id, "Нажмите на кнопку:", reply_markup=keyboard)


# Обработчик выбора Настройки -> Настройка PPPoE -> TP-LINK
@bot.message_handler(func=lambda message: message.text == "TP-LINK")
def handle_subsection_set_pppoe_tplink(message):
    # Обработка действий Настройки -> Настройка PPPoE -> TP-LINK
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_set_pppoe_tplink_c20 = types.KeyboardButton(
        text="TP-LINK C20",
        web_app=WebAppInfo(url="https://choigan.github.io/c20ppp.html"),
    )
    keyboard.add(btn_set_pppoe_tplink_c20)

    btn_set_pppoe_tplink_8960n = types.KeyboardButton(
        text="TP-LINK 8961N",
        web_app=WebAppInfo(url="https://choigan.github.io/8961nppp"),
    )
    keyboard.add(btn_set_pppoe_tplink_8960n)

    keyboard.add("Назад")

    bot.send_message(message.chat.id, "Нажмите на кнопку:", reply_markup=keyboard)


# Обработчик выбора Настройки -> Настройка WI-FI -> Keenetic
@bot.message_handler(func=lambda message: message.text == "Keenetic.")
def handle_subsection_set_wifi_keenetic(message):
    # Обработка действий Настройки -> Настройка Wi_FI -> Keenetic
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_set_wifi_keenetic_start = types.KeyboardButton(
        text="Keenetic Start.",
        web_app=WebAppInfo(url="https://choigan.github.io/my"),
    )
    keyboard.add(btn_set_wifi_keenetic_start)

    btn_set_wifi_keenetic_lite = types.KeyboardButton(
        text="Keenetic Zyxel Lite.",
        web_app=WebAppInfo(url="https://choigan.github.io/tpy"),
    )
    keyboard.add(btn_set_wifi_keenetic_lite)

    keyboard.add("Назад")

    bot.send_message(message.chat.id, "Нажмите на кнопку:", reply_markup=keyboard)


# Обработчик выбора Настройки -> Настройка WI-FI -> TP-LINK
@bot.message_handler(func=lambda message: message.text == "TP-LINK.")
def handle_subsection_set_wifi_tplink(message):
    # Обработка действий Настройки -> Настройка WI-FI -> TP-LINK
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_set_wifi_tplink_c20 = types.KeyboardButton(
        text="TP-LINK C20.",
        web_app=WebAppInfo(url="https://choigan.github.io/my"),
    )
    keyboard.add(btn_set_wifi_tplink_c20)

    btn_set_wifi_tplink_8960n = types.KeyboardButton(
        text="TP-LINK 8960N.", web_app=WebAppInfo(url="https://choigan.github.io/tpy")
    )
    keyboard.add(btn_set_wifi_tplink_8960n)

    keyboard.add("Назад")

    bot.send_message(message.chat.id, "Нажмите на кнопку:", reply_markup=keyboard)


# Обработчик нажатия кнопки "Назад"
@bot.message_handler(func=lambda message: message.text == "Назад")
def handle_back(message):
    # Перенаправляем в начальное меню
    handle_start(message)


# Запускаем бота
bot.polling()
