from __future__ import annotations

from enum import Enum

from ConsoleM.Style.const.ascii import AsciiEscapeCode

def get_all_colors() -> list[str]:
    return ["reset", "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white", "default", "gray"]

class Color256:
    GRAY = "5;8"

class Color(Enum):
    NONE = -1
    RESET = 0
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
    DEFAULT = 39
    BRIGHT_BLACK = 90
    BRIGHT_RED = 91
    BRIGHT_GREEN = 92
    BRIGHT_YELLOW = 93
    BRIGHT_BLUE = 94
    BRIGHT_MAGENTA = 95
    BRIGHT_CYAN = 96
    BRIGHT_WHITE = 97

    GRAY = Color256.GRAY

    def __str__(self) -> str:
        return f"{AsciiEscapeCode.OCTAL.value}{self.value}m"

    @classmethod
    def get_color_from_str(cls, color: str) -> Color:
        if color.lower() in get_all_colors():
            return cls[color.upper()] # type: ignore
        return cls.DEFAULT