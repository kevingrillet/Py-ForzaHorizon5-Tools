import logging
import math
import os
import sys
import time
from datetime import datetime
from pathlib import Path

from game import constant
from game.autocarbuy import AutoCarBuy
from game.autocarbuyauction import AutoCarBuyAuction
from game.autocarbuyleastexpensive import AutoCarBuyLeastExpensive
from game.autocarmastery import AutoCarMastery
from game.autogpsdestination import AutoGPSDestination
from game.autolabreplay import AutoLabReplay
from game.autophotoallmycars import AutoPhotoAllMyCars
from game.autoracerestart import AutoRaceRestart
from game.autowheelspins import AutoWheelspins
from game.common import GameCommon
from game.constant import Car, AlreadyOwnedChoice
from utils import common
from utils.constant import DebugLevel, Lang
from utils.handlerconfig import HandlerConfig
from utils.handlercv2 import HandlerCv2
from utils.handlertime import HandlerTime
from utils.handlerwin32 import HandlerWin32


def AutoCarBuy_Then_AutoCarMastery(_acb: AutoCarBuy, _acm: AutoCarMastery, nbcar: int = None):
    """
    From main, used to do AutoCarBuy (already places on the pontiac) then AutoCarMastery
    :param _acb:
    :param _acm:
    :param nbcar:
    """
    if nbcar is None:
        if constant.CAR.value == Car.FORD.value:
            nbcar = math.floor(999 / 5)
        elif constant.CAR.value == Car.PONTIAC.value:
            nbcar = math.floor(999 / 14)
        elif constant.CAR.value == Car.PORSCHE.value:
            nbcar = math.floor(999 / 14)  # 11
        else:
            raise NameError('Unknow car')
    common.info('AutoCarBuy + AutoCarMastery for ' + str(nbcar) + ' cars')
    _acb.run(nbcar)
    common.press('left')
    _acm.run(nbcar)  # 1rst car is 'always' already done


def AutoCarBuy_Then_AutoCarMastery_from_menu_to_menu(_gc: GameCommon, _acb: AutoCarBuy, _acm: AutoCarMastery,
                                                     nbcar: int = None):
    """
    From main, used to do AutoCarBuy (from game) then AutoCarMastery then get in my lambo :)
    :param _gc:
    :param _acb:
    :param _acm:
    :param nbcar:
    """
    _gc.go_home_garage()
    _gc.go_to_car_to_buy()
    AutoCarBuy_Then_AutoCarMastery(_acb, _acm, nbcar)
    _gc.home_getmycar()
    common.press('esc', 10)


def load_config():
    """
    Load config from config file
    Create it if not existing
    :return:
    """
    hcfg = HandlerConfig('config.ini')
    constant.CAR = Car(hcfg.get_value('car', constant.CAR.value))
    constant.DEBUG_LEVEL = DebugLevel(int(hcfg.get_value('debug', str(constant.DEBUG_LEVEL.value))))
    constant.DEV_MODE = hcfg.get_value('dev', str(constant.DEV_MODE)) == 'True'
    constant.LANG = Lang(hcfg.get_value('language', constant.LANG.value))
    constant.OWNED = AlreadyOwnedChoice(int(hcfg.get_value('owned', str(constant.OWNED.value))))
    constant.SCALE = float(hcfg.get_value('scale', str(constant.SCALE)))


def quit_game():
    """
    Quit game after 30 secs
    """
    common.sleep(30)
    common.alt_f4()


def show_menu():
    """
    Show menu
    """
    print(' ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
    print(' ┃                    Py-ForzaHorizon5-Tools                   ┃')
    print(' ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫')
    print(' ┃ Basic                         ┃ Advanced                    ┃')
    print(' ┃  1 - AutoWheelspins           ┃  45  - AutoCarBuy           ┃')
    print(' ┃  2 - AutoGPSDestination       ┃           + AutoCarMastery  ┃')
    print(' ┃  3 - AutoLabReplay            ┃                             ┃')
    print(' ┃  4 - AutoCarBuy               ┃  453 - 45 + AutoLabReplay   ┃')
    print(' ┃  5 - ⚠ AutoCarMastery ⚠       ┃                             ┃')
    print(' ┃  6 - AutoCarBuyLeastExpensive ┃  457 - 45 + AutoRaceRestart ┃')
    print(' ┃  7 - AutoRaceRestart          ┃                             ┃')
    print(' ┃  8 - AutoPhotoAllMyCars       ┃  99  - Just press z         ┃')
    print(' ┃  9 - AutoCarBuyAuction        ┃                             ┃')
    print(' ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
    common.log('Your choice:')


if __name__ == '__main__':
    try:
        Path('logs/').mkdir(parents=True, exist_ok=True)
        logging.basicConfig(handlers=[logging.StreamHandler(sys.stdout),
                                      logging.FileHandler('logs/' + str(datetime.now()).replace(':', '.') + '.log')],
                            format='%(message)s', level=logging.DEBUG)
        common.info('Started')
        start_time = time.time()

        load_config()
        show_menu()
        intinput = int(input() or '-1')
        common.log(str(intinput))
        hcv2 = HandlerCv2(scale=constant.SCALE)
        hcv2.threshold = 0.9 if constant.SCALE == 1 else 0.8

        # Menu
        if intinput == 1:
            AutoWheelspins(hcv2).run()
        elif intinput == 2:
            AutoGPSDestination(hcv2).run()
        elif intinput == 3:
            AutoLabReplay(hcv2).run()
        elif intinput == 4:
            common.log('Number of cars to buy: (default: 50)')
            nb_buy = int(input() or '50')
            AutoCarBuy(hcv2).run(nb_buy)
        elif intinput == 5:
            common.log('Number of cars to master: (default: 50)')
            nb_mastery = int(input() or '50')
            AutoCarMastery(hcv2).run(nb_mastery)
        elif intinput == 6:
            common.log('Number of cars to buy: (default: 50)')
            nb_buy = int(input() or '50')
            AutoCarBuyLeastExpensive(hcv2).run(nb_buy)
        elif intinput == 7:
            common.log('Number of restart: (default: 100)')
            nb_restart = int(input() or '100')
            AutoRaceRestart(hcv2).run(nb_restart)
        elif intinput == 8:
            common.log('Where to start: (default: 1)')
            nb_start = int(input() or '1')
            AutoPhotoAllMyCars(hcv2).run(nb_start)
        elif intinput == 9:
            common.log('Number of cars to buy: (default: 1)')
            nb_car_to_buy = int(input() or '1')
            AutoCarBuyAuction(hcv2).run(nb_car_to_buy)

        # Just press Z
        elif intinput == 99:
            common.alt_tab()
            common.moveTo((10, 10))
            common.press('esc', 0)
            common.keyDown('z')

        # Advanced
        elif intinput == 45:
            common.log('Number of cars to buy & master: (default: None)')
            nb_cars = int(input() or None)
            common.alt_tab()
            common.moveTo((10, 10))
            AutoCarBuy_Then_AutoCarMastery(AutoCarBuy(hcv2), AutoCarMastery(hcv2), nb_cars)
        elif intinput == 453:
            common.debug('AutoCarBuy + AutoCarMastery + AutoLabReplay')
            gc = GameCommon(hcv2)
            acb = AutoCarBuy(hcv2)
            acm = AutoCarMastery(hcv2, gc)
            alr = AutoLabReplay(hcv2, gc, True)
            common.alt_tab()
            common.moveTo((10, 10))
            common.press('esc', 2)
            if gc.check_mastery():
                AutoCarBuy_Then_AutoCarMastery_from_menu_to_menu(gc, acb, acm)
            running = True
            while running:
                alr.run()
                AutoCarBuy_Then_AutoCarMastery_from_menu_to_menu(gc, acb, acm)
                # running = gc.check_super_wheelspins()
            quit_game()
        elif intinput == 457:
            common.debug('AutoCarBuy + AutoCarMastery + AutoRaceRestart')
            common.log('Number of restart: (default: 100)')
            nb_restart = int(input() or '100')
            gc = GameCommon(hcv2)
            acb = AutoCarBuy(hcv2)
            acm = AutoCarMastery(hcv2, gc)
            arr = AutoRaceRestart(hcv2)
            common.alt_tab()
            common.moveTo((10, 10))
            common.press('esc', 2)
            if gc.check_mastery():
                AutoCarBuy_Then_AutoCarMastery_from_menu_to_menu(gc, acb, acm)
            running = True
            while running:
                gc.go_to_last_lab_race()
                arr.run(nb_restart)
                gc.quit_race()
                AutoCarBuy_Then_AutoCarMastery_from_menu_to_menu(gc, acb, acm)
                # running = gc.check_super_wheelspins()
            quit_game()

        # Dev
        elif intinput == 0:
            common.log(HandlerWin32.get_keyboard_language())
            common.log(common.convert_layout('z'))
            hcv2.hwin32.list_window_names()
            hcv2.dev()
        elif intinput == 98:
            arr = os.listdir('./images/common/')
            arr.extend(os.listdir('./images/' + constant.LANG.value + '/'))
            arr = [s.replace('.jpg', '') for s in arr]
            arr.sort()
            common.log('\nList of images:')
            for i in range(0, len(arr), 4):
                s1 = arr[i] if i < len(arr) else ''
                s2 = arr[i + 1] if i + 1 < len(arr) else ''
                s3 = arr[i + 2] if i + 2 < len(arr) else ''
                s4 = arr[i + 3] if i + 3 < len(arr) else ''
                common.log('{0:40} {1:40} {2:40} {3:40}'.format(s1, s2, s3, s4))
            common.log('\nChoose image to search:')
            img_name = input() or 'default'
            common.log(img_name)
            common.log('How many times?')
            repeat = int(input() or '1')
            common.log(str(repeat))
            cnt = 0
            for i in range(repeat):
                found = hcv2.check_match(hcv2.load_images([img_name])[img_name], True)
                if found:
                    cnt += 1
                common.log(hcv2.log())
            if repeat > 1:
                common.log('\nFound: ' + str(cnt) + '/' + str(repeat))
        elif intinput == 97:
            common.log('Number of mastery points: (default: 999)')
            nb_mastery = int(input() or '999')
            common.log(str(nb_mastery))
            common.log('Number of race until 999: ' + str(math.ceil((999 - nb_mastery) / 10)))
            if constant.CAR.value == Car.FORD.value:
                cost_per_car = 5
            elif constant.CAR.value == Car.PONTIAC.value:
                cost_per_car = 14
            elif constant.CAR.value == Car.PORSCHE.value:
                cost_per_car = 14  # 11
            else:
                raise NameError('Unknow car')
            common.log('Number of car mastery intil 0: ' + str(math.floor(nb_mastery / cost_per_car)))

        else:
            raise NameError('Not an option')

        common.info('Finished after ' + HandlerTime.handle_stringify(time.time() - start_time))
    except Exception as e:
        log = logging.getLogger()
        for hdlr in log.handlers[:]:  # remove the existing file handlers
            if not isinstance(hdlr, logging.FileHandler):
                log.removeHandler(hdlr)
        handler = logging.StreamHandler(sys.stderr)
        log.addHandler(handler)
        logging.error(e, exc_info=True)
