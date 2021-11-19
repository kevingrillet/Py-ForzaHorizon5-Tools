import time

import pyautogui

from game.constant import AutoLabReplayStep, AutoSpinAlreadyOwnedChoice
from utils import common
from utils.handlercv2 import HandlerCv2


class AutoLabReplay:
    count = 0
    step = None

    def __init__(self, hcv2: HandlerCv2 = None):
        self.already_owned_choice = AutoSpinAlreadyOwnedChoice.SELL
        common.debug("Create AutoLabReplay")
        if hcv2:
            self.hcv2 = hcv2
        else:
            self.hcv2 = HandlerCv2()
        self.images = self.hcv2.load_images(["car_already_owned",
                                             "continue",
                                             "race_quit",
                                             "race_reward",
                                             "race_skip",
                                             "race_start",
                                             "race_type"])
        self.running = False
        self.step = AutoLabReplayStep.INIT
        self.timer = time.time()

    def next_step(self, step: AutoLabReplayStep = None):
        common.debug("Step: " + self.step.name + " [" + str(self.count) + " in " + str(round(time.time() - self.timer, 2)) + "s]")
        if step:
            self.step = step
        else:
            self.step = self.step.next()
        self.count = 0
        self.timer = time.time()

    def run(self):
        common.debug("Start AutoLabReplay (after 5 secs)")
        time.sleep(5)
        pyautogui.moveTo(10, 10)
        self.whereami()
        self.running = True
        while self.running:
            self.hcv2.require_new_capture = True
            if self.step == AutoLabReplayStep.PREPARING:
                if self.hcv2.check_match(self.images["race_start"]):
                    # common.press_then_sleep("enter")
                    common.click_then_sleep(self.hcv2.random_find())
                    pyautogui.keyDown("z")
                    self.next_step()
            if self.step == AutoLabReplayStep.RACING:
                if self.hcv2.check_match(self.images["continue"]) \
                        or self.hcv2.check_match(self.images["race_skip"]) \
                        or self.hcv2.check_match(self.images["race_reward"]):
                    pyautogui.keyUp("z")
                    self.next_step()
            if self.step == AutoLabReplayStep.REWARDS:
                if self.hcv2.check_match(self.images["continue"]) \
                        or self.hcv2.check_match(self.images["race_skip"]) \
                        or self.hcv2.check_match(self.images["race_reward"]):
                    common.press_then_sleep("enter")
                    if self.hcv2.check_match(self.images["car_already_owned"]):
                        if self.already_owned_choice == AutoSpinAlreadyOwnedChoice.SELL:
                            common.press_then_sleep("down", .25)
                            common.press_then_sleep("down", .25)
                        pyautogui.press("enter")
                    self.count = 0
                else:
                    if self.step == AutoLabReplayStep.REWARDS:
                        self.count += 1
                        if self.count >= 3:
                            self.next_step()
            if self.step == AutoLabReplayStep.RESTART:
                default_sleep = 5
                common.debug("Restarting the race (after 30 secs)")
                time.sleep(30)
                # Open menu
                common.press_then_sleep("esc", default_sleep)
                # GoTo Creation
                common.press_then_sleep("pagedown", .25)
                common.press_then_sleep("pagedown", .25)
                common.press_then_sleep("pagedown", .25)
                common.press_then_sleep("pagedown", .25)
                # Enter Lab
                common.press_then_sleep("enter", default_sleep)
                # Enter my races
                common.press_then_sleep("right", .25)
                common.press_then_sleep("enter", default_sleep)
                # GoTo History
                common.press_then_sleep("pagedown", .25)
                common.press_then_sleep("pagedown", default_sleep)
                # Select last race
                common.press_then_sleep("enter", default_sleep)
                # Solo
                if self.hcv2.check_match(self.images["race_type"]):
                    common.press_then_sleep("enter", default_sleep)
                # Same car
                common.press_then_sleep("enter", default_sleep)
                self.next_step(AutoLabReplayStep.PREPARING)
            time.sleep(1)
        common.debug("Done AutoLabReplay")

    def whereami(self):
        if self.hcv2.check_match(self.images["race_quit"]):
            common.press_then_sleep("esc")
            pyautogui.keyDown("z")
            self.next_step(AutoLabReplayStep.RACING)
        elif self.hcv2.check_match(self.images["race_start"]):
            self.next_step(AutoLabReplayStep.PREPARING)
        else:
            common.press_then_sleep("esc")
            self.next_step(AutoLabReplayStep.RESTART)
