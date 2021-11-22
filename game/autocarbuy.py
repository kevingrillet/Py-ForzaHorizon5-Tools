import time

from utils import common
from utils.handlercv2 import HandlerCv2
from utils.handlertime import HandlerTime


class AutoCarBuy:
    count = 0
    ht = HandlerTime()
    max_try = 50
    running = False

    def __init__(self, hcv2: HandlerCv2 = HandlerCv2()):
        """
        Prepare to auto buy cars
        :param hcv2:
        """
        common.debug("Create AutoCarBuy")
        self.hcv2 = hcv2
        self.images = self.hcv2.load_images(["not_enaugh_cr", "buy_car"])

    def run(self, max_try: int = max_try):
        """
        Buys the car where you are placed (in car collection)
        :param max_try:
        """
        self.max_try = max_try
        common.debug("Start AutoCarBuy (after 5 secs)")
        time.sleep(5)
        self.running = True
        self.ht.start()
        while self.running and self.count < self.max_try:
            if self.hcv2.check_match(self.images["not_enaugh_cr"], True):
                common.press_then_sleep("esc")
                common.press_then_sleep("esc")
                self.running = False
            elif self.hcv2.check_match(self.images["buy_car"]):
                common.press_then_sleep("enter")
                self.count += 1
                common.debug(
                    "Car bought! [" + str(self.count) + "/" + str(self.max_try) + " in " + self.ht.stringify() + "]")
            else:
                common.press_then_sleep("y")
            time.sleep(1)

        common.press_then_sleep("esc", 2)
        common.debug("Done AutoCarBuy")
