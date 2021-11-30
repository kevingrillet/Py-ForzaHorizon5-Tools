from game.common import GameCommon
from utils import common
from utils.constant import DebugLevel
from utils.handlercv2 import HandlerCv2
from utils.handlertime import HandlerTime


class AutoPhotoAllMyCars:
    ht = HandlerTime()
    running = False

    def __init__(self, hcv2: HandlerCv2 = None, gc: GameCommon = None):
        """
        Prepare to AutoPhotoAllMyCars
        :param hcv2:
        :param gc:
        """
        common.debug('Create AutoPhotoAllMyCars', DebugLevel.CLASS)
        self.hcv2 = hcv2 if hcv2 else HandlerCv2()
        self.gc = gc if gc else GameCommon(self.hcv2)
        self.images = self.hcv2.load_images(
            ['home', 'last_car_manufacturer_selected', 'loading_please_wait', 'processing_photo'])

    def run(self, nb_right: int = 1):
        """
        Take a photo of all my cars
        :param nb_right:
        """
        common.debug('Start AutoPhotoAllMyCars (after 5 secs)', DebugLevel.FUNCTIONS)
        common.sleep(5)
        common.moveTo((10, 10))
        common.press('esc', 3)
        count = 0
        count_try = 0
        # Should be able to get all cars, but will be so slow :/
        # 0 => nb_right
        # 1 => nb_right again
        # 2 => nb_right + Down
        nb_right = nb_right
        self.running = True
        self.ht.start()
        while self.running:
            old_count_try = count_try
            old_nb_right = nb_right
            common.press('esc', 3)
            common.press('pagedown')  # Cars
            common.press('left', .125)  # Change car
            common.press('enter', 2)  # Select

            # Go to next car
            for _ in range(nb_right):
                common.press('right', .125)
            if count_try == 2:
                common.press('down', .125)
                count_try = 0
                nb_right += 1
            else:
                count_try += 1

            if self.hcv2.check_match(self.images['last_car_manufacturer_selected'], True):
                common.debug('LAST!', DebugLevel.INFO)
                self.running = False

            # Get in the car
            common.press('enter', .75)  # Select
            common.press('enter', .75)  # Get in car
            common.press('enter', 2)  # Deliver Car
            self.wait('home', 'Not outside home', False)

            # Take photo
            common.press('p', 2)  # Enter photo mode
            self.wait('loading_please_wait', "Loading didn't end?")
            common.sleep(2)
            common.press('enter')  # Take photo
            self.wait('processing_photo', "Processing didn't end?")
            common.sleep(2)
            common.press('esc', .75)  # Exit horizon promo
            common.press('esc', .75)  # Exit photo
            common.press('enter', 2)  # Exit photo mode > Yes
            self.wait('loading_please_wait', "Loading didn't end?")
            self.wait('home', 'Not outside home', False)

            count += 1
            common.debug('Photo taken! [' + str(count) + ' (' + str(old_nb_right) + '/' + str(
                old_count_try) + ') in ' + self.ht.stringify() + ']', DebugLevel.INFO)

        common.debug('Done AutoPhotoAllMyCars', DebugLevel.FUNCTIONS)

    def wait(self, image_name: str, err_msg: str, expected: bool = True):
        """
        Wait until image_name match is in expected result, if 15 fail, then err_msg
        :param image_name:
        :param err_msg:
        :param expected:
        """
        cnt = 0
        while self.hcv2.check_match(self.images[image_name], True) == expected:
            common.sleep(1)
            cnt += 1
            if cnt > 15:
                if image_name == 'home':
                    common.warn(err_msg + ' [' + image_name + ']')
                    self.gc.go_home_garage()
                    common.press('esc')
                    self.wait('home', 'Not outside home', False)
                else:
                    raise NameError(err_msg + ' [' + image_name + ']')
