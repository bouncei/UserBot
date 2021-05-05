from telebot import TeleBot, util, types

bot_token = "1727697640:AAERXgE0dkMYVgAzVP-AgRr97MVuuDK4DJg"

api_id = "1896641"

api_hash = "00a354721554e421af6168db0a972ecf"

admin = 1190069449

customText = ''

bot = TeleBot(token=bot_token)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    """This initiates the bot into action"""
    bot.reply_to(message, f'Hey, welcome {user.first_name}.')

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     """Echoes all incoming text messages back to the sender"""
#     bot.reply_to(message, message.text)


@bot.message_handler(commands=['contentmessage'])
def start(message):

    """ Start Conversation With Admin"""

    if message.from_user.id != admin:

        bot.reply_to(message, "Unauthorized User!")


    else:
        bot.reply_to(message, "Hello Dave")
        # markup = types.ReplyKeyboardMarkup(row_width=2)
        # itembtn1 = types.KeyboardButton('a')
        # itembtn2 = types.KeyboardButton('v')
        # itembtn3 = types.KeyboardButton('d')
        # markup.add(itembtn1, itembtn2, itembtn3)
        # bot.send_message(admin, "Choose one letter:", reply_markup=markup)

        question = bot.send_message(admin, "What would you like to send today?")
        bot.register_next_step_handler(message=question, callback=customMessage)


def customMessage(msg):
    """Confirming Custom Message"""

    global customText
    
    # Adding keyboard custom replies to keyboard
    mark_up = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text="Yes", callback_data='yes')
    b = types.InlineKeyboardButton(text="No", callback_data='no')
    mark_up.add(a,b)

    # Save custom message
    customText = msg.text 

    # Send Question
    question = bot.send_message(
        msg.from_user.id,
        f"Do you wish to send '{msg.text}' to all stored users in database?",
        reply_markup=mark_up
    )

    return customText







@bot.message_handler(commands=['bulk'])
def bulk(message):
    """ Sending A Large Text Messages """

    large_text = open("New Text Document.txt", "rb").read()

    # Split the text each 3000 characters.
    # split_string returns a list with the splitted text.
    split_text = util.split_string(large_text, 3000)

    for text in split_text:
        bot.reply_to(message, text)
    











# user = bot.get_me()
# print(user)






# Keep bot live
print("Bot running.....")

bot.polling(none_stop=True)
while True:
    pass

