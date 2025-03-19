Terminal
========

.. automodule:: ConsoleM.Core.terminal
   :members:
   :undoc-members:
   :show-inheritance:
   :inherited-members:

The Terminal class provides a high-level interface for terminal manipulation. Here are some common use cases:

Cursor Movement
--------------

.. code-block:: python

    from ConsoleM import Terminal

    term = Terminal()

    # Move cursor to absolute position
    term.move_cursor(10, 5)  # Move to column 10, row 5

    # Move cursor relative to current position
    term.move_cursor_relative(1, 0)  # Move one column right
    term.move_cursor_relative(-1, 0)  # Move one column left
    term.move_cursor_relative(0, 1)   # Move one row down
    term.move_cursor_relative(0, -1)  # Move one row up

Screen Management
----------------

.. code-block:: python

    from ConsoleM import Terminal

    term = Terminal()

    # Clear the entire screen
    term.clear()

    # Clear current line
    term.clear_line()

    # Clear n lines above current position
    term.clear_lines_above(3)

    # Clear from cursor to end of line
    term.clear_end_of_line()

    # Create and restore alternate screen
    term.create_alternate_screen()
    try:
        # Your full-screen application code here
        pass
    finally:
        term.restore_alternate_screen()

Input Handling
-------------

.. code-block:: python

    from ConsoleM import Terminal

    term = Terminal()

    # Start capturing keyboard input
    term.handle_key_input()

    try:
        while True:
            # Get the next key press
            key = term.get_key_from_queue()
            print(f"Pressed: {key}")
    except KeyboardInterrupt:
        # Stop capturing keyboard input
        term.stop_handle_key_input()

Terminal Information
------------------

.. code-block:: python

    from ConsoleM import Terminal

    term = Terminal()

    # Get terminal size
    width, height = term.get_terminal_size()
    print(f"Terminal size: {width}x{height}")

    # Get current cursor position
    x, y = term.get_cursor_position()
    print(f"Cursor position: ({x}, {y})") 