import re
import os
import sys
import shutil
import termios

class LinuxDriver:
    def __init__(self):
        self.OldStdinMode = None
        self.width, self.height = self.get_terminal_size()
        self.init_termios()

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
            _ = ""
            sys.stdout.write("\x1b[6n")
            sys.stdout.flush()
            while not (_ := _ + sys.stdin.read(1)).endswith('R'):
                pass
            res = re.match(r".*\[(?P<y>\d*);(?P<x>\d*)R", _)
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, self.OldStdinMode)
        if res:
            return int(res.group("x")), int(res.group("y"))
        return -1, -1


if __name__ == "__main__":
    from ConsoleM.Core.terminal import Terminal
    print(os.getcwd())
    driver = LinuxDriver()
    print(driver.get_terminal_size())  # (80, 24)
    print(os.get_terminal_size())
    print(driver.get_cursor_position())
    terminal = Terminal().move_cursor(10, 10)
    print(driver.get_cursor_position())