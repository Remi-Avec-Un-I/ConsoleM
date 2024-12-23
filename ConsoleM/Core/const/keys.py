from enum import Enum


class Keys(Enum):
    ARROW = '\x1b'
    UP_ARROW = '\x1b[A'
    DOWN_ARROW = '\x1b[B'
    RIGHT_ARROW = '\x1b[C'
    LEFT_ARROW = '\x1b[D'
    TAB = '\t'
    ENTER = '\n'

if __name__ == "__main__":
    print("\x1b" in Keys)
