from game.constant import RaceStep
from utils import common
from utils.constant import DebugLevel
from utils.handlercv2 import HandlerCv2
from utils.handlertime import HandlerTime


class AutoRaceRestart:
    count = 0
    count_try = 0
    ht = HandlerTime()
    max_try = 100
    running = False
    step = RaceStep.INIT

    def __init__(self, hcv2: HandlerCv2 = None):
        """
        Prepare for farming races
        :param hcv2:
        """
        common.debug("Create AutoRaceRestart", DebugLevel.CLASS)
        self.hcv2 = hcv2 if hcv2 else HandlerCv2()
        self.images = self.hcv2.load_images(
            ["race_continue", "race_quit", "race_start"])

    def next_step(self, step: RaceStep = None):
        """
        Set next step and reset count
        :param step:
        """
        next_step: RaceStep = step if step else self.step.next()
        common.debug(
            "Step done: " + self.step.name + " [" + str(self.count) + " in " + self.ht.stringify() + "] -> next: " +
            next_step.name, DebugLevel.INFO)
        self.step = next_step
        self.count = 0

    def run(self, max_try: int = max_try):
        """
        Need to be started from race, or esc menu, or race preparation menu
        :param max_try:
        """
        common.debug("Start AutoRaceRestart (after 5 secs)", DebugLevel.FUNCTIONS)
        self.count_try = 0
        self.max_try = max_try
        common.sleep(5)
        common.moveTo((10, 10))
        self.ht.start()
        self.whereami()
        self.running = True
        while self.running and self.count_try < max_try:
            self.hcv2.require_new_capture = True

            if self.step == RaceStep.PREPARING:
                if self.hcv2.check_match(self.images["race_start"]):
                    common.click(self.hcv2.random_find())
                    common.keyDown("z")
                    self.next_step()
                else:
                    common.sleep(1)
                    self.count += 1
                    if self.count > 10:
                        self.whereami()

            elif self.step == RaceStep.RACING:
                if self.hcv2.check_match(self.images["race_continue"]):
                    common.keyUp("z")
                    self.next_step()

            elif self.step == RaceStep.REWARDS:
                common.sleep(1)
                if self.hcv2.check_match(self.images["race_continue"]):
                    self.count_try += 1
                    common.debug("Race done. [" + str(self.count_try) + "/" + str(self.max_try) + "]", DebugLevel.INFO)
                    common.press("x")
                    common.press("enter", 5)
                    self.next_step(RaceStep.PREPARING)

        common.debug("Done AutoRaceRestart", DebugLevel.FUNCTIONS)

    def whereami(self):
        """
        Check where am i to set initial step
        """
        if self.hcv2.check_match(self.images["race_quit"]):
            common.press("esc")
            common.keyDown("z")
            self.next_step(RaceStep.RACING)
        elif self.hcv2.check_match(self.images["race_start"]):
            self.next_step(RaceStep.PREPARING)
        else:
            raise NameError("Not where I am supposed to be [race_quit, race_start]")
