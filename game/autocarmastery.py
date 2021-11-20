import time

from utils import common
from utils.handlercv2 import HandlerCv2
from utils.handlertime import HandlerTime


class AutoCarMastery:
    count = 0
    max_try = 50

    def __init__(self, hcv2: HandlerCv2 = None):
        common.debug("Create AutoCarMastery")
        if hcv2:
            self.hcv2 = hcv2
        else:
            self.hcv2 = HandlerCv2()
        self.ht = HandlerTime()
        self.images = self.hcv2.load_images(["already_done",
                                             "cant_buy",
                                             "pontiac",
                                             "pontiac_name",
                                             "pontiac_name_selected",
                                             "my_cars"])
        self.running = False

    def checkBuy(self):
        if self.hcv2.check_match(self.images["cant_buy"], True):
            common.press_then_sleep("enter")
            common.press_then_sleep("esc", 2)
            common.press_then_sleep("esc", 1.5)
            common.press_then_sleep("right", .125)
            raise NameError("Can't buy, not enaugh mastery points")

    def run(self, max_try: int = max_try):
        common.debug("Start AutoCarMastery (after 5 secs)")
        self.max_try = max_try
        time.sleep(5)
        self.running = True
        self.ht.start()
        while self.running and self.count < self.max_try:
            if self.hcv2.check_match(self.images["my_cars"], True):
                # My cars
                common.press_then_sleep("enter", 2)
                # Constructor
                common.press_then_sleep("backspace", 1)
                if not self.hcv2.check_match(self.images["pontiac_name"], True):
                    common.press_then_sleep("up", 1)
                    if not self.hcv2.check_match(self.images["pontiac_name"], True):
                        raise NameError("Pontiac name not found")
                common.click_then_sleep(self.hcv2.random_find(), .125)
                if self.hcv2.check_match(self.images["pontiac_name_selected"], True):
                    common.press_then_sleep("enter", 1)
                time.sleep(1)
                # Find car to delete
                if self.count > 1:  # Need to skip it 2 times to begin
                    if not self.hcv2.check_match(self.images["pontiac"], True):
                        raise NameError("Pontiac to delete not found")
                    # common.click_then_sleep(self.hcv2.random_find())
                    # common.debug("Choose car to delete (in 3 secs)")
                    # time.sleep(3)
                    # common.click_then_sleep((1180, 530))
                    common.press_then_sleep("right", .125)
                    common.press_then_sleep("enter")
                    # Delete button
                    common.press_then_sleep("down", .125)
                    common.press_then_sleep("down", .125)
                    common.press_then_sleep("down", .125)
                    common.press_then_sleep("down", .125)
                    common.press_then_sleep("enter")
                    # Confirm
                    common.press_then_sleep("enter", 2)
                # Find car to use
                if not self.hcv2.check_match(self.images["pontiac"], True):
                    raise NameError("Pontiac to drive not found")
                # common.click_then_sleep(self.hcv2.random_find())
                # common.debug("Choose car to use (in 3 secs)")
                # time.sleep(3)
                # common.click_then_sleep((1180, 530))
                common.press_then_sleep("up", .125)
                common.press_then_sleep("right", .125)
                # Enter car
                common.press_then_sleep("enter")
                common.press_then_sleep("enter", 1)
                cnt = 0
                while not self.hcv2.check_match(self.images["my_cars"], True):
                    common.press_then_sleep("esc", 1)
                    cnt += 1
                    if cnt > 10:
                        raise NameError("My cars not found")
                # Boost
                common.press_then_sleep("left", .125)
                common.press_then_sleep("enter", 1.5)
                # Mastery
                common.press_then_sleep("right", .125)
                common.press_then_sleep("right", .125)
                common.press_then_sleep("down", .125)
                common.press_then_sleep("enter", 2.5)
                if not self.hcv2.check_match(self.images["already_done"], True):
                    # MASTERRR
                    common.press_then_sleep("enter", 1)
                    self.checkBuy()
                    common.press_then_sleep("right", .125)
                    common.press_then_sleep("enter", .75)
                    self.checkBuy()
                    common.press_then_sleep("right", .125)
                    common.press_then_sleep("enter", .75)
                    self.checkBuy()
                    common.press_then_sleep("up", .125)
                    common.press_then_sleep("enter", .75)
                    self.checkBuy()
                    common.press_then_sleep("right", .125)
                    common.press_then_sleep("enter", .75)
                    self.checkBuy()
                    common.press_then_sleep("up", .125)
                    common.press_then_sleep("enter", .75)
                    self.checkBuy()
                # Get back to menu
                common.press_then_sleep("esc", 2)
                common.press_then_sleep("esc", 1.5)
                common.press_then_sleep("right", .125)
            else:
                raise NameError("Not in home")
            self.count += 1
            common.debug("Car done! [" + str(self.count) + "/" + str(self.max_try) + " in " + self.ht.stringify() + "]")
        common.debug("Done AutoCarMastery")
