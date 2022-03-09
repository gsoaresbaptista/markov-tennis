from __future__ import annotations
from typing import Tuple, Union


class Markov:
    def __init__(self, name: str) -> None:
        #
        self.__name: str = name
        self.__left: Union[Markov, None] = None
        self.__right: Union[Markov, None] = None
        self.__finish = True

    @property
    def name(self) -> str:
        return self.__name

    @property
    def left(self) -> Union[Markov, None]:
        return self.__left

    @left.setter
    def left(self, left: Markov) -> None:
        self.__left = left
        self.__finish = False

    @property
    def right(self) -> Union[Markov, None]:
        return self.__right

    @right.setter
    def right(self, right: Markov) -> None:
        self.__right = right
        self.__finish = False

    def copy(self) -> Tuple[str, Union[Markov, None],
                            Union[Markov, None],
                            bool]:
        return self.__name, self.__left, \
            self.__right, self.__finish

    def is_over(self) -> bool:
        return self.__finish

    def process(self, p: bool) -> None:
        if (self.__right is not None and self.__left is not None):
            self.__name, self.__left, self.__right, self.__finish = \
                self.__left.copy() if p else self.__right.copy()
