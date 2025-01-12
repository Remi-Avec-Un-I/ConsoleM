from enum import Enum


class Keys(Enum):
    ARROW = '\x1b'
    UP_ARROW = '\x1b[A'
    DOWN_ARROW = '\x1b[B'
    RIGHT_ARROW = '\x1b[C'
    LEFT_ARROW = '\x1b[D'
    TAB = '\t'
    ENTER = '\n'
    BACKSPACE = '\x7f'

    @property
    def get_name(self):
        return self.name.lower().replace("_", " ")

    @classmethod
    def get_all_keys(cls):
        return [key for key in cls]

if __name__ == "__main__":
    print("\x1b" in Keys)
    # get Keys.ARROW from "ARROW"
    print(Keys["ARROW"])
