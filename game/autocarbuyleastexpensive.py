from utils import common
from utils.constant import DebugLevel
from utils.handlercv2 import HandlerCv2
from utils.handlertime import HandlerTime


class AutoCarBuyLeastExpensive:
    count = 0
    ht = HandlerTime()
    max_try = 25
    running = False

    def __init__(self, hcv2: HandlerCv2 = None):
        """
        Prepare to auto buy lest expensive car
        :param hcv2:
        """
        common.debug('Create AutoCarBuyLeastExpensive', DebugLevel.CLASS)
        self.hcv2 = hcv2 if hcv2 else HandlerCv2()
        self.images = self.hcv2.load_images(
            ['autoshow', 'colors', 'not_owned', 'insufficient_cr', 'value', 'value_menu', 'value_selected'])

    def run(self, max_try: int = max_try):
        """
        Need to be run from home buy/sell tab
        :param max_try:
        """
        common.debug('Start AutoCarBuyLeastExpensive (after 5 secs)', DebugLevel.FUNCTIONS)
        self.max_try = max_try
        common.sleep(5)
        common.moveTo((10, 10))
        self.running = True
        self.ht.start()
        while self.running and self.count < self.max_try:
            # Enter salon
            if not self.hcv2.check_match(self.images['autoshow'], True):
                raise NameError('Not at autoshow [autoshow]')
            common.press('enter', 2)
            # Filter not buy
            common.press('y')
            if not self.hcv2.check_match(self.images['not_owned'], True):
                raise NameError('Filter not found [not_owned]')
            common.click(self.hcv2.random_find(), .125)
            common.press('esc', 2)
            # Sort
            common.press('x')
            if not self.hcv2.check_match(self.images['value'], True):
                raise NameError('Sort not found [value]')
            common.click(self.hcv2.random_find(), .125)
            if self.hcv2.check_match(self.images['value_selected'], True):
                common.press('enter')
            common.sleep(1)
            # GoTo least expensive
            common.press('backspace')
            if not self.hcv2.check_match(self.images['value_menu'], True):
                raise NameError('Jump to value not found [value_menu]')
            common.click((570, self.hcv2.find_end[2] + 54))
            if self.hcv2.check_match(self.images['value_menu'], True):
                common.press('enter', 2)
            # Buy
            common.press('enter', 1)
            while not self.hcv2.check_match(self.images['colors'], True):
                common.sleep(.1)
            common.press('y', 2)
            common.press('enter', 1)
            common.press('enter', 1)
            if self.hcv2.check_match(self.images['insufficient_cr'], True):
                raise NameError('Not enough CR [insufficient_cr]')
            common.press('enter', 20)
            common.press('esc', 3)

            self.count += 1
            common.debug(
                'Car bought! [' + str(self.count) + '/' + str(self.max_try) + ' in ' + self.ht.stringify() + ']',
                DebugLevel.INFO)
            common.sleep(1)
        common.debug('Done AutoCarBuyLeastExpensive', DebugLevel.FUNCTIONS)
