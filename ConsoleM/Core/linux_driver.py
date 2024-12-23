import io
import queue
import re
import os
import select
import sys
import shutil
import termios
import tty


class LinuxDriver:
    def __init__(self):
        self.OldStdinMode = termios.tcgetattr(sys.stdin)
        self.width, self.height = self.get_terminal_size()
        self._handle = False
        self.inited = False
        self.getting_pos = False

    def init_termios(self):
        self.OldStdinMode = termios.tcgetattr(sys.stdin)
        _ = termios.tcgetattr(sys.stdin)
        _[3] = _[3] & ~(termios.ECHO | termios.ICANON)
        termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, _)

    def get_terminal_size(self) -> tuple[int, int]:
        width: int | None = 80
        height: int | None = 24

        try:
            width, height = shutil.get_terminal_size()
        except Exception:
            try:
                width, height = shutil.get_terminal_size()
            except Exception:
                pass
        width = width or 80
        height = height or 24
        return width, height

    def get_cursor_position(self) -> tuple[int, int]:
        try:
            self.getting_pos = True
            _ = ""
            sys.stdout.write("\x1b[6n")
            sys.stdout.flush()
            while not (_ := _ + sys.stdin.read(1)).endswith('R'):
                pass
            res = re.match(r".*\[(?P<y>\d*);(?P<x>\d*)R", _)
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, self.OldStdinMode)
            self.getting_pos = False
        if res:
            return int(res.group("x")), int(res.group("y"))
        return -1, -1

    def hide_cursor(self):
        print("\033[?25l", end="", flush=True)

    def show_cursor(self):
        print("\033[?25h", end="", flush=True)

    def handle_key_input(self, q: queue.Queue):
        self._handle = True
        try:
            self.set_raw_mode()
            while self._handle:
                if not self.getting_pos and select.select([sys.stdin], [], [], 0.05)[0]:
                    key = sys.stdin.read(1)
                    if key == "\x1b": # arrow keys, the escape sequence is 3 bytes long
                        key += sys.stdin.read(2)
                        q.put(key)
                    else:
                        q.put(key)
        finally:
            self.remove_raw_mode()

    def stop_handle_key_input(self):
        self._handle = False

    def remove_raw_mode(self):
        if not self.inited:
            self.init_termios()
            self.inited = True
        termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, self.OldStdinMode)

    def set_raw_mode(self):
        tty.setcbreak(sys.stdin.fileno())

if __name__ == "__main__":
    from ConsoleM.Core.terminal import move_cursor

    print(os.getcwd())
    driver = LinuxDriver()
    print(driver.get_terminal_size())  # (80, 24)
    print(os.get_terminal_size())
    print(driver.get_cursor_position())
    move_cursor(10, 10)
    print(driver.get_cursor_position())