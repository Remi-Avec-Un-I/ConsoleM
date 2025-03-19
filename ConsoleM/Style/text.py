from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from .render import Render

if TYPE_CHECKING:
    from _typeshed import SupportsWrite


class Text:
    """A powerful interface for creating styled terminal output using markup syntax.
    
    The Text class allows you to create styled text using markup syntax:
    - Colors: [red]text[/], [blue]text[/], etc.
    - Styles: [bold]text[/], [underline]text[/], etc.
    - Emojis: :emoji_name:
    - Reset: [reset] to clear all styling
    
    Available Colors:
        [red], [blue], [green], [yellow], [magenta], [cyan], [white], [black], [gray], [default]
    
    Available Styles:
        [bold] or [b], [dim] or [d], [italic] or [i], [underline] or [u],
        [blink], [blink2], [reverse] or [r], [conceal] or [c], [strike] or [s],
        [underline2] or [uu], [frame], [encircle], [overline] or [o]
    
    Example:
        >>> Text("[red]Error:[/] Something went wrong").print()
        >>> Text("[bold blue]Important:[/] This is a message").print()
        >>> Text("[green]Success![/] :check_mark: Operation completed").print()
    """

    def __init__(self, content: str):
        """Initialize a Text object for styled terminal output.
        
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
        """Return the rendered text with all styling applied.
        
        Returns:
            str: The rendered text with ANSI escape codes and emojis
        """
        return self._render()
    
    @property
    def content(self):
        """Get or set the rendered content of the text.
        
        The content is cached after first rendering for better performance.
        
        Returns:
            str: The rendered text with all styling applied
            
        Raises:
            TypeError: If trying to set content to a non-string value
        """
        if self.cache is None:
            self.cache = self._render()
        return self.cache
    
    @property
    def raw_content(self):
        """Get the raw content before rendering.
        
        Returns:
            str: The original text with markup syntax
        """
        return self.ctn
    
    @content.setter
    def content(self, value):
        """Set the content of the text.
        
        Args:
            value (str): New content with optional styling markup
            
        Raises:
            TypeError: If value is not a string
        """
        if not isinstance(value, str):
            raise TypeError("Can't set content to a non-string value")
        self.cache = None
        self.ctn = value

    def _render(self):
        """Render the text by converting markup to ANSI escape codes and emojis.
        
        Returns:
            str: The rendered text with all styling applied
        """
        return Render(self.ctn).render()

    def print(self,
              *values: object,
              sep: str | None = " ",
              end: str | None = "\n",
              file: SupportsWrite[str] | None = None,
              flush: Literal[False] = False) -> None:
        """Print the rendered text to the console.
        
        This method wraps Python's built-in print function and supports all its parameters.
        
        Args:
            *values: Additional values to print
            sep: Separator between values (default: " ")
            end: String to print at the end (default: "\n")
            file: File to write to (default: None, uses sys.stdout)
            flush: Whether to flush the output (default: False)
        """
        if values:
            return print(*values, sep=sep, end=end, file=file, flush=flush)
        return print(self._render(), sep=sep, end=end, file=file, flush=flush)
