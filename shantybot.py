import telebot
from telebot import types
import time

TOKEN = "7379713109:AAHMSMSc_aUT7lhPvx2H7eMB_S0z5F6XIrs"
bot = telebot.TeleBot(TOKEN)


mute_list = []
ban_list = []
counter = {}
mute_data = {}



@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    bot.reply_to(message, text='''⚠️правила группы:
🧸Бан - блокировка без возможности возвращения в чат. 
🕖Мут - блокировка на определённое время. Время выбирает администратор чата по своему усмотрению. 
🚩Мут/бан - администратор группы выбирает, что именно делать с нарушителем по своему усмотрению. 

🚫 Запрещено:

🫦 1. Картинки/стикеры 18+ ( на первый раз (в количестве не более 1 картинки) - предупредительный мут на две недели, второй раз - бан) 

‼️ 2. Спам/флуд - мут/бан

❌ 3. Токсичность/ оскорбления/агрессия - мут

👀 4. Реклама других пабликов с ссылкой на канал, чаты, магазины, боты - мут/бан. 

🧑‍✈️5. Политика - мут/бан

🧂6. Что либо, отсылающее к запрещенным веществам - мут/бан''')


@bot.message_handler(commands=['shanty'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Twitch', url='https://www.twitch.tv/etoshanty', callback_data='twitch')
    button2 = types.InlineKeyboardButton(text='Telegram', url='https://t.me/etoshanty',  callback_data='tg')
    button3 = types.InlineKeyboardButton(text='Etoshanty Shop', url='https://t.me/etoshanty_shop_bot', callback_data='shop')
    markup.add(button1, button2, button3)
    bot.send_photo(message.chat.id, photo=open(r'photo_2024-09-23_23-31-28.jpg', 'rb'), caption='''Где меня найти?️''', reply_markup=markup)


@bot.message_handler(commands=['info'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Команды', callback_data='commands')
    button2 = types.InlineKeyboardButton(text='Правила', callback_data='rules')
    markup.add(button1, button2)
    bot.send_photo(message.chat.id, photo=open(r'Снимок экрана 2024-09-22 235550.png', 'rb'), caption='''Информация обо мне!
Меня зовут Юмико. Я дочка Лизы и сестра Данфорта. В свободное время отдыхаю, играю в Fortnite и слежу за чатом!
Для ознакомления с командами и правилами, помогающими следить мне за чатом, вы можете нажать кнопки снизу!

Всех люблю💙''', reply_markup=markup)


@bot.message_handler(commands=['rules'])
def start(message):
    bot.send_message(message.chat.id, '''⚠️правила группы:
🧸Бан - блокировка без возможности возвращения в чат. 
🕖Мут - блокировка на определённое время. Время выбирает администратор чата по своему усмотрению. 
🚩Мут/бан - администратор группы выбирает, что именно делать с нарушителем по своему усмотрению. 

🚫 Запрещено:

🫦 1. Картинки/стикеры 18+ ( на первый раз (в количестве не более 1 картинки) - предупредительный мут на две недели, второй раз - бан) 

‼️ 2. Спам/флуд - мут/бан

❌ 3. Токсичность/ оскорбления/агрессия - мут

👀 4. Реклама других пабликов с ссылкой на канал, чаты, магазины, боты - мут/бан. 

🧑‍✈️5. Политика - мут/бан

🧂6. Что либо, отсылающее к запрещенным веществам - мут/бан''')


@bot.message_handler(commands=['commands'])
def start(message):
    bot.send_message(message.chat.id, '''Основные команды чата:
• /info - информация обо мне
• /shanty - где найти shanty?
• /commands - команды
• /rules - правила чата

Команды для администраторов:
• /mute - замутить котёнка
• /unmute - рузмутить котёнка
• /ban - заблокировать котёнка
• /unban - разблокировать котёнка''')


@bot.callback_query_handler(func=lambda call: call.data == 'commands')
def like2_handler(call):
    bot.send_message(call.message.chat.id,'''Основные команды чата:
• /info - информация обо мне
• /shanty - где найти shanty?
• /commands - команды
• /rules - правила чата

Команды для администраторов:
• /mute - замутить котёнка
• /unmute - рузмутить котёнка
• /ban - заблокировать котёнка
• /unban - разблокировать котёнка''')


@bot.callback_query_handler(func=lambda call: call.data == 'rules')
def like111_handler(call):
    bot.send_message(call.message.chat.id, '''⚠️правила группы:
🧸Бан - блокировка без возможности возвращения в чат. 
🕖Мут - блокировка на определённое время. Время выбирает администратор чата по своему усмотрению. 
🚩Мут/бан - администратор группы выбирает, что именно делать с нарушителем по своему усмотрению. 

🚫 Запрещено:

🫦 1. Картинки/стикеры 18+ ( на первый раз (в количестве не более 1 картинки) - предупредительный мут на две недели, второй раз - бан) 

‼️ 2. Спам/флуд - мут/бан

❌ 3. Токсичность/ оскорбления/агрессия - мут

👀 4. Реклама других пабликов с ссылкой на канал, чаты, магазины, боты - мут/бан. 

🧑‍✈️5. Политика - мут/бан

🧂6. Что либо, отсылающее к запрещенным веществам - мут/бан''')



@bot.message_handler(commands=['ban'])
def ban_user(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_status = bot.get_chat_member(chat_id, user_id).status
    if user_status == 'administrator' or user_status == 'creator':
        if message.reply_to_message:
            chat_id = message.chat.id
            user_id = message.reply_to_message.from_user.id
            user_status = bot.get_chat_member(chat_id, user_id).status
            if user_status == 'administrator' or user_status == 'creator':
                bot.reply_to(message, f"К сожалению котёнок @{message.reply_to_message.from_user.username} является частью персонала группы.")
            else:
                bot.kick_chat_member(chat_id, user_id)
                bot.reply_to(message, f"Котёнок @{message.reply_to_message.from_user.username} был забанен.")
                ban_list.append(message.from_user.id)
                bans_id_add(message)
        else:
            bot.reply_to(message,"Эта команда должна быть использована в ответ на сообщение котёнка, которого вы хотите забанить.")
    else:
        bot.reply_to(message,f"К сожалению у вас недостаточно прав, чтобы забанить котёнка @{message.reply_to_message.from_user.username}.")


@bot.message_handler(commands=['unban'])
def unban_user(message):
    if message.reply_to_message:
        user_id = message.from_user.i
        if user_id in ban_list:
            chat_id = message.chat.id
            user_id = message.from_user.id
            if is_user_admin(chat_id, user_id):
                user_status = bot.get_chat_member(chat_id, user_id).status
                if user_status != 'administrator' or user_status != 'creator':
                    user_to_unban = message.reply_to_message.from_user.id
                    bot.unban_chat_member(chat_id, user_to_unban)
                    bot.reply_to(message, f"Котёнок @{message.reply_to_message.from_user.username} разбанен.")
                    ban_list.remove(message.from_user.id)
                    bans_id_remove(message)
            else:
                bot.reply_to(message, "У вас нет прав для этой команды.")
        else:
            bot.reply_to(message, f"Котёнок @{message.reply_to_message.from_user.username} не забанен.")
    else:
            bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение котёнка, которого вы хотите разбанить.")

def is_user_admin(chat_id, user_id):
    chat_member = bot.get_chat_member(chat_id, user_id)
    return chat_member.status == "administrator" or chat_member.status == "creator"



@bot.message_handler(commands=['unmute'])
def unmute_user(message):
    user_id = message.from_user.id
    if user_id in mute_list:
        chat_id = message.chat.id
        user_id = message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'administrator' or user_status == 'creator':
            if message.reply_to_message:
                chat_id = message.chat.id
                user_id = message.reply_to_message.from_user.id
                user_status = bot.get_chat_member(chat_id, user_id).status
                if user_status == 'administrator' or user_status == 'creator':
                    bot.reply_to(message,f"К сожалению котёнок @{message.reply_to_message.from_user.username} является частью персонала группы.")
                else:
                    chat_id = message.chat.id
                    user_id = message.reply_to_message.from_user.id
                    bot.restrict_chat_member(chat_id, user_id, can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True, can_add_web_page_previews=True)
                    bot.reply_to(message, f"Котёнок @{message.reply_to_message.from_user.username} размучен.")
                    mute_list.remove(message.from_user.id)
                    mutes_id_remove(message)
            else:
                bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение котёнка, которого вы хотите размутить.")
        else:
            bot.reply_to(message,"У вас нет прав для данной команды.")
    else:
        bot.reply_to(message, 'Котёнок не замучен.')


@bot.message_handler(commands=['mute'])
def mute_user(message):
    user_id = message.from_user.id
    if user_id not in mute_list:
        chat_id = message.chat.id
        user_id = message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'administrator' or user_status == 'creator':
            if message.reply_to_message:
                chat_id = message.chat.id
                user_id = message.reply_to_message.from_user.id
                user_status = bot.get_chat_member(chat_id, user_id).status
                if user_status == 'administrator' or user_status == 'creator':
                    bot.reply_to(message,f"К сожалению котёнок @{message.reply_to_message.from_user.username} является частью персонала группы.")
                else:
                    text_mute = message.text
                    mute_count = text_mute.split(' ')
                    user_id = message.reply_to_message.from_user.id
                    duration = 60
                    min = duration * 1
                    hour = duration * 60
                    day = duration * 1440
                    week = duration * 10080
                    if mute_count:
                        if int(mute_count[1]) < 1:
                            bot.reply_to(message, "Время должно быть положительным числом.")
                            return
                        try:
                            if mute_count[2] == 'min':
                                bot.restrict_chat_member(chat_id, user_id, until_date=time.time() + min * int(mute_count[1]))
                                bot.reply_to(message, f"Котёнок @{message.reply_to_message.from_user.username} замучен на {mute_count[1]} минут.")
                                mutes_id_add(message)
                                mute_list.append(message.from_user.id)
                            elif mute_count[2] == 'hour':
                                bot.restrict_chat_member(chat_id, user_id, until_date=time.time() + hour * int(mute_count[1]))
                                bot.reply_to(message, f"Котёнок @{message.reply_to_message.from_user.username} замучен на {mute_count[1]} часов.")
                                mutes_id_add(message)
                                mute_list.append(message.from_user.id)
                            elif mute_count[2] == 'day':
                                bot.restrict_chat_member(chat_id, user_id, until_date=time.time() + day * int(mute_count[1]))
                                bot.reply_to(message, f"Котёнок @{message.reply_to_message.from_user.username} замучен на {mute_count[1]} дней.")
                                mutes_id_add(message)
                                mute_list.append(message.from_user.id)
                            elif mute_count[2] == 'week':
                                bot.restrict_chat_member(chat_id, user_id, until_date=time.time() + week * int(mute_count[1]))
                                bot.reply_to(message, f"Котёнок @{message.reply_to_message.from_user.username} замучен на {mute_count[1]} недель.")
                                mutes_id_add(message)
                                mute_list.append(message.from_user.id)
                        except:
                            bot.reply_to(message, "Время указано некоректно.")
            else:
                bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение котёнка, которого вы хотите замутить.")
        else:
            bot.reply_to(message,"У вас нет прав для данной команды.")
    elif user_id in mute_list:
        mute_list.remove(message.from_user.id)
        bot.reply_to(message, 'Произошла ошибка, попробуйте ещё раз.')




@bot.message_handler(commands=['mute_list'])
def mute_user(message):
    try:
        if len(mute_list) == 0:
            bot.reply_to(message, '')
            return
        else:
            bot.reply_to(message, mute_list)
    except:
        bot.reply_to(message, 'список пуст')

@bot.message_handler(regexp="http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
def delete_message(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_status = bot.get_chat_member(chat_id, user_id).status
    if user_status != 'administrator' or user_status != 'creator':
        bot.delete_message(message.chat.id, message.message_id)
        bot.restrict_chat_member(chat_id, user_id, until_date=time.time() + 300)
        bot.send_message(message.chat.id, f'Котёнок , ссылки в чате запрещены.')
        mute_list.append(message.from_user.id)
    elif user_status == 'administrator' or user_status == 'creator':
        bot.send_message(message.chat.id, '')






def mutes_id_add(message):
    user_id = message.reply_to_message.from_user.id
    with open('mutes.txt', 'r') as original:
        data = original.read()
    with open('mutes.txt', 'w') as modified:
        modified.write(str(user_id) + '\n' + data)


def mutes_id_remove(message):
    user_id = message.reply_to_message.from_user.id
    with open("mutes.txt", "r") as f:
        data = f.readlines()
    with open("mutes.txt", "w") as f:
        for line in data:
            if line.strip("\n") != str(user_id):
                f.write(line)


def bans_id_remove(message):
    user_id = message.reply_to_message.from_user.id
    with open("bans.txt", "r") as f:
        data = f.readlines()
    with open("bans.txt", "w") as f:
        for line in data:
            if line.strip("\n") != str(user_id):
                f.write(line)


def bans_id_add(message):
    user_id = message.reply_to_message.from_user.id
    with open('bans.txt', 'r') as original:
        data = original.read()
    with open('bans.txt', 'w') as modified:
        modified.write(user_id + '\n' + data)



if __name__ == '__main__':
    bot.polling(none_stop=True)



