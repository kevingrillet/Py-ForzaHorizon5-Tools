import os

from game import constant
from game.advance import Advance
from game.autocarbuy import AutoCarBuy
from game.autocarbuyleastexpensive import AutoCarBuyLeastExpensive
from game.autocarmastery import AutoCarMastery
from game.autogpsdestination import AutoGPSDestination
from game.autolabreplay import AutoLabReplay
from game.autoracerestart import AutoRaceRestart
from game.autowheelspins import AutoWheelspins
from game.common import GameCommon
from game.constant import Car, AlreadyOwnedChoice
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
    constant.OWNED = AlreadyOwnedChoice(int(hcfg.get_value("owned", str(constant.OWNED.value))))
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
    hcv2.threshold = 0.9 if constant.SCALE == 1 else 0.8

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
        Advance.AutoCarBuy_Then_AutoCarMastery(AutoCarBuy(hcv2), AutoCarMastery(hcv2), 70)
    elif intinput == 453:
        common.debug("AutoCarBuy + AutoCarMastery + AutoLabReplay")
        a = Advance()
        gc = GameCommon(hcv2)
        acb = AutoCarBuy(hcv2)
        acm = AutoCarMastery(hcv2, gc)
        alr = AutoLabReplay(hcv2, gc, True)
        common.alt_tab()
        common.click((10, 10), .125)
        common.press("esc", 2)
        if gc.check_mastery():
            a.AutoCarBuy_Then_AutoCarMastery_from_menu_to_menu(gc, acb, acm)
        running = True
        while running:
            alr.run()
            a.AutoCarBuy_Then_AutoCarMastery_from_menu_to_menu(gc, acb, acm)
            # running = gc.check_super_wheelspins()
        common.sleep(5)
        common.alt_f4()
    elif intinput == 457:
        common.debug("AutoCarBuy + AutoCarMastery + AutoRaceRestart")
        a = Advance()
        gc = GameCommon(hcv2)
        acb = AutoCarBuy(hcv2)
        acm = AutoCarMastery(hcv2, gc)
        arr = AutoRaceRestart(hcv2)
        common.alt_tab()
        common.click((10, 10), .125)
        common.press("esc", 2)
        if gc.check_mastery():
            a.AutoCarBuy_Then_AutoCarMastery_from_menu_to_menu(gc, acb, acm)
        running = True
        while running:
            gc.go_to_last_lab_race()
            arr.run()
            gc.quit_race()
            a.AutoCarBuy_Then_AutoCarMastery_from_menu_to_menu(gc, acb, acm)
            # running = gc.check_super_wheelspins()
        common.sleep(5)
        common.alt_f4()

    # Dev
    elif intinput == 0:
        print(common.get_keyboard_language())
        print(common.convert_layout("z"))
        hcv2.hwin32.list_window_names()
        hcv2.dev()
    elif intinput == 98:
        arr = os.listdir("./images/common/")
        arr.extend(os.listdir("./images/en/"))
        arr.sort()
        print("\nList of images:")
        for i in range(0, len(arr), 5):
            s1 = arr[i].replace(".jpg", "") if i < len(arr) else ""
            s2 = arr[i + 1].replace(".jpg", "") if i + 1 < len(arr) else ""
            s3 = arr[i + 2].replace(".jpg", "") if i + 2 < len(arr) else ""
            s4 = arr[i + 3].replace(".jpg", "") if i + 3 < len(arr) else ""
            s5 = arr[i + 4].replace(".jpg", "") if i + 4 < len(arr) else ""
            print('{0:30}  {1:30} {2:30} {3:30} {4:30}'.format(s1, s2, s3, s4, s5))

        print("\nChoose image to search:")
        img_name = input()
        print("\nfind: " + str(hcv2.check_match(hcv2.load_images([img_name])[img_name]))
              + " find_max_val: " + str(hcv2.find_max_val)
              + " find_start: " + str(hcv2.find_start)
              + " find_end: " + str(hcv2.find_end))

    else:
        raise NameError("Not an option")
