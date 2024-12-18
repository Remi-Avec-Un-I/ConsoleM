from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Union, Tuple, Dict, Optional, Any

@dataclass
class IntinputConfig:
    """
    The configuration for the intinput function.
    :param prompt: The prompt to display.
    :param range: The range of accepted values. If None, any value is accepted. If both range and choice are provided, the choice list is prioritized.
    :param choice: The list of accepted values. If None, any value is accepted. If both range and choice are provided, the choice list is prioritized.
    :param error_message: The error message to display when the input is invalid.
    :param error_message_range: The error message to display when the input is out of range. The range is getting formatted with the range tuple.
    :param error_message_choice: The error message to display when the input is not in the choice list. The choice list is getting formatted with the choice list.
    """
    prompt: Optional[str] = None
    range: Optional[Tuple[int, int]] = None
    choice: Optional[Iterable[int]] = None
    error_message: str = "Please enter a valid number."
    error_message_range: str = "Please enter a number between {range[0]} and {range[1]}."
    error_message_choice: str = "Please enter a number from the list: {choice}."

def intinput(
    prompt: Optional[str] = None,
    range: Optional[Tuple[int, int]] = None,
    choice: Optional[Iterable[int]] = None,
    error_message: str = "Please enter a valid number.",
    error_message_range: str = "Please enter a number between {range[0]} and {range[1]}.",
    error_message_choice: str = "Please enter a number from the list: {choice}.",
    config: Union[IntinputConfig, Dict[str, Any], None] = None,
) -> int:
    """
    Get an integer input from the user, following the provided configuration.
    :param prompt: The prompt to display.
    :param range: The range of accepted values. If None, any value is accepted. If both range and choice are provided, the choice list is prioritized.
    :param choice: The list of accepted values. If None, any value is accepted. If both range and choice are provided, the choice list is prioritized.
    :param error_message: The error message to display when the input is invalid.
    :param error_message_range: The error message to display when the input is out of range. The range is getting formatted with the range tuple.
    :param error_message_choice: The error message to display when the input is not in the choice list. The choice list is getting formatted with the choice list.
    :param config: The configuration object/dict. If provided, the other arguments are ignored. If None, the other arguments are used.
    :return: The integer input.

    Example:
    ```
    value = intinput("Enter a number: ")
    ```

    ```
    value = intinput("Enter a number between 1 and 10 included: ", (1, 10)")
    ```

    ```
    config = IntinputConfig("Enter a number between 1 and 10 included: ", (1, 10), error_message_range="Please enter a number between {range[0]} and {range[1]}.")
    value = intinput(config=config)
    ```

    ```
    config_dict = {
        "prompt": "Enter a number between 1 and 10 included: ",
        "range": (1, 10),
        "error_message_range": "Please enter a number between {range[0]} and {range[1]}."
    }
    value = intinput(config=config_dict)
    ```

    ```
    value = intinput("Enter a number from the list: ", choice=[1, 2, 3, 4, 5])
    ```
    """
    if config:
        if isinstance(config, dict):
            config = IntinputConfig(**config)
        prompt = config.prompt or prompt
        range = config.range or range
        choice = config.choice or choice
        error_message = config.error_message or error_message
        error_message_range = config.error_message_range or error_message_range
        error_message_choice = config.error_message_choice or error_message_choice

    prompt = prompt or ""

    while True:
        value = input(prompt)
        if value.isdigit() or (value[0] in ["-", "+"] and value[1:].isdigit()):
            value = int(value)
            if choice:
                if value in choice:
                    return value
                print(error_message_choice.format(choice=choice))
            elif range:
                if range[0] <= value <= range[1]:
                    return value
                print(error_message_range.format(range=range))
            else:
                return value
        else:
            print(error_message)

if __name__ == "__main__":
    value = intinput("Enter a number: ")
    print(value)
    value = intinput("Enter a number between 1 and 10 included: ", (1, 10))
    print(value)
    config = IntinputConfig(prompt="Enter a number between 1 and 10 included: ", range=(1, 10), error_message_range="Please enter a number between {range[0]} and {range[1]}.")
    value = intinput(config=config)
    print(value)
    config_dict = {
        "prompt": "Enter a number between 1 and 10 included: ",
        "range": (1, 10),
        "error_message_range": "Please enter a number between {range[0]} and {range[1]}."
    }
    value = intinput(config=config_dict)
    print(value)
    value = intinput("Enter a number from the list: ", choice=[1, 2, 3, 4, 5])
    print(value)