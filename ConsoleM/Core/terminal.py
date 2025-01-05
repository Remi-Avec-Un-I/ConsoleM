import os
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

    def handle_key_input(self):
        self._tr_key_input = threading.Thread(target=self.driver.handle_key_input, args=(self.keys,))
        self._tr_key_input.start()

    def clear(self):
        print("\033[2J", end="")

    def clear_end_of_line(self):
        print("\033[K", end="")

    def stop_handle_key_input(self):
        self.driver.stop_handle_key_input()
        self._tr_key_input.join()

    def move_cursor(self, x: int, y: int):
        """
        Move the cursor to the specified position.
        ex: move_cursor(1, 1) will move the cursor to the top left corner of the terminal.
        """
        print(f"\033[{y};{x}H", end="", flush=True)

    def move_cursor_relative(self, x: int, y: int):
        """
        Move the cursor relative to its current position.
        ex: move_cursor_relative(1, 0) will move the cursor one column to the right.
        move_cursor_relative(-1, 0) will move the cursor one column to the left.
        """
        if x > 0:
            print(f"\033[{x}C", end="", flush=True)
        elif x < 0:
            print(f"\033[{abs(x)}D", end="", flush=True)
        if y > 0:
            print(f"\033[{y}B", end="", flush=True)
        elif y < 0:
            print(f"\033[{abs(y)}A", end="", flush=True)

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

    def clear_line(self):
        print("\033[2K", end="", flush=True)


if __name__ == "__main__":
    terminal = Terminal()
    terminal.handle_key_input()
