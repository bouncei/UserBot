from config import *


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



