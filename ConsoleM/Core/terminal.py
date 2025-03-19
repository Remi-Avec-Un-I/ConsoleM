from __future__ import annotations

import os
import sys
import threading
import queue

if os.name == 'nt':
    raise NotImplementedError('Windows is not supported yet')
else:
    from ConsoleM.Core.linux_driver import  LinuxDriver as Driver

from ConsoleM.Core.const.keys import Keys


class Terminal:
    """A high-level interface for terminal manipulation and input handling.
    
    This class provides methods for:
    - Screen manipulation (clear, move cursor)
    - Input handling
    - Cursor control
    - Terminal size detection
    
    Example:
        >>> term = Terminal()
        >>> term.clear()
        >>> term.move_cursor(1, 1)
        >>> width, height = term.get_terminal_size()
    """

    def __init__(self):
        """Initialize a new Terminal instance.
        
        This creates a terminal interface that supports:
        - Screen manipulation (clear, move cursor)
        - Input handling
        - Cursor control
        - Terminal size detection
        
        Raises:
            NotImplementedError: If running on Windows (not supported yet) or unsupported OS
        """
        self.keys = queue.Queue()
        self._tr_key_input: threading.Thread | None = None
        self.driver = Driver()

    @staticmethod
    def clear_line():
        """Clear the current line from cursor position to the end.
        
        This is useful for updating progress or status lines.
        """
        sys.stdout.write("\033[2K")
        sys.stdout.flush()

    @staticmethod
    def clear_lines_above(n: int):
        """Clear n lines above the current cursor position.
        
        Args:
            n (int): Number of lines to clear above the current position
        """
        for _ in range(n):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[2K")
        sys.stdout.flush()

    @staticmethod
    def create_alternate_screen():
        """Create an alternate screen buffer.
        
        This is useful for full-screen applications like text editors.
        The original screen content is preserved and can be restored.
        """
        sys.stdout.write("\033[?1049h")
        sys.stdout.flush()

    @staticmethod
    def restore_alternate_screen():
        """Restore the original screen after using alternate screen.
        
        This restores the terminal to its previous state.
        """
        sys.stdout.write("\033[?1049l")
        sys.stdout.flush()

    @staticmethod
    def clear():
        """Clear the entire terminal screen.
        
        This is equivalent to the 'clear' command in the terminal.
        """
        sys.stdout.write("\033[2J")

    @staticmethod
    def clear_end_of_line():
        """Clear from cursor position to the end of the current line."""
        sys.stdout.write("\033[K")

    @staticmethod
    def move_cursor(x: int, y: int):
        """Move the cursor to the specified position.
        
        Args:
            x (int): Column position (1-based)
            y (int): Row position (1-based)
            
        Example:
            >>> term.move_cursor(1, 1)  # Move to top-left corner
        """
        sys.stdout.write(f"\033[{y};{x}H")
        sys.stdout.flush()

    @staticmethod
    def move_cursor_relative(x: int, y: int):
        """Move the cursor relative to its current position.
        
        Args:
            x (int): Number of columns to move (positive = right, negative = left)
            y (int): Number of rows to move (positive = down, negative = up)
            
        Example:
            >>> term.move_cursor_relative(1, 0)  # Move one column right
            >>> term.move_cursor_relative(-1, 0)  # Move one column left
        """
        if x > 0:
            sys.stdout.write(f"\033[{x}C")
        elif x < 0:
            sys.stdout.write(f"\033[{abs(x)}D")
        if y > 0:
            sys.stdout.write(f"\033[{y}B")
        elif y < 0:
            sys.stdout.write(f"\033[{abs(y)}A")
        sys.stdout.flush()

    @staticmethod
    def write(text: str):
        """Write text to the terminal.
        
        Args:
            text (str): Text to write
        """
        sys.stdout.write(text)
        sys.stdout.flush()

    def handle_key_input(self):
        """Start capturing keyboard input in a separate thread.
        
        This enables non-blocking keyboard input handling.
        Use get_key_from_queue() to retrieve pressed keys.
        """
        self._tr_key_input = threading.Thread(target=self.driver.handle_key_input, args=(self.keys,))
        self._tr_key_input.start()

    def stop_handle_key_input(self):
        """Stop capturing keyboard input.
        
        This should be called when you're done with input handling.
        """
        self.driver.stop_handle_key_input()
        self._tr_key_input.join()

    def get_key_from_str(self, key: str) -> Keys | None:
        """Get the key objectfrom a string.
        
        Args:
            key (str): The key to get
        
        Returns:
            Keys: The key or None if not found
        """
        return Keys.get(key)

    def hide_cursor(self):
        """Hide the terminal cursor.
        
        Useful for full-screen applications or when you don't want the cursor visible.
        """
        self.driver.hide_cursor()

    def show_cursor(self):
        """Show the terminal cursor.
        
        Restores cursor visibility after hiding it.
        """
        self.driver.show_cursor()

    def get_cursor_position(self) -> tuple[int, int]:
        """Get the current cursor position.
        
        Returns:
            tuple[int, int]: Current (x, y) position of the cursor
        """
        return self.driver.get_cursor_position()

    def get_terminal_size(self) -> tuple[int, int]:
        """Get the current terminal dimensions.
        
        Returns:
            tuple[int, int]: Current (width, height) of the terminal
        """
        return self.driver.get_terminal_size()

    def get_key_from_queue(self) -> str:
        """Get the next key press from the input queue.
        
        Returns:
            str: The pressed key or special key name (e.g., 'UP_ARROW', 'ENTER')
        """
        key: str = self.keys.get()
        if key in Keys:
            return Keys(key).name
        return key
    