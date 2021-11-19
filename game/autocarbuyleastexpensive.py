import time

from utils import common
from utils.handlercv2 import HandlerCv2


class AutoCarBuyLeastExpensive:
    count = 0
    max = 25
    nb_row = 1

    def __init__(self, hcv2: HandlerCv2 = None):
        common.debug("Create AutoCarBuyLeastExpensive")
        if hcv2:
            self.hcv2 = hcv2
        else:
            self.hcv2 = HandlerCv2()
        self.images = self.hcv2.load_images(["color",
                                             "not_buy",
                                             "not_enaugh_cr",
                                             "salon_auto",
                                             "valor",
                                             "valor_menu",
                                             "valor_selected"])
        self.running = False

    def run(self):
        common.debug("Start AutoCarBuyLeastExpensive (after 5 secs)")
        time.sleep(5)
        self.running = True
        timer = time.time()
        while self.running and self.count < self.max:
            # Enter salon
            if not self.hcv2.check_match(self.images["salon_auto"], True):
                raise NameError("Not at salon")
            common.press_then_sleep("enter", 2)
            # Filter not buy
            common.press_then_sleep("y")
            if not self.hcv2.check_match(self.images["not_buy"], True):
                raise NameError("Filter not found")
            common.click_then_sleep(self.hcv2.random_find(), .125)
            common.press_then_sleep("esc", 2)
            # Sort
            common.press_then_sleep("x")
            if not self.hcv2.check_match(self.images["valor"], True):
                raise NameError("Sort not found")
            common.click_then_sleep(self.hcv2.random_find(), .125)
            if self.hcv2.check_match(self.images["valor_selected"], True):
                common.press_then_sleep("enter")
            time.sleep(1)
            # GoTo least expensive
            common.press_then_sleep("backspace")
            if self.nb_row == 2:
                common.click_then_sleep((570, 770), .125)
            elif self.nb_row == 2:
                common.click_then_sleep((570, 740), .125)
            else:
                common.click_then_sleep((570, 710), .125)

            if self.hcv2.check_match(self.images["valor_menu"], True):
                common.press_then_sleep("enter", 2)
            # Buy
            common.press_then_sleep("enter", 1)
            while not self.hcv2.check_match(self.images["color"], True):
                time.sleep(.1)
            common.press_then_sleep("y", 2)
            common.press_then_sleep("enter", 1)
            common.press_then_sleep("enter", 1)
            if self.hcv2.check_match(self.images["not_enaugh_cr"], True):
                raise NameError("Not Enaugh CR")
            common.press_then_sleep("enter", 20)
            common.press_then_sleep("esc", 3)

            self.count += 1
            common.debug("Car bought! [" + str(self.count) + "/" + str(self.max) + " in " + str(
                round(time.time() - timer, 2)) + "s]")
            timer = time.time()
            time.sleep(1)
        common.debug("Done AutoCarBuyLeastExpensive")
