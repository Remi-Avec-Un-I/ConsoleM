class Terminal:
    def __init__(self):
        pass

    def clear(self):
        print("\033[2J", end="")

    def move_cursor(self, x: int, y: int):
        print(f"\033[{y};{x}H", end="")


if __name__ == "__main__":
    terminal = Terminal()
    terminal.move_cursor(10, 10)