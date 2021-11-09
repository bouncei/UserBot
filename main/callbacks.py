from main.start import *
from main.functions import *


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    """ Confirm User's Input """
   
        
        
    # check if the input is an image
    if call.data == "image":

        bot.register_next_step_handler(message=forceReply(), callback=customImg)
        
    # check if the input is a link
    if call.data == "link":
        
        bot.register_next_step_handler(message=forceReply(), callback=customMessage)
       
    # check if the input is a text message
    if call.data == "text":
        bot.register_next_step_handler(message=forceReply(), callback=customMessage)

        
    if call.data == 'yes':
        messageUsers()

    if call.data == "yea":
        imageUsers()

    if call.data == 'no':
        bot.send_message(call.from_user.id, "Thanks for using this service.")
