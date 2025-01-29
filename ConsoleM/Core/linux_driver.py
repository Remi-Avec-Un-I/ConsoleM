from __future__ import annotations

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

    def getch(self):
        # See the "Description" section here: https://en.wikipedia.org/wiki/UTF-8
        b = os.read(0, 1)
        b = ord(b)
        if b & 0b10000000 == 0:
            bs = bytes([b])
        elif b & 0b11100000 == 0b11000000:
            b2 = os.read(0, 1)
            b2 = ord(b2)
            bs = bytes([b, b2])
        elif b & 0b11110000 == 0b11100000:
            b23 = os.read(0, 2)
            b23 = [ord(str(i)) for i in b23]
            bs = bytes([b, *b23])
        elif b & 0b11111000 == 0b11110000:
            b234 = os.read(0, 3)
            b234 = [ord(str(i)) for i in b234]
            bs = bytes([b, *b234])
        else:
            raise ValueError(f'unexpected byte value {b}')
        key = bs.decode()
        return key

    def handle_key_input(self, q: queue.Queue):
        self._handle = True
        try:
            self.set_raw_mode()
            first = ""
            while self._handle:
                if not self.getting_pos and select.select([0], [], [], 0.05)[0]:
                    key = self.getch()
                    if key == "\x1b":
                        if select.select([0], [], [], 0.05)[0]:
                            first = self.getch()
                        if first == "[":
                            if select.select([0], [], [], 0.05)[0]:
                                key += first + self.getch()
                            q.put(key)
                        elif first == "":
                            q.put(key)
                        else:
                            q.put(first)
                            q.put(key)
                        first = ""
                        """    
                    elif key.startswith("\x1b["): # special key, like the escape sequence that are 2 bytes long
                        key += os.read(0, 1)
                        q.put(key)
                        """
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
    from ConsoleM.Core.terminal import Terminal
    terminal = Terminal()
    move_cursor = terminal.move_cursor

    print(os.getcwd())
    driver = LinuxDriver()
    print(driver.get_terminal_size())  # (80, 24)
    print(os.get_terminal_size())
    print(driver.get_cursor_position())
    move_cursor(10, 10)
    print(driver.get_cursor_position())
