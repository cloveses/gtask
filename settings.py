import os

port = 8000

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
CURRENT_PATH = os.path.dirname(CURRENT_PATH)
HDL_DIR = ["hdls",]
web_server = {
    # 'xsrf_cookies': True,
    'cookie_secret': "jjjhjtyy656#%^@##%^&(*(ghgy6FFFH(*^$#%&yhkgGTG",
    # 'cookie_expires': 86400,
    # 'autoescape': None,
    'debug': True,
}
