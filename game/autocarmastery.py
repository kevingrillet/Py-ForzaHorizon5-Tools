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
            ['already_done', 'cannot_afford_perk', 'my_cars', 'new_common', 'new_rare', self.car, self.car + '_name',
             self.car + '_name_selected'])
        self.count = 0
        self.count_done = 0
        self.ht = HandlerTime()
        self.running = False

    def check_buy(self):
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

    def delete(self, fast_sleep: float = .125) -> bool:
        """
        Delete car after selecting it
        :param fast_sleep:
        :return: If car has been deleted
        """
        if constant.CAR == Car.FORD or Car.PONTIAC:
            result = not self.hcv2.check_match(self.images['new_common'], True)
        elif constant.CAR == Car.PORSCHE:
            result = not self.hcv2.check_match(self.images['new_rare'], True)
        else:
            raise NameError('Unknow car')

        if result:
            common.press('enter')
            for _ in range(4):
                common.press('down', fast_sleep)
            common.press('enter')
            common.press('enter', 1)

        return result

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

    def do_path(self, path: str = ''):
        """
        Do the path in mastery.
        Example: _erereuerel_ue
        Equivalent to: Enter, Right Enter, Right Enter, Up Enter, Right Enter, Left Up Enter
        :param path:
        """
        path = list(path)
        while len(str) > 0 and self.running:
            step = path.pop(0)
            enter = path.pop(0) == 'e'
            self.do_step(step, enter)

    def do_step(self, step: str = '', enter: bool = True, fast_sleep: float = .125):
        """
        Do step, then enter if required, then check if buy did work
        :param step: _, l, r, u, d
        :param enter: True, False
        :param fast_sleep: .125
        """
        if step == 'l':
            common.press('left', fast_sleep)
        elif step == 'r':
            common.press('right', fast_sleep)
        elif step == 'u':
            common.press('up', fast_sleep)
        elif step == 'd':
            common.press('down', fast_sleep)

        if enter:
            common.press('enter', .75)
            self.check_buy()

    def find_car(self, fast_sleep: float = .125):
        """
        Look for the car
        :param fast_sleep:
        """
        if constant.CAR == Car.PONTIAC:
            deleted = True
            # Find car to delete
            if self.count > 1:  # Need to skip it 2 times to begin
                if not self.hcv2.check_match(self.images[self.car], True):
                    raise NameError(self.car.capitalize() + ' to delete not found [' + self.car + ']')
                common.press('right', fast_sleep)
                deleted = self.delete()
            # Find car to use
            if not self.hcv2.check_match(self.images[self.car], True):
                raise NameError(self.car.capitalize() + ' to drive not found [' + self.car + ']')
            if deleted:
                common.press('up', fast_sleep)
                common.press('right', fast_sleep)

        elif constant.CAR == Car.FORD or Car.PORSCHE:
            # Find car to delete
            if self.count > 1:  # Need to skip it 2 times to begin
                if not self.hcv2.check_match(self.images[self.car], True):
                    raise NameError(self.car.capitalize() + ' to delete not found [' + self.car + ']')
                if self.delete():
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
            if not self.hcv2.check_match(self.images['already_done'], True):
                if constant.CAR == Car.FORD:
                    self.do_path('_ereue')
                elif constant.CAR == Car.PONTIAC:
                    self.do_path('_erereuereue')
                elif constant.CAR == Car.PORSCHE:
                    self.do_path('_erereuerel_ue')
                else:
                    raise NameError('Unknow car')

                if self.running:
                    self.count_done += 1

            if self.running:
                # Get back to menu
                common.press('esc', 2)
                common.press('esc', 1.5)
                common.press('right', .125)
                self.count += 1
                common.info(
                    'Car done! [' + str(self.count) + '(' + str(self.count_done) + ')/' + str(
                        max_try) + ' in ' + self.ht.stringify() + ']')
