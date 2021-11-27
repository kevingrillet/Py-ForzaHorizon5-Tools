from game import constant
from game.autocarbuy import AutoCarBuy
from game.autocarbuyleastexpensive import AutoCarBuyLeastExpensive
from game.autocarmastery import AutoCarMastery
from game.autogpsdestination import AutoGPSDestination
from game.autolabreplay import AutoLabReplay
from game.autoracerestart import AutoRaceRestart
from game.autowheelspins import AutoWheelspins
from game.common import GameCommon
from game.constant import Car
from utils import common
from utils.constant import DebugLevel, Lang
from utils.handlerconfig import HandlerConfig
from utils.handlercv2 import HandlerCv2


def load_config():
    hcfg = HandlerConfig("config.ini")
    constant.CAR = Car(hcfg.get_value("car", constant.CAR.value))
    constant.DEBUG_LEVEL = DebugLevel(int(hcfg.get_value("debug", str(constant.DEBUG_LEVEL.value))))
    constant.DEV_MODE = hcfg.get_value("dev", str(constant.DEV_MODE)) == "True"
    constant.LANG = Lang(hcfg.get_value("language", constant.LANG.value))
    constant.SCALE = float(hcfg.get_value("scale", str(constant.SCALE)))


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
    print(" ┃ 7 - AutoRaceRestart          ┃")
    print(" ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print("Your choice:")


if __name__ == "__main__":
    load_config()
    show_menu()
    intinput = int(input())
    hcv2 = HandlerCv2(scale=constant.SCALE)

    # Menu
    if intinput == 1:
        AutoWheelspins(hcv2).run()
    elif intinput == 2:
        AutoGPSDestination(hcv2).run()
    elif intinput == 3:
        AutoLabReplay(hcv2).run()
    elif intinput == 30:
        common.alt_tab()
        AutoLabReplay(hcv2, stop_on_max_mastery=True).run()
        common.sleep(10)
        common.alt_f4()
    elif intinput == 4:
        AutoCarBuy(hcv2).run()
    elif intinput == 5:
        AutoCarMastery(hcv2).run()
    elif intinput == 6:
        AutoCarBuyLeastExpensive(hcv2).run()
    elif intinput == 7:
        AutoRaceRestart(hcv2).run()
    elif intinput == 70:
        AutoRaceRestart(hcv2).run()
        common.sleep(10)
        common.alt_f4()

    # Just press Z
    elif intinput == 99:
        common.alt_tab()
        common.press("esc", 0)
        common.keyDown("z")

    # Combination
    elif intinput == 45:
        common.alt_tab()
        GameCommon.AutoCarBuy_Then_AutoCarMastery(AutoCarBuy(hcv2), AutoCarMastery(hcv2), 70)
    elif intinput == 453:
        common.debug("AutoCarBuy + AutoCarMastery + AutoLabReplay")
        gc = GameCommon(hcv2)
        acb = AutoCarBuy(hcv2)
        acm = AutoCarMastery(hcv2)
        alr = AutoLabReplay(hcv2, gc, True)
        common.alt_tab()
        common.click((10, 10), .125)
        common.press("esc", 2)
        if gc.check_mastery():
            gc.AutoCarBuy_Then_AutoCarMastery_from_menu_to_menu(acb, acm)
        running = True
        while running:
            alr.run()
            gc.AutoCarBuy_Then_AutoCarMastery_from_menu_to_menu(acb, acm)
            # running = gc.check_super_wheelspins()
        common.sleep(5)
        common.alt_f4()
    elif intinput == 457:
        common.debug("AutoCarBuy + AutoCarMastery + AutoRaceRestart")
        gc = GameCommon(hcv2)
        acb = AutoCarBuy(hcv2)
        acm = AutoCarMastery(hcv2)
        arr = AutoRaceRestart(hcv2)
        common.alt_tab()
        common.click((10, 10), .125)
        common.press("esc", 2)
        if gc.check_mastery():
            gc.AutoCarBuy_Then_AutoCarMastery_from_menu_to_menu(acb, acm)
        running = True
        while running:
            gc.go_to_last_lab_race()
            arr.run()
            gc.quit_race()
            gc.AutoCarBuy_Then_AutoCarMastery_from_menu_to_menu(acb, acm)
            # running = gc.check_super_wheelspins()
        common.sleep(5)
        common.alt_f4()

    # Dev
    elif intinput == 0:
        hcv2.hwin32.list_window_names()
        hcv2.dev()

    # WIP
    elif intinput == 98:
        img_name = "skip"
        print("find: " + str(hcv2.check_match(hcv2.load_images([img_name])[img_name])) + " find_start: " + str(
            hcv2.find_start) + " find_end: " + str(hcv2.find_end))

    else:
        raise NameError("Not an option")
