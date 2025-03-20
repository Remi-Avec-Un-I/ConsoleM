# use getwche() to read input from the console
import msvcrt
import queue
import threading
import os
import shutil
import struct
import ctypes
from ctypes import windll, wintypes, byref
from ConsoleM.Core.const.keys import Keys

class WindowsDriver:
    def __init__(self):
        self._handle = False

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
    
    def get_cursor_pos(self) -> tuple[int, int]:
        h = ctypes.windll.kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
        buf = ctypes.create_string_buffer(22)  # Buffer for console info
        ctypes.windll.kernel32.GetConsoleScreenBufferInfo(h, buf)
        
        # Unpack the buffer to extract cursor position
        _, _, _, _, _, _, _, x, y, _, _ = struct.unpack("hhhhHhhhhhh", buf.raw)
        return x, y  # (column, row)

    def hide_cursor(self):
        ctypes.windll.kernel32.SetConsoleCursorInfo(ctypes.windll.kernel32.GetStdHandle(-11), (1, 0))

    def show_cursor(self):
        ctypes.windll.kernel32.SetConsoleCursorInfo(ctypes.windll.kernel32.GetStdHandle(-11), (0, 1))

    def getch(self):
        return msvcrt.getwche()

    def handle_key_input(self, q: queue.Queue):
        self._handle = True
        while self._handle:
            key = self.getch()
            q.put(key)

    def stop_handle_key_input(self):
        self._handle = False


