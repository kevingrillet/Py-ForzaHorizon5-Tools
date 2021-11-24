import time

import pyautogui

from game import constant
from game.autocarbuy import AutoCarBuy
from game.autocarbuyleastexpensive import AutoCarBuyLeastExpensive
from game.autocarmastery import AutoCarMastery
from game.autogpsdestination import AutoGPSDestination
from game.autolabreplay import AutoLabReplay
from game.autowheelspins import AutoWheelspins
from game.common import GameCommon
from utils import common
from utils.constant import DebugLevel, Lang
from utils.handlerconfig import HandlerConfig
from utils.handlercv2 import HandlerCv2


def load_config():
    hcfg = HandlerConfig("config.ini")
    constant.DEBUG_LEVEL = DebugLevel(int(hcfg.get_value("debug")))
    constant.DEV_MODE = hcfg.get_value("dev") == "True"
    constant.LANG = Lang(hcfg.get_value("language"))
    constant.SCALE = float(hcfg.get_value("scale"))


def show_menu():
    print(" ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(" ┃   Py-ForzaHorizon5-Tools     ┃")
    print(" ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print(" ┃ 1 - AutoWheelspins           ┃")
    print(" ┃ 2 - AutoGPSDestination       ┃")
    print(" ┃ 3 - AutoLabReplay            ┃")
    print(" ┃ 4 - AutoCarBuy               ┃")
    print(" ┃ 5 - ⚠ AutoCarMastery ⚠       ┃")
    print(" ┃ 6 - AutoCarBuyLeastExpensive ┃")
    print(" ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print("Your choice:")


if __name__ == "__main__":
    load_config()
    show_menu()
    intinput = int(input())
    hcv2 = HandlerCv2(scale=constant.SCALE)
    if intinput == 1:
        AutoWheelspins(hcv2).run()
    elif intinput == 2:
        AutoGPSDestination(hcv2).run()
    elif intinput == 3:
        AutoLabReplay(hcv2).run()
    elif intinput == 30:
        common.alt_tab()
        AutoLabReplay(hcv2, stop_on_max_mastery=True).run()
        time.sleep(10)
        common.alt_f4()
    elif intinput == 4:
        AutoCarBuy(hcv2).run()
    elif intinput == 5:
        AutoCarMastery(hcv2).run()
    elif intinput == 6:
        AutoCarBuyLeastExpensive(hcv2).run()
    elif intinput == 0:
        hcv2.hwin32.list_window_names()
        hcv2.dev()
    elif intinput == 99:
        common.alt_tab()
        pyautogui.press("esc")
        pyautogui.keyDown("z")
    elif intinput == 45:
        common.alt_tab()
        GameCommon.AutoCarBuy_Then_AutoCarMastery(AutoCarBuy(hcv2), AutoCarMastery(hcv2), 70)
    elif intinput == 453:
        common.debug("AutoCarBuy + AutoCarMastery + AutoLabReplay")
        gc = GameCommon()
        acb = AutoCarBuy(hcv2)
        acm = AutoCarMastery(hcv2)
        alr = AutoLabReplay(hcv2, gc, True)
        common.alt_tab()
        common.click_then_sleep((10, 10), .125)
        common.press_then_sleep("esc", 2)
        if gc.check_mastery():
            gc.AutoCarBuy_Then_AutoCarMastery_from_menu_to_menu(acb, acm)
        running = True
        while running:
            alr.run()
            gc.AutoCarBuy_Then_AutoCarMastery_from_menu_to_menu(acb, acm)
            # running = gc.check_super_wheelspins()
        time.sleep(5)
        common.alt_f4()
    else:
        raise NameError("Not an option")
