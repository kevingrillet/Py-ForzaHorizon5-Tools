import time

import pyautogui

from game.common import GameCommon
from game.constant import AutoLabReplayStep, AutoSpinAlreadyOwnedChoice
from utils import common
from utils.handlercv2 import HandlerCv2
from utils.handlertime import HandlerTime


class AutoLabReplay:
    already_owned_choice = AutoSpinAlreadyOwnedChoice.SELL
    count = 0
    count_try = 0
    ht = HandlerTime()
    max_try = 10
    running = False
    step = AutoLabReplayStep.INIT

    def __init__(self, hcv2: HandlerCv2 = HandlerCv2(), gc: GameCommon = GameCommon(),
                 stop_on_max_mastery: bool = False):
        """
        Prepare for farming lab races
        :param hcv2:
        :param gc:
        :param stop_on_max_mastery: (False)
        """
        common.debug("Create AutoLabReplay")
        self.gc = gc
        self.hcv2 = hcv2
        self.images = self.hcv2.load_images(
            ["accolades", "continue", "race_quit", "race_reward", "race_skip", "race_start", "race_type"])
        self.stop_on_max_mastery = stop_on_max_mastery

    def esc_to_menu(self):
        common.debug("I'm lost!!!")
        lost = True
        while lost:
            common.press_then_sleep("esc", 2)
            if self.hcv2.check_match(self.images["accolades"]) or self.hcv2.check_match(self.images["race_start"]):
                lost = False

    def next_step(self, step: AutoLabReplayStep = None):
        """
        Set next step and reset count
        :param step:
        """
        next_step: AutoLabReplayStep = step if step else self.step.next()
        common.debug(
            "Step done: " + self.step.name + " [" + str(self.count) + " in " + self.ht.stringify() + "] -> next: " +
            next_step.name)
        self.step = next_step
        self.count = 0

    def run(self, max_try: int = max_try):
        """
        Need to be started from race, or esc menu, or race preparation menu
        :param max_try:
        :return:
        """
        common.debug("Start AutoLabReplay (after 5 secs)")
        self.max_try = max_try
        default_sleep = 5
        time.sleep(5)
        pyautogui.moveTo(10, 10)
        self.ht.start()
        self.whereami()
        self.count_try = 0
        self.running = True
        while self.running and self.count_try < max_try:
            self.hcv2.require_new_capture = True

            if self.step == AutoLabReplayStep.PREPARING:
                if self.hcv2.check_match(self.images["race_start"]):
                    common.click_then_sleep(self.hcv2.random_find())
                    pyautogui.keyDown("z")
                    self.next_step()
                else:
                    time.sleep(1)
                    self.count += 1
                    if self.count > 10:
                        self.count = 0
                        self.esc_to_menu()
                        self.whereami()

            elif self.step == AutoLabReplayStep.RACING:
                if self.hcv2.check_match(self.images["continue"]) \
                        or self.hcv2.check_match(self.images["race_skip"]) \
                        or self.hcv2.check_match(self.images["race_reward"]):
                    pyautogui.keyUp("z")
                    self.next_step()

            elif self.step == AutoLabReplayStep.REWARDS:
                time.sleep(1)
                if self.hcv2.check_match(self.images["continue"]) \
                        or self.hcv2.check_match(self.images["race_skip"]) \
                        or self.hcv2.check_match(self.images["race_reward"]):
                    common.press_then_sleep("enter")
                    self.gc.check_car_already_own()
                    self.count = 0
                else:
                    self.count += 1
                    if self.count >= 3:
                        self.count_try += 1
                        common.debug("Race done. [" + str(self.count_try) + "/" + str(self.max_try) + "]")
                        self.next_step()

            elif self.step == AutoLabReplayStep.CHECK:
                if self.stop_on_max_mastery and self.gc:
                    self.running = not self.gc.check_mastery()
                self.next_step()

            elif self.step == AutoLabReplayStep.RESTART:
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
        """
        Check where am i to set initial step
        """
        if self.hcv2.check_match(self.images["race_quit"]):
            common.press_then_sleep("esc")
            pyautogui.keyDown("z")
            self.next_step(AutoLabReplayStep.RACING)
        elif self.hcv2.check_match(self.images["race_start"]):
            self.next_step(AutoLabReplayStep.PREPARING)
        else:
            common.press_then_sleep("esc")
            self.next_step(AutoLabReplayStep.RESTART)
