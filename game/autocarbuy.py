from utils import common, superdecorator
from utils.handlercv2 import HandlerCv2
from utils.handlertime import HandlerTime


@superdecorator.decorate_all_functions()
class AutoCarBuy:

    def __init__(self, hcv2: HandlerCv2 = None):
        """
        Prepare to auto buy cars
        :param hcv2:
        """
        self.hcv2 = hcv2 if hcv2 else HandlerCv2()
        self.images = self.hcv2.load_images(['buy_car', 'insufficient_cr'])
        self.ht = HandlerTime()
        self.running = False

    def run(self, max_try: int = 50):
        """
        Buys the car where you are placed (in car collection)
        :param max_try:
        """
        common.sleep(5, 'Waiting 5 secs, please focus Forza Horizon 5.')
        common.moveTo((10, 10))
        count = 0
        self.running = True
        self.ht.start()
        while self.running and count < max_try:
            if self.hcv2.check_match(self.images['insufficient_cr'], True):
                common.press('esc')
                common.press('esc')
                self.running = False
            elif self.hcv2.check_match(self.images['buy_car']):
                common.press('enter')
                count += 1
                common.info('Car bought! [' + str(count) + '/' + str(max_try) + ' in ' + self.ht.stringify() + ']')
            else:
                common.press('y')
            common.sleep(1)
        common.press('esc', 2)
