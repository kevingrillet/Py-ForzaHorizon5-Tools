from utils import common, superdecorator
from utils.handlercv2 import HandlerCv2
from utils.handlertime import HandlerTime


@superdecorator.decorate_all_functions()
class AutoCarBuyAuction:

    def __init__(self, hcv2: HandlerCv2 = None):
        """
        Prepare to auto buy cars
        :param hcv2:
        """
        self.hcv2 = hcv2 if hcv2 else HandlerCv2()
        self.images = self.hcv2.load_images(
            ['auction_house_won', 'auctions_options', 'auction_house_waiting', 'buyout_successful', 'search'])
        self.ht = HandlerTime()
        self.running = False

    def run(self, nb_car_to_buy: int = 1):
        """
        Buys the car where you are placed (in car collection)
        :param nb_car_to_buy:
        """
        common.sleep(5, 'Waiting 5 secs, please focus Forza Horizon 5.')
        common.moveTo((10, 10))
        count = 0
        self.running = True
        self.ht.start()
        while self.running and count < nb_car_to_buy:
            if not self.hcv2.check_match(self.images['search'], True):
                raise NameError('Not in auction house search [search]')
            common.press('enter', 2)
            while not self.hcv2.check_match(self.images['auction_house_won'], True) and count < nb_car_to_buy:
                while self.hcv2.check_match(self.images['auction_house_waiting'], True):
                    common.sleep(1)
                if not self.hcv2.check_match(self.images['auctions_options'], True):
                    common.info(
                        'No car to buy! [' + str(count) + '/' + str(nb_car_to_buy) + ' in ' + self.ht.stringify() + ']')
                else:
                    common.press('y', 1)
                    common.press('down')
                    common.press('enter')
                    common.press('enter')
                    attempt = 0
                    while not self.hcv2.check_match(self.images['buyout_successful'], True):
                        attempt += 1
                        common.sleep(1)
                        if attempt > 30:
                            raise NameError('Failed to buy! [buyout_successful]')
                    common.press('enter')
                    common.press('esc')
                    count += 1
                    common.info(
                        'Car bought! [' + str(count) + '/' + str(nb_car_to_buy) + ' in ' + self.ht.stringify() + ']')
                    common.press('down')
            common.press('esc', 1)
            common.press('enter')
        common.press('esc', 2)
