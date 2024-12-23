from ConsoleM.Core import Terminal

terminal = Terminal()
terminal.handle_key_input()


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