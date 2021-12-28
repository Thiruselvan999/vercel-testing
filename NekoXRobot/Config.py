
#MIT License
#Copyright (C) 2017-2019, Paul Larsen
#Copyright (C) 2021 Horimaya
#Copyright (c) 2021, Yūki • Black Knights Union, <https://github.com/Hodacka>
#This file is part of @NekoXRobot (Telegram Bot)
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/NekoXRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "8564523"
    API_HASH = "1a39289e7dc9aa69b32683dc2adfc875"
    BOT_ID = "2098257484"
    TOKEN = "2098257484:AAGgg4x3n2EUNoFRLQiJvFFhaAePvspqY4k"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1989750989  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "HMF_OWNER_1"
    SUDO_USERS = "1989750989"
    SUPPORT_USERS = "1989750989"
    SUPPORT_CHAT = "Stuxnet_1_official"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001648239341
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001648239341
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "something://somewhat:user@hosturl:port/databasename"  # needed for any database modules
    REDIS_URI = "http://redis-19313.c275.us-east-1-4.ec2.cloud.redislabs.com:19313"


    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    INFOPIC = True
    URL = None
    HEROKU_API_KEY = ""
    HEROKU_APP_NAME = ""
    BOT_USERNAME = "XAlpha_robot"
    SPAMWATCH_API = "ucc_ZXjpLaOloFk_72qZhjfsk4whMUd8P3Ue2gkj1HoIVzAxpDW9yxBy52MkDFuu"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    ARQ_API_KEY = "UDJYNO-IDNNXL-UMMVGP-ONRTBG-ARQ"
    ARQ_API_URL = "https://thearq.tech/"
    TEMP_DOWNLOAD_DIRECTORY = "./"
    OPENWEATHERMAP_ID = ""
    VIRUS_API_KEY =
    REDIS_URL = "redis://:p9a119a1f3289a38d90303f6e79207dcfa2e1979acf1370a843863f9fbab9a9ae@ec2-44-198-197-51.compute-1.amazonaws.com:20559"
    LASTFM_API_KEY = ""
    ALLOW_CHATS = "True"
    

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    ALLOW_CHATS = ""
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    WHITELIST_USERS = get_user_list("elevated_users.json", "whitelists")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "V7NS1NBFEL4X24L6"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "xyz"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "2AS711XS1O9B"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = ""  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    REM_BG_API_KEY = "dxsh728mZMDmj4ijSZCNPZig"
    GENIUS_API_TOKEN = "LstbAM4nzj2txUk2DGKh-PC0z6BxY1JYhMxMdj1NdRtmm7B7XYs0WcYBj4bFLK"
    MONGO_DB = "mongodb+srv://xforce:xforce@cluster0.2glge.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    STRING_SESSION = ""
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
