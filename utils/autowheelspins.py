import time

import pyautogui

from utils import common
from utils.constant import AutoSpinAlreadyOwnedChoice, AutoSpinStep
from utils.handlercv2 import HandlerCv2


class AutoWheelspins:
    step = None

    def __init__(self, cv2: HandlerCv2 = None):
        common.debug("Create AutoWheelspins")
        self.already_owned_choice = AutoSpinAlreadyOwnedChoice.SELL
        self.count = 0
        if cv2:
            self.cv2 = cv2
        else:
            self.cv2 = HandlerCv2()
        self.images = self.cv2.load_images(["./images/collect_prize_and_spin_again.jpg",
                                            "./images/skip.jpg",
                                            "./images/0_spins_remaining.jpg",
                                            "./images/car_already_owned.jpg"])
        self.running = False
        self.step = AutoSpinStep.INIT

    def next_step(self, step: AutoSpinStep = None):
        self.count = 0
        if step:
            self.step = step
        else:
            self.step = self.step.next()

    def run(self):
        common.debug("Start AutoWheelspins")
        time.sleep(2)
        self.running = True
        while self.running:
            common.debug("Step: " + self.step.name + "; Count: " + str(self.count))
            if self.step <= AutoSpinStep.WAITING:
                if self.cv2.check_match(self.images["./images/collect_prize_and_spin_again.jpg"]):
                    pyautogui.press('enter')
                    self.next_step(AutoSpinStep.SPINNING)
                else:

                    if self.count >= 3:
                        self.next_step(AutoSpinStep.SPINNING)

            if self.step <= AutoSpinStep.SPINNING:
                if self.cv2.check_match(self.images["./images/skip.jpg"]):
                    pyautogui.press('enter')
                    self.next_step()
                else:
                    if self.count >= 3:
                        self.next_step()
            if self.step <= AutoSpinStep.REWARD:
                if self.cv2.check_match(self.images["./images/car_already_owned.jpg"]):
                    if self.already_owned_choice == AutoSpinAlreadyOwnedChoice.SELL:
                        pyautogui.press('down')
                        pyautogui.press('down')
                    pyautogui.press('enter')
                    self.next_step()
                else:
                    if self.count >= 2:
                        self.next_step()
            if self.step <= AutoSpinStep.END:
                if self.cv2.check_match(self.images["./images/0_spins_remaining.jpg"]):
                    time.sleep(.5)
                    pyautogui.press('enter')
                    self.running = False
                else:
                    if self.count >= 2:
                        self.next_step(AutoSpinStep.WAITING)

            self.cv2.require_new_capture = True
            self.count += 1
            time.sleep(.5)
        common.debug("Done AutoWheelspins")
