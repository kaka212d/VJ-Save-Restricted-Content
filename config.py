import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7843258567:AAHEIGkPz8ejpu6Z9baINbPeslUPKvDg0uM")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29394091"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "018cd3c9df6204212cd4ecf2063c273d")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "1687889706"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://jbi65230:TSwjS6MJ0pCeFZoT@cluster0.1ximvfd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
