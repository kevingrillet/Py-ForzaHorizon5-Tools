from game.common import GameCommon
from game.constant import RaceStep, AlreadyOwnedChoice
from utils import common, superdecorator
from utils.handlercv2 import HandlerCv2
from utils.handlertime import HandlerTime


@superdecorator.decorate_all_functions()
class AutoLabReplay:

    def __init__(self, hcv2: HandlerCv2 = None, gc: GameCommon = None, stop_on_max_mastery: bool = False):
        """
        Prepare for farming lab races
        :param hcv2:
        :param gc:
        :param stop_on_max_mastery: (False)
        """
        self.hcv2 = hcv2 if hcv2 else HandlerCv2()
        self.gc = gc if gc else GameCommon(self.hcv2)
        self.images = self.hcv2.load_images(
            ['accolades', 'race_continue', 'race_quit', 'race_reward', 'race_skip', 'race_start'])
        self.stop_on_max_mastery = stop_on_max_mastery
        self.ht = HandlerTime()
        self.already_owned_choice = AlreadyOwnedChoice.SELL
        self.count = 0
        self.running = False
        self.step = RaceStep.INIT

    def esc_to_menu(self):
        """
        If lost, get back to menu (at least try)
        """
        common.warn("I'm lost!!!")
        lost = True
        cnt = 0
        while lost:
            if cnt < 5:
                common.press('esc', 2)
                cnt += 1
            else:
                common.press('enter', 2)
                cnt = 0
            if self.hcv2.check_match(self.images['accolades'], True) or self.hcv2.check_match(
                    self.images['race_start']):
                lost = False

    def next_step(self, step: RaceStep = None):
        """
        Set next step and reset count
        :param step:
        """
        next_step: RaceStep = step if step else self.step.next()
        common.info(
            'Step done: ' + self.step.name + ' [' + str(self.count) + ' in ' + self.ht.stringify() + '] -> next: ' +
            next_step.name)
        self.step = next_step
        self.count = 0

    def run(self, max_try: int = 10):
        """
        Need to be started from race, or esc menu, or race preparation menu
        :param max_try:
        """
        common.sleep(5, 'Waiting 5 secs, please focus Forza Horizon 5.')
        common.moveTo((10, 10))
        self.ht.start()
        self.whereami()
        count_try = 0
        self.running = True
        while self.running and count_try < max_try:
            self.hcv2.require_new_capture = True

            if self.step == RaceStep.PREPARING:
                if self.hcv2.check_match(self.images['race_start']):
                    common.click(self.hcv2.random_find())
                    common.keyDown('z')
                    self.next_step()
                else:
                    common.sleep(1)
                    self.count += 1
                    if self.count > 10:
                        self.count = 0
                        self.esc_to_menu()
                        self.whereami()

            elif self.step == RaceStep.RACING:
                if self.hcv2.check_match(self.images['race_continue']) \
                        or self.hcv2.check_match(self.images['race_skip']) \
                        or self.hcv2.check_match(self.images['race_reward']):
                    common.keyUp('z')
                    self.next_step()

            elif self.step == RaceStep.REWARDS:
                common.sleep(1)
                if self.hcv2.check_match(self.images['race_continue']) \
                        or self.hcv2.check_match(self.images['race_skip']) \
                        or self.hcv2.check_match(self.images['race_reward']):
                    common.press('enter')
                    self.gc.check_car_already_own()
                    self.count = 0
                else:
                    self.count += 1
                    if self.count >= 3:
                        count_try += 1
                        common.info('Race done. [' + str(count_try) + '/' + str(max_try) + ']')
                        self.next_step()

            elif self.step == RaceStep.CHECK:
                if self.stop_on_max_mastery and self.gc:
                    self.running = not self.gc.check_mastery()
                self.next_step()

            elif self.step == RaceStep.RESTART:
                self.gc.go_to_last_lab_race()
                self.next_step(RaceStep.PREPARING)

            common.sleep(1)

    def whereami(self):
        """
        Check where am I to set initial step
        """
        if self.hcv2.check_match(self.images['race_quit']):
            common.press('esc')
            common.keyDown('z')
            self.next_step(RaceStep.RACING)
        elif self.hcv2.check_match(self.images['race_start']):
            self.next_step(RaceStep.PREPARING)
        else:
            common.press('esc')
            self.next_step(RaceStep.RESTART)
