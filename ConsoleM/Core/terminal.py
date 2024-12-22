import os
import threading
import queue
from ConsoleM.Core.linux_driver import  LinuxDriver


class Terminal:
    def __init__(self):
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

    def stop_handle_key_input(self):
        self.driver.stop_handle_key_input()
        self._tr_key_input.join()

    def move_cursor(self, x: int, y: int):
        print(f"\033[{y};{x}H", end="")

    def clear(self):
        print("\033[2J", end="")


if __name__ == "__main__":
    terminal = Terminal()
    terminal.handle_key_input()