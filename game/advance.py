import math

from game import constant
from game.autocarbuy import AutoCarBuy
from game.autocarmastery import AutoCarMastery
from game.common import GameCommon
from game.constant import Car
from utils import common
from utils.constant import DebugLevel


class Advance:
    def __init__(self):
        self.car = constant.CAR.value

    @staticmethod
    def AutoCarBuy_Then_AutoCarMastery(acb: AutoCarBuy, acm: AutoCarMastery, nbcar: int = 70):
        """
        From main, used to do AutoCarBuy (already places on the pontiac) then AutoCarMastery
        """
        common.debug("AutoCarBuy + AutoCarMastery for " + str(nbcar) + " cars", DebugLevel.INFO)
        acb.run(nbcar)
        common.press("left")
        acm.run(nbcar)

    def AutoCarBuy_Then_AutoCarMastery_from_menu_to_menu(self, gc: GameCommon, acb: AutoCarBuy, acm: AutoCarMastery):
        """
        From main, used to do AutoCarBuy (from game) then AutoCarMastery then get in my lambo :)
        """
        if self.car == Car.FORD.value:
            nbcar = math.floor(999 / 5)
        elif self.car == Car.PONTIAC.value:
            nbcar = math.floor(999 / 14)
        elif self.car == Car.PORSCHE.value:
            nbcar = math.floor(999 / 11)
        else:
            raise NameError("Unknow car")

        gc.go_home_garage()
        gc.go_to_car_to_buy()
        self.AutoCarBuy_Then_AutoCarMastery(acb, acm, nbcar)
        gc.home_getmycar()
        common.press("esc", 10)
