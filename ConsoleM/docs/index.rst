.. ConsoleM documentation master file, created by
   sphinx-quickstart on Wed Mar 19 00:52:06 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ConsoleM's documentation!
================================

ConsoleM is a powerful Python library for terminal manipulation and text styling. It provides a simple and intuitive API for creating beautiful terminal applications with advanced features like cursor control, text styling, and keyboard input handling.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   api/index
   examples
   troubleshooting

Features
--------

* **Terminal Manipulation**
  * Precise cursor movement (absolute and relative positioning)
  * Screen clearing and line management
  * Alternate screen support for full-screen applications
  * Terminal size detection and cursor position tracking
  * Cursor visibility control
  * Non-blocking keyboard input handling

* **Text Styling**
  * Rich text formatting with intuitive markup syntax
  * 256-color support (foreground and background)
  * Text styles (bold, underline, italic, etc.)
  * Emoji support with automatic conversion
  * Easy-to-use BBCode-like markup syntax
  * Automatic style reset and cleanup

* **Input Handling**
  * Non-blocking keyboard input capture
  * Key event queue management
  * Special key detection (arrows, function keys, etc.)
  * Thread-safe input processing
  * Clean shutdown handling

* **Cross-Platform Support**
  * Native Linux support
  * Windows support (coming soon)
  * Consistent API across platforms
  * Automatic platform detection

Getting Started
--------------

.. code-block:: python

    from ConsoleM import Terminal
    from ConsoleM.Style.text import Text

    # Create a terminal instance
    term = Terminal()

    # Print styled text
    Text("[blue bold]Welcome to ConsoleM![/]").print()

    # Get terminal size
    width, height = term.get_terminal_size()
    Text(f"[green]Terminal size: {width}x{height}[/]").print()

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

