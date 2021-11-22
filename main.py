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
from utils.handlerconfig import HandlerConfig
from utils.handlercv2 import HandlerCv2


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
    hcfg = HandlerConfig("config.ini")
    constant.LANG = constant.Lang(hcfg.get_value("language", constant.LANG.value))
    constant.DEBUG_LEVEL = int(hcfg.get_value("debug", str(constant.DEBUG_LEVEL)))
    constant.DEV_MODE = hcfg.get_value("dev", str(constant.DEV_MODE)) == "True"

    show_menu()
    intinput = int(input())
    if intinput == 1:
        AutoWheelspins().run()
    elif intinput == 2:
        AutoGPSDestination().run()
    elif intinput == 3:
        AutoLabReplay().run()
    elif intinput == 30:
        common.alt_tab()
        AutoLabReplay(stop_on_max_mastery=True).run()
        time.sleep(10)
        common.alt_f4()
    elif intinput == 4:
        AutoCarBuy().run()
    elif intinput == 5:
        AutoCarMastery().run()
    elif intinput == 6:
        AutoCarBuyLeastExpensive().run()
    elif intinput == 0:
        hcv2 = HandlerCv2()
        hcv2.hwin32.list_window_names()
        hcv2.dev()
    elif intinput == 99:
        common.alt_tab()
        pyautogui.press("esc")
        pyautogui.keyDown("z")
    elif intinput == 45:
        hcv2 = HandlerCv2()
        common.alt_tab()
        GameCommon.AutoCarBuy_Then_AutoCarMastery(AutoCarBuy(hcv2), AutoCarMastery(hcv2), 70)
    elif intinput == 453:
        common.debug("AutoCarBuy + AutoCarMastery + AutoLabReplay")
        hcv2 = HandlerCv2()
        gc = GameCommon()
        acb = AutoCarBuy(hcv2)
        acm = AutoCarMastery(hcv2)
        alr = AutoLabReplay(hcv2, gc, True)
        common.alt_tab()
        common.click_then_sleep((10, 10), .125)
        first = True
        while True:
            if first and gc.check_mastery():
                gc.go_home_garage()
                gc.go_to_car_to_buy()
                GameCommon.AutoCarBuy_Then_AutoCarMastery(acb, acm, 70)
            else:
                gc.home_getmycar()
                common.press_then_sleep("esc", 10)
                common.press_then_sleep("esc", 5)
                alr.run()
            first = False
    else:
        raise NameError("Not an option")
