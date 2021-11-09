# Importing the needed variables
import telebot
from telebot import TeleBot, util, types
import logging
import time
import requests
import json
import pprint
import csv
from flask import Flask, request
import os



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



# Setup Logging
logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)  # Outputs debug messages to console.
logging.basicConfig(filename='Log_file.log', format='%(levelname)s: %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S') # saves debug messages in a file(Log_file.log)

### Define Variables ###

bot_token = "1727697640:AAERXgE0dkMYVgAzVP-AgRr97MVuuDK4DJg"

admin = 1190069449     ## PLEASE ADD YOUR CHAT ID HERE ##

bot = TeleBot(token=bot_token)

server = Flask(__name__)

import importdir
importdir.do("main", globals())
