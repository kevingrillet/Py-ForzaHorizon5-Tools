from game import constant
from game.common import GameCommon
from utils import common
from utils.constant import DebugLevel
from utils.handlercv2 import HandlerCv2
from utils.handlertime import HandlerTime


class AutoCarMastery:
    count = 0
    ht = HandlerTime()
    max_try = 50
    running = False

    def __init__(self, hcv2: HandlerCv2 = None, gc: GameCommon = None):
        """
        Prepare to auto master car
        :param hcv2:
        """
        common.debug("Create AutoCarMastery", DebugLevel.CLASS)
        self.car = constant.CAR.value
        self.hcv2 = hcv2 if hcv2 else HandlerCv2()
        self.gc = gc if gc else GameCommon(self.hcv2)
        self.images = self.hcv2.load_images(
            ["already_done", "cannot_afford_perk", "my_cars", self.car, self.car + "_name",
             self.car + "_name_selected"])

    def car_ford(self, fast_sleep: float = .125):
        # Filter B & HotHatch
        common.press("y", 1)
        for _ in range(6):
            common.press("down", fast_sleep / 2)
        common.press("enter", fast_sleep)
        for _ in range(16):
            common.press("down", fast_sleep / 2)
        common.press("enter", fast_sleep)
        common.press("esc", 1)

        self.go_to_manufacturer()
        self.find_car()
        self.gc.enter_car()
        self.go_to_mastery()

        if not self.hcv2.check_match(self.images["already_done"], True):
            # MASTERRR
            common.press("enter", 1)
            self.checkBuy()
            common.press("right", fast_sleep)
            common.press("enter", .75)
            self.checkBuy()
            common.press("up", fast_sleep)
            common.press("enter", .75)
            self.checkBuy()

    def car_pontiac(self, fast_sleep: float = .125):
        self.go_to_manufacturer()

        # Find car to delete
        if self.count > 1:  # Need to skip it 2 times to begin
            if not self.hcv2.check_match(self.images[self.car], True):
                raise NameError(self.car.capitalize() + " to delete not found [" + self.car + "]")
            common.press("right", fast_sleep)
            common.press("enter")
            self.delete()
        # Find car to use
        if not self.hcv2.check_match(self.images[self.car], True):
            raise NameError(self.car.capitalize() + " to drive not found [" + self.car + "]")
        common.press("up", fast_sleep)
        common.press("right", fast_sleep)

        self.gc.enter_car()
        self.go_to_mastery()

        if not self.hcv2.check_match(self.images["already_done"], True):
            # MASTERRR
            common.press("enter", 1)
            self.checkBuy()
            common.press("right", fast_sleep)
            common.press("enter", .75)
            self.checkBuy()
            common.press("right", fast_sleep)
            common.press("enter", .75)
            self.checkBuy()
            common.press("up", fast_sleep)
            common.press("enter", .75)
            self.checkBuy()
            common.press("right", fast_sleep)
            common.press("enter", .75)
            self.checkBuy()
            common.press("up", fast_sleep)
            common.press("enter", .75)
            self.checkBuy()

    def car_porsche(self, fast_sleep: float = .125):
        # Filter A & HotHatch
        common.press("y", 1)
        for _ in range(7):
            common.press("down", fast_sleep / 2)
        common.press("enter", fast_sleep)
        for _ in range(10):
            common.press("down", fast_sleep / 2)
        common.press("enter", fast_sleep)
        common.press("esc", 1)

        self.go_to_manufacturer()
        self.find_car()
        self.gc.enter_car()
        self.go_to_mastery()

        if not self.hcv2.check_match(self.images["already_done"], True):
            # MASTERRR
            common.press("enter", 1)
            self.checkBuy()
            common.press("right", fast_sleep)
            common.press("enter", .75)
            self.checkBuy()
            common.press("right", fast_sleep)
            common.press("enter", .75)
            self.checkBuy()
            common.press("up", fast_sleep)
            common.press("enter", .75)
            self.checkBuy()
            # common.press("right", fast_sleep)
            # common.press("enter", .75)
            # self.checkBuy()
            # common.press("left", fast_sleep)
            common.press("up", fast_sleep)
            common.press("enter", .75)
            self.checkBuy()

    def checkBuy(self):
        """
        Check if the mastery had been bought
        """
        if self.hcv2.check_match(self.images["cannot_afford_perk"], True):
            common.press("enter")
            common.press("esc", 2)
            common.press("esc", 1.5)
            common.press("right", .125)
            raise NameError("Can't buy, not enaugh mastery points [cannot_afford_perk]")

    @staticmethod
    def delete():
        for _ in range(4):
            common.press("down", .125)
        common.press("enter")
        common.press("enter", 1)

    def find_car(self, fast_sleep: float = .125):
        # Find car to delete
        if self.count > 1:  # Need to skip it 2 times to begin
            if not self.hcv2.check_match(self.images[self.car], True):
                raise NameError(self.car.capitalize() + " to delete not found [" + self.car + "]")
            common.press("enter")
            self.delete()
            common.press("up", fast_sleep)
            common.press("right", fast_sleep)
        # Find car to use
        if not self.hcv2.check_match(self.images[self.car], True):
            raise NameError(self.car.capitalize() + " to drive not found [" + self.car + "]")

    def go_to_manufacturer(self):
        common.press("backspace")
        if self.hcv2.check_match(self.images[self.car + "_name_selected"], True):
            common.press("enter", 1)
        else:
            if not self.hcv2.check_match(self.images[self.car + "_name"], True):
                common.press("up")
                if not self.hcv2.check_match(self.images[self.car + "_name"], True):
                    raise NameError(self.car.capitalize() + " name not found [" + self.car + "_name]")
            common.click(self.hcv2.random_find(), .125)
            if self.hcv2.check_match(self.images[self.car + "_name_selected"], True):
                common.press("enter", 1)
        common.sleep(1)

    @staticmethod
    def go_to_mastery(fast_sleep: float = .125):
        # Boost
        common.press("left", fast_sleep)
        common.press("enter", 1.5)
        # Mastery
        common.press("right", fast_sleep)
        common.press("right", fast_sleep)
        common.press("down", fast_sleep)
        common.press("enter", 2.5)

    def run(self, max_try: int = max_try):
        """
        Need to be run from home garage
        :param max_try:
        """
        common.debug("Start AutoCarMastery (after 5 secs)", DebugLevel.FUNCTIONS)
        self.count = 0
        self.max_try = max_try
        common.sleep(5)
        self.running = True
        self.ht.start()
        while self.running and self.count < self.max_try:
            if not self.hcv2.check_match(self.images["my_cars"], True):
                raise NameError("Not in home [my_cars]")
            # My cars
            common.press("enter", 2)
            if self.car == constant.Car.FORD.value:
                self.car_ford()
            elif self.car == constant.Car.PONTIAC.value:
                self.car_pontiac()
            elif self.car == constant.Car.PORSCHE.value:
                self.car_porsche()
            else:
                raise NameError("Unknow car")

            # Get back to menu
            common.press("esc", 2)
            common.press("esc", 1.5)
            common.press("right", .125)
            self.count += 1
            common.debug("Car done! [" + str(self.count) + "/" + str(self.max_try) + " in " + self.ht.stringify() + "]",
                         DebugLevel.INFO)
        common.debug("Done AutoCarMastery", DebugLevel.FUNCTIONS)
