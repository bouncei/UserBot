############################################################################################################################################################################
############################################################################################################################################################################

## This code was written by Bouncei
## Compactible with Python3 Interpreter

############################################################################################################################################################################
############################################################################################################################################################################

## This is a telegram user bot that interacts only with the Admin
## To activate the automatic forwarding of a custom message
## To all users in the Google Sheet Database

############################################################################################################################################################################


# Importing the needed variables
import telebot
from telebot import TeleBot, util, types
import logging
import time


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

        text = "What would you like to send today?"
        mark_up = types.InlineKeyboardMarkup(row_width=2)
        a = types.InlineKeyboardButton(text="Document", callback_data='docs')
        b = types.InlineKeyboardButton(text="Image", callback_data='image')
        c = types.InlineKeyboardButton(text="Link", callback_data='link')
        d = types.InlineKeyboardButton(text="text", callback_data='text')
        mark_up.row(a,b)
        mark_up.row(c, d)
        quest = bot.send_message(admin, "What would you like send", reply_markup=mark_up)

        # bot.register_next_step_handler(message=quest, callback=customMessage)


        # A question to the admin   
        # question = bot.send_message(admin, "What would you like to send today?")
        # bot.register_next_step_handler(message=question, callback=customMessage)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    """ """

    if call.data == "docs":
        forceReply()
        

    if call.data == "image":
        forceReply()
        
    if call.data == "link":
       forceReply()

    if call.data == "text":
        forceReply()
        
    if call.data == 'yes':
        messageUsers()

    if call.data == 'no':
        bot.send_message(call.from_user.id, "Thanks for using this service.")


def forceReply():
    markup = types.ForceReply(selective=False)
    q = bot.send_message(admin, "Send me the message:", reply_markup=markup)
    bot.register_next_step_handler(message=q, callback=customMessage)


def customMessage(msg):
    """Confirming Custom Message"""

    global customText
    
    # Adding keyboard custom replies to keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text="Yes", callback_data='yes')
    b = types.InlineKeyboardButton(text="No", callback_data='no')
    keyboard.add(a,b)

    # Save custom message
    customText = msg.get_file()
    
    print(customText)

    # Send Question
    question = bot.send_message(
        msg.from_user.id,
        f"Do you wish to send '{msg.document('file_name')}' to all stored users in database?",
        reply_markup=keyboard
    )

    return customText


@bot.callback_query_handler(func=lambda check: True)
def checktext(check):
    """ Confirm User's Input"""





def messageUsers():
    """ Sends The Custom Message"""






    











# user = bot.get_me()
# print(user)






# Keep bot live
print("Bot running.....")

bot.polling(none_stop=True)
while True:
    pass

