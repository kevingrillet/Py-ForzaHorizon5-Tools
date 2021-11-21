import time

from game.autocarbuy import AutoCarBuy
from game.autocarmastery import AutoCarMastery
from utils import common
from utils.handlercv2 import HandlerCv2
from utils.handlertime import HandlerTime


class GameCommon:
    def __init__(self, hcv2: HandlerCv2 = None):
        common.debug("Create GameCommon")
        if hcv2:
            self.hcv2 = hcv2
        else:
            self.hcv2 = HandlerCv2()
        self.ht = HandlerTime()
        self.images = self.hcv2.load_images(["999_mastery",
                                             "campaign_selected",
                                             "lamborghini_name",
                                             "lamborghini_name_selected",
                                             "pontiac_name",
                                             "pontiac_name_selected",
                                             "my_cars"])

    @staticmethod
    def AutoCarBuy_Then_AutoCarMastery(acb: AutoCarBuy, acm: AutoCarMastery, nbcar: int = 70):
        common.debug("AutoCarBuy + AutoCarMastery for " + str(nbcar) + " cars")
        acb.run(nbcar)
        common.press_then_sleep("left")
        acm.run(nbcar)

    def check_mastery(self) -> bool:
        common.debug("Start GameCommon.check_mastery")
        common.press_then_sleep("esc", 2)
        common.press_then_sleep("pagedown")
        common.press_then_sleep("right", .125)
        common.press_then_sleep("down", .125)
        common.press_then_sleep("enter", 2)
        ret = self.hcv2.check_match(self.images["999_mastery"])
        common.press_then_sleep("esc, 1")
        common.press_then_sleep("pageup, 1")
        common.debug("End GameCommon.check_mastery")
        return ret

    def go_home_garage(self):
        common.debug("Start GameCommon.go_home_garage")
        if not self.hcv2.check_match(self.images["campaign_selected"]):
            common.press_then_sleep("esc", 2)
            if not self.hcv2.check_match(self.images["campaign_selected"]):
                raise NameError("Not in menu")
        common.press_then_sleep("pagedown")
        common.press_then_sleep("pagedown")
        common.press_then_sleep("enter")
        common.press_then_sleep("enter", 5)
        common.press_then_sleep("pageup")
        common.debug("End GameCommon.go_home_garage")

    def go_to_car_to_buy(self):
        common.debug("Start GameCommon.go_to_car_to_buy")
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
        common.debug("End GameCommon.go_to_car_to_buy")

    def home_getmycar(self):
        common.debug("Start GameCommon.home_getmycar")
        self.home_goinmycars()
        self.home_mycars_getinlambo()
        common.debug("End GameCommon.home_getmycar")

    def home_goinmycars(self):
        common.debug("Start GameCommon.home_goinmycars")
        if not self.hcv2.check_match(self.images["my_cars"], True):
            raise NameError("Not in home")
        common.press_then_sleep("enter", 2)
        common.debug("End GameCommon.home_goinmycars")

    def home_mycars_getinlambo(self):
        common.debug("Start GameCommon.home_mycars_getinlambo")
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
        common.debug("End GameCommon.home_mycars_getinlambo")
