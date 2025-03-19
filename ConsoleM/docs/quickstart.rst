Quick Start
===========

This guide will help you get started with ConsoleM quickly. We'll cover the basic features and show you how to use them.

Installation
-----------

.. code-block:: bash

    pip install ConsoleM

Basic Terminal Operations
------------------------

Here's a simple example of how to use ConsoleM for basic terminal operations:

.. code-block:: python

    from ConsoleM import Terminal

    # Create a terminal instance
    term = Terminal()

    # Clear the screen
    term.clear()

    # Move cursor to position (x, y)
    term.move_cursor(10, 5)

    # Get terminal size
    width, height = term.get_terminal_size()

    # Hide/show cursor
    term.hide_cursor()
    term.show_cursor()

Text Styling
------------

ConsoleM provides powerful text styling capabilities:

.. code-block:: python

    from ConsoleM import Terminal
    from ConsoleM.Style.text import Text

    # Create a terminal instance
    term = Terminal()

    # Basic text styling
    text = Text("[red]Hello[/] [blue]World[/]")
    text.print()

    # Multiple styles
    text = Text("[bold cyan]Styled[/] [underline]text[/]")
    text.print()

    # With emojis
    text = Text("[green]Hello[/] :smile: :heart:")
    text.print()

Available markup tags:
* Colors: ``[red]``, ``[blue]``, ``[green]``, ``[yellow]``, ``[magenta]``, ``[cyan]``
* Styles: ``[bold]``, ``[underline]``, ``[italic]``
* Emojis: ``:smile:``, ``:heart:``, etc.
* Reset: ``[reset]``

Keyboard Input Handling
----------------------

Here's how to handle keyboard input:

.. code-block:: python

    from ConsoleM import Terminal
    from ConsoleM.Style.text import Text

    term = Terminal()

    # Start capturing keyboard input
    term.handle_key_input()

    try:
        while True:
            # Get the next key press
            key = term.get_key_from_queue()
            Text(f"[green]Pressed:[/] {key}").print()
    except KeyboardInterrupt:
        # Stop capturing keyboard input
        term.stop_handle_key_input()

Advanced Features
----------------

Alternate Screen
~~~~~~~~~~~~~~~

Create a full-screen alternate display:

.. code-block:: python
    from ConsoleM import Terminal
    from ConsoleM.Style.text import Text
    import time

    def main():
        # Create terminal instance
        term = Terminal()
        
        # Create alternate screen
        term.create_alternate_screen()
        
        try:
            # Get terminal dimensions
            width, height = term.get_terminal_size()
            
            # Clear the screen
            term.clear()
            
            # Draw a box around the screen
            top = "┌" + "─" * (width - 2) + "┐"
            top = Text("[blue]" + top + "[/]").content
            middle = "\n".join(["│" + " " * (width - 2) + "│" for _ in range(height - 2)])
            middle = Text("[blue]" + middle + "[/]").content
            bottom = "└" + "─" * (width - 2) + "┘"
            bottom = Text("[blue]" + bottom + "[/]").content
            term.write(top + middle + bottom)
            
            # Add some text
            term.move_cursor(3, 3)
            Text("[bold cyan]Welcome to Full Screen Mode[/]").print()
            term.move_cursor(3, 4)
            Text("[yellow]Press 'q' to quit[/]").print()
            
            # Handle input
            term.handle_key_input()
            while True:
                key = term.get_key_from_queue()
                if key.lower() == 'q':
                    break
                
        finally:
            # Cleanup
            term.stop_handle_key_input()
            term.restore_alternate_screen()

    if __name__ == "__main__":
        main()

Line Management
~~~~~~~~~~~~~~

Manage terminal lines:

.. code-block:: python

    from ConsoleM import Terminal
    from ConsoleM.Style.text import Text

    term = Terminal()

    # Clear current line
    term.clear_line()

    # Clear n lines above current position
    term.clear_lines_above(3)

    # Clear from cursor to end of line
    term.clear_end_of_line()

    # Example: Progress bar
    def show_progress(percent):
        width, _ = term.get_terminal_size()
        bar_width = width - 20
        filled = int(bar_width * percent / 100)
        bar = "█" * filled + "░" * (bar_width - filled)
        Text(f"[cyan]Progress:[/] [{bar}] {percent}%").print()

    # Show progress animation
    for i in range(101):
        show_progress(i)
        term.move_cursor_relative(0, -1)  # Move up one line
        term.clear_line()  # Clear the line 