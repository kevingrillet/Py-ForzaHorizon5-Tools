import time

from utils import common
from utils.handlercv2 import HandlerCv2


class AutoCarBuy:
    count = 0
    max = 50

    def __init__(self, hcv2: HandlerCv2 = None):
        common.debug("Create AutoCarBuy")
        if hcv2:
            self.hcv2 = hcv2
        else:
            self.hcv2 = HandlerCv2()
        self.images = self.hcv2.load_images(["not_enaugh_cr",
                                             "buy_car"])
        self.running = False

    def run(self):
        common.debug("Start AutoCarBuy (after 5 secs)")
        time.sleep(5)
        self.running = True
        timer = time.time()
        while self.running and self.count < self.max:
            self.hcv2.require_new_capture = True
            if self.hcv2.check_match(self.images["not_enaugh_cr"]):
                common.press_then_sleep("esc")
                common.press_then_sleep("esc")
                self.running = False
            elif self.hcv2.check_match(self.images["buy_car"]):
                common.press_then_sleep("enter")
                self.count += 1
                common.debug("Car bought! [" + str(self.count) + " in " + str(round(time.time() - timer, 2)) + "s]")
                timer = time.time()
            else:
                common.press_then_sleep("y")
            time.sleep(1)
        common.debug("Done AutoCarBuy")
