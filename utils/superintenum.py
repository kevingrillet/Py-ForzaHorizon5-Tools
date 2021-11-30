from enum import IntEnum


class SuperIntEnum(IntEnum):
    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

    def _generate_next_value_(self, start, count, last_values):
        return count

    def first(self):
        """
        return first element of the enum
        """
        cls = self.__class__
        members = list(cls)
        if len(members) == 0:
            raise ValueError('Enumeration has no values')
        return members[0]

    def last(self):
        """
        return last element of the enum
        """
        cls = self.__class__
        members = list(cls)
        if len(members) == 0:
            raise ValueError('Enumeration has no values')
        return members[-1]

    def prev(self, step: int = 1):
        """
        return previous element of the enum
        """
        cls = self.__class__
        members = list(cls)
        index = members.index(self) - step
        if index < 0:
            raise StopIteration('Enumeration ended')
        return members[index]

    def next(self, step: int = 1):
        """
        return next element of the enum
        """
        cls = self.__class__
        members = list(cls)
        index = members.index(self) + step
        if index >= len(members):
            raise StopIteration('Enumeration ended')
        return members[index]
