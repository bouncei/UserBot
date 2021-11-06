from config import *

def menu(msg):
    mark_up = types.InlineKeyboardMarkup(row_width=2)
        
    b = types.InlineKeyboardButton(text="Image", callback_data='image')
    c = types.InlineKeyboardButton(text="Link", callback_data='link')
    d = types.InlineKeyboardButton(text="Text", callback_data='text')

    mark_up.row(b)
    mark_up.row(c, d)



@bot.message_handler(commands=['start'])
def start(message):

    """ Start Conversation With Admin"""

    if message.from_user.id != admin:

        bot.reply_to(message, "Unauthorized User!")


    else:
        bot.reply_to(message, "Hello Dave.")
        

        # text = "What would you like to send today?"

        
        quest = bot.send_message(admin, "What would you like to send today?", reply_markup=menu(message))