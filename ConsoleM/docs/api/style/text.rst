Text Styling
===========

.. automodule:: ConsoleM.Style.text
   :members:
   :undoc-members:
   :show-inheritance:
   :inherited-members:

The Text class provides a powerful way to create styled text output using markup syntax. Here are some examples:

Basic Usage
----------

.. code-block:: python

    from ConsoleM.Style.text import Text

    # Simple colored text
    text = Text("[red]Hello[/] World")
    text.print()

    # Multiple styles
    text = Text("[blue bold]Styled[/] text")
    text.print()

    # With emojis
    text = Text("[green]Hello[/] :smile: :heart:")
    text.print()

Available Markup Tags
-------------------

Colors
~~~~~~

* ``[red]text[/]`` - Red text
* ``[blue]text[/]`` - Blue text
* ``[green]text[/]`` - Green text
* ``[yellow]text[/]`` - Yellow text
* ``[magenta]text[/]`` - Magenta text
* ``[cyan]text[/]`` - Cyan text

Styles
~~~~~~

* ``[bold]text[/]`` - Bold text
* ``[underline]text[/]`` - Underlined text
* ``[italic]text[/]`` - Italic text

Special Tags
~~~~~~~~~~~

* ``[reset]`` - Reset all styling
* ``:emoji_name:`` - Insert an emoji

Advanced Usage
-------------

.. code-block:: python

    from ConsoleM.Style.text import Text

    # Create a text object
    text = Text("[red bold]Hello[/] [blue]World[/]")

    # Get the rendered content
    rendered = str(text)
    print(rendered)

    # Update the content
    text.content = "[green]New[/] content"

    # Print with custom parameters
    text.print(end="", flush=True) 