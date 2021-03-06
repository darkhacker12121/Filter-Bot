# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os

def get_user_list(config, key):
    with open('{}/bot/{}'.format(os.getcwd(), config), 'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1423025003:AAHTvOTARswwuPoMwv55lXceIQvbZhUzD8A"
    OWNER_ID = "1131653685"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "kavinduaj"
    OWNER_NAME = "KAvindu AJ"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgresql://filterbot:dkkaj0123456@postgresql/postgres'  # needed for any database modules
    WEBHOOK = True
    URL = None

    # OPTIONAL
    #ID Seperation format [1,2,3,4]
    SUDO_USERS = get_user_list('elevated_users.json', 'sudos')  # List of id's -  (not usernames) for users which have sudo access to the bot.
    DEV_USERS = get_user_list('elevated_users.json', 'devs')  # List of id's - (not usernames) for developers who will have the same perms as the owner
    SUPPORT_USERS = get_user_list('elevated_users.json', 'supports')  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = get_user_list('elevated_users.json', 'whitelists')  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    ALLOW_EXCL = True  # Allow ! commands as well as /
    
   
  
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
