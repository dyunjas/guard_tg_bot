import telebot
from telebot import types
import time
from types import GenericAlias


TOKEN = "7379713109:AAHMSMSc_aUT7lhPvx2H7eMB_S0z5F6XIrs"
bot = telebot.TeleBot(TOKEN)


mute_list = []
ban_list = []
counter = {}
user_dic = {}


@bot.message_handler(commands=['set_rules'])
def start(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_status = bot.get_chat_member(chat_id, user_id).status
    if user_status == 'administrator' or user_status == 'creator':
        text = message.text
        with open("rules.txt", "a", encoding='utf-8') as f:
            f.write(text)
        with open("rules.txt", "r", encoding='utf-8') as f:
            data = f.readlines()
        with open("rules.txt", "w", encoding='utf-8') as f:
            for line in data:
                if line.strip() != '/set_rules':
                    f.write(line)
        bot.send_message(message.chat.id, 'Для изменения правил группы используйте команду [ /edit_rules ].')
    else:
        bot.reply_to(message, 'К сожалению у вас нет прав для использования данной команды.')


@bot.message_handler(commands=['edit_rules'])
def start(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_status = bot.get_chat_member(chat_id, user_id).status
    if user_status == 'administrator' or user_status == 'creator':
        with open('rules.txt', 'r+') as f:
            f.truncate(0)
        text = message.text
        with open("rules.txt", "a", encoding='utf-8') as f:
            f.write(text)
        with open("rules.txt", "r", encoding='utf-8') as f:
            data = f.readlines()
        with open("rules.txt", "w", encoding='utf-8') as f:
            for line in data:
                if line.strip() != '/edit_rules':
                    f.write(line)
        bot.send_message(message.chat.id, 'Правила чата изменены.')
    else:
        bot.reply_to(message, 'К сожалению у вас нет прав для использования данной команды.')


@bot.message_handler(commands=['admin_examples'])
def mute_user(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_status = bot.get_chat_member(chat_id, user_id).status
    if user_status == 'administrator' or user_status == 'creator':
        bot.send_message(user_id, '')
        bot.reply_to(message, f'Примеры использования команд были отправлены вам в личные сообщения.')
    else:
        bot.reply_to(message, 'Команда доступна только для персонала группы.')


@bot.message_handler(commands=['add_user'])
def start(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.from_user.id
        with open('users.txt', 'r') as original:
            data = original.read()
        with open('users.txt', 'w') as modified:
            modified.write('@' + message.reply_to_message.from_user.username + ' : '+ str(user_id) + '\n' + data)
        
    


@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    send_rules(message)


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
    bot.send_photo(message.chat.id, photo=open(r'Снимок экрана 2024-09-22 235550.png', 'rb'), caption = '''Меня зовут Юмико!
Я являюсь модератором этого чата!
Для получения подробносетй нажмите на кнопки снизу!''', reply_markup=markup)



@bot.message_handler(commands=['rules'])
def start(message):
    send_rules(message)



@bot.message_handler(commands=['commands'])
def start(message):
    send_commands(message)


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
    send_rules(call.message)



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
                bot.reply_to(message, "У вас нет прав для использования этой команды.")
        else:
            bot.reply_to(message, f"Котёнок @{message.reply_to_message.from_user.username} не забанен.")
    else:
            bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение котёнка, которого вы хотите разбанить.")

def is_user_admin(chat_id, user_id):
    chat_member = bot.get_chat_member(chat_id, user_id)
    return chat_member.status == "administrator" or chat_member.status == "creator"

@bot.message_handler(commands=['unban_user'])
def unban_user(message):
    global user_id
    chat_id = message.chat.id
    user_id1 = message.from_user.id
    user_status = bot.get_chat_member(chat_id, user_id1).status
    if user_status == 'administrator' or user_status == 'creator':
        try:
            text_ban = message.text
            unban_count = text_ban.split(' ')
            with open('users_id.txt') as file:
                lines = file.read().splitlines()
            dic = {}
            for line in lines:
                key, value = line.split(': ')
                dic.update({key: value})
            user_id_go = dic[unban_count[1] + ' ']
            user_id = int(user_id_go)
        except:
            bot.reply_to(message, '''Пользователя нет в базе.
Для добавления пользователя в базу используйте 
команду [/add_user]
в ответ на сообщение пользователя.''')
            user_id = ''
            try:
                bot.unban_chat_member(chat_id, user_id)
                bot.reply_to(message, f"Котёнок {unban_count[1]} разбанен.")
                user_id = ''
            except:
                bot.reply_to(message, 'Котёнок не забанен.')
        


@bot.message_handler(commands=['ban_user'])
def ban_user(message):
    global user_id
    chat_id = message.chat.id
    user_id1 = message.from_user.id
    user_status = bot.get_chat_member(chat_id, user_id1).status
    if user_status == 'administrator' or user_status == 'creator':
        try:
            text_ban = message.text
            ban_count = text_ban.split(' ')
            with open('users_id.txt') as file:
                lines = file.read().splitlines()
            dic = {}
            for line in lines:
                key, value = line.split(': ')
                dic.update({key: value})
            user_id_go = dic[ban_count[1] + ' ']
            user_id = int(user_id_go)
        except:
            bot.reply_to(message, '''Пользователя нет в базе.
Для добавления пользователя в базу используйте 
команду [/add_user]
в ответ на сообщение пользователя.''')
            user_id = ''
        return
        try:
            bot.kick_chat_member(chat_id, user_id)
            bot.reply_to(message, f"Котёнок {ban_count[1]} был забанен.")
            ban_list.append(message.from_user.id)
            bans_id_add(message)
            user_id = ''
        except:
            bot.reply_to(message, f"Котёнок {ban_count[1]} не забанен.")
            user_id = ''
    else:
        bot.reply_to(message, "У вас нет прав для использования этой команды.")




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
            bot.reply_to(message,"У вас нет прав для использования данной команды.")
    elif user_id in mute_list:
        mute_list.remove(message.from_user.id)
        bot.reply_to(message, 'Произошла ошибка, попробуйте ещё раз.')


# @bot.message_handler(commands=['unmute_user'])
# def unban_user(message):
#     global user_id
#     chat_id = message.chat.id
#     user_id1 = message.from_user.id
#     user_status = bot.get_chat_member(chat_id, user_id1).status
#     if user_status == 'administrator' or user_status == 'creator':
#         g


@bot.message_handler(commands=['mute_user'])
def mute_user(message):
    global user_id
    chat_id1 = message.chat.id
    user_id1 = message.from_user.id
    user_status = bot.get_chat_member(chat_id1, user_id1).status
    if user_status == 'administrator' or user_status == 'creator':
        text_mute = message.text
        mute_count = text_mute.split(' ')
        duration = 60
        min = duration * 1
        hour = duration * 60
        day = duration * 1440
        week = duration * 10080
        try:
            with open('users_id.txt') as file:
                lines = file.read().splitlines()
            dic = {}
            for line in lines:
                key, value = line.split(': ')
                dic.update({key: value})
            user_id_go = dic[mute_count[1] + ' ']
            user_id = int(user_id_go)
        except:
            bot.reply_to(message, '''Пользователя нет в базе.
Для добавления пользователя в базу используйте 
команду [/add_user]
в ответ на сообщение пользователя.''')
            user_id = ''
        return
        try:
            if mute_count[3] == 'min':
                bot.restrict_chat_member(message.chat.id, user_id, until_date=time.time() + min * int(mute_count[2]))
                bot.reply_to(message,f"Котёнок {mute_count[1]} замучен на {mute_count[2]} минут.")
                mute_list.append(mute_count[1])
                user_id = ''
            elif mute_count[3] == 'hour':
                bot.restrict_chat_member(message.chat.id, user_id, until_date=time.time() + hour * int(mute_count[2]))
                bot.reply_to(message,f"Котёнок {mute_count[1]} замучен на {mute_count[2]} минут.")
                mute_list.append(mute_count[1])
                user_id = ''
            elif mute_count[3] == 'day':
                bot.restrict_chat_member(message.chat.id, user_id, until_date=time.time() + day * int(mute_count[2]))
                bot.reply_to(message,f"Котёнок {mute_count[1]} замучен на {mute_count[2]} минут.")
                mute_list.append(mute_count[1])
                user_id = ''
            elif mute_count[3] == 'week':
                bot.restrict_chat_member(message.chat.id, user_id, until_date=time.time() + week * int(mute_count[2]))
                bot.reply_to(message,f"Котёнок {mute_count[1]} замучен на {mute_count[2]} минут.")
                mute_list.append(mute_count[1])
                user_id = ''
        except:
            bot.reply_to(message, '''Котёнок является частью персонала группы или время указанно некорректно.
Для получения примеров использования команд используйте [/admin_examples]''')
            user_id = ''
    else:
        bot.reply_to(message, "У вас нет прав для использования данной команды.")




@bot.message_handler(commands=['mute_list'])
def mute_user(message):
    try:
        if len(mute_list) == 0:
            bot.reply_to(message, '0')
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
        mutes_id_add(message)
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


def send_rules(message):
    try:
        f = open('rules.txt', 'r', encoding='utf-8')
        rules_content = f.read()
        bot.reply_to(message, rules_content)
        f.close()
    except:
        bot.reply_to(message, 'Котёнок, правила для этого чата ещё не установлены.')

def send_commands(message):
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

def file_to_dict():
    file = open("users_id.txt")
    onstring = file.read().split("\n")[:-1]
    dict = dict()
    for item in onstring:
        key = item.split(" ")[0]
        value = item.split(" ")[1:]
        dict[key] = value
    file.close()


def users_id_add(message):
    user_id = message.reply_to_message.from_user.id
    with open('bans.txt', 'r') as original:
        data = original.read()
    with open('bans.txt', 'w') as modified:
        modified.write('@' + message.reply_to_message.from_user.username + ' : '+ user_id + '\n' + data)


if __name__ == '__main__':
    bot.polling(none_stop=True)



