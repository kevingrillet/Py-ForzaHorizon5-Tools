import time

import pyautogui

from game.common import GameCommon
from game.constant import AutoSpinAlreadyOwnedChoice
from utils import common
from utils.constant import DebugLevel
from utils.handlercv2 import HandlerCv2
from utils.handlertime import HandlerTime


class AutoWheelspins:
    already_owned_choice = AutoSpinAlreadyOwnedChoice.SELL
    count = 0
    ht = HandlerTime()
    running = False

    def __init__(self, hcv2: HandlerCv2 = None, gc: GameCommon = None):
        """
        Prepare to auto wheelspin
        :param hcv2:
        """
        common.debug("Create AutoWheelspins", DebugLevel.CLASS)
        self.gc = gc if gc else GameCommon()
        self.hcv2 = hcv2 if hcv2 else HandlerCv2()
        self.images = self.hcv2.load_images(
            ["collect_prize_and_spin_again", "skip", "0_spins_remaining"])

    def run(self):
        """
        Need to be run in the spin window
        """
        common.debug("Start AutoWheelspins (after 5 secs)", DebugLevel.FUNCTIONS)
        time.sleep(5)
        self.running = True
        self.ht.start()
        while self.running:
            if self.hcv2.check_match(self.images["collect_prize_and_spin_again"], True):
                pyautogui.press("enter")
                self.count += 1
                common.debug("Collect [" + str(self.count) + " in " + self.ht.stringify() + "]", DebugLevel.INFO)
            elif self.hcv2.check_match(self.images["skip"]):
                pyautogui.press("enter")
            elif self.gc.check_car_already_own():
                pass
            elif self.hcv2.check_match(self.images["0_spins_remaining"]):
                time.sleep(1)
                if self.hcv2.check_match(self.images["0_spins_remaining"], True):
                    pyautogui.press("enter")
                    self.running = False
        common.debug("Done AutoWheelspins", DebugLevel.FUNCTIONS)
