from ConsoleM.Core import Terminal

terminal = Terminal()
print(terminal.get_raw_mode())
exit()
terminal.handle_key_input()


for _ in range(10):
    print("Test", flush=True)
    print(terminal.get_cursor_position(), flush=True)
terminal.stop_handle_key_input()
exit()


while True:
    key = terminal.keys.get()
    if key == 'q':
        print("Exiting...")
        break
    if key == "\x1b":
        print("arrow key detected")
        key += terminal.keys.get()
        key += terminal.keys.get()
        if key == "\x1b[A":
            print("Up arrow key detected")
        elif key == "\x1b[B":
            print("Down arrow key detected")
        elif key == "\x1b[C":
            print("Right arrow key detected")
        elif key == "\x1b[D":
            print("Left arrow key detected")
        else:
            print(f"Unknown arrow key: {key!r}")
        continue
    print(f"Key: {key!r}", end="\r")
terminal.stop_handle_key_input()