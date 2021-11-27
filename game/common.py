from game import constant
from game.autocarbuy import AutoCarBuy
from game.autocarmastery import AutoCarMastery
from game.constant import AlreadyOwnedChoice, Car
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
        self.car = constant.CAR.value
        self.hcv2 = hcv2 if hcv2 else HandlerCv2()
        self.images = self.hcv2.load_images(
            ["999_mastery", "999_super_wheelspins", "accolades", "car_already_owned", "lamborghini_name",
             "lamborghini_name_selected", "my_cars", self.car + "_name", self.car + "_name_selected", "race_start",
             "race_type"])

    @staticmethod
    def AutoCarBuy_Then_AutoCarMastery(acb: AutoCarBuy, acm: AutoCarMastery, nbcar: int = 70):
        """
        From main, used to do AutoCarBuy (already places on the pontiac) then AutoCarMastery
        """
        common.debug("AutoCarBuy + AutoCarMastery for " + str(nbcar) + " cars", DebugLevel.INFO)
        acb.run(nbcar)
        common.press("left")
        acm.run(nbcar)

    def AutoCarBuy_Then_AutoCarMastery_from_menu_to_menu(self, acb: AutoCarBuy, acm: AutoCarMastery):
        """
        From main, used to do AutoCarBuy (from game) then AutoCarMastery then get in my lambo :)
        """
        if self.car == Car.PONTIAC.value:
            nbcar = 71
        elif self.car == Car.PONTIAC.value:
            nbcar = 199
        else:
            raise NameError("Unknow car")

        self.go_home_garage()
        self.go_to_car_to_buy()
        GameCommon.AutoCarBuy_Then_AutoCarMastery(acb, acm, nbcar)
        self.home_getmycar()
        common.press("esc", 10)

    def check_car_already_own(self, aoc: AlreadyOwnedChoice = constant.OWNED) -> bool:
        """
        From anywhere where you can get a new car :)
        """
        common.debug("Start GameCommon.check_car_already_own", DebugLevel.FUNCTIONS)
        if self.hcv2.check_match(self.images["car_already_owned"], True):
            if constant.DEV_MODE:
                self.hcv2.save_image()
            if aoc == AlreadyOwnedChoice.SELL:
                common.press("down", .125)
                common.press("down", .125)
            common.press("enter", 1)
        common.debug("End GameCommon.check_car_already_own", DebugLevel.FUNCTIONS)
        return False

    def check_mastery(self) -> bool:
        """
        From game, check if mastery is at 999
        :return: True/False
        """
        common.debug("Start GameCommon.check_mastery", DebugLevel.FUNCTIONS)
        # Open menu
        common.press("esc", 2)
        # Go to Mastery
        common.press("pagedown")
        common.press("right", .125)
        common.press("down", .125)
        common.press("enter", 2)
        # Check number of points
        ret = self.hcv2.check_match(self.images["999_mastery"], True)
        # Get back to esc menu
        common.press("esc", 1)
        common.press("esc", 2)
        common.debug("End GameCommon.check_mastery", DebugLevel.FUNCTIONS)
        return ret

    def check_super_wheelspins(self) -> bool:
        """
        From game, check if SuperWheelSpins is at 999
        :return: True/False
        """
        common.debug("Start GameCommon.check_mastery", DebugLevel.FUNCTIONS)
        common.press("esc", 2)
        common.press("pagedown")
        common.press("left", .125)
        common.press("down", .125)
        common.press("enter", 2)
        ret = not self.hcv2.check_match(self.images["999_super_wheelspins"], True)
        common.debug("End GameCommon.check_mastery", DebugLevel.FUNCTIONS)
        return ret

    def go_home_garage(self):
        """
        From game, go to home > garage
        """
        common.debug("Start GameCommon.go_home_garage", DebugLevel.FUNCTIONS)
        if not self.hcv2.check_match(self.images["accolades"], True):
            common.press("esc", 2)
            if not self.hcv2.check_match(self.images["accolades"], True):
                raise NameError("Not in menu")
        common.press("pagedown")
        common.press("pagedown")
        common.press("enter")
        common.press("enter", 10)
        common.press("pageup")
        common.debug("End GameCommon.go_home_garage", DebugLevel.FUNCTIONS)

    def go_to_car_to_buy(self):
        """
        Starting in garage, get in car collection, then filter pontiac and go to firebird
        """
        common.debug("Start GameCommon.go_to_car_to_buy", DebugLevel.FUNCTIONS)
        common.press("right", .125)
        common.press("enter", 2)
        common.press("backspace", 1)
        if not self.hcv2.check_match(self.images[self.car + "_name"], True):
            common.scroll(10, (450, 450), .125, constant.SCALE)
            if not self.hcv2.check_match(self.images[self.car + "_name"], True):
                common.scroll(-10, (450, 450), .125, constant.SCALE)
                if not self.hcv2.check_match(self.images[self.car + "_name"], True):
                    raise NameError("Pontiac name not found")
        common.click(self.hcv2.random_find(), .125)
        if self.hcv2.check_match(self.images[self.car + "_name_selected"], True):
            common.press("enter", 1)
        common.sleep(1)

        if self.car == constant.Car.PONTIAC.value:
            for _ in range(3):
                common.press("right", .125)
        elif self.car == constant.Car.FORD.value:
            for _ in range(5):
                common.press("down", .125)
            for _ in range(4):
                common.press("right", .125)
        else:
            NameError("Unknow car")

        common.debug("End GameCommon.go_to_car_to_buy", DebugLevel.FUNCTIONS)

    def go_to_last_lab_race(self, default_sleep: float = 5):
        """
        Starting in game, go to last lab race
        :param default_sleep:
        """
        common.debug("Start GameCommon.go_to_last_lab_race", DebugLevel.FUNCTIONS)
        common.debug("Restarting the race (after 30 secs)", DebugLevel.INFO)
        common.sleep(30)
        # Open menu
        common.press("esc", default_sleep)
        # GoTo Creation
        for _ in range(4):
            common.press("pagedown", .25)
        # Enter Lab
        common.press("enter", default_sleep)
        # Enter my races
        common.press("right", .25)
        common.press("enter", default_sleep)
        # GoTo History
        common.press("pagedown", .25)
        common.press("pagedown", default_sleep)
        # Select last race
        common.press("enter", default_sleep)
        # Solo
        if self.hcv2.check_match(self.images["race_type"], True):
            common.press("enter", default_sleep)
        # Same car
        common.press("enter", default_sleep)
        while not self.hcv2.check_match(self.images["race_start"], True):
            common.sleep(1)
        common.debug("End GameCommon.go_to_last_lab_race", DebugLevel.FUNCTIONS)

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
        common.press("enter", 2)
        common.debug("End GameCommon.home_goinmycars", DebugLevel.FUNCTIONS)

    def home_mycars_getinlambo(self):
        """
        Starting in garage > my cars, filter favorite & lambo, then get in, then esc to garage
        """
        common.debug("Start GameCommon.home_mycars_getinlambo", DebugLevel.FUNCTIONS)
        # Filter favorites
        common.press("y")
        common.press("enter")
        common.press("esc", 2)
        # Constructor
        common.press("backspace", 1)
        if not self.hcv2.check_match(self.images["lamborghini_name"], True):
            raise NameError("No lambo in favorites")
        common.click(self.hcv2.random_find(), .125)
        if self.hcv2.check_match(self.images["lamborghini_name_selected"], True):
            common.press("enter", 1)
        # Get in car
        common.press("enter")
        common.press("enter", 1)
        cnt = 0
        while not self.hcv2.check_match(self.images["my_cars"], True):
            common.press("esc", 1)
            cnt += 1
            if cnt > 10:
                raise NameError("My cars not found")
        common.debug("End GameCommon.home_mycars_getinlambo", DebugLevel.FUNCTIONS)

    def quit_race(self):
        """
        From race preparation screen, leave race
        """
        common.debug("Start GameCommon.quit_race", DebugLevel.FUNCTIONS)
        while not self.hcv2.check_match(self.images["race_start"], True):
            common.sleep(1)
        common.press("right", .125)
        common.press("down", .125)
        common.press("down", .125)
        common.press("enter")
        common.press("enter", 30)
        common.debug("End GameCommon.quit_race", DebugLevel.FUNCTIONS)
