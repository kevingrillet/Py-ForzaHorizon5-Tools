import time
from datetime import timedelta
from string import Formatter


class HandlerTime:
    my_timer = time.time()

    def get_timer(self) -> float:
        """
        Get time since start
        :return: difference in seconds
        """
        return time.time() - self.my_timer

    @staticmethod
    def handle_stringify(timer: float) -> str:
        """
        Beautify output
        :param timer: time to beautify
        :return: time formated
        """
        if timer >= 3600:
            fmt = '{H:02}h {M:2}m {S:02.02f}s'
        elif timer >= 60:
            fmt = '{M:02}m {S:02.02f}s'
        else:
            fmt = '{S:02.02f}s'
        return HandlerTime.strfdelta(timedelta(seconds=timer), fmt)

    def start(self):
        """
        Start timer
        """
        self.my_timer = time.time()

    def stringify(self) -> str:
        """
        Beautify output
        :return: time formated
        """
        ret = self.handle_stringify(self.get_timer())
        self.start()
        return ret

    @staticmethod
    # https://stackoverflow.com/questions/538666/format-timedelta-to-string/63198084#63198084
    def strfdelta(tdelta, fmt='{D:02}d {H:02}h {M:02}m {S:02.0f}s', inputtype='timedelta') -> str:
        """
        Convert a datetime.timedelta object or a regular number to a custom-
        formatted string, just like the stftime() method does for datetime.datetime
        objects.

        The fmt argument allows custom formatting to be specified.  Fields can
        include seconds, minutes, hours, days, and weeks.  Each field is optional.

        Some examples:
            '{D:02}d {H:02}h {M:02}m {S:02.0f}s' --> '05d 08h 04m 02s' (default)
            '{W}w {D}d {H}:{M:02}:{S:02.0f}'     --> '4w 5d 8:04:02'
            '{D:2}d {H:2}:{M:02}:{S:02.0f}'      --> ' 5d  8:04:02'
            '{H}h {S:.0f}s'                       --> '72h 800s'

        The inputtype argument allows tdelta to be a regular number instead of the
        default, which is a datetime.timedelta object.  Valid inputtype strings:
            's', 'seconds',
            'm', 'minutes',
            'h', 'hours',
            'd', 'days',
            'w', 'weeks'
        """

        # Convert tdelta to integer seconds.
        if inputtype == 'timedelta':
            remainder = tdelta.total_seconds()
        elif inputtype in ['s', 'seconds']:
            remainder = float(tdelta)
        elif inputtype in ['m', 'minutes']:
            remainder = float(tdelta) * 60
        elif inputtype in ['h', 'hours']:
            remainder = float(tdelta) * 3600
        elif inputtype in ['d', 'days']:
            remainder = float(tdelta) * 86400
        elif inputtype in ['w', 'weeks']:
            remainder = float(tdelta) * 604800

        f = Formatter()
        desired_fields = [field_tuple[1] for field_tuple in f.parse(fmt)]
        possible_fields = ('Y', 'm', 'W', 'D', 'H', 'M', 'S', 'mS', 'µS')
        constants = {'Y': 86400 * 365.24, 'm': 86400 * 30.44, 'W': 604800, 'D': 86400, 'H': 3600, 'M': 60, 'S': 1,
                     'mS': 1 / pow(10, 3), 'µS': 1 / pow(10, 6)}
        values = {}
        for field in possible_fields:
            if field in desired_fields and field in constants:
                Quotient, remainder = divmod(remainder, constants[field])
                values[field] = int(Quotient) if field != 'S' else Quotient + remainder
        return f.format(fmt, **values)
