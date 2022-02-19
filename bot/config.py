import os


class Config:

    API_ID = 5019679
    API_HASH = "a25681486dc94d31353e99384da28521"
    BOT_TOKEN = "1938116581:AAG9-EA5p77NG_ABKboXoEUsbVEHV5N3OaY"
    SESSION_NAME = "imjerin"
    LOG_CHANNEL = -1001302779504
    DATABASE_URL = "mongodb+srv://jerinjohny:jerinjohny@cluster0.jk3zi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    AUTH_USERS = [1329457821]
    MAX_PROCESSES_PER_USER = int(os.environ.get("MAX_PROCESSES_PER_USER", 2))
    MAX_TRIM_DURATION = int(os.environ.get("MAX_TRIM_DURATION", 600))
    TRACK_CHANNEL = -1001302779504
    SLOW_SPEED_DELAY = 0
    HOST = "http://localhost:8080"
    TIMEOUT = int(os.environ.get("TIMEOUT", 60 * 30))
    DEBUG = bool(os.environ.get("DEBUG"))
    WORKER_COUNT = int(os.environ.get("WORKER_COUNT", 20))
    IAM_HEADER = os.environ.get("IAM_HEADER", "")

    COLORS = [
        "white",
        "black",
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "purple",
        "brown",
        "gold",
        "silver",
        "pink",
    ]
    FONT_SIZES_NAME = ["Small", "Medium", "Large"]
    FONT_SIZES = [30, 40, 50]
    POSITIONS = [
        "Top Left",
        "Top Center",
        "Top Right",
        "Center Left",
        "Centered",
        "Center Right",
        "Bottom Left",
        "Bottom Center",
        "Bottom Right",
    ]
