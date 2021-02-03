from bot.sample_config import Config


class Development(Config):
    ALLOW_EXCL = True
    OWNER_ID = 1131653685  # my telegram ID
    OWNER_NAME = "ㅤㅤㅤㅤㅤ"
    OWNER_USERNAME = "kavinduaj"  # my telegram username
    API_KEY = "1423025003:AAHTvOTARswwuPoMwv55lXceIQvbZhUzD8A"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://filterbot:dkkaj0123456@postgresql/postgres'  # sample db credentials
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [1131653685]  # List of id's for users which have sudo access to the bot.
    SPAMMERS = "123456"
    SW_API = "DFOm~tAD3jGW_l_pxisfl1FETDTytFaz831fAciaKZg9kCoAYuPAP0lYSO5QDdbC"
    START_IMG = "https://telegra.ph/file/fc734b227985a1524e715.jpg"

