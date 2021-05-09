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

lastUpdate = ''

blacklist=[]

customText = ''

customDocument = ''

customImage = ''

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






# @bot.message_handler(commands=['bulk'])
# def bulk(message):
#     """ Sending Large Text Messages """

#     large_text = open("New Text Document.txt", "rb").read()

#     # Split the bulk text each 3000 characters and return a list with splitted text.
#     split_text = util.split_string(large_text, 3000)

#     for text in split_text:
#         bot.reply_to(message, text)




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




# def forceReply():
#     markup = types.ForceReply(selective=False)
#     q = bot.send_message(admin, "Send me the message:", reply_markup=markup)
#     bot.register_next_step_handler(message=q, callback=customMessage)


def customDoc(msg):
    """Confirming Custom Document """
    
    global customDocument

    # Adding keyboard custom replies to keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text="Yes", callback_data='yes')
    b = types.InlineKeyboardButton(text="No", callback_data='no')
    keyboard.add(a,b)

    # Saving Custom Document
    customDocument = msg.document
    print(customDocument)
    print(customDocument.file_id)

    # Ask Admin Confirmation to Send Document 
    question = bot.send_message(
        msg.from_user,
        f"Do you wish to send {customDocument.file_name} to all stored users in the database?",
        reply_markup=keyboard
    )

    return customDocument

    pass


def customImg(msg):
    """Confirming Custom Image """
    
    global customImage

    # Adding keyboard custom replies to keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text="Yes", callback_data='yes')
    b = types.InlineKeyboardButton(text="No", callback_data='no')
    keyboard.add(a,b)

    # Saving Custom Document
    customDocument = msg.text

    # Ask Admin Confirmation to Send Document 
    question = bot.send_message(
        msg.from_user,
        f"Do you wish to send {msg.text} to all stored users in the database?",
        reply_markup=keyboard
    )

    # return customDocument
    pass





def customMessage(msg):
    """Confirming Custom Text/Link"""

    global customText
    
    # Adding keyboard custom replies to keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text="Yes", callback_data='yes')
    b = types.InlineKeyboardButton(text="No", callback_data='no')
    keyboard.add(a,b)

    # Save custom message
    if len(msg.text) > 5000: #sending large messages
        split_text = util.split_string(customText, 3000) # Split the text each 3000 characters, split_string returns a list with the splitted text.
        for text in split_text:
            customText = text

    else:
        customText = msg.text
    
    

    # Send Question
    question = bot.send_message(
        msg.from_user.id,
        f"Do you wish to send '{msg.text}' to all stored users in database?",
        reply_markup=keyboard
    )

    return customText






@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    """ Confirm User's Input """

    if call.data == "docs":
        markup = types.ForceReply(selective=False)
        q = bot.send_message(admin, "Send me the message:", reply_markup=markup)
        bot.register_next_step_handler(message=q, callback=customDoc)
    
        
        

    if call.data == "image":
        markup = types.ForceReply(selective=False)
        q = bot.send_message(admin, "Send me the message:", reply_markup=markup)
        bot.register_next_step_handler(message=q, callback=customImg)
        
        
    if call.data == "link":
        markup = types.ForceReply(selective=False)
        q = bot.send_message(admin, "Send me the message:", reply_markup=markup)
        bot.register_next_step_handler(message=q, callback=customMessage)
       

    if call.data == "text":
        markup = types.ForceReply(selective=False)
        q = bot.send_message(admin, "Send me the message:", reply_markup=markup)
        bot.register_next_step_handler(message=q, callback=customMessage)

        
    if call.data == 'yes':
        messageUsers()

    if call.data == 'no':
        bot.send_message(call.from_user.id, "Thanks for using this service.")





def messageUsers():
    """ Sends The Custom Message"""

    global lastUpdate
    runTime = time.localtime()
    # Updating admin on last time messages were sent
    lastUpdate = f"A Custom Message was last sent on {runTime.tm_mday}/{runTime.tm_mon}/{runTime.tm_year}."

    # Send Custom Message
    bot.send_chat_action(admin, action='typing')
    bot.send_message(admin, "Your custom message is being sent to users in the database.")

    # Iterating through the list of users and send message
    database = sheet.get_all_records()
    [bot.send_message(admin, f"{data} {customText} ----- Reply “Unsubsribe” to Unsubscribe from this servie.") for data in database if data not in blacklist]

    # Custom Message Sent Successful
    bot.send_message(admin, "Successfully sent to all Users in the Database.")


    return lastUpdate



@bot.message_handler(commands=['status'])
def status(msg):
    """ Displays Record of Most Recent Action """

    if msg.from_user.id != admin:
        bot.reply_to(msg, "Unauthorized User!")

    else:
        bot.reply_to(msg, lastUpdate)
        


@bot.message_handler(commands=['Unsubscribe'])
def unsubscribe(msg):
    """Unsubscribe The User From Receiving Messages"""

    global blacklist

    user = msg.from_user.id

    # Add user to blacklist
    if user not in blacklist:
        blacklist.append(user)

    # Send to User
    bot.send_message(user, "You have successfully unsubsribed from this service!")

    return blacklist





# Keep bot live
print("Bot running.....")

bot.polling(none_stop=True)
while True:
    pass

