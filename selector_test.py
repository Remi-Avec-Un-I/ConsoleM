from ConsoleM.Input import selector, Items

items = [
    Items("Item 1", 1),
    Items("Item 2", 2),
    Items("Item 3", 3),
    Items("Item 4"*100, 4),
    Items("Item 5", 5),
]
rst = selector(items, "Select an item: ", 1, 3, arrow="->", empty_arrow="  ")
print(rst)