import time

from game import constant
from game.autocarbuy import AutoCarBuy
from game.autocarmastery import AutoCarMastery
from game.constant import AutoSpinAlreadyOwnedChoice
from utils import common
from utils.constant import DebugLevel
from utils.handlercv2 import HandlerCv2
from utils.handlertime import HandlerTime


class GameCommon:
    ht = HandlerTime()

    def __init__(self, hcv2: HandlerCv2 = None):
        """
        Game common things
        :param hcv2:
        """
        common.debug("Create GameCommon", DebugLevel.CLASS)
        self.hcv2 = hcv2 if hcv2 else HandlerCv2()
        self.images = self.hcv2.load_images(
            ["999_mastery", "999_super_wheelspins", "campaign_selected", "car_already_owned", "lamborghini_name",
             "lamborghini_name_selected", "my_cars", "pontiac_name", "pontiac_name_selected"])

    @staticmethod
    def AutoCarBuy_Then_AutoCarMastery(acb: AutoCarBuy, acm: AutoCarMastery, nbcar: int = 70):
        """
        From main, used to do AutoCarBuy (already places on the pontiac) then AutoCarMastery
        """
        common.debug("AutoCarBuy + AutoCarMastery for " + str(nbcar) + " cars", DebugLevel.INFO)
        acb.run(nbcar)
        common.press_then_sleep("left")
        acm.run(nbcar)

    def AutoCarBuy_Then_AutoCarMastery_from_menu_to_menu(self, acb: AutoCarBuy, acm: AutoCarMastery):
        """
        From main, used to do AutoCarBuy (from game) then AutoCarMastery then get in my lambo :)
        """
        self.go_home_garage()
        self.go_to_car_to_buy()
        GameCommon.AutoCarBuy_Then_AutoCarMastery(acb, acm, 70)
        self.home_getmycar()
        common.press_then_sleep("esc", 10)
        common.press_then_sleep("esc", 5)

    def check_car_already_own(self, aoc: AutoSpinAlreadyOwnedChoice = AutoSpinAlreadyOwnedChoice.SELL) -> bool:
        """
        From anywhere where you can get a new car :)
        """
        common.debug("Start GameCommon.check_car_already_own", DebugLevel.FUNCTIONS)
        if self.hcv2.check_match(self.images["car_already_owned"], True):
            if constant.DEV_MODE:
                self.hcv2.save_image()
            if aoc == AutoSpinAlreadyOwnedChoice.SELL:
                common.press_then_sleep("down", .125)
                common.press_then_sleep("down", .125)
            common.press_then_sleep("enter", 1)
        common.debug("End GameCommon.check_car_already_own", DebugLevel.FUNCTIONS)
        return False

    def check_mastery(self) -> bool:
        """
        From game, check if mastery is at 999
        :return: True/False
        """
        common.debug("Start GameCommon.check_mastery", DebugLevel.FUNCTIONS)
        common.press_then_sleep("esc", 2)
        common.press_then_sleep("pagedown")
        common.press_then_sleep("right", .125)
        common.press_then_sleep("down", .125)
        common.press_then_sleep("enter", 2)
        ret = self.hcv2.check_match(self.images["999_mastery"], True)
        common.press_then_sleep("esc, 1")
        common.press_then_sleep("pageup, 1")
        common.debug("End GameCommon.check_mastery", DebugLevel.FUNCTIONS)
        return ret

    def check_super_wheelspins(self) -> bool:
        """
        From game, check if SuperWheelSpins is at 999
        :return: True/False
        """
        common.debug("Start GameCommon.check_mastery", DebugLevel.FUNCTIONS)
        common.press_then_sleep("esc", 2)
        common.press_then_sleep("pagedown")
        common.press_then_sleep("left", .125)
        common.press_then_sleep("down", .125)
        common.press_then_sleep("enter", 2)
        ret = not self.hcv2.check_match(self.images["999_super_wheelspins"], True)
        common.debug("End GameCommon.check_mastery", DebugLevel.FUNCTIONS)
        return ret

    def go_home_garage(self):
        """
        From game, go to home > garage
        """
        common.debug("Start GameCommon.go_home_garage", DebugLevel.FUNCTIONS)
        if not self.hcv2.check_match(self.images["campaign_selected"]):
            common.press_then_sleep("esc", 2)
            if not self.hcv2.check_match(self.images["campaign_selected"]):
                raise NameError("Not in menu")
        common.press_then_sleep("pagedown")
        common.press_then_sleep("pagedown")
        common.press_then_sleep("enter")
        common.press_then_sleep("enter", 5)
        common.press_then_sleep("pageup")
        common.debug("End GameCommon.go_home_garage", DebugLevel.FUNCTIONS)

    def go_to_car_to_buy(self):
        """
        Starting in garage, get in car collection, then filter pontiac and go to firebird
        """
        common.debug("Start GameCommon.go_to_car_to_buy", DebugLevel.FUNCTIONS)
        common.press_then_sleep("right", .125)
        common.press_then_sleep("enter", 2)
        common.press_then_sleep("backspace", 1)
        if not self.hcv2.check_match(self.images["pontiac_name"], True):
            common.press_then_sleep("up", 1)
            if not self.hcv2.check_match(self.images["pontiac_name"], True):
                raise NameError("Pontiac name not found")
        common.click_then_sleep(self.hcv2.random_find(), .125)
        if self.hcv2.check_match(self.images["pontiac_name_selected"], True):
            common.press_then_sleep("enter", 1)
        time.sleep(1)
        common.press_then_sleep("right", .125)
        common.press_then_sleep("right", .125)
        common.press_then_sleep("right", .125)
        common.debug("End GameCommon.go_to_car_to_buy", DebugLevel.FUNCTIONS)

    def home_getmycar(self):
        """
        Starting in garage, get in my lambo then get back to garage
        """
        common.debug("Start GameCommon.home_getmycar", DebugLevel.FUNCTIONS)
        self.home_goinmycars()
        self.home_mycars_getinlambo()
        common.debug("End GameCommon.home_getmycar", DebugLevel.FUNCTIONS)

    def home_goinmycars(self):
        """
        Starting in garage, get in my cars
        """
        common.debug("Start GameCommon.home_goinmycars", DebugLevel.FUNCTIONS)
        if not self.hcv2.check_match(self.images["my_cars"], True):
            raise NameError("Not in home")
        common.press_then_sleep("enter", 2)
        common.debug("End GameCommon.home_goinmycars", DebugLevel.FUNCTIONS)

    def home_mycars_getinlambo(self):
        """
        Starting in garage > my cars, filter favorite & lambo, then get in, then esc to garage
        """
        common.debug("Start GameCommon.home_mycars_getinlambo", DebugLevel.FUNCTIONS)
        # Filter favorites
        common.press_then_sleep("y")
        common.press_then_sleep("enter")
        common.press_then_sleep("esc", 2)
        # Constructor
        common.press_then_sleep("backspace", 1)
        if not self.hcv2.check_match(self.images["lamborghini"], True):
            raise NameError("No lambo in favorites")
        common.click_then_sleep(self.hcv2.random_find(), .125)
        if self.hcv2.check_match(self.images["lamborghini_name_selected"], True):
            common.press_then_sleep("enter", 1)
        # Get in car
        common.press_then_sleep("enter")
        common.press_then_sleep("enter", 1)
        cnt = 0
        while not self.hcv2.check_match(self.images["my_cars"], True):
            common.press_then_sleep("esc", 1)
            cnt += 1
            if cnt > 10:
                raise NameError("My cars not found")
        common.debug("End GameCommon.home_mycars_getinlambo", DebugLevel.FUNCTIONS)
