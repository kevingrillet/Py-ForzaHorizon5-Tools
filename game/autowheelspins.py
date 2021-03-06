from game.common import GameCommon
from utils import common, superdecorator
from utils.handlercv2 import HandlerCv2
from utils.handlertime import HandlerTime


@superdecorator.decorate_all_functions()
class AutoWheelspins:
    def __init__(self, hcv2: HandlerCv2 = None, gc: GameCommon = None):
        """
        Prepare to auto wheelspin
        :param hcv2:
        """
        self.hcv2 = hcv2 if hcv2 else HandlerCv2()
        self.gc = gc if gc else GameCommon(self.hcv2)
        self.images = self.hcv2.load_images(['0_spins_remaining', 'collect_prize_and_spin_again', 'skip'])
        self.ht = HandlerTime()
        self.running = False

    def run(self):
        """
        Need to be run in the spin window
        """
        common.sleep(5, 'Waiting 5 secs, please focus Forza Horizon 5.')
        common.moveTo((10, 10))
        count = 0
        self.running = True
        self.ht.start()
        while self.running:
            if self.hcv2.check_match(self.images['collect_prize_and_spin_again'], True):
                common.press('enter')
                count += 1
                common.info('Collect [' + str(count) + ' in ' + self.ht.stringify() + ']')
            elif self.hcv2.check_match(self.images['skip']):
                common.press('enter')
            elif self.gc.check_car_already_own():
                pass
            elif self.hcv2.check_match(self.images['0_spins_remaining']):
                common.sleep(2)
                if self.hcv2.check_match(self.images['0_spins_remaining'], True):
                    common.press('enter')
                    self.running = False
