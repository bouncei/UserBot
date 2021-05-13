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

from config import *


lastUpdate = ''

blacklist=[]

database = []

customText = ''

customDocument = ''

fileName = ''

customImage = ''


with open('Test.csv', 'r', encoding="utf8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        database.append(row['USERID'])





@bot.message_handler(commands=['contentmessage'])
def start(message):

    """ Start Conversation With Admin"""

    if message.from_user.id != admin:

        bot.reply_to(message, "Unauthorized User!")


    else:
        bot.reply_to(message, "Hello Dave.")
        

        text = "What would you like to send today?"
        mark_up = types.InlineKeyboardMarkup(row_width=2)
        a = types.InlineKeyboardButton(text="Document", callback_data='docs')
        b = types.InlineKeyboardButton(text="Image", callback_data='image')
        c = types.InlineKeyboardButton(text="Link", callback_data='link')
        d = types.InlineKeyboardButton(text="Text", callback_data='text')
        mark_up.row(a,b)
        mark_up.row(c, d)
        quest = bot.send_message(admin, "What would you like to send today?", reply_markup=mark_up)

        






def customDoc(msg):
    """Confirming Custom Document """
    
    global customDocument
    
    # Adding keyboard custom replies to keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text="Yes", callback_data='yes')
    b = types.InlineKeyboardButton(text="No", callback_data='no')
    keyboard.add(a,b)

    # Saving Custom Document
    if msg.document:

        file = msg.document

        r = requests.get(f'https://api.telegram.org/bot{bot_token}/getFile?file_id={file.file_id}') #Getting the required path information for the file
        filePath = r.json()['result']['file_path'] # Gets file path in javascript notation

        
        # customDocument = (f'https://api.telegram.org/file/bot{bot_token}/{filePath}')

        downloadDoc = bot.download_file(filePath)

        with open('new_doc.pdf', 'wb') as new_file:
            new_file.write(downloadDoc)  

        customDocument = open('new_doc.pdf', 'rb')


        time.sleep(1)
        # Ask Admin Confirmation to Send Document 
        question = bot.send_message(
            msg.from_user.id,
            f"Do you wish to send '{file.file_name}' to all stored users in the database?",
            reply_markup=keyboard
        )

    else:
        time.sleep(1)
        bot.reply_to(msg, "Wrong input, expected a pdf file. Please send the command(/contentmessage) again.")
        pass
            

    


    return customDocument


def customImg(msg):
    """Confirming Custom Image """
    
    global customImage

    # Adding keyboard custom replies to keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text="Yes", callback_data='yea')
    b = types.InlineKeyboardButton(text="No", callback_data='no')
    keyboard.add(a,b)

    if msg.content_type != "text":

        file = download_attachment(msg.photo)
        customImage = open(f"images/{fileName}", "rb").read()
        # Ask Admin Confirmation to Send Document 
        question = bot.send_message(
            msg.from_user.id,
            f"Do you wish to send this {fileName} to all stored users in the database?",
            reply_markup=keyboard
        )
        
    else:
        bot.reply_to(msg, "Wrong input, expected an image file. Please send the command(/contentmessage) again.")
        pass


    
    return customImage
        
    # Saving Custom Image   
        
        
    #     fileID = msg.photo[-1].file_id

        

    #     r = requests.get(f'https://api.telegram.org/bot{bot_token}/getFile?file_id={fileID}') #Getting the required path information for the file
        
    #     filePath = r.json()['result']['file_path'] # Gets file path in javascript notation

    #     name = filePath.split("/")[1]

    #     downloadImg = bot.download_file(filePath)

    #     with open('new_file.jpg', 'wb') as new_file:
    #         new_file.write(downloadImg) 

    #     customImage = open('new_file.jpg', 'rb')
        
    #     # customImage = (f'https://api.telegram.org/file/bot{bot_token}/{filePath}')


    #     time.sleep(1)
    #     # Ask Admin Confirmation to Send Document 
    #     question = bot.send_message(
    #         msg.from_user.id,
    #         f"Do you wish to send {name} to all stored users in the database?",
    #         reply_markup=keyboard
    #     )

    # else:
    #     bot.reply_to(msg, "Wrong input, expected an image file. Please send the command(/contentmessage) again.")

    #     pass

    # return customImage

def download_attachment(img):
    "Downloads the Attached Image File To Source Directory So It Can Be Reused"
    global fileName
    
    file_id = img[0].file_id

    file_url = bot.get_file_url(file_id)
    fileName = file_url.split("/")[-1]

    #Download image
    image = requests.get(file_url, allow_redirects=True)
    open(f"images/{fileName}", "wb").write(image.content)
    return fileName




def customMessage(msg):
    """Confirming Custom Text/Link"""

    global customText

    
    # Adding keyboard custom replies to keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text="Yes", callback_data='yes')
    b = types.InlineKeyboardButton(text="No", callback_data='no')
    keyboard.add(a,b)

    if msg.content_type == "text":
        # Save custom message
        customText = msg.text
        
        
        time.sleep(1)
        # Send Question
        question = bot.send_message(
            msg.from_user.id,
            f"Do you wish to send '{msg.text}' to all stored users in database?",
            reply_markup=keyboard
        )

    else:
        bot.reply_to(msg, "Wrong input, expected an image file. Please send the command(/contentmessage) again.")

        pass


    return customText



def forceReply():
    markup = types.ForceReply(selective=False)
    q = bot.send_message(admin, "Send me the message:", reply_markup=markup)
    
    return q #return a force reply question to admin




@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    """ Confirm User's Input """

    # check if the input is a document
    if call.data == "docs":
        bot.register_next_step_handler(message=forceReply(), callback=customDoc)
    
        
        
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


def imageUsers():
    """ Sends The Custom Image """

    global lastUpdate
    runTime = time.localtime()

    # Updating admin on last time messages were sent
    lastUpdate = f"A Custom Message was last sent on {runTime.tm_mday}/{runTime.tm_mon}/{runTime.tm_year}."

    # Send Custom Message
    bot.send_chat_action(admin, action='typing')
    bot.send_message(admin, "Your custom message is being sent to users in the database.")

    [bot.send_photo(f"{data}", customImage) for data in database if data not in blacklist]

    # Custom Image Sent Successful
    bot.send_message(admin, "Successfully sent to all Users in the Database.")



    return lastUpdate




def messageUsers():
    """ Sends The Custom Message"""

    global lastUpdate
    runTime = time.localtime()
    # Updating admin on last time messages were sent
    lastUpdate = f"A Custom Message was last sent on {runTime.tm_mday}/{runTime.tm_mon}/{runTime.tm_year}."

    # Send Custom Message
    bot.send_chat_action(admin, action='typing')
    bot.send_message(admin, "Your custom message is being sent to users in the database.")


  
    [bot.send_message(f"{data}", customText) for data in database if data not in blacklist]

    


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




# @server.route('/' + bot_token, methods=['POST'])
# def getMessage():
#     bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
#     return "!", 200

# @server.route("/")
# def webhook():
#     bot.remove_webhook()
#     bot.set_webhook(url='https://glacial-sea-44368.herokuapp.com/' + bot_token)
#     return "!", 200


# if __name__ == "__main__":
#     server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))




