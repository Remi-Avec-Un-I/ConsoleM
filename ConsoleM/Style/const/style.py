from __future__ import annotations

from enum import Enum

STYLE_ATTRIBUTES = {
    "dim": "dim",
    "d": "dim",
    "bold": "bold",
    "b": "bold",
    "italic": "italic",
    "i": "italic",
    "underline": "underline",
    "u": "underline",
    "blink": "blink",
    "blink2": "blink2",
    "reverse": "reverse",
    "r": "reverse",
    "conceal": "conceal",
    "c": "conceal",
    "strike": "strike",
    "s": "strike",
    "underline2": "underline2",
    "uu": "underline2",
    "frame": "frame",
    "encircle": "encircle",
    "overline": "overline",
    "o": "overline",
}

def get_all_styles() -> list[str]:
    return ["bold", "dim", "italic", "underline", "blink", "blink2", "reverse", "hide", "strike"]

class Style(Enum):
    NONE = -1
    NORMAL = 0
    BOLD = 1
    DIM = 2
    ITALIC = 3
    UNDERLINE = 4
    BLINK = 5
    BLINK2 = 6
    REVERSE = 7
    HIDE = 8
    STRIKE = 9
    UNDERLINE2 = 21
    FRAME = 51
    ENCIRCLE = 52
    OVERLINE = 53

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def get_style_from_str(cls, style: str) -> Style:
        if style.lower() in get_all_styles():
            return cls[style.upper()] # type: ignore
        return cls.NORMAL
