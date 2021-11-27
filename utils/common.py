import ctypes
import time
from datetime import datetime

import pyautogui

from game import constant
from utils.constant import DebugLevel


def alt_f4():
    """
    send alt + f4
    """
    keyDown("alt", .125)
    press("f4", 0)
    keyUp("alt")


def alt_tab():
    """
    send alt tab
    """
    keyDown("alt", .125)
    press("tab", 0)
    keyUp("alt")


def click(location: (int, int) = (0, 0), secs: float = .5, scale: float = 1):
    """
    click at location then sleep
    :param location:
    :param secs:
    :param scale:
    """
    if scale != 1:
        location = (int(location[0] * scale), int(location[1] * scale))
    moveTo(location)
    pyautogui.mouseDown()
    time.sleep(secs)
    pyautogui.mouseUp()
    moveTo((10, 10))


def debug(msg: str = "", debug_level: int = DebugLevel.ALWAYS):
    """
    print debug if enough level
    :param msg:
    :param debug_level:
    """
    if debug_level <= constant.DEBUG_LEVEL:
        print("[DEBUG] " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + " - " + msg)


def fps() -> float:
    """
    :return: fps
    """
    new_frame = time.time()
    timer = 1 / (new_frame - fps.frame)
    fps.frame = new_frame
    return timer


def keyDown(key: str, secs: float = 0):
    """
    press key then sleep x secs
    :param key:
    :param secs:
    """
    pyautogui.keyDown(key)
    sleep(secs)


def keyUp(key: str):
    """
    release key
    :param key:
    """
    pyautogui.keyUp(key)


def get_keyboard_language():
    # https://stackoverflow.com/a/66756115
    """
    Gets the keyboard language in use by the current
    active window process.
    """

    languages = {'0x436': "Afrikaans - South Africa", '0x041c': "Albanian - Albania", '0x045e': "Amharic - Ethiopia",
                 '0x401': "Arabic - Saudi Arabia", '0x1401': "Arabic - Algeria", '0x3c01': "Arabic - Bahrain",
                 '0x0c01': "Arabic - Egypt", '0x801': "Arabic - Iraq", '0x2c01': "Arabic - Jordan",
                 '0x3401': "Arabic - Kuwait", '0x3001': "Arabic - Lebanon", '0x1001': "Arabic - Libya",
                 '0x1801': "Arabic - Morocco", '0x2001': "Arabic - Oman", '0x4001': "Arabic - Qatar",
                 '0x2801': "Arabic - Syria", '0x1c01': "Arabic - Tunisia", '0x3801': "Arabic - U.A.E.",
                 '0x2401': "Arabic - Yemen", '0x042b': "Armenian - Armenia", '0x044d': "Assamese",
                 '0x082c': "Azeri (Cyrillic)", '0x042c': "Azeri (Latin)", '0x042d': "Basque", '0x423': "Belarusian",
                 '0x445': "Bengali (India)", '0x845': "Bengali (Bangladesh)", '0x141A': "Bosnian (Bosnia/Herzegovina)",
                 '0x402': "Bulgarian", '0x455': "Burmese", '0x403': "Catalan", '0x045c': "Cherokee - United States",
                 '0x804': "Chinese - People's Republic of China", '0x1004': "Chinese - Singapore",
                 '0x404': "Chinese - Taiwan", '0x0c04': "Chinese - Hong Kong SAR", '0x1404': "Chinese - Macao SAR",
                 '0x041a': "Croatian", '0x101a': "Croatian (Bosnia/Herzegovina)", '0x405': "Czech", '0x406': "Danish",
                 '0x465': "Divehi", '0x413': "Dutch - Netherlands", '0x813': "Dutch - Belgium", '0x466': "Edo",
                 '0x409': "English - United States", '0x809': "English - United Kingdom",
                 '0x0c09': "English - Australia", '0x2809': "English - Belize", '0x1009': "English - Canada",
                 '0x2409': "English - Caribbean", '0x3c09': "English - Hong Kong SAR", '0x4009': "English - India",
                 '0x3809': "English - Indonesia", '0x1809': "English - Ireland", '0x2009': "English - Jamaica",
                 '0x4409': "English - Malaysia", '0x1409': "English - New Zealand", '0x3409': "English - Philippines",
                 '0x4809': "English - Singapore", '0x1c09': "English - South Africa", '0x2c09': "English - Trinidad",
                 '0x3009': "English - Zimbabwe", '0x425': "Estonian", '0x438': "Faroese", '0x429': "Farsi",
                 '0x464': "Filipino", '0x040b': "Finnish", '0x040c': "French - France", '0x080c': "French - Belgium",
                 '0x2c0c': "French - Cameroon", '0x0c0c': "French - Canada",
                 '0x240c': "French - Democratic Rep. of Congo", '0x300c': "French - Cote d'Ivoire",
                 '0x3c0c': "French - Haiti", '0x140c': "French - Luxembourg", '0x340c': "French - Mali",
                 '0x180c': "French - Monaco", '0x380c': "French - Morocco", '0xe40c': "French - North Africa",
                 '0x200c': "French - Reunion", '0x280c': "French - Senegal", '0x100c': "French - Switzerland",
                 '0x1c0c': "French - West Indies", '0x462': "Frisian - Netherlands", '0x467': "Fulfulde - Nigeria",
                 '0x042f': "FYRO Macedonian", '0x083c': "Gaelic (Ireland)", '0x043c': "Gaelic (Scotland)",
                 '0x456': "Galician", '0x437': "Georgian", '0x407': "German - Germany", '0x0c07': "German - Austria",
                 '0x1407': "German - Liechtenstein", '0x1007': "German - Luxembourg", '0x807': "German - Switzerland",
                 '0x408': "Greek", '0x474': "Guarani - Paraguay", '0x447': "Gujarati", '0x468': "Hausa - Nigeria",
                 '0x475': "Hawaiian - United States", '0x040d': "Hebrew", '0x439': "Hindi", '0x040e': "Hungarian",
                 '0x469': "Ibibio - Nigeria", '0x040f': "Icelandic", '0x470': "Igbo - Nigeria", '0x421': "Indonesian",
                 '0x045d': "Inuktitut", '0x410': "Italian - Italy", '0x810': "Italian - Switzerland",
                 '0x411': "Japanese", '0x044b': "Kannada", '0x471': "Kanuri - Nigeria", '0x860': "Kashmiri",
                 '0x460': "Kashmiri (Arabic)", '0x043f': "Kazakh", '0x453': "Khmer", '0x457': "Konkani",
                 '0x412': "Korean", '0x440': "Kyrgyz (Cyrillic)", '0x454': "Lao", '0x476': "Latin", '0x426': "Latvian",
                 '0x427': "Lithuanian", '0x043e': "Malay - Malaysia", '0x083e': "Malay - Brunei Darussalam",
                 '0x044c': "Malayalam", '0x043a': "Maltese", '0x458': "Manipuri", '0x481': "Maori - New Zealand",
                 '0x044e': "Marathi", '0x450': "Mongolian (Cyrillic)", '0x850': "Mongolian (Mongolian)",
                 '0x461': "Nepali", '0x861': "Nepali - India", '0x414': "Norwegian (Bokmål)",
                 '0x814': "Norwegian (Nynorsk)", '0x448': "Oriya", '0x472': "Oromo", '0x479': "Papiamentu",
                 '0x463': "Pashto", '0x415': "Polish", '0x416': "Portuguese - Brazil", '0x816': "Portuguese - Portugal",
                 '0x446': "Punjabi", '0x846': "Punjabi (Pakistan)", '0x046B': "Quecha - Bolivia",
                 '0x086B': "Quecha - Ecuador", '0x0C6B': "Quecha - Peru", '0x417': "Rhaeto-Romanic",
                 '0x418': "Romanian", '0x818': "Romanian - Moldava", '0x419': "Russian", '0x819': "Russian - Moldava",
                 '0x043b': "Sami (Lappish)", '0x044f': "Sanskrit", '0x046c': "Sepedi", '0x0c1a': "Serbian (Cyrillic)",
                 '0x081a': "Serbian (Latin)", '0x459': "Sindhi - India", '0x859': "Sindhi - Pakistan",
                 '0x045b': "Sinhalese - Sri Lanka", '0x041b': "Slovak", '0x424': "Slovenian", '0x477': "Somali",
                 '0x042e': "Sorbian", '0x0c0a': "Spanish - Spain (Modern Sort)",
                 '0x040a': "Spanish - Spain (Traditional Sort)", '0x2c0a': "Spanish - Argentina",
                 '0x400a': "Spanish - Bolivia", '0x340a': "Spanish - Chile", '0x240a': "Spanish - Colombia",
                 '0x140a': "Spanish - Costa Rica", '0x1c0a': "Spanish - Dominican Republic",
                 '0x300a': "Spanish - Ecuador", '0x440a': "Spanish - El Salvador", '0x100a': "Spanish - Guatemala",
                 '0x480a': "Spanish - Honduras", '0xe40a': "Spanish - Latin America", '0x080a': "Spanish - Mexico",
                 '0x4c0a': "Spanish - Nicaragua", '0x180a': "Spanish - Panama", '0x3c0a': "Spanish - Paraguay",
                 '0x280a': "Spanish - Peru", '0x500a': "Spanish - Puerto Rico", '0x540a': "Spanish - United States",
                 '0x380a': "Spanish - Uruguay", '0x200a': "Spanish - Venezuela", '0x430': "Sutu", '0x441': "Swahili",
                 '0x041d': "Swedish", '0x081d': "Swedish - Finland", '0x045a': "Syriac", '0x428': "Tajik",
                 '0x045f': "Tamazight (Arabic)", '0x085f': "Tamazight (Latin)", '0x449': "Tamil", '0x444': "Tatar",
                 '0x044a': "Telugu", '0x041e': "Thai", '0x851': "Tibetan - Bhutan",
                 '0x451': "Tibetan - People's Republic of China", '0x873': "Tigrigna - Eritrea",
                 '0x473': "Tigrigna - Ethiopia", '0x431': "Tsonga", '0x432': "Tswana", '0x041f': "Turkish",
                 '0x442': "Turkmen", '0x480': "Uighur - China", '0x422': "Ukrainian", '0x420': "Urdu",
                 '0x820': "Urdu - India", '0x843': "Uzbek (Cyrillic)", '0x443': "Uzbek (Latin)", '0x433': "Venda",
                 '0x042a': "Vietnamese", '0x452': "Welsh", '0x434': "Xhosa", '0x478': "Yi", '0x043d': "Yiddish",
                 '0x046a': "Yoruba", '0x435': "Zulu", '0x04ff': "HID (Human Interface Device)"}

    user32 = ctypes.WinDLL('user32', use_last_error=True)

    # Get the current active window handle
    handle = user32.GetForegroundWindow()

    # Get the thread id from that window handle
    threadid = user32.GetWindowThreadProcessId(handle, 0)

    # Get the keyboard layout id from the threadid
    layout_id = user32.GetKeyboardLayout(threadid)

    # Extract the keyboard language id from the keyboard layout id
    language_id = layout_id & (2 ** 16 - 1)

    # Convert the keyboard language id from decimal to hexadecimal
    language_id_hex = hex(language_id)

    # Check if the hex value is in the dictionary.
    if language_id_hex in languages.keys():
        return languages[language_id_hex]
    else:
        # Return language id hexadecimal value if not found.
        return str(language_id_hex)


def moveTo(location: (int, int) = (0, 0), secs: float = .5, scale: float = 1):
    """
    move mouse to location then sleep
    :param location:
    :param secs:
    :param scale:
    """
    if scale != 1:
        location = (int(location[0] * scale), int(location[1] * scale))
    pyautogui.moveTo(location)
    sleep(secs)


def press(key: str, secs: float = .5):
    """
    press key then sleep x secs
    :param key:
    :param secs:
    """
    pyautogui.press(key)
    sleep(secs)


def scroll(clicks: int = 1, location: (int, int) = (0, 0), secs: float = .5, scale=1):
    """
    Scroll at location then sleep x secs
    :param scale:
    :param clicks:
    :param location:
    :param secs:
    :return:
    """
    if scale != 1:
        location = (int(location[0] * scale), int(location[1] * scale))
    moveTo(location, secs)
    pyautogui.scroll(clicks)
    moveTo((10, 10), secs)


def sleep(secs: float = 0):
    """
    sleep for x secs
    :param secs:
    """
    time.sleep(secs)


def warn(msg: str = ""):
    """
    print warn
    :param msg:
    """
    print("[WARN ] " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + " - " + msg)


# https://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
fps.frame = time.time()
