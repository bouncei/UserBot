from config import *

def forceReply():
    markup = types.ForceReply(selective=False)
    q = bot.send_message(admin, "Send me the message:", reply_markup=markup)
    
    return q #return a force reply question to admin




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
        bot.reply_to(msg, "Wrong input, expected an image file. Please send the command (/contentmessage) again.")
        pass


    
    # Saving Custom Image   
    return customImage
        
        
        
   

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