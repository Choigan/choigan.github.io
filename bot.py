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
    keyboard.add(
        button1, button2, button3, button4, button5, button6, button7, button8, button9
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
    button1 = types.KeyboardButton("Физики")
    button2 = types.KeyboardButton("Юрики")
    button3 = types.KeyboardButton("Назад")
    keyboard.add(button1, button2, button3)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выберите подраздел:", reply_markup=keyboard)


# Обработчик выбора Акции
@bot.message_handler(func=lambda message: message.text == "Акции")
def handle_section_prom(message):
    # Открываем файл и выводим как сообщение
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_prom_cam = types.KeyboardButton(
        text="Акции видеонаблюдения",
        web_app=WebAppInfo(url="https://choigan.github.io/my"),
    )
    keyboard.add(btn_prom_cam)
    btn_prom_et = types.KeyboardButton(
        text="Акции интернета", web_app=WebAppInfo(url="https://tuva.ru/promo/")
    )
    keyboard.add(btn_prom_et)
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
    button1 = types.KeyboardButton("Роутеры")
    button2 = types.KeyboardButton("Терминалы")
    button3 = types.KeyboardButton("Приставки")
    button4 = types.KeyboardButton("Камеры")
    button5 = types.KeyboardButton("Назад")
    keyboard.add(button1, button2, button3, button4, button5)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выберите подраздел:", reply_markup=keyboard)


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
    button1 = types.KeyboardButton("Настройка плеера")
    button2 = types.KeyboardButton("Каналы с TimeShift")
    button3 = types.KeyboardButton("Назад")
    keyboard.add(button1, button2, button3)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выберите подраздел:", reply_markup=keyboard)


# Обработчик выбора Видео
@bot.message_handler(func=lambda message: message.text == "Видео")
def handle_section_video(message):
    # Создаем клавиатуру с подразделами Видео
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Проверка камер")
    button2 = types.KeyboardButton("Назад")
    keyboard.add(button1, button2)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выберите подраздел:", reply_markup=keyboard)


# Обработчик выбора Домофон
@bot.message_handler(func=lambda message: message.text == "Домофон")
def handle_section_dom(message):
    # Создаем клавиатуру с подразделами Домофон
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Проверка домофона")
    button2 = types.KeyboardButton("Стоимость установки")
    button3 = types.KeyboardButton("Назад")
    keyboard.add(button1, button2, button3)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выберите подраздел:", reply_markup=keyboard)


# Обработчик выбора ЛС
@bot.message_handler(func=lambda message: message.text == "ЛС")
def handle_section_lc(message):
    # Создаем клавиатуру с подразделами ЛС
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("РТК")
    button2 = types.KeyboardButton("МинОбр")
    button3 = types.KeyboardButton("Назад")
    keyboard.add(button1, button2, button3)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выберите подраздел:", reply_markup=keyboard)


# ---------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------Подразделы 2 уровня--------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# Обработчик выбора ТП -> Физики
@bot.message_handler(
    func=lambda message: message.text == "Физики" or message.text == "tpf"
)
def handle_subsection_tp_fiz(message):
    # Обработка действий ТП -> Физики
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Тарифные планы для физиков:")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора ТП -> Юрики
@bot.message_handler(func=lambda message: message.text == "Юрики")
def handle_subsection_tp_yur(message):
    # Обработка действий ТП -> Юрики
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Тарифные планы для юриков:")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Команды -> ETTH
@bot.message_handler(func=lambda message: message.text == "ETTH")
def handle_subsection_com_etth(message):
    # Создаем клавиатуру с подразделами Команды -> ETTH
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("QTech ETTH")
    button2 = types.KeyboardButton("Zyxel ETTH")
    button3 = types.KeyboardButton("Назад")
    keyboard.add(button1, button2, button3)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выберите подраздел:", reply_markup=keyboard)


# Обработчик выбора Команды -> GPON
@bot.message_handler(func=lambda message: message.text == "GPON")
def handle_subsection_com_gpon(message):
    # Обработка действий Команды -> GPON
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Город")
    button2 = types.KeyboardButton("Районы")
    button3 = types.KeyboardButton("Назад")
    keyboard.add(button1, button2, button3)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выберите подраздел:", reply_markup=keyboard)


# Обработчик выбора Команды -> ADSL
@bot.message_handler(func=lambda message: message.text == "ADSL")
def handle_subsection_com_adsl(message):
    # Обработка действий Команды -> ADSL
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Zyxel DSL")
    button2 = types.KeyboardButton("QTech DSL")
    button3 = types.KeyboardButton("Назад")
    keyboard.add(button1, button2, button3)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выберите подраздел:", reply_markup=keyboard)


# Обработчик выбора Устройства -> Роутеры
@bot.message_handler(func=lambda message: message.text == "Роутеры")
def handle_subsection_dev_rout(message):
    # Обработка действий Устройства -> Роутеры
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Наименования и цены роутеров:")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Устройства -> Терминалы
@bot.message_handler(func=lambda message: message.text == "Терминалы")
def handle_subsection_dev_term(message):
    # Обработка действий Устройства -> Терминалы
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Наименования и цены терминалов:")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Устройства -> Приставки
@bot.message_handler(func=lambda message: message.text == "Приставки")
def handle_subsection_dev_pris(message):
    # Обработка действий Устройства -> Приставки
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Наименования и цены приставок:")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Устройства -> Камеры
@bot.message_handler(func=lambda message: message.text == "Камеры")
def handle_subsection_dev_cam(message):
    # Обработка действий Устройства -> Камеры
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Наименования и цены приставок:")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Настройки -> Настройка PPPoE
@bot.message_handler(func=lambda message: message.text == "Настройка PPPoE")
def handle_subsection_set_pppoe(message):
    # Обработка действий Настройки -> Настройка PPPoE
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton("ПК")
    button2 = types.KeyboardButton("Keenetic")
    button3 = types.KeyboardButton("TP-LINK C20")
    button4 = types.KeyboardButton("TP-LINK 8960N")
    button5 = types.KeyboardButton("Qtech R8")
    button6 = types.KeyboardButton("ASUS")
    button7 = types.KeyboardButton("D-LINK")
    button8 = types.KeyboardButton("Xiaomi")
    button9 = types.KeyboardButton("Mercusys")
    button10 = types.KeyboardButton("Назад")
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
    )

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выберите подраздел:", reply_markup=keyboard)


# Обработчик выбора Настройки -> Настройка WI-FI
@bot.message_handler(func=lambda message: message.text == "Настройка WI-FI")
def handle_subsection_set_wifi(message):
    # Обработка действий Настройки -> Настройка WI-FI
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton("Keenetic.")
    button2 = types.KeyboardButton("TP-LINK C20.")
    button3 = types.KeyboardButton("TP-LINK 8960N.")
    button4 = types.KeyboardButton("Qtech R8.")
    button5 = types.KeyboardButton("ASUS.")
    button6 = types.KeyboardButton("D-LINK.")
    button7 = types.KeyboardButton("Xiaomi.")
    button8 = types.KeyboardButton("Mercusys.")
    button9 = types.KeyboardButton("Назад")
    keyboard.add(
        button1, button2, button3, button4, button5, button6, button7, button8, button9
    )

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выберите подраздел:", reply_markup=keyboard)


# Обработчик выбора Настройки -> Настройка ТВ
@bot.message_handler(func=lambda message: message.text == "Настройка ТВ")
def handle_subsection_set_tv(message):
    # Обработка действий Настройки -> Настройка ТВ
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Android")
    button2 = types.KeyboardButton("Samsung")
    button3 = types.KeyboardButton("LG")
    button4 = types.KeyboardButton("Назад")
    keyboard.add(button1, button2, button3, button4)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выберите подраздел:", reply_markup=keyboard)


# Обработчик выбора Настройки -> Проброс портов
@bot.message_handler(func=lambda message: message.text == "Проброс портов")
def handle_subsection_set_pp(message):
    # Обработка действий Настройки -> Проброс портов
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Инструкция по пробросу портов:")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора IPTV -> Настройка плеера
@bot.message_handler(func=lambda message: message.text == "Настройка плеера")
def handle_subsection_iptv_player(message):
    # Обработка действий IPTV -> Настройка плеера
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Инструкция по настройке плеера:")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора IPTV -> Каналы с TimeShift
@bot.message_handler(func=lambda message: message.text == "Каналы с TimeShift")
def handle_subsection_iptv_timeshift(message):
    # Обработка действий IPTV -> Каналы с TimeShift
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Список каналов с TimeShift:")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Видео -> Проверка камер
@bot.message_handler(func=lambda message: message.text == "Проверка камер")
def handle_subsection_video_prov(message):
    # Обработка действий Видео -> Проверка камер
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Инструкция по проверке камер:")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Домофон -> Проверка домофона
@bot.message_handler(func=lambda message: message.text == "Проверка домофона")
def handle_subsection_dom_prov(message):
    # Обработка действий Домофон -> Проверка домофона
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Инструкция по проверке домофона:")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Домофон -> Стоимость установки
@bot.message_handler(func=lambda message: message.text == "Стоимость установки")
def handle_subsection_dom_price(message):
    # Обработка действий Домофон -> Стоимость установки
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Стоимость установки домофона:")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора ЛС -> РТК
@bot.message_handler(func=lambda message: message.text == "РТК")
def handle_subsection_lc_rtk(message):
    # Обработка действий ЛС -> РТК
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Лицевые счета РТК:")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора ЛС -> МинОбр
@bot.message_handler(func=lambda message: message.text == "МинОбр")
def handle_subsection_lc_minobr(message):
    # Обработка действий ЛС -> МинОбр
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Лицевые счета МинОбр:")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------Подразделы 3 уровня-----------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# Обработчик выбора Команды -> ETTH -> QTech ETTH
@bot.message_handler(func=lambda message: message.text == "QTech ETTH")
def handle_subsection_com_etth_qtech(message):
    # Обработка действий Команды -> ETTH -> QTech ETTH
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Команды коммутатора QTech: ")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Команды -> ETTH -> Zyxel ETTH
@bot.message_handler(func=lambda message: message.text == "Zyxel ETTH")
def handle_subsection_com_etth_zyxel(message):
    # Обработка действий Команды -> ETTH -> QTech ETTH
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Команды коммутатора Zyxel: ")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Команды -> GPON -> Город
@bot.message_handler(func=lambda message: message.text == "Город")
def handle_subsection_com_gpon_city(message):
    # Обработка действий Команды -> GPON -> Город
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Команды оптического коммутатора Eltex: ")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Команды -> GPON -> Районы
@bot.message_handler(func=lambda message: message.text == "Районы")
def handle_subsection_com_gpon_district(message):
    # Обработка действий Команды -> GPON -> Районы
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Команды оптического коммутатора QTech: ")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Команды -> ADSL -> Zyxel ADSL
@bot.message_handler(func=lambda message: message.text == "Zyxel DSL")
def handle_subsection_com_adsl_zyxel(message):
    # Обработка действий Команды -> ADSL -> Zyxel ADSL
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Команды DSL коммутатора Zyxel: ")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Команды -> ADSL -> Qtech ADSL
@bot.message_handler(func=lambda message: message.text == "QTech DSL")
def handle_subsection_com_adsl_zyxel(message):
    # Обработка действий Команды -> ADSL -> Qtech ADSL
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Команды DSL коммутатора QTech: ")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Настройки -> Настройка PPPoE -> ПК
@bot.message_handler(func=lambda message: message.text == "ПК")
def handle_subsection_set_pppoe_pc(message):
    # Обработка действий Настройки -> Настройка PPPoE -> ПК
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Инструкция по настройке PPPoE на ПК: ")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Настройки -> Настройка PPPoE -> Keenetic
@bot.message_handler(func=lambda message: message.text == "Keenetic")
def handle_subsection_set_pppoe_keenetic(message):
    # Обработка действий Настройки -> Настройка PPPoE -> Keenetic
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(
            message.chat.id, "Инструкция по настройке PPPoE на роутере Keenetic: "
        )
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Настройки -> Настройка PPPoE -> TP-LINK C20
@bot.message_handler(func=lambda message: message.text == "TP-LINK C20")
def handle_subsection_set_pppoe_tplinkc20(message):
    # Обработка действий Настройки -> Настройка PPPoE -> TP-LINK C20
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(
            message.chat.id, "Инструкция по настройке PPPoE на роутере TP-LINK C20: "
        )
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Настройки -> Настройка PPPoE -> TP-LINK 8960N
@bot.message_handler(func=lambda message: message.text == "TP-LINK 8960N")
def handle_subsection_set_pppoe_tplink8960n(message):
    # Обработка действий Настройки -> Настройка PPPoE -> TP-LINK 8960N
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(
            message.chat.id, "Инструкция по настройке PPPoE на роутере TP-LINK 8960N: "
        )
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Настройки -> Настройка PPPoE -> Qtech R8
@bot.message_handler(func=lambda message: message.text == "Qtech R8")
def handle_subsection_set_pppoe_qtechr8(message):
    # Обработка действий Настройки -> Настройка PPPoE -> Qtech R8
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(
            message.chat.id, "Инструкция по настройке PPPoE на роутере Qtech R8: "
        )
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Настройки -> Настройка PPPoE -> ASUS
@bot.message_handler(func=lambda message: message.text == "ASUS")
def handle_subsection_set_pppoe_asus(message):
    # Обработка действий Настройки -> Настройка PPPoE -> ASUS
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(
            message.chat.id, "Инструкция по настройке PPPoE на роутере ASUS: "
        )
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Настройки -> Настройка PPPoE -> D-LINK
@bot.message_handler(func=lambda message: message.text == "D-LINK")
def handle_subsection_set_pppoe_dlink(message):
    # Обработка действий Настройки -> Настройка PPPoE -> D-LINK
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(
            message.chat.id, "Инструкция по настройке PPPoE на роутере D-LINK: "
        )
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Настройки -> Настройка PPPoE -> Xiaomi
@bot.message_handler(func=lambda message: message.text == "Xiaomi")
def handle_subsection_set_pppoe_xiaomi(message):
    # Обработка действий Настройки -> Настройка PPPoE -> Xiaomi
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(
            message.chat.id, "Инструкция по настройке PPPoE на роутере Xiaomi: "
        )
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Настройки -> Настройка PPPoE -> Mercusys
@bot.message_handler(func=lambda message: message.text == "Mercusys")
def handle_subsection_set_pppoe_mercusys(message):
    # Обработка действий Настройки -> Настройка PPPoE -> Mercusys
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(
            message.chat.id, "Инструкция по настройке PPPoE на роутере Mercusys: "
        )
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Настройки -> Настройка WI-FI -> Keenetic
@bot.message_handler(func=lambda message: message.text == "Keenetic.")
def handle_subsection_set_wifi_keenetic(message):
    # Обработка действий Настройки -> Настройка Wi_FI -> Keenetic
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(
            message.chat.id, "Инструкция по настройке WI-FI на роутере Keenetic: "
        )
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Настройки -> Настройка WI-FI -> TP-LINK C20
@bot.message_handler(func=lambda message: message.text == "TP-LINK C20.")
def handle_subsection_set_wifi_tplinkc20(message):
    # Обработка действий Настройки -> Настройка WI-FI -> TP-LINK C20
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(
            message.chat.id, "Инструкция по настройке WI-FI на роутере TP-LINK C20: "
        )
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Настройки -> Настройка WI-FI -> TP-LINK 8960N
@bot.message_handler(func=lambda message: message.text == "TP-LINK 8960N.")
def handle_subsection_set_wifi_tplink8960n(message):
    # Обработка действий Настройки -> Настройка WI-FI -> TP-LINK 8960N
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(
            message.chat.id, "Инструкция по настройке WI-FI на роутере TP-LINK 8960N: "
        )
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Настройки -> Настройка WI-FI -> Qtech R8
@bot.message_handler(func=lambda message: message.text == "Qtech R8.")
def handle_subsection_set_wifi_qtechr8(message):
    # Обработка действий Настройки -> Настройка WI-FI -> Qtech R8
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(
            message.chat.id, "Инструкция по настройке WI-FI на роутере Qtech R8: "
        )
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Настройки -> Настройка WI-FI -> ASUS
@bot.message_handler(func=lambda message: message.text == "ASUS.")
def handle_subsection_set_wifi_asus(message):
    # Обработка действий Настройки -> Настройка WI-FI -> ASUS
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(
            message.chat.id, "Инструкция по настройке WI-FI на роутере ASUS: "
        )
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Настройки -> Настройка WI-FI -> D-LINK
@bot.message_handler(func=lambda message: message.text == "D-LINK.")
def handle_subsection_set_wifi_dlink(message):
    # Обработка действий Настройки -> Настройка WI-FI -> D-LINK
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(
            message.chat.id, "Инструкция по настройке WI-FI на роутере D-LINK: "
        )
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Настройки -> Настройка WI-FI -> Xiaomi
@bot.message_handler(func=lambda message: message.text == "Xiaomi.")
def handle_subsection_set_wifi_xiaomi(message):
    # Обработка действий Настройки -> Настройка WI-FI -> Xiaomi
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(
            message.chat.id, "Инструкция по настройке WI-FI на роутере Xiaomi: "
        )
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Настройки -> Настройка WI-FI -> Mercusys
@bot.message_handler(func=lambda message: message.text == "Mercusys.")
def handle_subsection_set_wifi_mercusys(message):
    # Обработка действий Настройки -> Настройка WI-FI -> Mercusys
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(
            message.chat.id, "Инструкция по настройке WI-FI на роутере Mercusys: "
        )
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Настройки -> Настройка ТВ -> Android
@bot.message_handler(func=lambda message: message.text == "Android")
def handle_subsection_set_tv_android(message):
    # Обработка действий Настройки -> Настройка ТВ -> Android
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(
            message.chat.id, "Инструкция по настройке телевизора с ОС Android: "
        )
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Настройки -> Настройка ТВ -> Samsung
@bot.message_handler(func=lambda message: message.text == "Samsung")
def handle_subsection_set_tv_samsung(message):
    # Обработка действий Настройки -> Настройка ТВ -> Samsung
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(
            message.chat.id, "Инструкция по настройке телевизора Samsung: "
        )
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик выбора Настройки -> Настройка ТВ -> LG
@bot.message_handler(func=lambda message: message.text == "LG")
def handle_subsection_set_tv_lg(message):
    # Обработка действий Настройки -> Настройка ТВ -> LG
    with open("1.html", "r", encoding="utf-8") as file:
        file_content = file.read()
        bot.send_message(message.chat.id, "Инструкция по настройке телевизора LG: ")
        bot.send_message(message.chat.id, file_content, parse_mode="HTML")


# Обработчик нажатия кнопки "Назад"
@bot.message_handler(func=lambda message: message.text == "Назад")
def handle_back(message):
    # Перенаправляем в начальное меню
    handle_start(message)


# Запускаем бота
bot.polling()
