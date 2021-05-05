import telebot
from telebot import TeleBot, util, types
import logging


### Define Variables ###

bot_token = "1727697640:AAERXgE0dkMYVgAzVP-AgRr97MVuuDK4DJg"

api_id = "1896641"

api_hash = "00a354721554e421af6168db0a972ecf"

admin = 1190069449

customText = ''

bot = TeleBot(token=bot_token)


# Setup Logging
logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)  # Outputs debug messages to console.
logging.basicConfig(filename='Log_file.log', format='%(levelname)s: %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S') # saves debug messages in a file(Log_file.log)



@bot.message_handler(commands=['start', 'help'])
def start(message):
    """This initiates the bot into action"""
    user = message.from_user

    bot.reply_to(message, f'Hey, welcome {user.first_name}.')




# Echos back message to the user
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     """Echoes all incoming text messages back to the sender"""
#     bot.reply_to(message, message.text)

@bot.message_handler(commands=['bulk'])
def bulk(message):
    """ Sending Large Text Messages """

    large_text = open("New Text Document.txt", "rb").read()

    # Split the bulk text each 3000 characters and return a list with splitted text.
    split_text = util.split_string(large_text, 3000)

    for text in split_text:
        bot.reply_to(message, text)




@bot.message_handler(commands=['contentmessage'])
def start(message):

    """ Start Conversation With Admin"""

    if message.from_user.id != admin:

        bot.reply_to(message, "Unauthorized User!")


    else:
        bot.reply_to(message, "Hello Dave")

        text = "WHAT DO YOU WANT?"
        mark_up = types.InlineKeyboardMarkup(row_width=2)
        a = types.InlineKeyboardButton(text="Document", callback_data='yes')
        b = types.InlineKeyboardButton(text="Image", callback_data='no')
        c = types.InlineKeyboardButton(text="Link", callback_data='yes')
        d = types.InlineKeyboardButton(text="text", callback_data='no')
        mark_up.row(a,b)
        mark_up.row(c, d)
        bot.send_message(admin, text, reply_markup=mark_up)




        # A question to the admin   
        question = bot.send_message(admin, "What would you like to send today?")
        bot.register_next_step_handler(message=question, callback=customMessage)



def customMessage(msg):
    """Confirming Custom Message"""

    global customText
    
    # Adding keyboard custom replies to keyboard
    mark_up = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text="yes", callback_data='yes')
    b = types.InlineKeyboardButton(text="no", callback_data='no')
    mark_up.add(a,b)

    # mark_up = types.InlineReplyKeyboardMarkup()
    # a = types.InlinekeyboardButton('documents')
    # b = types.InlinekeyboardButton('images')
    # c = types.InlinekeyboardButton('links')
    # d = types.InlinekeyboardButton('text')

    # mark_up.row(a, b)
    # mark_up.row(c, d)

    # bot.send_message(admin, "Choose one letter:", reply_markup=markup)

    



    # Save custom message
    customText = msg.text 

    # Send Question
    question = bot.send_message(
        msg.from_user.id,
        f"Do you wish to send '{msg.text}' to all stored users in database?",
        reply_markup=mark_up
    )

    return customText








    











# user = bot.get_me()
# print(user)






# Keep bot live
print("Bot running.....")

bot.polling(none_stop=True)
while True:
    pass

