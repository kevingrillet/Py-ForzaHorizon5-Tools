import time

import pyautogui

from game.constant import AutoSpinAlreadyOwnedChoice
from utils import common
from utils.handlercv2 import HandlerCv2


class AutoWheelspins:

    def __init__(self, hcv2: HandlerCv2 = None):
        common.debug("Create AutoWheelspins")
        self.already_owned_choice = AutoSpinAlreadyOwnedChoice.SELL
        self.count = 0
        if hcv2:
            self.hcv2 = hcv2
        else:
            self.hcv2 = HandlerCv2()
        self.images = self.hcv2.load_images(["collect_prize_and_spin_again",
                                             "skip",
                                             "0_spins_remaining",
                                             "car_already_owned"])
        self.running = False

    def run(self):
        common.debug("Start AutoWheelspins (after 5 secs)")
        time.sleep(5)
        self.running = True
        timer = time.time()
        while self.running:
            self.hcv2.require_new_capture = True
            if self.hcv2.check_match(self.images["collect_prize_and_spin_again"]):
                pyautogui.press("enter")
                self.count += 1
                common.debug("Collect [" + str(self.count) + " in " + str(round(time.time() - timer, 2)) + "s]")
                timer = time.time()
            elif self.hcv2.check_match(self.images["skip"]):
                pyautogui.press("enter")
            elif self.hcv2.check_match(self.images["car_already_owned"]):
                if self.already_owned_choice == AutoSpinAlreadyOwnedChoice.SELL:
                    common.press_then_sleep("down", .25)
                    common.press_then_sleep("down", .25)
                pyautogui.press("enter")
            elif self.hcv2.check_match(self.images["0_spins_remaining"]):
                pyautogui.press("enter")
                self.running = False
        common.debug("Done AutoWheelspins")
