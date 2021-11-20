from utils import common
from utils.handlercv2 import HandlerCv2
from utils.handlertime import HandlerTime


class GameCommon:
    def __init__(self, hcv2: HandlerCv2 = None):
        common.debug("Create GameCommon")
        if hcv2:
            self.hcv2 = hcv2
        else:
            self.hcv2 = HandlerCv2()
        self.ht = HandlerTime()
        self.images = self.hcv2.load_images(["lamborghini",
                                             "lamborghini_name_selected",
                                             "my_cars"])

    def home_getmycar(self):
        self.home_goinmycars()
        self.home_mycars_getinlambo()

    def home_goinmycars(self):
        if not self.hcv2.check_match(self.images["my_cars"], True):
            raise NameError("Not in home")
        common.press_then_sleep("enter", 2)

    def home_mycars_getinlambo(self):
        # Filter favorites
        common.press_then_sleep("y")
        common.press_then_sleep("enter")
        common.press_then_sleep("esc", 2)
        # Constructor
        common.press_then_sleep("backspace", 1)
        if not self.hcv2.check_match(self.images["lamborghini"], True):
            raise NameError("No lambo in favorites")
        common.click_then_sleep(self.hcv2.random_find(), .125)
        if self.hcv2.check_match(self.images["lamborghini_name_selected"], True):
            common.press_then_sleep("enter", 1)
        # Get in car
        common.press_then_sleep("enter")
        common.press_then_sleep("enter", 1)
        cnt = 0
        while not self.hcv2.check_match(self.images["my_cars"], True):
            common.press_then_sleep("esc", 1)
            cnt += 1
            if cnt > 10:
                raise NameError("My cars not found")
