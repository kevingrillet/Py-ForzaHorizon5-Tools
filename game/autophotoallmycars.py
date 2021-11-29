from utils import common
from utils.constant import DebugLevel
from utils.handlercv2 import HandlerCv2
from utils.handlertime import HandlerTime


class AutoPhotoAllMyCars:
    ht = HandlerTime()
    running = False

    def __init__(self, hcv2: HandlerCv2 = None):
        """
        Prepare to AutoPhotoAllMyCars
        :param hcv2:
        """
        common.debug("Create AutoPhotoAllMyCars", DebugLevel.CLASS)
        self.hcv2 = hcv2 if hcv2 else HandlerCv2()
        self.images = self.hcv2.load_images(
            ["home", "last_car_manufacturer_selected", "loading_please_wait", "processing_photo"])

    def run(self):
        """
        Take a photo of all my cars
        """
        common.debug("Start AutoPhotoAllMyCars (after 5 secs)", DebugLevel.FUNCTIONS)
        common.sleep(5)
        common.press("esc", 3)
        count = 0
        count_try = 0
        # Should be able to get all cars, but will be so slow :/
        # 0 => nb_right
        # 1 => nb_right again
        # 2 => nb_right + Down
        nb_right = 1
        self.running = True
        self.ht.start()
        while self.running:
            common.press("esc", 3)
            common.press("pagedown")  # Cars
            common.press("left")  # Change car
            common.press("enter", 2)  # Select

            # Go to next car
            for _ in range(nb_right):
                common.press("right")
            if count_try == 2:
                common.press("down")
                count_try = 0
                nb_right += 1
            else:
                count_try += 1

            if self.hcv2.check_match(self.images["last_car_manufacturer_selected"], True):
                self.running = False

            # Get in the car
            common.press("enter")  # Select
            common.press("enter")  # Get in car
            common.press("enter")  # Deliver Car

            while not self.hcv2.check_match(self.images["home"], True):
                common.sleep(1)

            # Take photo
            common.press("p", 2)  # Enter photo mode
            while self.hcv2.check_match(self.images["loading_please_wait"], True):
                common.sleep(1)
            common.sleep(1)
            common.press("enter")  # Take photo
            while self.hcv2.check_match(self.images["processing_photo"], True):
                common.sleep(1)
            common.sleep(1)
            common.press("esc")  # Exit horizon promo
            common.press("esc")  # Exit photo
            common.press("enter", 2)  # Exit photo mode > Yes
            while self.hcv2.check_match(self.images["loading_please_wait"], True):
                common.sleep(1)
            while not self.hcv2.check_match(self.images["home"], True):
                common.sleep(1)

            count += 1
            common.debug("Photo taken! [" + str(count) + " in " + self.ht.stringify() + "]", DebugLevel.INFO)

        common.debug("Done AutoPhotoAllMyCars", DebugLevel.FUNCTIONS)
