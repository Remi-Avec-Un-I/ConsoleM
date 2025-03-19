from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from .render import Render

if TYPE_CHECKING:
    from _typeshed import SupportsWrite


class Text:
    def __init__(self, content: str):
        """
        Initialize a Text object for styled terminal output.

        The Text class allows you to create styled text using markup syntax:
        - Colors: [red]text[/], [blue]text[/], etc.
        - Styles: [bold]text[/], [underline]text[/], etc.
        - Emojis: :emoji_name:
        - Reset: [reset] to clear all styling

        Args:
            content (str): The text content with optional styling markup

        Examples:
            >>> Text("[red]Hello[/] World").print()
            Hello World  # "Hello" will be red
            
            >>> Text("[blue bold]Styled[/] :smile: text").print() 
            Styled 😊 text  # "Styled" will be blue and bold
        """
        self.ctn = content
        self.cache = None

    def __str__(self):
        return self._render()
    
    @property
    def content(self):
        if self.cache is None:
            self.cache = self._render()
        return self.cache
    
    @property
    def raw_content(self):
        return self.ctn
    
    @content.setter
    def content(self, value):
        if not isinstance(value, str):
            raise TypeError("Can't set content to a non-string value")
        self.cache = None
        self.ctn = value

    def _render(self):
        return Render(self.ctn).render()

    def print(self,
              *values: object,
              sep: str | None = " ",
              end: str | None = "\n",
              file: SupportsWrite[str] | None = None,
              flush: Literal[False] = False) -> None:
        if values:
            return print(*values, sep=sep, end=end, file=file, flush=flush)
        return print(self._render(), sep=sep, end=end, file=file, flush=flush)
