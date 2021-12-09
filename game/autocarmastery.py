from game import constant
from game.common import GameCommon
from game.constant import Car
from utils import common, superdecorator
from utils.handlercv2 import HandlerCv2
from utils.handlertime import HandlerTime


@superdecorator.decorate_all_functions()
class AutoCarMastery:
    def __init__(self, hcv2: HandlerCv2 = None, gc: GameCommon = None):
        """
        Prepare to auto master car
        :param hcv2:
        """
        self.car = constant.CAR.value
        self.hcv2 = hcv2 if hcv2 else HandlerCv2()
        self.gc = gc if gc else GameCommon(self.hcv2)
        self.images = self.hcv2.load_images(
            ['already_done', 'cannot_afford_perk', 'my_cars', self.car, self.car + '_name',
             self.car + '_name_selected'])
        self.count = 0
        self.count_done = 0
        self.ht = HandlerTime()
        self.running = False

    def checkBuy(self):
        """
        Check if the mastery had been bought
        """
        if self.hcv2.check_match(self.images['cannot_afford_perk'], True):
            common.press('enter')
            common.press('esc', 2)
            common.press('esc', 1.5)
            common.press('right', .125)
            common.warn("Can't buy, not enough mastery points [cannot_afford_perk]")
            self.running = False

    @staticmethod
    def delete(fast_sleep: float = .125):
        """
        Delete car after selecting it
        :param fast_sleep:
        """
        common.press('enter')
        for _ in range(4):
            common.press('down', fast_sleep)
        common.press('enter')
        common.press('enter', 1)

    @staticmethod
    def filter(fast_sleep: float = .125):
        """
        Apply filter to find the car
        :param fast_sleep:
        """
        if constant.CAR == Car.FORD or Car.PORSCHE:
            common.press('y', 1)
            if constant.CAR == Car.FORD:
                # Filter B & HotHatch
                for _ in range(4):  # Warn: May change during Winter -> 4 or 6 here
                    common.press('down', fast_sleep / 2)
                common.press('enter', fast_sleep)
                for _ in range(16):
                    common.press('down', fast_sleep / 2)
                common.press('enter', fast_sleep)
            elif constant.CAR == Car.PORSCHE:
                # Filter A & HotHatch
                for _ in range(5):  # Warn: May change during Winter -> 5 or 7 here
                    common.press('down', fast_sleep / 2)
                common.press('enter', fast_sleep)
                for _ in range(10):
                    common.press('down', fast_sleep / 2)
                common.press('enter', fast_sleep)
            common.press('esc', 1)

    def find_car(self, fast_sleep: float = .125):
        """
        Look for the car
        :param fast_sleep:
        """
        if constant.CAR == Car.PONTIAC:
            # Find car to delete
            if self.count > 1:  # Need to skip it 2 times to begin
                if not self.hcv2.check_match(self.images[self.car], True):
                    raise NameError(self.car.capitalize() + ' to delete not found [' + self.car + ']')
                common.press('right', fast_sleep)
                AutoCarMastery.delete()
            # Find car to use
            if not self.hcv2.check_match(self.images[self.car], True):
                raise NameError(self.car.capitalize() + ' to drive not found [' + self.car + ']')
            common.press('up', fast_sleep)
            common.press('right', fast_sleep)

        elif constant.CAR == Car.FORD or Car.PORSCHE:
            # Find car to delete
            if self.count > 1:  # Need to skip it 2 times to begin
                if not self.hcv2.check_match(self.images[self.car], True):
                    raise NameError(self.car.capitalize() + ' to delete not found [' + self.car + ']')
                AutoCarMastery.delete()
                common.press('up', fast_sleep)
                common.press('right', fast_sleep)
            # Find car to use
            common.sleep(fast_sleep * 2)
            if not self.hcv2.check_match(self.images[self.car], True):
                raise NameError(self.car.capitalize() + ' to drive not found [' + self.car + ']')

    def go_to_manufacturer(self):
        """
        Go to the manufacturer
        """
        common.press('backspace')
        if self.hcv2.check_match(self.images[self.car + '_name_selected'], True):
            common.press('enter', 1)
        else:
            if not self.hcv2.check_match(self.images[self.car + '_name'], True):
                common.press('up')
                if not self.hcv2.check_match(self.images[self.car + '_name'], True):
                    raise NameError(self.car.capitalize() + ' name not found [' + self.car + '_name]')
            common.click(self.hcv2.random_find(), .125)
            if self.hcv2.check_match(self.images[self.car + '_name_selected'], True):
                common.press('enter', 1)
        common.sleep(1)

    @staticmethod
    def go_to_mastery(fast_sleep: float = .125):
        """
        Go to mastery page
        :param fast_sleep:
        """
        # Boost
        common.press('left', fast_sleep)
        common.press('enter', 1.5)
        # Mastery
        common.press('right', fast_sleep)
        common.press('right', fast_sleep)
        common.press('down', fast_sleep)
        common.press('enter', 2.5)

    def master_ford(self, fast_sleep: float = .125):
        """
        master for Ford
        :param fast_sleep:
        """
        if not self.hcv2.check_match(self.images['already_done'], True):
            # MASTERRR
            common.press('enter', 1)
            self.checkBuy()
            common.press('right', fast_sleep)
            common.press('enter', .75)
            self.checkBuy()
            common.press('up', fast_sleep)
            common.press('enter', .75)
            self.checkBuy()
            if self.running:
                self.count_done += 1

    def master_pontiac(self, fast_sleep: float = .125):
        """
        master for Pontiac
        :param fast_sleep:
        """
        if not self.hcv2.check_match(self.images['already_done'], True):
            # MASTERRR
            common.press('enter', 1)
            self.checkBuy()
            common.press('right', fast_sleep)
            common.press('enter', .75)
            self.checkBuy()
            common.press('right', fast_sleep)
            common.press('enter', .75)
            self.checkBuy()
            common.press('up', fast_sleep)
            common.press('enter', .75)
            self.checkBuy()
            common.press('right', fast_sleep)
            common.press('enter', .75)
            self.checkBuy()
            common.press('up', fast_sleep)
            common.press('enter', .75)
            self.checkBuy()
            if self.running:
                self.count_done += 1

    def master_porsche(self, fast_sleep: float = .125):
        """
        master for Porsche
        :param fast_sleep:
        """
        if not self.hcv2.check_match(self.images['already_done'], True):
            # MASTERRR
            common.press('enter', 1)
            self.checkBuy()
            common.press('right', fast_sleep)
            common.press('enter', .75)
            self.checkBuy()
            common.press('right', fast_sleep)
            common.press('enter', .75)
            self.checkBuy()
            common.press('up', fast_sleep)
            common.press('enter', .75)
            self.checkBuy()
            common.press('right', fast_sleep)
            common.press('enter', .75)
            self.checkBuy()
            common.press('left', fast_sleep)
            common.press('up', fast_sleep)
            common.press('enter', .75)
            self.checkBuy()
            if self.running:
                self.count_done += 1

    def run(self, max_try: int = 50):
        """
        Need to be run from home garage
        :param max_try:
        """
        common.sleep(5, 'Waiting 5 secs, please focus Forza Horizon 5.')
        common.moveTo((10, 10))
        self.count = 0
        self.count_done = 0
        self.running = True
        self.ht.start()
        while self.running and self.count < max_try:
            if not self.hcv2.check_match(self.images['my_cars'], True):
                raise NameError('Not in home [my_cars]')
            # My cars
            common.press('enter', 2)
            self.filter()
            self.go_to_manufacturer()
            self.find_car()
            self.gc.enter_car()
            AutoCarMastery.go_to_mastery()
            if constant.CAR == Car.FORD:
                self.master_ford()
            elif constant.CAR == Car.PONTIAC:
                self.master_pontiac()
            elif constant.CAR == Car.PORSCHE:
                self.master_porsche()
            else:
                raise NameError('Unknow car')

            if self.running:
                # Get back to menu
                common.press('esc', 2)
                common.press('esc', 1.5)
                common.press('right', .125)
                self.count += 1
                common.info(
                    'Car done! [' + str(self.count) + '(' + str(self.count_done) + ')/' + str(
                        max_try) + ' in ' + self.ht.stringify() + ']')
