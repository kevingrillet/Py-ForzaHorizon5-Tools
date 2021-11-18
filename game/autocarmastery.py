import time

from utils import common
from utils.handlercv2 import HandlerCv2


class AutoCarMastery:
    count = 0
    max = 50

    def __init__(self, hcv2: HandlerCv2 = None):
        common.debug("Create AutoCarMastery")
        if hcv2:
            self.hcv2 = hcv2
        else:
            self.hcv2 = HandlerCv2()
        self.images = self.hcv2.load_images(["already_done",
                                             "pontiac",
                                             "pontiac_name",
                                             "pontiac_name_selected",
                                             "my_cars"])
        self.running = False

    def run(self):
        common.debug("Start AutoCarMastery (after 5 secs)")
        time.sleep(5)
        self.running = True
        timer = time.time()
        while self.running and self.count < self.max:
            if self.hcv2.check_match(self.images["my_cars"], True):
                # My cars
                common.press_then_sleep("enter", 2)
                # Constructor
                common.press_then_sleep("backspace", 1)
                if self.hcv2.check_match(self.images["pontiac_name"], True):
                    common.click_then_sleep(self.hcv2.random_find(), 1)
                    if self.hcv2.check_match(self.images["pontiac_name_selected"], True):
                        common.press_then_sleep("enter", 1)
                else:
                    raise NameError("Pontiac name not found")
                time.sleep(1)
                # Find car to delete
                if self.count > 1:  # Need to skip it 2 times to begin
                    if self.hcv2.check_match(self.images["pontiac"], True):
                        # common.click_then_sleep(self.hcv2.random_find())
                        # common.debug("Choose car to delete (in 3 secs)")
                        # time.sleep(3)
                        # common.click_then_sleep((1180, 530))
                        common.press_then_sleep("right", .25)
                    else:
                        raise NameError("Pontiac to delete not found")
                    common.press_then_sleep("enter")
                    # Delete button
                    common.press_then_sleep("down", .25)
                    common.press_then_sleep("down", .25)
                    common.press_then_sleep("down", .25)
                    common.press_then_sleep("down", .25)
                    common.press_then_sleep("enter", 1)
                    # Confirm
                    common.press_then_sleep("enter", 2)
                # Find car to use
                if self.hcv2.check_match(self.images["pontiac"], True):
                    # common.click_then_sleep(self.hcv2.random_find())
                    # common.debug("Choose car to use (in 3 secs)")
                    # time.sleep(3)
                    # common.click_then_sleep((1180, 530))
                    common.press_then_sleep("up", .25)
                    common.press_then_sleep("right", .25)
                else:
                    raise NameError("Pontiac to drive not found")
                common.press_then_sleep("enter", 1)
                common.press_then_sleep("enter", 10)
                if not self.hcv2.check_match(self.images["my_cars"], True):
                    common.press_then_sleep("esc", 2)
                # Boost
                common.press_then_sleep("left", 1.5)
                common.press_then_sleep("enter", 2)
                # Mastery
                common.press_then_sleep("right", .25)
                common.press_then_sleep("right", .25)
                common.press_then_sleep("down", .25)
                common.press_then_sleep("enter", 2)
                if not self.hcv2.check_match(self.images["already_done"], True):
                    # MASTERRR
                    common.press_then_sleep("enter", 1)
                    common.press_then_sleep("right", .25)
                    common.press_then_sleep("enter", 1)
                    common.press_then_sleep("right", .25)
                    common.press_then_sleep("enter", 1)
                    common.press_then_sleep("up", .25)
                    common.press_then_sleep("enter", 1)
                    common.press_then_sleep("right", .25)
                    common.press_then_sleep("enter", 1)
                    common.press_then_sleep("up", .25)
                    common.press_then_sleep("enter", 1)
                # Get back to menu
                common.press_then_sleep("esc", 3)
                common.press_then_sleep("esc", 2)
                common.press_then_sleep("right", .25)
            else:
                raise NameError("Not in home")
            self.count += 1
            common.debug("Car done! [" + str(self.count) + " in " + str(round(time.time() - timer, 2)) + "s]")
            timer = time.time()
        common.debug("Done AutoCarMastery")
