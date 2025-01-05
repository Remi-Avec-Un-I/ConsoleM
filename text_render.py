from ConsoleM import Text


Text("[red underline]Hello[reset], :aries: [blue bold]World[/]!").print()

if __name__ == "__main__":
    import os
    from ConsoleM.Core.terminal import Terminal
    from ConsoleM.Core.linux_driver import LinuxDriver
    print(os.getcwd())
    driver = LinuxDriver()
    print(driver.get_terminal_size())  # (80, 24)
    print(os.get_terminal_size())
    print(driver.get_cursor_position())
    terminal = Terminal().move_cursor(0, 0)
    print(driver.get_cursor_position(), flush=True)