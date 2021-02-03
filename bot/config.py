from bot.sample_config import Config


class Development(Config):
    OWNER_ID = 1131653685  # my telegram ID
    OWNER_USERNAME = "kavinduaj"  # my telegram username
    API_KEY = "1423025003:AAHxRn9YSX2N73S72QadcImmwPH_4JQhyjU"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://filterbot:dkkaj0123456@postgresql/postgres'  # sample db credentials
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [1131653685]  # List of id's for users which have sudo access to the bot.
