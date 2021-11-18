import time

import pyautogui

from utils import common
from utils.handlercv2 import HandlerCv2


class AutoCarBuy:
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
        common.debug("Start AutoCarBuy (after 2 secs)")
        time.sleep(2)
        self.running = True
        while self.running:
            self.hcv2.require_new_capture = True
            if self.hcv2.check_match(self.images["not_enaugh_cr"]):
                common.press_then_sleep("esc")
                common.press_then_sleep("esc")
                self.running = False
            elif self.hcv2.check_match(self.images["buy_car"]):
                common.press_then_sleep("enter")
            else:
                common.press_then_sleep("enter")
            time.sleep(1)
        common.debug("Done AutoCarBuy")
