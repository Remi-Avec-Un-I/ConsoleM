from __future__ import annotations

import os
import sys
import threading
import queue
from ConsoleM.Core.linux_driver import  LinuxDriver
from ConsoleM.Core.const.keys import Keys


class Terminal:
    def __init__(self):
        """
        Utility class for interacting with the terminal.
        This is a wrapper around the LinuxDriver class and WindowsDriver class (wip).
        """
        self.keys = queue.Queue()
        self._tr_key_input: threading.Thread | None = None
        if os.name == 'nt':
            raise NotImplementedError('Windows is not supported yet')
        elif os.name == 'posix':
            self.driver = LinuxDriver()
        else:
            raise NotImplementedError('Unsupported OS')

    @staticmethod
    def clear_line():
        sys.stdout.write("\033[2K")
        sys.stdout.flush()

    @staticmethod
    def clear_lines_above(n: int):
        for _ in range(n):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[2K")
        sys.stdout.flush()

    @staticmethod
    def create_alternate_screen():
        sys.stdout.write("\033[?1049h")
        sys.stdout.flush()

    @staticmethod
    def restore_alternate_screen():
        sys.stdout.write("\033[?1049l")
        sys.stdout.flush()

    @staticmethod
    def clear():
        sys.stdout.write("\033[2J")

    @staticmethod
    def clear_end_of_line():
        sys.stdout.write("\033[K")

    @staticmethod
    def move_cursor(x: int, y: int):
        """
        Move the cursor to the specified position.
        ex: move_cursor(1, 1) will move the cursor to the top left corner of the terminal.
        """
        sys.stdout.write(f"\033[{y};{x}H")
        sys.stdout.flush()

    @staticmethod
    def move_cursor_relative(x: int, y: int):
        """
        Move the cursor relative to its current position.
        ex: move_cursor_relative(1, 0) will move the cursor one column to the right.
        move_cursor_relative(-1, 0) will move the cursor one column to the left.
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
        sys.stdout.write(text)
        sys.stdout.flush()

    def handle_key_input(self):
        self._tr_key_input = threading.Thread(target=self.driver.handle_key_input, args=(self.keys,))
        self._tr_key_input.start()

    def stop_handle_key_input(self):
        self.driver.stop_handle_key_input()
        self._tr_key_input.join()

    def hide_cursor(self):
        self.driver.hide_cursor()

    def show_cursor(self):
        self.driver.show_cursor()

    def get_cursor_position(self) -> tuple[int, int]:
        return self.driver.get_cursor_position()

    def get_terminal_size(self) -> tuple[int, int]:
        return self.driver.get_terminal_size()

    def get_key_from_queue(self) -> str:
        key: str = self.keys.get()
        if key in Keys:
            return Keys(key).name
        return key




if __name__ == "__main__":
    terminal = Terminal()
    terminal.handle_key_input()
