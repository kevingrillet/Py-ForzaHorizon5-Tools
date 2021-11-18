import time

import pyautogui

from utils import common
from utils.constant import AutoSpinAlreadyOwnedChoice, AutoSpinStep
from utils.handlercv2 import HandlerCv2


class AutoWheelspins:
    step = None

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
        self.step = AutoSpinStep.INIT

    def next_step(self, step: AutoSpinStep = None):
        self.count = 0
        if step:
            self.step = step
        else:
            self.step = self.step.next()

    def run(self):
        common.debug("Start AutoWheelspins (after 5 secs)")
        time.sleep(5)
        self.next_step()
        self.running = True
        while self.running:
            self.hcv2.require_new_capture = True
            common.debug("Step: " + self.step.name + "; Count: " + str(self.count))
            if self.step <= AutoSpinStep.WAITING:
                if self.hcv2.check_match(self.images["collect_prize_and_spin_again"]):
                    pyautogui.press("enter")
                    self.next_step(AutoSpinStep.SPINNING)
                else:

                    if self.count >= 3:
                        self.next_step(AutoSpinStep.SPINNING)

            if self.step <= AutoSpinStep.SPINNING:
                if self.hcv2.check_match(self.images["skip"]):
                    pyautogui.press("enter")
                    self.next_step()
                else:
                    if self.count >= 3:
                        self.next_step()
            if self.step <= AutoSpinStep.REWARD:
                if self.hcv2.check_match(self.images["car_already_owned"]):
                    if self.already_owned_choice == AutoSpinAlreadyOwnedChoice.SELL:
                        common.press_then_sleep("down")
                        common.press_then_sleep("down")
                    pyautogui.press("enter")
                    self.next_step()
                else:
                    if self.count >= 2:
                        self.next_step()
            if self.step <= AutoSpinStep.END:
                if self.hcv2.check_match(self.images["0_spins_remaining"]):
                    common.press_then_sleep("enter")
                    self.running = False
                else:
                    if self.count >= 2:
                        self.next_step(AutoSpinStep.WAITING)

            self.count += 1
            time.sleep(.5)
        common.debug("Done AutoWheelspins")
