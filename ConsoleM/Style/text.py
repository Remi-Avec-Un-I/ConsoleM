from __future__ import annotations

from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from _typeshed import SupportsWrite

from . import Render

class Text:
    def __init__(self, content: str, print: bool = False):
        self.content = content
        if print:
            self.print()

    def __str__(self):
        return self._render()

    def _render(self):
        return Render(self.content).render()

    def print(self,
              *values: object,
              sep: str | None = " ",
              end: str | None = "\n",
              file: SupportsWrite[str] | None = None,
              flush: Literal[False] = False) -> None:
        if values:
            return print(*values, sep=sep, end=end, file=file, flush=flush)
        return print(self._render(), sep=sep, end=end, file=file, flush=flush)