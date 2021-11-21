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


def AutoCarBuy_Then_AutoCarMastery(nbcar: int = 70):
    common.debug("AutoCarBuy + AutoCarMastery for " + str(nbcar) + " cars")
    AutoCarBuy(hcv2).run(nbcar)
    common.press_then_sleep("left")
    AutoCarMastery(hcv2).run(nbcar)


if __name__ == "__main__":
    hcfg = HandlerConfig("config.ini")
    constant.LANG = hcfg.get_value("language", constant.LANG.value)
    constant.DEBUG_LEVEL = int(hcfg.get_value("debug", str(constant.DEBUG_LEVEL)))

    hcv2 = HandlerCv2()
    # hcv2.show_debug_image = True
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
    intinput = int(input())
    if intinput == 1:
        AutoWheelspins(hcv2).run()
    elif intinput == 2:
        AutoGPSDestination(hcv2).run()
    elif intinput == 3:
        AutoLabReplay(hcv2).run()
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
        AutoCarBuy_Then_AutoCarMastery(70)
    elif intinput == 453:
        common.debug("AutoCarBuy + AutoCarMastery + AutoLabReplay")
        gc = GameCommon()
        common.alt_tab()
        common.click_then_sleep((10, 10), .125)
        if gc.check_mastery():
            gc.go_home_garage()
            gc.go_to_car_to_buy()
            AutoCarBuy_Then_AutoCarMastery(70)
        else:
            gc.home_getmycar()
            common.press_then_sleep("esc", 10)
            common.press_then_sleep("esc", 5)
            AutoLabReplay(hcv2).run()

    else:
        raise NameError("Not an option")
