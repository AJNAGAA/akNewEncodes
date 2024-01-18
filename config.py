import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "26180117")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "fa5e31c8139703d6ab8f11f817e8d450") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6315721888:AAG_v8F38OIDp0DNxI32LEBqfH2kZCp6agE") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1001575860161') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://appibeans06:appibeans06@cluster0.mzkon6e.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","Cluster0") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "6166648132")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002006007017')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/5d0e09278a78ea7c517f4.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Encoded Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
