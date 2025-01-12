from enum import Enum
from typing import Union


class AsciiEscapeCode(Enum):
    """Control Sequence Introducer (CSI) marks the beginning of a control sequence, e.g. "\\u1b[31m"."""

    OCTAL = "\033"
    """Supported in: Bash, C, Python 3."""

    HEX = "\x1b"
    """Supported in: Bash, C, Python 3."""

    UNICODE = "\u001b"
    """Supported in: Bash, Python 3."""

    def __str__(self) -> str:
        return str(self.value)

    def build(self, *codes: Union[int, str]) -> str:
        if len(codes) > 2:
            raise ValueError("Too many codes. Only 2 codes are allowed.")

        if len(codes) == 1:
            return f"{self.value}[{codes[0]}m"

        return f"{self.value}[{codes[0]};{codes[1]}m"